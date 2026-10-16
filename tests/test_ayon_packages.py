import logging
import sys
import types
import unittest
from unittest import mock

from tests import _stubs  # noqa: F401
import ayon_packages
from ayon_packages import (pair_representation, repre_summary, collect_package_records,
                           merged_version_data, merged_repre_data, write_package_records,
                           DATA_KEY)
from ayon_shotlist import parse_product_filters, matched_version_rows
import sequencer


def summ(rid, name, files):
    """repre_summary of a representation with files [(name, size), ...]"""
    return repre_summary({'id': rid, 'name': name,
                          'files': [{'name': n, 'size': sz} for n, sz in files]})


class ParseFilterProductOnlyTest(unittest.TestCase):
    def test_product_only(self):
        f = parse_product_filters(":renderCompMain:")
        self.assertEqual((f[0]['task'], f[0]['product'], f[0]['repre']), ('', 'renderCompMain', ''))


class ReprSummaryTest(unittest.TestCase):
    def test_ext_and_size_from_files(self):
        s = summ('r1', 'exr', [('sh010_v007.1001.EXR', 100), ('sh010_v007.1002.exr', 150)])
        self.assertEqual((s['ext'], s['size'], s['files']), ('exr', 250, 2))

    def test_fallbacks(self):
        self.assertEqual(repre_summary({'id': 'r', 'name': 'review', 'context': {'ext': 'MOV'}})['ext'], 'mov')
        s = repre_summary({'id': 'r', 'name': 'jpeg'})
        self.assertEqual((s['ext'], s['size']), ('jpg', None))
        # json string context, missing size
        s = repre_summary({'id': 'r', 'name': 'x', 'context': '{"ext": "dpx"}',
                           'files': [{'path': '/a/b', 'size': None}]})
        self.assertEqual((s['ext'], s['size']), ('dpx', None))


class PairRepresentationTest(unittest.TestCase):
    def setUp(self):
        self.repres = [
            summ('r_exr', 'exr', [('a.1001.exr', 100), ('a.1002.exr', 100)]),
            summ('r_mov', 'mov', [('a.mov', 5000)]),
            summ('r_h264', 'h264', [('a_h264.mov', 900)]),
            summ('r_jpg', 'thumbnail', [('a.jpg', 10)]),
        ]

    def test_unique_extension(self):
        r, how = pair_representation('.EXR', 0, self.repres)
        self.assertEqual((r['id'], how), ('r_exr', 'extension'))

    def test_alias_extension(self):
        r, how = pair_representation('jpeg', None, self.repres)
        self.assertEqual(r['id'], 'r_jpg')

    def test_same_extension_by_size(self):
        r, how = pair_representation('mov', 900, self.repres)
        self.assertEqual((r['id'], how), ('r_h264', 'extension+size'))

    def test_same_extension_no_size(self):
        r, how = pair_representation('mov', 0, self.repres)
        self.assertIsNone(r)
        self.assertIn('size unknown', how)

    def test_same_extension_wrong_size(self):
        r, how = pair_representation('mov', 1234, self.repres)
        self.assertIsNone(r)
        self.assertIn('none with size 1234', how)

    def test_size_only_when_extension_differs(self):
        r, how = pair_representation('mp4', 5000, self.repres)
        self.assertEqual((r['id'], how), ('r_mov', 'size'))

    def test_nothing(self):
        r, how = pair_representation('dpx', 1, self.repres)
        self.assertIsNone(r)
        r, how = pair_representation('exr', 1, [])
        self.assertEqual(how, 'no representations')

    def test_allowed_names(self):
        r, how = pair_representation('mov', 0, self.repres, allowed=['H264'])
        self.assertEqual(r['id'], 'r_h264')
        r, how = pair_representation('exr', 0, self.repres, allowed=['mov'])
        self.assertIsNone(r)


class MergeDataTest(unittest.TestCase):
    info = {'date': '2026-10-16T10:00:00+02:00', 'user': 'jan'}

    def test_new_version_keeps_other_data(self):
        old = {'colorspace': 'ACEScg', DATA_KEY: {'packages': {'pkg_A': {'representations': ['exr']}}}}
        new = merged_version_data(old, 'pkg_B', {'mov', 'exr'}, self.info)
        self.assertEqual(new['colorspace'], 'ACEScg')
        self.assertEqual(new[DATA_KEY]['packages']['pkg_A'], {'representations': ['exr']})
        self.assertEqual(new[DATA_KEY]['packages']['pkg_B'],
                         {'date': self.info['date'], 'user': 'jan', 'representations': ['exr', 'mov']})
        # old dict not changed
        self.assertNotIn('pkg_B', old[DATA_KEY]['packages'])

    def test_same_package_same_repres_is_noop(self):
        old = {DATA_KEY: {'packages': {'pkg_A': {'representations': ['exr', 'mov'], 'date': 'd0'}}}}
        self.assertIsNone(merged_version_data(old, 'pkg_A', ['mov', 'exr'], self.info))

    def test_same_package_changed_repres(self):
        old = {DATA_KEY: {'packages': {'pkg_A': {'representations': ['exr'], 'date': 'd0'}}}}
        new = merged_version_data(old, 'pkg_A', ['mov'], self.info)
        entry = new[DATA_KEY]['packages']['pkg_A']
        self.assertEqual((entry['representations'], entry['date'], entry['updated']),
                         (['mov'], 'd0', self.info['date']))

    def test_json_string_and_broken_data(self):
        new = merged_version_data('{"a": 1}', 'p', [], self.info)
        self.assertEqual(new['a'], 1)
        new = merged_version_data({DATA_KEY: 'junk'}, 'p', [], self.info)
        self.assertEqual(new[DATA_KEY]['packages']['p']['representations'], [])
        self.assertIsNotNone(merged_version_data(None, 'p', [], self.info))

    def test_repre(self):
        new = merged_repre_data({}, 'pkg', self.info)
        self.assertEqual(new[DATA_KEY]['packages']['pkg'], self.info)
        self.assertIsNone(merged_repre_data(new, 'pkg', self.info))


class CollectTest(unittest.TestCase):
    def test_collect(self):
        items = [
            {'_ayon_version_id': 'v1', '_ayon_repre_id': 'r1', '_ayon_repre_name': 'exr'},
            {'_ayon_version_id': 'v1', '_ayon_repre_id': 'r2', '_ayon_repre_name': 'mov'},
            {'_ayon_version_id': 'v2'},                 # no repre found
            {'name': 'not matched'},
        ]
        rec = collect_package_records(items)
        self.assertEqual(rec['versions'], {'v1': {'exr', 'mov'}, 'v2': set()})
        self.assertEqual(rec['repres'], {'r1': 'v1', 'r2': 'v1'})


class FakeCon:
    def __init__(self, versions, repres):
        self.versions = versions
        self.repres = repres

    def get_versions(self, project, version_ids=None, fields=None):
        return [{'id': i, 'data': self.versions[i]} for i in version_ids if i in self.versions]

    def get_representations(self, project, representation_ids=None, fields=None):
        return [{'id': i, 'data': self.repres[i]} for i in representation_ids if i in self.repres]


class FakeSession:
    instances = []

    def __init__(self, con):
        self.updates = []
        self.committed = False
        FakeSession.instances.append(self)

    def update_entity(self, project, entity_type, entity_id, update_data):
        self.updates.append((project, entity_type, entity_id, update_data))

    def commit(self):
        self.committed = True


def fake_operations():
    mod = types.ModuleType('ayon_api.operations')
    mod.OperationsSession = FakeSession
    return {'ayon_api.operations': mod}


class WriteTest(unittest.TestCase):
    info = {'date': 'D', 'user': 'jan'}

    def setUp(self):
        FakeSession.instances = []

    def test_writes_only_changes(self):
        con = FakeCon(
            versions={'v1': {'x': 1}, 'v2': {DATA_KEY: {'packages': {'pkg': {'representations': ['exr']}}}}},
            repres={'r1': {}, 'r2': {DATA_KEY: {'packages': {'pkg': {}}}}})
        records = {'versions': {'v1': {'exr'}, 'v2': {'exr'}, 'v9': set()},
                   'repres': {'r1': 'v1', 'r2': 'v2'}}
        with mock.patch.dict(sys.modules, fake_operations()):
            res = write_package_records(con, 'proj', records, 'pkg', self.info)
        self.assertEqual((res['versions'], res['repres'], res['versions_same'], res['repres_same']),
                         (1, 1, 1, 1))
        self.assertEqual(res['errors'], ['version v9 not found'])
        session = FakeSession.instances[0]
        self.assertTrue(session.committed)
        written = {(t, i): d['data'] for _, t, i, d in session.updates}
        self.assertEqual(set(written), {('version', 'v1'), ('representation', 'r1')})
        self.assertEqual(written[('version', 'v1')]['x'], 1)
        self.assertEqual(written[('version', 'v1')][DATA_KEY]['packages']['pkg']['representations'], ['exr'])

    def test_dry_run_writes_nothing(self):
        con = FakeCon({'v1': {}}, {})
        with mock.patch.dict(sys.modules, fake_operations()):
            res = write_package_records(con, 'proj', {'versions': {'v1': set()}, 'repres': {}},
                                        'pkg', self.info, dry_run=True)
        self.assertEqual(res['versions'], 1)
        self.assertEqual(FakeSession.instances, [])

    def test_read_failure(self):
        con = mock.Mock()
        con.get_versions.side_effect = RuntimeError("offline")
        res = write_package_records(con, 'p', {'versions': {'v1': set()}, 'repres': {}}, 'pkg', self.info)
        self.assertIn('offline', res['errors'][0])


class MatchedRowsCarryRepresTest(unittest.TestCase):
    def test_rows_have_repre_summaries(self):
        rows = matched_version_rows(
            {'f1': {'Folder Path': '/sh010'}},
            [{'id': 'p1', 'name': 'renderCompMain', 'folderId': 'f1'}],
            [{'id': 'v1', 'version': 3, 'productId': 'p1'}],
            [{'id': 'r1', 'name': 'exr', 'versionId': 'v1', 'files': [{'name': 'a.exr', 'size': 7}]}],
            {}, {}, parse_product_filters(':renderCompMain:'))
        self.assertEqual(rows[0]['_repres'][0]['size'], 7)


class SequencerPairAndRecordTest(unittest.TestCase):
    def bare(self, filters=':renderCompMain:'):
        s = sequencer.Sequencer.__new__(sequencer.Sequencer)
        s.log = logging.getLogger('test')
        s.settings = {}
        s.output = {'package_name': 'pkg_20261016_v001'}
        s.static_keywords = {}
        s.ayon_gui = {'prefix': 'list_', 'version_match': True,
                      'version_match_pkg': '{version}', 'version_match_data': '{Version}',
                      'product_filters': parse_product_filters(filters)}
        repres = [summ('r_exr', 'exr', [('a.1001.exr', 10), ('a.1002.exr', 10)]),
                  summ('r_mov', 'mov', [('a.mov', 500)]),
                  summ('r_prev', 'review', [('a_review.mov', 90)])]
        s.ayon_matched_versions = [
            {'_folder_id': 'f1', '_version_id': 'v3', '_repres': repres, 'Product': 'renderCompMain',
             'Version': '3', 'Preferred': 'yes', 'Matched Files': '', 'Version Exists': 'False'},
        ]
        s.merged_list = [
            {'name': 'seq', 'version': '003', 'extension': 'exr', 'size_bytes': 20, '_ayon_folder_ids': {'f1'}},
            {'name': 'review', 'version': '003', 'extension': 'mov', 'size_bytes': 90, '_ayon_folder_ids': {'f1'}},
            {'name': 'unknown size', 'version': '003', 'extension': 'mov', 'size_bytes': 0,
             '_ayon_folder_ids': {'f1'}},
            {'name': 'skipped', 'version': '003', 'extension': 'mov', 'size_bytes': 500,
             '_ayon_folder_ids': {'f1'}, 'vendor_ignore_sub': True},
            {'name': 'other shot', 'version': '001', 'extension': 'exr', 'size_bytes': 1},
        ]
        return s

    def test_pairing(self):
        s = self.bare()
        s.ayon_versions_assign()
        seq, review, nosize, skipped, other = s.merged_list
        self.assertEqual((seq['_ayon_repre_id'], seq['list_Matched Representation By']), ('r_exr', 'extension'))
        self.assertEqual(review['list_Matched Representation'], 'review')
        self.assertEqual(review['list_Matched Representation By'], 'extension+size')
        self.assertEqual(nosize['_ayon_version_id'], 'v3')
        self.assertNotIn('_ayon_repre_id', nosize)
        self.assertEqual(nosize['list_Matched Representation'], '')
        self.assertNotIn('_ayon_version_id', other)
        # a second run clears stale pairs
        s.merged_list[0]['extension'] = 'dpx'
        s.merged_list[0]['size_bytes'] = 3
        s.ayon_versions_assign()
        self.assertNotIn('_ayon_repre_id', s.merged_list[0])

    def test_filter_repre_restricts(self):
        s = self.bare('comp:renderCompMain:exr')
        s.ayon_versions_assign()
        self.assertEqual(s.merged_list[0]['_ayon_repre_id'], 'r_exr')
        self.assertNotIn('_ayon_repre_id', s.merged_list[1])

    def test_record(self):
        s = self.bare()
        s.ayon_versions_assign()
        s.my_ayon = mock.Mock(error=None)
        s.my_ayon.record_packages.return_value = {'versions': 1, 'repres': 2, 'versions_same': 0,
                                                  'repres_same': 0, 'errors': []}
        s.ayon_record_packages()
        records, package = s.my_ayon.record_packages.call_args[0]
        self.assertEqual(package, 'pkg_20261016_v001')
        # the vendor-skipped file (mov 500) is not in the package
        self.assertEqual(records, {'versions': {'v3': {'exr', 'review'}},
                                   'repres': {'r_exr': 'v3', 'r_prev': 'v3'}})

    def test_record_needs_package_name_and_ayon(self):
        s = self.bare()
        s.ayon_versions_assign()
        s.my_ayon = None
        self.assertIsNone(s.ayon_record_packages())
        s.my_ayon = mock.Mock(error=None)
        s.output = {'package_name': 'pkg_{yy}'}
        self.assertIsNone(s.ayon_record_packages())
        s.my_ayon.record_packages.assert_not_called()


if __name__ == '__main__':
    unittest.main()
