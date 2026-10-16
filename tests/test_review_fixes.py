"""
Bugs found in the tooltip review (claude/tooltip_review_bugs.md): crashes on
braces, wrong defaults, controls that did nothing, stale values on refresh.
"""
import csv
import logging
import os
import shutil
import tempfile
import time
import unittest

from tests import _stubs  # noqa: F401
import ayon_shotlist
import metadata
import sequencer
import settings as settings_module
from sequencer import expand_tokens, format_keep, unresolved_tokens


def make_seq(values=None, items=None):
    s = sequencer.Sequencer.__new__(sequencer.Sequencer)
    s.log = logging.getLogger('SubmissionHelper')
    s.headless = True
    s.ui = None
    s.output = {}
    s.static_keywords = {}
    s.settings = {k: {'value': v} for k, v in (values or {}).items()}
    s.merged_list = items if items is not None else []
    return s


class TokenHelpers(unittest.TestCase):

    def test_expand_tokens_keeps_regex_counts(self):
        self.assertEqual(expand_tokens(r'^{shot}_\d{3}$', {'shot': 'sh010'}), r'^sh010_\d{3}$')

    def test_expand_tokens_first_mapping_wins_unknown_kept(self):
        self.assertEqual(expand_tokens('{a}{b}{c}', {'a': 1}, {'a': 2, 'b': 3}), '13{c}')

    def test_format_keep_supports_format_specs(self):
        self.assertEqual(format_keep('{cnt:0>4}', {'cnt': 7}), '0007')

    def test_format_keep_never_raises_on_stray_braces(self):
        for text in ('{}', '{0}', 'a { b', r'x\d{3}', '{shot} }'):
            format_keep(text, {'shot': 'sh010'})   # no exception
        self.assertEqual(format_keep(r'{shot}_\d{3}', {'shot': 'sh010'}), r'sh010_\d{3}')

    def test_format_keep_keeps_unknown_tokens(self):
        self.assertEqual(format_keep('{shot}/{nope}', {'shot': 'a'}), 'a/{nope}')

    def test_unresolved_tokens_ignores_regex_counts(self):
        self.assertEqual(unresolved_tokens(r'\d{3}x{2,4}{name}'), ['name'])


class PackageName(unittest.TestCase):

    def setUp(self):
        self.root = tempfile.mkdtemp()
        self.pkg = os.path.join(self.root, 'temp_name').replace('\\', '/')
        os.makedirs(self.pkg)
        self.today = time.strftime('%y%m%d')

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def _seq(self, **over):
        values = {
            'name_from_template': True,
            'name_template': 'sub_{yy}{mm}{dd}_{package_version}',
            'name_date_regex': 'sub_{yy}{mm}{dd}',
            'name_version_regex': r'_(\d{3})$',
            'package_folder': self.pkg,
            'name_version_per_date': True,
            'name_version_zeroes': 3,
            'name_version_use_letters': False,
            'name_version_letters_uppercase': True,
        }
        values.update(over)
        return make_seq(values)

    def _dirs(self, *names):
        for n in names:
            os.makedirs(os.path.join(self.root, n))

    def test_default_date_regex_with_tokens_works_per_date(self):
        # used to raise UnboundLocalError (no capture group, tokens not expanded)
        self._dirs(f'sub_{self.today}_001', f'sub_{self.today}_002', 'sub_990101_007')
        s = self._seq()
        s.prepare_package_name()
        self.assertEqual(s.static_keywords['package_name'], f'sub_{self.today}_003')

    def test_versions_compare_as_numbers(self):
        self._dirs('sub_x_009', 'sub_x_010')
        s = self._seq(name_version_per_date=False, name_template='sub_x_{package_version}',
                      name_date_regex='')
        s.prepare_package_name()
        self.assertEqual(s.static_keywords['package_name'], 'sub_x_011')

    def test_letters_ignore_numeric_versions(self):
        self._dirs('pkg_A', 'pkg_B', 'pkg_001')
        s = self._seq(name_version_per_date=False, name_template='pkg_{package_version}',
                      name_date_regex='', name_version_regex='_([A-Za-z0-9]+)$',
                      name_version_use_letters=True)
        s.prepare_package_name()
        self.assertEqual(s.static_keywords['package_name'], 'pkg_C')

    def test_unknown_template_token_does_not_crash(self):
        s = self._seq(name_template='{shot}_{package_version}', name_version_per_date=False)
        s.prepare_package_name()
        self.assertEqual(s.static_keywords['package_name'], '{shot}_001')

    def test_no_package_folder_does_not_crash(self):
        s = self._seq(package_folder='')
        s.prepare_package_name()
        self.assertIn('package_name', s.static_keywords)


class VendorKeys(unittest.TestCase):

    def _seq(self, p_key, v_key, items, rows, **over):
        values = {'vendor_csv_package_key': p_key, 'vendor_csv_vendor_key': v_key,
                  'vendor_csv_ignore': True, 'vendor_csv_skip_by': '{shot}',
                  'vendor_csv_skip_what': '', 'vendor_csv_skip': False}
        values.update(over)
        s = make_seq(values, items)
        s.vendor_csv_transformed = rows
        return s

    def test_old_regex_default_doesnt_crash_or_pair(self):
        items = [{'name': 'a', 'hide_sub': False}]
        s = self._seq(r'_(\d{3})$', r'_(\d{3})$', items, [{'vendor_Filename': 'a'}])
        with self.assertLogs('SubmissionHelper', level='WARNING'):
            s.vendor_csv_add()
        self.assertTrue(items[0]['vendor_ignore_sub'])

    def test_pairing_and_skip_by_per_file(self):
        items = [{'name': 'a', 'shot': 'sh010', 'hide_sub': False},
                 {'name': 'b', 'shot': 'sh020', 'hide_sub': False},
                 {'name': 'c', 'shot': 'sh030', 'hide_sub': False}]
        rows = [{'vendor_Filename': 'a'}, {'vendor_Filename': 'b'}]
        s = self._seq('{name}', '{vendor_Filename}', items, rows,
                      vendor_csv_skip=True, vendor_csv_skip_what='sh020')
        s.vendor_csv_add()
        self.assertEqual([i['vendor_ignore_sub'] for i in items], [False, True, True])
        self.assertEqual([i['vendor_skip'] for i in items], [False, True, True])


class Rename(unittest.TestCase):

    def test_regex_count_in_pattern_works(self):
        item = {'category': 'video', 'path_prs': '/p/0x0', 'name': 'sh010_v001',
                'width': 1920, 'height': 1080}
        s = make_seq({}, [item])
        s.renames = [{'filter': '', 'src': 1, 'pattern': r'_v(\d{3})$', 'repl': r'_ver\1'}]
        s.rename_preprocess()
        self.assertEqual(item['rename'], '/p/0x0/sh010_ver001')

    def test_stale_rename_source_is_cleared(self):
        item = {'category': 'video', 'path_prs': '/p', 'name': 'a', 'rename_source': '/old'}
        s = make_seq({}, [item])
        s.renames = []
        s.rename_preprocess()
        self.assertEqual(item['rename'], '')
        self.assertNotIn('rename_source', item)


class Converts(unittest.TestCase):

    def _seq(self, items):
        values = {'package_folder': '/pkg'}
        for n in range(1, 9):
            values.update({f'thumbs_if_{n:02d}': '', f'thumbs_exe_{n:02d}': '',
                           f'thumbs_args_{n:02d}': '', f'thumbs_name_{n:02d}': ''})
        values.update({'thumbs_if_01': "'{extension}' == 'mov'", 'thumbs_exe_01': 'A',
                       'thumbs_args_01': 'a {name}', 'thumbs_name_01': '/pkg/a_{name}.jpg',
                       'thumbs_exe_02': 'B', 'thumbs_args_02': 'b {name}',
                       'thumbs_name_02': '/pkg/b_{name}.jpg'})
        s = make_seq(values, items)
        s.paths = {'ffmpeg': '', 'ffprobe': '', 'oiiotool': '', 'ocio': '', 'vfx-transcode': ''}
        return s

    def test_commands_keep_their_convert_number_and_dont_pile_up(self):
        item = {'extension': 'exr', 'name': 'sh010'}
        s = self._seq([item])
        s.prepare_converts()
        s.prepare_converts()
        # row 01 is filtered out for exr: row 02 must stay paired with path 02
        self.assertEqual(item['convert_cmd'], {'02': 'B b sh010'})
        self.assertIsNone(item['convert_path01'])
        self.assertEqual(item['convert_path02'], '/pkg/b_sh010.jpg')
        self.assertEqual(item['convert_path_relative02'], 'b_sh010.jpg')


class Parsing(unittest.TestCase):

    def _regex(self, key, pattern, source='{name}', repl='', flt=''):
        import re
        return {'key': key, 'filter': flt, 'source': source, 'repl': repl,
                'compiled': re.compile(pattern)}

    def test_filtered_row_leaves_no_old_value(self):
        item = {'name': 'sh010_comp', 'path': '/p/sh010_comp.exr'}
        s = make_seq({}, [item])
        s.regexes = {'01': self._regex('shot', '^([^_]+)')}
        s.fill_regexes()
        self.assertEqual(item['shot'], 'sh010')
        # the row now applies to mov files only: the exr has no shot any more
        s.regexes = {'01': self._regex('shot', '^([^_]+)', flt='.mov')}
        s.fill_regexes()
        self.assertNotIn('shot', item)

    def test_overwritten_builtin_token_is_restored(self):
        item = {'name': 'sh010_comp', 'path': '/p/x'}
        s = make_seq({}, [item])
        s.regexes = {'01': self._regex('name', '^([^_]+)')}
        s.fill_regexes()
        s.fill_regexes()
        self.assertEqual(item['name'], 'sh010')     # parsed from the original, not from 'sh010'
        s.regexes = {}
        s.fill_regexes()
        self.assertEqual(item['name'], 'sh010_comp')

    def test_stray_brace_in_source_does_not_crash(self):
        item = {'name': 'sh010', 'path': '/p/x'}
        s = make_seq({}, [item])
        s.regexes = {'01': self._regex('x', '(.*)', source='{name} {')}
        s.fill_regexes()
        self.assertEqual(item['x'], 'sh010 {')


class Sidecars(unittest.TestCase):

    def test_row_6_filter_and_refresh(self):
        values = {'side_sub_only': False, 'side_log_only': False}
        for n in range(1, 7):
            values.update({f'side_pattern_{n}': '', f'side_repl_{n}': '', f'side_match_{n}': '',
                           f'side_dest_{n}': '', f'side_filter_{n}': ''})
        values.update({'side_pattern_6': r'^(\w+?)_', 'side_match_6': '{shot}',
                       'side_dest_6': '/out/{sidecar_file_noext}.{sidecar_ext}',
                       'side_filter_6': '.cdl'})
        item = {'shot': 'sh010'}
        s = make_seq(values, [item])
        s.sidecars = ['/lib/sh010_grade.cdl', '/lib/sh010_grade.txt']
        s.sidecar_files_filter()
        s.sidecar_files_filter()          # a refresh must not add it twice
        self.assertEqual(item['sidecars'], [
            {'result': 'sh010', 'file': '/lib/sh010_grade.cdl', 'dest': '/out/sh010_grade.cdl'}])
        s.sidecars = []
        s.sidecar_files_filter()          # no sidecar files any more: no old matches
        self.assertEqual(item['sidecars'], [])


class FileSizes(unittest.TestCase):

    def setUp(self):
        self.root = tempfile.mkdtemp().replace('\\', '/')

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def _item(self, sizes):
        for frame, size in sizes.items():
            with open(f"{self.root}/a.{frame:04d}.exr", 'wb') as f:
                f.write(b'x' * size)
        frames = sorted(sizes)
        return {'category': 'sequence', 'path_prs': self.root, 'clean_name': 'a.',
                'extension': 'exr', 'padding': 4, 'start_number': frames[0],
                'end_number': frames[-1],
                'missing_numbers': [n for n in range(frames[0], frames[-1] + 1) if n not in sizes]}

    def _seq(self, item, **over):
        values = {'check_sequence_size_consistency': True, 'check_sequence_holes': True,
                  'prefs_size_scan': True, 'prefs_size_ignore_first': 1,
                  'prefs_size_neighborhood': 2, 'prefs_size_threshold': 30}
        values.update(over)
        return make_seq(values, [item])

    def test_inconsistent_frame_number_is_right(self):
        sizes = {f: 1000 for f in range(1001, 1011)}
        sizes[1006] = 100
        item = self._item(sizes)
        self._seq(item, prefs_size_ignore_first=2).get_file_sizes()
        self.assertIn('[1006]', item['size_warning'])

    def test_frame_number_right_with_holes(self):
        sizes = {f: 1000 for f in range(1001, 1011) if f != 1003}
        sizes[1008] = 100
        item = self._item(sizes)
        self._seq(item).get_file_sizes()
        self.assertIn('1 missing files: [1003]', item['size_warning'])
        self.assertIn('[1008]', item['size_warning'])

    def test_checks_can_be_turned_off(self):
        sizes = {f: 1000 for f in range(1001, 1011) if f != 1003}
        sizes[1008] = 100
        item = self._item(sizes)
        self._seq(item, check_sequence_size_consistency=False,
                  check_sequence_holes=False).get_file_sizes()
        self.assertEqual(item['size_warning'], '')
        self.assertGreater(item['size_bytes'], 0)


class TimeCode(unittest.TestCase):

    def _meta(self, category, from_meta, from_seq, counter=False, default='01:00:00:00'):
        m = metadata.MetaData.__new__(metadata.MetaData)
        m.item = {'category': category}
        m.meta = {'time_code_from_metadata': from_meta, 'time_code_from_seq': from_seq}
        m.tc_from_counter = counter
        m.default_tc = default
        return m

    def test_from_metadata_first(self):
        self.assertEqual(self._meta('sequence', '10:00:00:00', '00:00:41:16').pick_time_code(),
                         '10:00:00:00')

    def test_from_frame_counter(self):
        self.assertEqual(self._meta('sequence', '10:00:00:00', '00:00:41:16', counter=True)
                         .pick_time_code(), '00:00:41:16')

    def test_default_for_video_without_timecode(self):
        self.assertEqual(self._meta('video', '', '').pick_time_code(), '01:00:00:00')

    def test_still_keeps_empty_timecode(self):
        self.assertEqual(self._meta('still', '', '').pick_time_code(), '')


class Presets(unittest.TestCase):

    def test_install_example_is_not_a_preset(self):
        d = tempfile.mkdtemp()
        try:
            for n in ('install.json', 'install.example.json', 'clientX.json'):
                open(os.path.join(d, n), 'w').close()
            found = [os.path.basename(p) for p in settings_module.Settings._find_in_dir(d)]
            self.assertEqual(found, ['clientX.json'])
        finally:
            shutil.rmtree(d, ignore_errors=True)


class AyonListExport(unittest.TestCase):

    def _list(self, do_csv, do_excel):
        a = ayon_shotlist.AyonShotlist.__new__(ayon_shotlist.AyonShotlist)
        a.log = logging.getLogger('SubmissionHelper')
        self.dir = tempfile.mkdtemp()
        a.data = [{'Folder Name': 'sh010', '_hide': False}]
        a.columns = ['Folder Name', '_hide']
        a.do_output = True
        a.do_output_csv = do_csv
        a.do_output_excel = do_excel
        a.output_csv_path = os.path.join(self.dir, 'ayon-list.csv')
        a.output_excel_path = os.path.join(self.dir, 'ayon-list.xlsx')
        return a

    def tearDown(self):
        shutil.rmtree(self.dir, ignore_errors=True)

    def test_csv_off_excel_on_writes_no_csv(self):
        a = self._list(False, True)
        a._write_rows_excel = lambda path, columns, rows, what: open(path, 'w').close()
        a.write_csv()
        self.assertFalse(os.path.exists(a.output_csv_path))
        self.assertTrue(os.path.exists(a.output_excel_path))

    def test_both_off_still_writes_csv(self):
        a = self._list(False, False)
        a.write_csv()
        with open(a.output_csv_path, encoding='utf-8-sig') as f:
            self.assertEqual(list(csv.reader(f)), [['Folder Name'], ['sh010']])


class Exports(unittest.TestCase):

    def test_spreadsheet_with_excel_and_csv_off_is_skipped_quietly(self):
        s = make_seq({})
        s.export_file_names = {'log': {'do_excel': False, 'do_csv': False}}
        with self.assertNoLogs('SubmissionHelper', level='ERROR'):
            self.assertIsNone(s.export_spreadsheet('log', [], []))


if __name__ == '__main__':
    unittest.main()
