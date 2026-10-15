import csv
import os
import tempfile
import unittest
from unittest import mock

from tests import _stubs  # noqa: F401
import ayon_shotlist
from ayon_shotlist import parse_product_filters, pick_versions, AyonShotlist


class ParseFiltersTest(unittest.TestCase):
    def test_examples(self):
        f = parse_product_filters("comp:renderCompMain:exr, :platePl01:exr")
        self.assertEqual(f[0], {'task': 'comp', 'product': 'renderCompMain', 'repre': 'exr',
                                'text': 'comp:renderCompMain:exr'})
        self.assertEqual((f[1]['task'], f[1]['product'], f[1]['repre']), ('', 'platePl01', 'exr'))

    def test_separators_and_short_forms(self):
        f = parse_product_filters("platePl01:exr; renderMain\n\n , :x:")
        self.assertEqual([(x['task'], x['product'], x['repre']) for x in f],
                         [('', 'platePl01', 'exr'), ('', 'renderMain', ''), ('', 'x', '')])

    def test_empty(self):
        self.assertEqual(parse_product_filters(''), [])
        self.assertEqual(parse_product_filters('comp::exr'), [])   # no product


def data_set():
    products = [
        {'id': 'p1', 'name': 'renderCompMain', 'folderId': 'f1', 'productType': 'render'},
        {'id': 'p2', 'name': 'platePl01', 'folderId': 'f1', 'productType': 'plate'},
        {'id': 'p3', 'name': 'platePl01', 'folderId': 'f2', 'productType': 'plate'},
        {'id': 'p4', 'name': 'renderCompMain', 'folderId': 'f3', 'productType': 'render'},
    ]
    versions = {
        'p1': {'id': 'v1', 'version': 7, 'taskId': 't_comp', 'author': 'ann', 'status': 'Approved',
               'createdAt': '2026-10-01T10:00:00', 'attrib': {'comment': 'final'}},
        'p2': {'id': 'v2', 'version': 2, 'taskId': None},
        'p3': {'id': 'v3', 'version': 1, 'taskId': None},
        'p4': {'id': 'v4', 'version': 3, 'taskId': 't_light'},
    }
    repres = [
        {'id': 'r1', 'name': 'exr', 'versionId': 'v1', 'attrib': {'path': '{root[work]}/sh010/v007.exr'}},
        {'id': 'r1b', 'name': 'mov', 'versionId': 'v1'},
        {'id': 'r2', 'name': 'exr', 'versionId': 'v2'},
        {'id': 'r3', 'name': 'mov', 'versionId': 'v3'},
        {'id': 'r4', 'name': 'exr', 'versionId': 'v4'},
    ]
    tasks = {'t_comp': 'comp', 't_light': 'lighting'}
    return products, versions, repres, tasks


class PickVersionsTest(unittest.TestCase):
    def test_first_filter_wins_and_fallback(self):
        products, versions, repres, tasks = data_set()
        filters = parse_product_filters("comp:renderCompMain:exr, :platePl01:exr")
        got = pick_versions(['f1', 'f2', 'f3', 'f4'], products, versions, repres, tasks, filters)
        # f1: preferred render exists
        self.assertEqual(got['f1']['Product'], 'renderCompMain')
        self.assertEqual(got['f1']['Version'], '7')
        self.assertEqual(got['f1']['Version Name'], 'v007')
        self.assertEqual(got['f1']['Version Task'], 'comp')
        self.assertEqual(got['f1']['Version Comment'], 'final')
        self.assertEqual(got['f1']['Representation'], 'exr')
        self.assertEqual(got['f1']['Repre Path'], '{root[work]}/sh010/v007.exr')
        self.assertEqual(got['f1']['Version Filter'], 'comp:renderCompMain:exr')
        # f2: plate has only mov -> no exr match
        self.assertNotIn('f2', got)
        # f3: render from lighting, not comp -> task filter rejects, no plate
        self.assertNotIn('f3', got)
        self.assertNotIn('f4', got)

    def test_wildcards_and_any_repre(self):
        products, versions, repres, tasks = data_set()
        got = pick_versions(['f2', 'f3'], products, versions, repres, tasks,
                            parse_product_filters(":PLATE*, render*:exr"))
        self.assertEqual(got['f2']['Product'], 'platePl01')
        self.assertEqual(got['f2']['Representation'], 'mov')   # any repre
        self.assertEqual(got['f3']['Version Task'], 'lighting')

    def test_highest_version_within_filter(self):
        products = [{'id': 'a', 'name': 'plateA', 'folderId': 'f'},
                    {'id': 'b', 'name': 'plateB', 'folderId': 'f'}]
        versions = {'a': {'id': 'va', 'version': 4}, 'b': {'id': 'vb', 'version': 9}}
        got = pick_versions(['f'], products, versions, [], {}, parse_product_filters('plate*'))
        self.assertEqual(got['f']['Product'], 'plateB')


class FakeAyon:
    def __init__(self, fail_fields=False):
        self.fail_fields = fail_fields
        self.calls = []
        p, v, r, t = data_set()
        self.p, self.v, self.r, self.t = p, v, r, t

    def get_folders(self, project, fields=None):
        return [
            {'name': 'sh010', 'id': 'f1', 'path': '/ep01/sh010', 'type': 'Shot', 'label': None,
             'status': 'In progress', 'hasTasks': True, 'attrib': attrib(), 'thumbnailId': None},
            {'name': 'sh010', 'id': 'f2', 'path': '/ep02/sh010', 'type': 'Shot', 'label': None,
             'status': 'Ready', 'hasTasks': False, 'attrib': attrib(), 'thumbnailId': None},
        ]

    def get_folder_links(self, *a, **k):
        return []

    def get_tasks(self, project, folder_ids=None, fields=None):
        return [{'name': 'comp', 'id': 't_comp', 'type': 'Compositing', 'label': None,
                 'assignees': ['ann', 'bob'], 'status': 'WIP', 'attrib': attrib(), 'thumbnailId': None}]

    def _maybe_fail(self, fields):
        if self.fail_fields and fields is not None:
            raise ValueError("unknown field")

    def get_products(self, project, folder_ids=None, product_names=None, fields=None):
        self._maybe_fail(fields)
        self.calls.append(('products', sorted(product_names or [])))
        return [p for p in self.p if p['folderId'] in folder_ids
                and (not product_names or p['name'] in product_names)]

    def get_last_versions(self, project, product_ids, fields=None):
        self._maybe_fail(fields)
        return {k: v for k, v in self.v.items() if k in product_ids}

    def get_representations(self, project, version_ids=None, representation_names=None, fields=None):
        self._maybe_fail(fields)
        return [r for r in self.r if r['versionId'] in version_ids
                and (not representation_names or r['name'] in representation_names)]


def attrib():
    return {'frameStart': 1001, 'frameEnd': 1100, 'handleStart': 8, 'handleEnd': 8,
            'resolutionWidth': 1920, 'resolutionHeight': 1080, 'pixelAspect': 1,
            'clipIn': 1, 'clipOut': 100}


def gui(out, **kw):
    g = {'project': 'P', 'prefix': 'ayon_', 'do_thumbs': False, 'out_folder': out,
         'filter_matched': False, 'do_csv': True, 'do_excel': False,
         'filter_assets': True, 'filter_shots': True, 'filter_tasks': True, 'filter_other': True,
         'filter_tasktype': False, 'filter_tasktypes': [], 'filter_assignee': False,
         'filter_assignees': [], 'do_versions': True,
         'product_filters': parse_product_filters("comp:renderCompMain:exr, :platePl01:exr")}
    g.update(kw)
    return g


class ShotlistWithVersionsTest(unittest.TestCase):
    def run_list(self, fake, **kw):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        out = os.path.join(tmp.name, 'new', 'out')
        with mock.patch.object(ayon_shotlist.ayon_api, 'get_server_api_connection', return_value=fake, create=True):
            a = AyonShotlist(gui(out, **kw), None, {'AYON_SERVER_URL': 'x', 'AYON_API_KEY': 'y'})
            rows = a.get_shotlist()
        return a, rows, out

    def test_versions_on_folder_and_task_rows(self):
        a, rows, out = self.run_list(FakeAyon())
        self.assertIsNone(a.error)
        # two folders with the same name are both kept now
        self.assertEqual(sorted(r['Folder Path'] for r in rows if r['Task Name'] == ''),
                         ['/ep01/sh010', '/ep02/sh010'])
        sh1 = [r for r in rows if r['Folder Path'] == '/ep01/sh010']
        self.assertEqual({r['Version'] for r in sh1}, {'7'})          # folder + comp task row
        sh2 = [r for r in rows if r['Folder Path'] == '/ep02/sh010'][0]
        self.assertEqual(sh2['Version'], '')                         # plate has no exr
        self.assertEqual(sh2['Folder Status'], 'Ready')
        # exact names -> narrowed queries
        self.assertIn(('products', ['platePl01', 'renderCompMain']), a.ayon.calls)
        # csv: output folder created, version columns written, no internal columns
        a.write_csv()
        with open(os.path.join(out, 'list.csv'), encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            written = list(reader)
        self.assertIn('Version', reader.fieldnames)
        self.assertNotIn('_folder_id', reader.fieldnames)
        self.assertNotIn('_hide', reader.fieldnames)
        self.assertEqual(len(written), 3)

    def test_fields_fallback(self):
        a, rows, _ = self.run_list(FakeAyon(fail_fields=True))
        self.assertEqual({r['Version'] for r in rows if r['Folder Path'] == '/ep01/sh010'}, {'7'})

    def test_versions_off_no_columns(self):
        a, rows, _ = self.run_list(FakeAyon(), do_versions=False)
        self.assertNotIn('Version', rows[0])
        self.assertNotIn('Version', a.columns)


if __name__ == '__main__':
    unittest.main()


class AyonOnlySequencerTest(unittest.TestCase):
    def settings(self, project):
        keys = ['ayon_do_shotlist', 'ayon_export_csv', 'ayon_export_excel', 'ayon_thumbnails',
                'ayon_filter_assets', 'ayon_filter_shots', 'ayon_filter_tasks', 'ayon_filter_other',
                'ayon_filter_matched', 'ayon_filter_tasktype_chbx', 'ayon_filter_assignee_chbx']
        st = {k: {'value': False} for k in keys}
        st.update({'ayon_project': {'value': project}, 'ayon_prefix': {'value': 'ayon_'},
                   'ayon_output_folder': {'value': ''}, 'ayon_filter_tasktypes': {'value': ''},
                   'ayon_filter_assignees': {'value': ''}})
        return st

    def make(self, project):
        import sequencer
        st = self.settings(project)
        obj = mock.Mock(settings=st, install_settings=None, args={})
        with mock.patch.object(sequencer.Sequencer, 'read_files') as rf:
            s = sequencer.Sequencer(None, gui=st, more_settings=obj, ui=mock.Mock(), headless=False)
            rf.assert_not_called()     # no package: no files read
        return s, sequencer

    def test_scan_without_project_warns(self):
        s, _ = self.make('')
        with self.assertLogs('Sequencer', 'WARNING') as cm:
            s.ayon_scan()
        self.assertIn('project', cm.output[0])

    def test_scan_reads_even_with_shotlist_off(self):
        s, sequencer = self.make('P')
        fake = mock.Mock(error=None)
        fake.get_shotlist.return_value = [{'Folder Path': '/a', '_hide': False}]
        fake.data = fake.get_shotlist.return_value
        with mock.patch.object(sequencer, 'AyonShotlist', return_value=fake):
            s.display_ayon_table = mock.Mock()
            s.ayon_scan()
        fake.get_shotlist.assert_called_once()
        s.display_ayon_table.assert_called()


class AttribColumnsTest(unittest.TestCase):
    def test_dates_and_range_with_handles(self):
        a = attrib()
        a.update({'startDate': '2026-10-01T00:00:00+00:00', 'endDate': '2026-11-15T00:00:00Z'})
        d = AyonShotlist.attribs_to_columns(a)
        self.assertEqual(d['Start Date'], '2026-10-01')
        self.assertEqual(d['End Date'], '2026-11-15')
        # 1001-1100 with 8 frame handles
        self.assertEqual(d['Range'], '993-1108')
        self.assertEqual(d['Length'], '116')

    def test_missing_attribs_do_not_crash(self):
        d = AyonShotlist.attribs_to_columns({'frameStart': 1001, 'frameEnd': 1010, 'startDate': None})
        self.assertEqual(d['Range'], '1001-1010')
        self.assertEqual(d['Start Date'], '')
        self.assertEqual(d['Width'], '')
        self.assertEqual(AyonShotlist.attribs_to_columns(None)['Length'], '1')

    def test_dates_in_rows_and_csv(self):
        fake = FakeAyon()
        orig_tasks = fake.get_tasks

        def tasks(*a, **k):
            out = orig_tasks(*a, **k)
            out[0]['attrib'] = dict(attrib(), startDate='2026-10-05T00:00:00Z', endDate=None)
            return out
        fake.get_tasks = tasks
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        with mock.patch.object(ayon_shotlist.ayon_api, 'get_server_api_connection', return_value=fake, create=True):
            a = AyonShotlist(gui(tmp.name, do_versions=False), None, {'AYON_SERVER_URL': 'x', 'AYON_API_KEY': 'y'})
            rows = a.get_shotlist()
        task_row = [r for r in rows if r['Task Name'] == 'comp'][0]
        self.assertEqual(task_row['Start Date'], '2026-10-05')
        self.assertEqual(task_row['End Date'], '')
        self.assertIn('Start Date', a.columns)
        self.assertLess(a.columns.index('Start Date'), a.columns.index('_hide'))


class VersionAttribDataTest(unittest.TestCase):
    def test_attrib_and_data_columns(self):
        products = [{'id': 'p', 'name': 'renderCompMain', 'folderId': 'f'}]
        versions = {'p': {'id': 'v', 'version': 5, 'taskId': 't',
                          'attrib': {'frameStart': 1001, 'frameEnd': 1100, 'handleStart': 8,
                                     'handleEnd': 8, 'fps': 23.976, 'resolutionWidth': 4096,
                                     'resolutionHeight': 2160, 'pixelAspect': 1.0},
                          'data': {'step': 1, 'host_name': 'nuke', 'colorspace': 'ACES - ACEScg'}}}
        repres = [{'id': 'r', 'name': 'exr', 'versionId': 'v'}]
        got = pick_versions(['f'], products, versions, repres, {'t': 'comp'},
                            parse_product_filters('comp:renderCompMain:exr'))['f']
        self.assertEqual(got['Version Frame Start'], '1001')
        self.assertEqual(got['Version Frame End'], '1100')
        self.assertEqual(got['Version Handle Start'], '8')
        self.assertEqual(got['Version Handle End'], '8')
        self.assertEqual(got['Version FPS'], '23.976')
        self.assertEqual(got['Version Width'], '4096')
        self.assertEqual(got['Version Height'], '2160')
        self.assertEqual(got['Version Pixel Aspect'], '1')
        self.assertEqual(got['Version Step'], '1')
        self.assertEqual(got['Version Host'], 'nuke')
        self.assertEqual(got['Version Colorspace'], 'ACES - ACEScg')

    def test_data_as_json_and_repre_colorspace_fallback(self):
        products = [{'id': 'p', 'name': 'plate', 'folderId': 'f'}]
        versions = {'p': {'id': 'v', 'version': 1, 'data': '{"host_name": "traypublisher"}'}}
        repres = [{'id': 'r', 'name': 'exr', 'versionId': 'v',
                   'data': {'colorspaceData': {'colorspace': 'ARRI LogC4'}}}]
        got = pick_versions(['f'], products, versions, repres, {},
                            parse_product_filters(':plate:exr'))['f']
        self.assertEqual(got['Version Host'], 'traypublisher')
        self.assertEqual(got['Version Colorspace'], 'ARRI LogC4')
        self.assertEqual(got['Version Step'], '')
        self.assertEqual(got['Version Frame Start'], '')

    def test_columns_listed(self):
        for c in ('Version FPS', 'Version Step', 'Version Host', 'Version Colorspace'):
            self.assertIn(c, ayon_shotlist.VERSION_COLUMNS)


class AyonColumnWidthTest(unittest.TestCase):
    def test_capped_width(self):
        import sequencer
        cw = sequencer.Sequencer.capped_width
        # like the wider neighbour
        self.assertEqual(cw([80, 900, 150], 1), 150)
        # at least the minimum
        self.assertEqual(cw([40, 900, 60], 1, 120), 120)
        # never wider than its own content
        self.assertEqual(cw([300, 90, 300], 1), 90)
        # first / last column
        self.assertEqual(cw([900, 200], 0), 200)

    def test_fit_uses_all_rows_and_caps_repre_path(self):
        import sequencer
        widths = {0: 100, 1: 1200, 2: 140}
        table = mock.Mock()
        table.columnWidth.side_effect = lambda i: widths[i]
        s = sequencer.Sequencer.__new__(sequencer.Sequencer)
        s.fit_ayon_columns(table, ['Representation', 'Repre Path', 'Version Filter'])
        table.horizontalHeader().setResizeContentsPrecision.assert_called_with(-1)
        table.resizeColumnsToContents.assert_called_once()
        table.setColumnWidth.assert_called_once_with(1, 140)


class AyonRowHeightTest(unittest.TestCase):
    def test_single_line_rows(self):
        import sequencer
        table = mock.Mock()
        table.fontMetrics().height.return_value = 14
        sequencer.Sequencer.single_line_rows(table)
        table.setWordWrap.assert_called_once_with(False)
        table.verticalHeader().setDefaultSectionSize.assert_called_once_with(20)
        table.verticalHeader().setSectionResizeMode.assert_called_once()
