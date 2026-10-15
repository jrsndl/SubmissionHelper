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
        with open(os.path.join(out, 'ayon-list.csv'), encoding='utf-8-sig') as f:
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


class MatchedVersionsTest(unittest.TestCase):
    def make(self, out, **kw):
        fake = FakeAyon()
        all_versions = [
            {'id': 'v1', 'version': 7, 'productId': 'p1', 'taskId': 't_comp', 'status': 'Approved',
             'attrib': {'fps': 25, 'comment': 'final'}, 'data': {'host_name': 'nuke'}},
            {'id': 'v1old', 'version': 6, 'productId': 'p1', 'taskId': 't_comp'},
            {'id': 'v2', 'version': 2, 'productId': 'p2'},
            {'id': 'v3', 'version': 1, 'productId': 'p3'},
            # product that is not in the filters, must not be listed
            {'id': 'v5', 'version': 4, 'productId': 'p5', 'taskId': 't_comp'},
        ]
        fake.p.append({'id': 'p5', 'name': 'workfileCompositing', 'folderId': 'f1', 'productType': 'workfile'})
        fake.r.append({'id': 'r6', 'name': 'exr', 'versionId': 'v1old'})
        fake.r.append({'id': 'r5', 'name': 'exr', 'versionId': 'v5'})
        fake.version_calls = 0

        def get_versions(project, product_ids=None, hero=True, fields=None):
            fake.version_calls += 1
            assert hero is False
            return [v for v in all_versions if v['productId'] in product_ids]
        fake.get_versions = get_versions
        with mock.patch.object(ayon_shotlist.ayon_api, 'get_server_api_connection', return_value=fake, create=True):
            a = AyonShotlist(gui(out, **kw), None, {'AYON_SERVER_URL': 'x', 'AYON_API_KEY': 'y'})
            a.get_shotlist()
        return a, fake

    def test_rows_only_for_matched_folders_and_preferred(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        a, fake = self.make(tmp.name)
        rows = a.get_matched_versions({'f1'})
        # only folder f1 (not f2), only configured products, sorted by folder path then version
        self.assertEqual({r['Folder Path'] for r in rows}, {'/ep01/sh010'})
        self.assertEqual([(r['Product'], r['Version']) for r in rows],
                         [('platePl01', '2'), ('renderCompMain', '6'), ('renderCompMain', '7')])
        self.assertNotIn('workfileCompositing', {r['Product'] for r in rows})
        pref = [r for r in rows if r['Preferred']]
        self.assertEqual([(r['Product'], r['Version']) for r in pref], [('renderCompMain', '7')])
        v7 = pref[0]
        self.assertEqual(v7['Version FPS'], '25')
        self.assertEqual(v7['Version Host'], 'nuke')
        self.assertEqual(v7['Version Task'], 'comp')
        self.assertEqual(v7['Representations'], 'exr mov')
        # cached: same folders -> no new query
        a.get_matched_versions({'f1'})
        self.assertEqual(fake.version_calls, 1)
        a.get_matched_versions({'f1', 'f2'})
        self.assertEqual(fake.version_calls, 2)

    def test_csv_names_and_versions_csv(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        a, _ = self.make(tmp.name, do_versions_csv=True)
        a.write_csv()
        a.write_versions_csv(a.get_matched_versions({'f1'}))
        self.assertTrue(os.path.isfile(os.path.join(tmp.name, 'ayon-list.csv')))
        with open(os.path.join(tmp.name, 'ayon-list-versions.csv'), encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        self.assertEqual(len(rows), 3)
        self.assertEqual(reader.fieldnames, [c for c in ayon_shotlist.MATCHED_VERSION_COLUMNS])
        self.assertFalse(os.path.exists(os.path.join(tmp.name, 'list.csv')))


class SequencerMatchedVersionsTest(unittest.TestCase):
    def bare(self):
        import logging
        import sequencer
        s = sequencer.Sequencer.__new__(sequencer.Sequencer)
        s.log = logging.getLogger('test')
        s.headless = True
        s.my_ayon = mock.Mock(error=None)
        s.my_ayon.get_matched_versions.return_value = [{'Product': 'x'}]
        s.ayon_data = [{'_folder_id': 'f1', '_matched': True}, {'_folder_id': 'f2'}]
        s.ayon_gui = {'do_versions': True}
        s.merged_list = [{'name': 'a'}]
        return s

    def test_only_matched_folders_are_asked(self):
        s = self.bare()
        s.ayon_versions_update()
        s.my_ayon.get_matched_versions.assert_called_once_with({'f1'})
        self.assertEqual(s.ayon_matched_versions, [{'Product': 'x'}])

    def test_needs_pull_versions_and_files(self):
        s = self.bare()
        s.ayon_gui = {'do_versions': False}
        s.ayon_versions_update()
        s.merged_list = []
        s.ayon_gui = {'do_versions': True}
        s.ayon_versions_update()
        s.my_ayon.get_matched_versions.assert_not_called()
        self.assertEqual(s.ayon_matched_versions, [])


class AyonMatchingDiagnosticsTest(unittest.TestCase):
    def run_assign(self, p1, d1):
        import logging
        import sequencer
        s = sequencer.Sequencer.__new__(sequencer.Sequencer)
        s.log = logging.getLogger('Sequencer')
        s.ayon_data = [
            {'Folder Name': 'HAR_204_404_0010', 'Folder Path': '/shots/HAR_204_404_0010',
             'Task Name': 'comp', '_folder_id': 'a', '_hide': False},
            {'Folder Name': 'HAR_204_404_0010', 'Folder Path': '/shots/HAR_204_404_0010',
             'Task Name': '', '_folder_id': 'a'},
        ]
        s.merged_list = [{'shot': 'HAR_204_404_0010', 'task': 'comp', 'name': 'HAR_204_404_0010_comp_v007'}]
        s.ayon_gui = {'prefix': 'ayon_'}
        s.settings = {'ayon_package1_chbx': {'value': True}, 'ayon_package1': {'value': p1},
                      'ayon_list1': {'value': d1}, 'ayon_package2_chbx': {'value': True},
                      'ayon_package2': {'value': '{task}'}, 'ayon_list2': {'value': '{Task Name}'},
                      'ayon_package3_chbx': {'value': False}, 'ayon_package3': {'value': ''},
                      'ayon_list3': {'value': ''}}
        return s

    def test_wrong_rule_is_explained(self):
        s = self.run_assign('/shots/{shot}', '{Folder Name}')
        with self.assertLogs('Sequencer', 'WARNING') as cm:
            s.ayon_data_assign()
        text = '\n'.join(cm.output)
        self.assertIn("'/shots/HAR_204_404_0010'  !=  list '{Folder Name}' -> 'HAR_204_404_0010'", text)
        self.assertIn("'comp'  ==", text)
        self.assertFalse(any(r.get('_matched') for r in s.ayon_data))

    def test_matching_rule_and_no_internal_keys(self):
        s = self.run_assign('/shots/{shot}', '{Folder Path}')
        with self.assertLogs('Sequencer', 'INFO') as cm:
            s.ayon_data_assign()
        self.assertIn('1 of 1', cm.output[0])
        self.assertTrue(s.ayon_data[0].get('_matched'))
        self.assertFalse(s.ayon_data[1].get('_matched'))
        self.assertEqual(s.merged_list[0]['ayon_Task Name'], 'comp')
        self.assertNotIn('ayon__folder_id', s.merged_list[0])


class MatchedVersionsFilterTest(unittest.TestCase):
    def test_filter_rules_and_sort(self):
        folders = {'f1': {'Folder Path': '/b'}, 'f2': {'Folder Path': '/a'}}
        products = [{'id': 'pr', 'name': 'renderCompMain', 'folderId': 'f1'},
                    {'id': 'pp', 'name': 'platePl01', 'folderId': 'f1'},
                    {'id': 'pa', 'name': 'platePl01', 'folderId': 'f2'},
                    {'id': 'pw', 'name': 'workfile', 'folderId': 'f1'}]
        versions = [{'id': 'r3', 'version': 3, 'productId': 'pr', 'taskId': 'tc'},
                    {'id': 'r2', 'version': 2, 'productId': 'pr', 'taskId': 'tl'},   # wrong task
                    {'id': 'p10', 'version': 10, 'productId': 'pp'},
                    {'id': 'p1', 'version': 1, 'productId': 'pp'},                    # no exr
                    {'id': 'a5', 'version': 5, 'productId': 'pa'},
                    {'id': 'w9', 'version': 9, 'productId': 'pw', 'taskId': 'tc'}]  # not configured
        repres = [{'name': 'exr', 'versionId': v} for v in ('r3', 'r2', 'p10', 'a5', 'w9')] + \
                 [{'name': 'mov', 'versionId': 'p1'}]
        rows = ayon_shotlist.matched_version_rows(
            folders, products, versions, repres, {'tc': 'comp', 'tl': 'lighting'}, {},
            parse_product_filters('comp:renderCompMain:exr, :platePl01:exr'))
        self.assertEqual([(r['Folder Path'], r['Version'], r['Product']) for r in rows],
                         [('/a', '5', 'platePl01'), ('/b', '3', 'renderCompMain'),
                          ('/b', '10', 'platePl01')])


class VersionMatchTest(unittest.TestCase):
    def bare(self, pkg='{version}', data='{Version}', on=True):
        import logging
        import sequencer
        s = sequencer.Sequencer.__new__(sequencer.Sequencer)
        s.log = logging.getLogger('Sequencer')
        s.ayon_gui = {'prefix': 'ayon_', 'version_match': on,
                      'version_match_pkg': pkg, 'version_match_data': data}
        s.ayon_matched_versions = [
            {'_folder_id': 'f1', 'Product': 'renderCompMain', 'Version': '6', 'Version Status': 'Rejected',
             'Preferred': '', 'Matched Files': ''},
            {'_folder_id': 'f1', 'Product': 'renderCompMain', 'Version': '7', 'Version Status': 'Approved',
             'Preferred': 'yes', 'Matched Files': ''},
            {'_folder_id': 'f2', 'Product': 'renderCompMain', 'Version': '7', 'Version Status': 'WIP',
             'Preferred': '', 'Matched Files': ''},
        ]
        s.merged_list = [
            {'name': 'sh010_comp_v006', 'version': '006', '_ayon_folder_ids': {'f1'}},
            {'name': 'sh010_comp_v009', 'version': '009', '_ayon_folder_ids': {'f1'}},
            {'name': 'unmatched_folder', 'version': '7'},
        ]
        return s

    def test_matches_version_in_same_folder(self):
        s = self.bare()
        with self.assertLogs('Sequencer', 'WARNING') as cm:
            s.ayon_versions_assign()
        a, b, c = s.merged_list
        # 006 == 6, only rows of the file's own folder
        self.assertEqual(a['ayon_Matched Version'], '6')
        self.assertEqual(a['ayon_Matched Version Status'], 'Rejected')
        self.assertNotIn('ayon_Matched _folder_id', a)
        self.assertNotIn('ayon_Matched Version', b)          # v009 doesn't exist
        self.assertNotIn('ayon_Matched Version', c)          # not matched to a folder
        self.assertEqual(s.ayon_matched_versions[0]['Matched Files'], '1')
        self.assertEqual(s.ayon_matched_versions[2]['Matched Files'], '')
        self.assertIn("1 of 2", cm.output[0])
        self.assertIn("'009'", cm.output[0])                  # shows what was compared

    def test_off_clears_previous_values(self):
        s = self.bare()
        s.ayon_versions_assign()
        s.ayon_gui['version_match'] = False
        s.ayon_versions_assign()
        self.assertNotIn('ayon_Matched Version', s.merged_list[0])
        self.assertEqual(s.ayon_matched_versions[0]['Matched Files'], '')

    def test_version_name_template(self):
        s = self.bare(pkg='v{version}', data='{Version Name}')
        for r in s.ayon_matched_versions:
            r['Version Name'] = 'v' + r['Version'].zfill(3)
        s.ayon_versions_assign()
        self.assertEqual(s.merged_list[0]['ayon_Matched Version'], '6')

    def test_same_value(self):
        import sequencer
        sv = sequencer.Sequencer._same_value
        self.assertTrue(sv('007', '7'))
        self.assertTrue(sv(' v007', 'v007'))
        self.assertFalse(sv('v007', 'v7'))
        self.assertFalse(sv('7', '8'))


class TaskFilterTest(unittest.TestCase):
    def rows(self):
        def r(name, ttype, who):
            return {'Folder Type': 'Shot/Task', 'Task Name': name, 'Task Type': ttype,
                    'Task Assignees': who}
        return [r('comp', 'Compositing', 'ann'), r('compFinal', 'Compositing', 'bob ann'),
                r('dmp', 'Compositing', 'ann'), r('light', 'Lighting', 'ann'),
                {'Folder Type': 'Shot', 'Task Name': '', 'Task Type': '', 'Task Assignees': ''}]

    def visible(self, **kw):
        a = AyonShotlist.__new__(AyonShotlist)
        a.data = self.rows()
        g = {'filter_assets': False, 'filter_shots': True, 'filter_tasks': True, 'filter_other': False,
             'filter_tasktype': False, 'filter_tasktypes': [], 'filter_assignee': False,
             'filter_assignees': [], 'filter_taskname': False, 'filter_tasknames': []}
        g.update(kw)
        a.ayon_gui = g
        a.filter_shotlist()
        return [r['Task Name'] or 'SHOT' for r in a.data if not r['_hide']]

    def test_task_names_with_wildcards(self):
        self.assertEqual(self.visible(filter_taskname=True, filter_tasknames=['comp*']),
                         ['comp', 'compFinal', 'SHOT'])
        # not case sensitive
        self.assertEqual(self.visible(filter_taskname=True, filter_tasknames=['COMP']),
                         ['comp', 'SHOT'])

    def test_names_and_types_combine(self):
        self.assertEqual(self.visible(filter_tasktype=True, filter_tasktypes=['compositing'],
                                      filter_taskname=True, filter_tasknames=['dmp', 'light']),
                         ['dmp', 'SHOT'])

    def test_assignee_narrows_and_multiple_assignees(self):
        # used to show 'light' again although the type filter hid it, and to
        # miss "bob ann"
        got = self.visible(filter_tasktype=True, filter_tasktypes=['compositing'],
                           filter_assignee=True, filter_assignees=['bob'])
        self.assertEqual(got, ['compFinal'])


class MatchedVersionsBandingTest(unittest.TestCase):
    def test_same_folder_same_shade(self):
        import sequencer
        s = sequencer.Sequencer.__new__(sequencer.Sequencer)
        s.ui = mock.Mock()
        s.ui.ayon_tables_tab.indexOf.return_value = 1
        s.fit_ayon_columns = mock.Mock()
        s.single_line_rows = mock.Mock()
        s.ayon_matched_versions = [
            {'Folder Path': '/a', 'Version': '1'}, {'Folder Path': '/a', 'Version': '2'},
            {'Folder Path': '/b', 'Version': '1'},
            {'Folder Path': '/c', 'Version': '1', 'Preferred': 'yes'}, {'Folder Path': '/c', 'Version': '2'},
        ]
        colors = []
        items = []

        def make_item(text):
            itm = mock.Mock()
            itm.setBackground.side_effect = lambda c: colors.append((len(items), c))
            items.append(itm)
            return itm
        with mock.patch.object(sequencer.QtWidgets, 'QTableWidgetItem', side_effect=make_item), \
                mock.patch.object(sequencer.QtGui, 'QColor', side_effect=lambda c: c):
            s.display_ayon_versions_table()
        cols = ayon_shotlist.MATCHED_VERSION_COLUMNS
        ncols = len(cols)
        path_col = cols.index('Folder Path')
        version_col = cols.index('Version')
        status_col = cols.index('Version Status')

        def color(row, col):
            return colors[row * ncols + col][1]
        per_row = [color(r, path_col) for r in range(5)]
        self.assertEqual(per_row[0], per_row[1])           # /a
        self.assertNotEqual(per_row[1], per_row[2])        # /a -> /b
        self.assertEqual(per_row[2], '#3a3a3a')
        self.assertEqual(per_row[3], '#4d4d4d')            # preferred row: path keeps the folder shade
        self.assertEqual(per_row[4], '#4d4d4d')            # /c back to the first shade
        # preferred mark only in the marked columns
        self.assertEqual(color(3, version_col), 'darkgreen')
        self.assertEqual(color(3, cols.index('Product')), 'darkgreen')
        self.assertEqual(color(3, status_col), '#4d4d4d')
        self.assertEqual(color(4, version_col), '#4d4d4d')
