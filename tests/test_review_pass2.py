"""
Second fixing pass (claude/bug_review_fix_plan.md): crashes, wrong or lost
data, speed / cleanup, Ayon publish Deadline argument quoting.
"""
import logging
import os
import shutil
import stat
import struct
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

from tests import _stubs  # noqa: F401
import ayon_publish
import ayon_shotlist
import helpers
import metadata
import parse_file_name
import parse_metadata
import sequencer
from submission_helper import setting_to_bool


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


class TimecodeHelpers(unittest.TestCase):

    def test_drop_frame_timecode(self):
        # 29.97 DF: one hour is 107892 frames, 00:01:00;02 is frame 1800
        self.assertEqual(helpers.tc_to_frames('01:00:00;00', 30000, 1001), 107892)
        self.assertEqual(helpers.tc_to_frames('00:01:00;02', 30000, 1001), 1800)

    def test_non_drop_and_fps_text(self):
        self.assertEqual(helpers.tc_to_frames('01:00:00:00', 24, 1), 86400)
        # vendor csv passes the fps as text, 23.976 counts as 24
        self.assertEqual(helpers.tc_to_frames('00:00:41:16', '23.976', '1'), 1000)
        self.assertEqual(helpers.frames_to_tc(1001, '23.976', '1'), '00:00:41:17')

    def test_bad_timecode_raises_value_error(self):
        with self.assertRaises(ValueError):
            helpers.tc_to_frames('garbage', 24, 1)

    def test_ffmpeg_time_milliseconds_padded(self):
        self.assertEqual(helpers.frames_to_ffmpeg_tc(1, 25), '00:00:00.040')
        self.assertEqual(helpers.frames_to_ffmpeg_tc(90001, 25), '01:00:00.040')

    def test_frames_to_seconds(self):
        self.assertEqual(helpers.frames_to_seconds(12, 24), '0.5')
        self.assertEqual(helpers.frames_to_seconds(24, '24000/1001'), '1.001')


def _exr(path, attributes, magic=20000630, end=True):
    with open(path, 'wb') as f:
        f.write(struct.pack('<i', magic) + bytes([2, 0, 0, 0]))
        for name, typ, value in attributes:
            f.write(name + b'\0' + typ + b'\0' + struct.pack('<i', len(value)) + value)
        if end:
            f.write(b'\0')


class ExrHeader(unittest.TestCase):

    def setUp(self):
        self.dir = tempfile.mkdtemp()
        self.path = os.path.join(self.dir, 'a.exr')
        # 01:00:00:12, BCD
        self.tc = struct.pack('<II', 2 | (1 << 4) | (1 << 24), 0)

    def tearDown(self):
        shutil.rmtree(self.dir, ignore_errors=True)

    def test_unknown_type_is_skipped_rest_is_read(self):
        _exr(self.path, [
            (b'weird', b'myCustomType', b'12345'),
            (b'timeCode', b'timecode', self.tc),
            (b'owner', b'string', b'me'),
        ])
        meta = parse_metadata.read_exr_header(self.path)
        self.assertNotIn('weird', meta)
        self.assertEqual(meta['timeCode']['timeAndFlags'], 2 | (1 << 4) | (1 << 24))
        self.assertEqual(meta['owner'], 'me')

    def test_truncated_file_returns_what_was_read(self):
        _exr(self.path, [(b'owner', b'string', b'me')], end=False)
        with open(self.path, 'ab') as f:
            f.write(b'timeCode\0time')       # cut in the middle
        self.assertEqual(parse_metadata.read_exr_header(self.path), {'owner': 'me'})

    def test_not_an_exr(self):
        _exr(self.path, [], magic=1234)
        with self.assertRaises(ValueError):
            parse_metadata.read_exr_header(self.path)

    def test_timecode_without_frame_rate(self):
        # many EXRs have a timeCode but no framesPerSecond: the timecode was lost
        _exr(self.path, [(b'timeCode', b'timecode', self.tc)])
        m = metadata.MetaData.__new__(metadata.MetaData)
        m.meta = {'file': self.path}
        out = m.read_metadata_from_exr_header()
        self.assertEqual(out['time_code'], '01:00:00:12')
        self.assertNotIn('fps_a', out)


def _dpx(path, big_endian=True):
    e = '>' if big_endian else '<'
    buf = bytearray(2048)
    buf[0:4] = b'SDPX' if big_endian else b'XPDS'
    buf[160:160 + 7] = b'Nuke 15'
    buf[260:260 + 4] = b'PROJ'
    buf[772:780] = struct.pack(e + 'II', 2048, 1080)
    buf[801] = 1                          # printing density: log
    buf[1556:1556 + 5] = b'A001C'
    buf[1628:1636] = struct.pack(e + 'II', 1, 1)
    buf[1724:1728] = struct.pack(e + 'f', 24.0)
    # 01:02:03:04 BCD, most significant byte = hours
    buf[1920:1924] = struct.pack(e + 'I', 0x01020304)
    with open(path, 'wb') as f:
        f.write(bytes(buf))


class DpxHeader(unittest.TestCase):

    def setUp(self):
        self.dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.dir, ignore_errors=True)

    def _read(self, big_endian):
        path = os.path.join(self.dir, 'a.dpx')
        _dpx(path, big_endian)
        m = metadata.MetaData.__new__(metadata.MetaData)
        m.meta = {'file': path}
        return m.read_metadata_from_dpx()

    def test_big_and_little_endian(self):
        # bytes were compared to str: every DPX was "not DPX"
        for big in (True, False):
            out = self._read(big)
            self.assertEqual(out['error'], '')
            self.assertEqual((out['width'], out['height']), (2048, 1080))
            self.assertEqual(out['creator'], 'Nuke 15')
            self.assertEqual(out['reel'], 'A001C')
            self.assertEqual(out['time_code'], '01:02:03:04')
            self.assertEqual((out['fps_a'], out['fps_b']), (24, 1))
            self.assertTrue(out['is_log'])

    def test_not_dpx(self):
        path = os.path.join(self.dir, 'b.dpx')
        with open(path, 'wb') as f:
            f.write(b'\0' * 2048)
        m = metadata.MetaData.__new__(metadata.MetaData)
        m.meta = {'file': path}
        self.assertIn('not DPX', m.read_metadata_from_dpx()['error'])


class OiioValues(unittest.TestCase):

    def test_matrix_is_row_major(self):
        m = metadata.MetaData.__new__(metadata.MetaData)
        out = m.convert_value_by_type_name('matrix', '1,2,3,4,5,6,7,8,9')
        self.assertEqual(out, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])


FAKE_FFPROBE = """#!/bin/sh
cat <<XML
<ffprobe><streams>
<stream codec_type="video" width="10" height="2" r_frame_rate="25/1" duration="2.0" duration_ts="256000"/>
</streams>
<format><tag key="timecode" value="10:00:00:00"/></format></ffprobe>
XML
"""


@unittest.skipIf(sys.platform == 'win32', 'uses a shell script as fake ffprobe')
class FfprobeValues(unittest.TestCase):

    def test_frames_from_duration_and_format_timecode(self):
        with tempfile.TemporaryDirectory() as d:
            exe = os.path.join(d, 'ffprobe')
            with open(exe, 'w') as f:
                f.write(FAKE_FFPROBE)
            os.chmod(exe, os.stat(exe).st_mode | stat.S_IEXEC)
            m = metadata.MetaData.__new__(metadata.MetaData)
            m.meta = {'file': os.path.join(d, 'a.mov')}
            m.ffprobe_path = exe
            out = m.probe_ffprobe()
        self.assertEqual(out['error'], '')
        # duration_ts (time base units) used to be taken as the frame count
        self.assertEqual(out['duration_frames'], 50)
        self.assertEqual(out['fps'], 25.0)
        self.assertEqual(out['time_code'], '10:00:00:00')


class GuiFrameRateFallback(unittest.TestCase):

    def test_sequence_without_fps_uses_preferences_rate(self):
        m = metadata.MetaData.__new__(metadata.MetaData)
        m.item = {'extension': 'jpg', 'category': 'sequence', 'number': 1001, 'start_number': 1001}
        m.meta = {'file': 'x.1001.jpg', 'fps_str': '', 'fps_a': 0, 'fps_b': 0, 'fps': 0.0, 'time_code': ''}
        m.gui_force_fps = False
        m.gui_fps = '25'
        m._MetaData__fix_fps()
        self.assertEqual(m.meta['fps_str'], '25')
        self.assertEqual((m.meta['fps_a'], m.meta['fps_b']), (25, 1))
        # so the frame counter timecode works
        self.assertEqual(m.get_source_tc_start('filename'), '00:00:40:01')


class Columns(unittest.TestCase):

    def test_one_column_per_line_and_clean_titles(self):
        s = make_seq()
        titles, exprs = s.prepare_columns("Shot = {shot}\nPath={path}, Note = a=b\n")
        self.assertEqual(titles, ['Shot', 'Path', 'Note'])
        self.assertEqual(exprs, ['{shot}', '{path}', 'a=b'])


class Counters(unittest.TestCase):

    def test_empty_package_totals(self):
        s = make_seq({'prefs_counter_start': 1})
        s.filter_items_add_counters()       # UnboundLocalError before
        self.assertEqual(s.static_keywords['total_sub'], 0)

    def test_counter_start_zero(self):
        items = [{'path': '/a', 'category': 'video'}, {'path': '/b', 'category': 'video'}]
        s = make_seq({'prefs_counter_start': 0, 'prefs_counter_step': 1, 'prefs_counter_zeroes': 2}, items)
        s.filter_items_add_counters()
        self.assertEqual([i['cnt_sub'] for i in items], ['00', '01'])


class ParseRows(unittest.TestCase):

    def test_pattern_without_group_gives_whole_match(self):
        item = {'path': '/x/sh010_comp_v003.exr', 'name': 'sh010_comp_v003'}
        s = make_seq({'parse_name_01': 'ver', 'parse_pattern_01': r'v\d{3}',
                      'parse_source_01': '{name}'}, [item])
        s.prepare_regex()
        s.fill_regexes()
        self.assertEqual(item['ver'], 'v003')


class ReplaceRules(unittest.TestCase):

    def test_every_rule_is_kept(self):
        item = {'extension': 'nk', 'full_path': '/a/comp.nk'}
        s = make_seq({}, [item])
        s.replace_data = [{'Extension': 'nk', 'Search': 'a', 'Replace': 'b'},
                          {'Extension': 'nk', 'Search': 'c', 'Replace': 'd'},
                          {'Extension': 'nk', 'Search': 'e', 'Replace': 'f'}]
        s.csv_replace_prepare()
        self.assertEqual(len(s.replace_prep['/a/comp.nk']), 3)


class VendorCsv(unittest.TestCase):

    def _seq(self, rows, prefs, items):
        s = make_seq({'vendor_csv_package_key': '{name}', 'vendor_csv_vendor_key': '{vendor_File}',
                      'vendor_csv_ignore': False, 'vendor_csv_skip_by': '', 'vendor_csv_skip_what': '',
                      'vendor_csv_skip': False}, items)
        s.vendor_csv_transformed = rows
        s.vendor_csv_prefs_repre = prefs
        return s

    def test_no_self_reference_after_two_passes(self):
        item = {'name': 'sh010', 'extension': 'exr'}
        rows = [{'vendor_File': 'sh010', 'vendor_row_errors': []}]
        s = self._seq(rows, {}, [item])
        s.vendor_csv_add()
        s.vendor_csv_add()
        self.assertNotIn('merged_item', item)

    def test_task_set_stored_and_errors_are_text(self):
        prefs = {'merge_repres_by': '{vendor_Shot}', 'repres': [],
                 'task_intent_repres': {'comp': [{'intents': ['WIP'], 'always': ['exr', 'review'],
                                                  'optional': []}]}}
        rows = [{'vendor_Shot': 'sh010', 'vendor_Task': 'comp', 'vendor_Intent': 'WIP',
                 'vendor_Output': 'exr', 'vendor_row_errors': []},
                {'vendor_Shot': 'sh010', 'vendor_Task': 'comp', 'vendor_Intent': 'WIP',
                 'vendor_Output': 'mov', 'vendor_row_errors': []}]
        s = self._seq(rows, prefs, [])
        s.vendor_csv_repre_checks()
        self.assertEqual(rows[0]['vendor_One_task_set']['always'], ['exr', 'review'])
        self.assertIsInstance(rows[0]['vendor_row_errors'], str)
        self.assertIn('review', rows[0]['vendor_row_errors'])           # required but missing
        # undefined: present in the group, not defined for the task (was reversed)
        self.assertIn('undefined in task_intent_repres: mov', rows[0]['vendor_row_errors'])


class Sequences(unittest.TestCase):

    def test_sub_sequences_are_separate(self):
        s = make_seq()
        files = [f'/p/a.{n:04d}.exr' for n in (1, 2, 3, 7, 8)]
        out = s.seq_list_from_file_list(files, mode='to_subsequences')
        self.assertEqual([(o['start_number'], o['end_number']) for o in out], [(1, 3), (7, 8)])

    def test_walk_dirs_file_and_missing(self):
        s = make_seq()
        with tempfile.TemporaryDirectory() as d:
            f = os.path.join(d, 'one.mov')
            open(f, 'w').close()
            os.makedirs(os.path.join(d, 'sub'))
            open(os.path.join(d, 'sub', 'other.mov'), 'w').close()
            self.assertEqual(s.walk_dirs(f), [f])
            # a missing path doesn't scan its parent folder
            self.assertEqual(s.walk_dirs(os.path.join(d, 'sub', 'typo') + '/'), [])
            self.assertEqual(len(s.walk_dirs(d + '/')), 2)

    def test_upper_case_extension_category(self):
        s = make_seq()
        out = s.other_files_from_file_list(['/p/sound.WAV'])
        self.assertEqual(out[0]['category'], 'audio')


class Exports(unittest.TestCase):

    def test_failed_write_is_logged_not_raised(self):
        s = make_seq()
        s.export_file_names = {'sub': {'do_excel': False, 'do_csv': True, 'do_skip': False, 'skip': '',
                                       'do_split': False, 'split': '', 'num': 3,
                                       'export_root': '/nonexistent/dir/for/sure/out'}}
        with self.assertLogs('SubmissionHelper', level='ERROR'):
            s.export_spreadsheet('sub', [['a', {}]], ['A'])

    def test_sidecar_copy_error_is_logged(self):
        s = make_seq()
        s.table_side = [['m', '/nonexistent/x/y.cdl', '/nonexistent/src.cdl']]
        with self.assertLogs('SubmissionHelper', level='ERROR'):
            s.sidecar_files_copy()


class DeadlineQuoting(unittest.TestCase):

    def _publisher(self):
        settings = {k: {'value': v} for k, v in {
            'dead_primpool': 'pool a', 'dead_group': None, 'dead_priority': 50,
            'dead_department': '', 'dead_limits': ''}.items()}
        paths = {'deadline': 'deadlinecommand', 'ayon': 'C:/ayon/ayon.exe',
                 'FTRACK_SERVER': 'srv', 'FTRACK_API_KEY': 'secret', 'FTRACK_API_USER': 'u',
                 'AYON_USERNAME': 'u', 'AYON_API_KEY': 'k', 'AYON_SERVER_URL': 'x'}
        a = ayon_publish.AyonPublish(settings, paths)
        a.build_ayon_csv_command('D:/My Shows/sub 01.csv', 'Big Project', '/ep 01/sh010', 'comp final')
        return a

    def test_arguments_with_spaces_stay_one_argument(self):
        a = self._publisher()
        captured = {}
        with mock.patch.object(a, 'external_execute', lambda args: captured.setdefault('args', args) and 0):
            a.publish_deadline()
        args = captured['args']
        joined = args[args.index('-arguments') + 1]
        self.assertIn('"D:/My Shows/sub 01.csv"', joined)
        self.assertIn('"Big Project"', joined)
        self.assertIn('"/ep 01/sh010"', joined)
        self.assertIn('"comp final"', joined)
        # None settings are sent as text, Popen can't take None
        self.assertTrue(all(isinstance(x, str) for x in args))

    def test_local_publish_does_not_touch_os_environ(self):
        a = self._publisher()
        before = os.environ.get('FTRACK_API_KEY')
        fake = mock.MagicMock()
        fake.communicate.return_value = ('', '')
        fake.returncode = 0
        with mock.patch.object(subprocess, 'Popen', return_value=fake) as popen:
            a.publish_local()
        self.assertEqual(os.environ.get('FTRACK_API_KEY'), before)
        self.assertEqual(popen.call_args.kwargs['env']['FTRACK_API_KEY'], 'secret')


class AyonShotlistFixes(unittest.TestCase):

    def test_failed_connection_keeps_attributes(self):
        gui = {'project': 'P', 'prefix': '', 'do_thumbs': False, 'out_folder': '',
               'filter_matched': False, 'do_csv': False, 'do_excel': False}
        with mock.patch.object(ayon_shotlist.ayon_api, 'get_server_api_connection',
                               side_effect=RuntimeError('down'), create=True):
            a = ayon_shotlist.AyonShotlist(gui, None, {'AYON_SERVER_URL': '', 'AYON_API_KEY': ''})
        self.assertTrue(a.error)
        self.assertEqual(a.data, [])
        self.assertEqual(a.get_shotlist(), [])

    def test_links_in_one_query(self):
        class Fake:
            calls = []

            def get_folders_links(self, project, folder_ids=None, link_direction=None):
                self.calls.append('batch')
                return {'f1': [{'entityId': 'f2', 'entityType': 'folder'}], 'f2': []}

            def get_folder_links(self, *a, **k):
                self.calls.append('single')
                return []

            def get_folders(self, project, folder_ids=None, fields=None):
                return [{'id': 'f2', 'name': 'asset_tree'}]

        a = ayon_shotlist.AyonShotlist.__new__(ayon_shotlist.AyonShotlist)
        a.log = logging.getLogger('test')
        a.project = 'P'
        a.ayon = Fake()
        out = a._links_by_folder(['f1', 'f2'])
        self.assertEqual(out, {'f1': ['asset_tree'], 'f2': []})
        self.assertEqual(Fake.calls, ['batch'])


class SmallFixes(unittest.TestCase):

    def test_setting_to_bool(self):
        for v in ('False', 'false', '0', '', 'off', False, 0, None):
            self.assertFalse(setting_to_bool(v), v)
        for v in ('True', 'true', '1', True, 1):
            self.assertTrue(setting_to_bool(v), v)

    def test_parse_file_name(self):
        self.assertEqual(parse_file_name.parse('/a/shot-0001.exr')['clean_name_sep_char'], '-')
        self.assertEqual(parse_file_name.path_from_path_and_number('/a/b.0001.exr', 7), '/a/b.0007.exr')
        self.assertEqual(parse_file_name.printf_pattern('/a/b.1001.exr')[0], 'b.%d.exr')
        self.assertEqual(parse_file_name.printf_pattern('/a/b.0001.exr')[0], 'b.%04d.exr')

    def test_ayon_max_version_with_text(self):
        self.assertEqual(sequencer.Sequencer._version_number('v007'), 7)
        self.assertEqual(sequencer.Sequencer._version_number(None), 0)


if __name__ == '__main__':
    unittest.main()
