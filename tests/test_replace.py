"""
Replace tab: Search and Replace CSV applied to package text files
(Replace button, Replace with Go, headless action 'e').
"""
import logging
import os
import shutil
import tempfile
import unittest
from unittest import mock

from tests import _stubs  # noqa: F401
import sequencer


def make_seq(values=None, items=None):
    s = sequencer.Sequencer.__new__(sequencer.Sequencer)
    s.log = logging.getLogger('SubmissionHelper')
    s.headless = True
    s.ui = None
    s.output = {}
    s.static_keywords = {}
    s.settings = {k: {'value': v} for k, v in (values or {}).items()}
    s.merged_list = items if items is not None else []
    s.paths = {}
    return s


class ReplaceExecute(unittest.TestCase):

    def setUp(self):
        self.dir = tempfile.mkdtemp()
        self.csv_dir = os.path.join(self.dir, 'rules')
        os.makedirs(self.csv_dir)
        self.pkg = os.path.join(self.dir, 'pkg')
        os.makedirs(self.pkg)

    def tearDown(self):
        shutil.rmtree(self.dir, ignore_errors=True)

    def _csv(self, rows):
        path = os.path.join(self.csv_dir, 'rules.csv')
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write('Extension,Pattern,Search,Replace\n')
            for row in rows:
                f.write(','.join(row) + '\n')
        return path

    def _file(self, name, data):
        path = os.path.join(self.pkg, name).replace('\\', '/')
        with open(path, 'wb') as f:
            f.write(data)
        return path

    def _read(self, path):
        with open(path, 'rb') as f:
            return f.read()

    def _seq(self, csv_path, files, enable=True):
        items = [{'extension': os.path.splitext(p)[1].lstrip('.'), 'full_path': p} for p in files]
        return make_seq({'replace_enable': enable, 'replace_csv_path': csv_path}, items)

    def test_replaces_in_place_and_keeps_crlf(self):
        nk = self._file('sh010_comp_v001.nk', b'read D:/projects/a.exr\r\nread D:/projects/b.exr\r\n')
        csv_path = self._csv([('nk', '', 'D:/projects/', '/mnt/projects/')])
        result = self._seq(csv_path, [nk]).replace_execute()
        self.assertEqual(result, {nk: 2})
        self.assertEqual(self._read(nk), b'read /mnt/projects/a.exr\r\nread /mnt/projects/b.exr\r\n')

    def test_extension_any_case(self):
        nk = self._file('a.NK', b'X')
        csv_path = self._csv([('nk', '', 'X', 'Y')])
        self._seq(csv_path, [nk]).replace_execute()
        self.assertEqual(self._read(nk), b'Y')

    def test_pattern_is_literal_and_filters_file_names(self):
        comp = self._file('sh010_comp_v001.nk', b'X')
        roto = self._file('sh010_roto_v001.nk', b'X')
        dots = self._file('sh010.comp.nk', b'X')
        csv_path = self._csv([('nk', '_comp_', 'X', 'Y'),
                              ('nk', '.c', 'X', 'Z')])   # '.' is not a regex wildcard
        self._seq(csv_path, [comp, roto, dots]).replace_execute()
        self.assertEqual(self._read(comp), b'Y')
        self.assertEqual(self._read(roto), b'X')
        self.assertEqual(self._read(dots), b'Z')

    def test_search_is_literal_and_rules_chain_in_order(self):
        nk = self._file('a.nk', b'a.*b')
        csv_path = self._csv([('nk', '', 'a.*', 'c'), ('nk', '', 'cb', 'done')])
        self._seq(csv_path, [nk]).replace_execute()
        self.assertEqual(self._read(nk), b'done')

    def test_empty_search_is_skipped(self):
        nk = self._file('a.nk', b'abc')
        csv_path = self._csv([('nk', '', '', 'Z')])
        self.assertEqual(self._seq(csv_path, [nk]).replace_execute(), {})
        self.assertEqual(self._read(nk), b'abc')

    def test_latin1_file_roundtrips(self):
        nk = self._file('a.nk', 'caf\xe9 D:/p/'.encode('latin-1'))
        csv_path = self._csv([('nk', '', 'D:/p/', '/mnt/p/')])
        self._seq(csv_path, [nk]).replace_execute()
        self.assertEqual(self._read(nk), 'caf\xe9 /mnt/p/'.encode('latin-1'))

    def test_unchanged_file_is_not_rewritten(self):
        nk = self._file('a.nk', b'nothing here')
        os.utime(nk, (1000, 1000))
        csv_path = self._csv([('nk', '', 'D:/', '/mnt/')])
        self.assertEqual(self._seq(csv_path, [nk]).replace_execute(), {nk: 0})
        self.assertEqual(os.path.getmtime(nk), 1000)

    def test_disabled_does_nothing(self):
        nk = self._file('a.nk', b'X')
        csv_path = self._csv([('nk', '', 'X', 'Y')])
        self.assertEqual(self._seq(csv_path, [nk], enable=False).replace_execute(), {})
        self.assertEqual(self._read(nk), b'X')

    def test_missing_file_is_logged_and_others_continue(self):
        nk = self._file('a.nk', b'X')
        gone = (self.pkg + '/gone.nk')
        csv_path = self._csv([('nk', '', 'X', 'Y')])
        result = self._seq(csv_path, [gone, nk]).replace_execute()
        self.assertEqual(result, {nk: 1})

    def test_running_twice_applies_twice(self):
        # documented, accepted risk
        nk = self._file('a.nk', b'a')
        csv_path = self._csv([('nk', '', 'a', 'ab')])
        s = self._seq(csv_path, [nk])
        s.replace_execute()
        s.replace_execute()
        self.assertEqual(self._read(nk), b'abb')


class ReplaceHooks(unittest.TestCase):

    def test_go_runs_replace_first_when_on(self):
        s = make_seq({'replace_withgo': True, 'side_copywithgo': False,
                      'thumbs_make_on_go': False})
        calls = []
        with mock.patch.object(s, 'replace_execute', lambda: calls.append('replace')), \
                mock.patch.object(s, 'sidecar_files_copy', lambda: calls.append('sidecar')):
            try:
                s.export_all()
            except (KeyError, AttributeError, TypeError):
                pass   # later Go steps need a full preset
        self.assertEqual(calls[:1], ['replace'])

    def test_go_skips_replace_when_off(self):
        s = make_seq({'replace_withgo': False, 'side_copywithgo': False,
                      'thumbs_make_on_go': False})
        calls = []
        with mock.patch.object(s, 'replace_execute', lambda: calls.append('replace')):
            try:
                s.export_all()
            except (KeyError, AttributeError, TypeError):
                pass
        self.assertEqual(calls, [])

    def test_headless_action_e(self):
        s = make_seq()
        s.settings_args = {'actions': 'e'}
        calls = []
        with mock.patch.object(s, 'replace_execute', lambda: calls.append('replace')):
            s._process_headless()
        self.assertEqual(calls, ['replace'])

    def test_cli_accepts_e(self):
        import sh_cli
        self.assertIn('e', sh_cli.CLI_ACTIONS)


if __name__ == '__main__':
    unittest.main()
