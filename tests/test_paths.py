import logging
import os
import stat
import sys
import tempfile
import unittest
from unittest import mock

from tests import _stubs  # noqa: F401
import sequencer
from ayon_publish import AyonPublish


def bare_sequencer():
    s = sequencer.Sequencer.__new__(sequencer.Sequencer)
    s.settings = None
    s.settings_inst = None
    s.log = logging.getLogger('test')
    return s


class ExecutableDiscoveryTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        ext = '.exe' if sys.platform == 'win32' else ''
        for n in ('ffprobe', 'ffmpeg', 'oiiotool', 'deadlinecommand'):
            p = os.path.join(self.tmp.name, n + ext)
            with open(p, 'w') as f:
                f.write('')
            os.chmod(p, os.stat(p).st_mode | stat.S_IEXEC)

    def tearDown(self):
        self.tmp.cleanup()

    def test_tools_on_path_are_registered(self):
        env = {'PATH': self.tmp.name}
        with mock.patch.dict(os.environ, env, clear=True):
            s = bare_sequencer()
            s._prep_paths_vars()
        for key in ('ffprobe', 'ffmpeg', 'oiiotool', 'deadline'):
            self.assertTrue(s.paths[key], f"{key} not found on PATH")
        self.assertNotIn('ffprob', s.paths)
        self.assertEqual(s.paths['vfx-transcode'], '')

    def test_deadline_path_env_overrides_path(self):
        other = tempfile.TemporaryDirectory()
        self.addCleanup(other.cleanup)
        name = 'deadlinecommand' + ('.exe' if sys.platform == 'win32' else '')
        open(os.path.join(other.name, name), 'w').close()
        with mock.patch.dict(os.environ, {'PATH': self.tmp.name, 'DEADLINE_PATH': other.name}, clear=True):
            s = bare_sequencer()
            s._prep_paths_vars()
        self.assertTrue(s.paths['deadline'].startswith(other.name.replace('\\', '/')))

    def test_custom_ocio_checkbox_off_is_respected(self):
        ocio = os.path.join(self.tmp.name, 'config.ocio')
        open(ocio, 'w').close()
        with mock.patch.dict(os.environ, {'PATH': '', 'OCIO': 'env.ocio'}, clear=True):
            s = bare_sequencer()
            s.settings = {'prefs_oiio_custom_ocio': {'value': False},
                          'prefs_oiio_custom_ocio_path': {'value': ocio}}
            s._prep_paths_vars()
        self.assertEqual(s.paths['ocio'], 'env.ocio')


class HeadlessActionsTest(unittest.TestCase):
    def test_unknown_action_does_not_crash(self):
        s = bare_sequencer()
        s.settings_args = {'actions': 'q'}
        s._process_headless()  # used to raise KeyError: 'q'


class AyonPublishPathsTest(unittest.TestCase):
    def test_missing_ayon_fails(self):
        a = AyonPublish({}, {'ayon': '', 'deadline': ''})
        self.assertFalse(a.are_paths_ok(mode='local'))

    def test_local_does_not_need_deadline(self):
        a = AyonPublish({}, {'ayon': '/bin/ayon', 'deadline': ''})
        self.assertTrue(a.are_paths_ok(mode='local'))
        self.assertFalse(a.are_paths_ok(mode='farm'))

    def test_csv_name_suffix(self):
        a = AyonPublish({}, {'ayon': 'ayon'})
        a.settings = {}
        try:
            a.build_ayon_csv_command('/x/sub_v001.csv', 'proj')
        except Exception:
            pass
        self.assertEqual(a.csv_name, 'sub_v001')


if __name__ == '__main__':
    unittest.main()
