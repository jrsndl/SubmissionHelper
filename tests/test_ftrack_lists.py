"""Ftrack tab > Get Lists queries (ftrack.py) on a fake ftrack session."""
import unittest

from tests import _stubs  # noqa: F401
import ftrack


class _Result:
    def __init__(self, items):
        self.items = items

    def all(self):
        return self.items


class FakeSession:
    """answers by the entity type of the query; records the queries"""

    def __init__(self, lists=(), list_objects=(), versions=(), refuse_link=False):
        self.lists = list(lists)
        self.list_objects = list(list_objects)
        self.versions = list(versions)
        self.refuse_link = refuse_link
        self.queries = []

    def query(self, q):
        self.queries.append(q)
        if ' from AssetVersionList ' in q:
            return _Result(self.lists)
        if ' from ListObject ' in q:
            return _Result([o for o in self.list_objects if o['list_id'] in q])
        if ' from AssetVersion ' in q:
            if self.refuse_link and 'parent.link' in q:
                raise ValueError("projection not allowed")
            return _Result([v for v in self.versions if f'"{v["id"]}"' in q])
        raise AssertionError(q)


def _version(vid, number, asset='compMain', path=('proj', 'sq010', 'sh010'),
             status='Approved', comment='final', atype='Render', user=None):
    return {
        'id': vid, 'version': number, 'comment': comment,
        'status': {'name': status},
        'asset': {'name': asset, 'type': {'name': atype},
                  'parent': {'link': [{'name': n} for n in path]}},
        'user': user if user is not None else {'first_name': 'Jan', 'last_name': 'Novak',
                                               'username': 'jnovak'},
    }


class VersionListsTest(unittest.TestCase):

    def test_lists_sorted_by_folder_without_folder_last(self):
        s = FakeSession(lists=[
            {'id': '1', 'name': 'b list', 'category': {'name': 'Dailies'}},
            {'id': '2', 'name': 'loose', 'category': None},
            {'id': '3', 'name': 'a list', 'category': {'name': 'dailies'}},
            {'id': '4', 'name': 'client', 'category': {'name': 'Client'}},
        ])
        out = ftrack.query_version_lists(s, 'pid')
        self.assertEqual([(d['folder'], d['name']) for d in out],
                         [('Client', 'client'), ('dailies', 'a list'), ('Dailies', 'b list'),
                          (ftrack.NO_FOLDER, 'loose')])
        self.assertIn('project.id is "pid"', s.queries[0])

    def test_no_session_or_project(self):
        self.assertEqual(ftrack.query_version_lists(None, 'pid'), [])
        self.assertEqual(ftrack.query_version_lists(FakeSession(), ''), [])

    def test_query_error_logged(self):
        class Bad:
            def query(self, q):
                raise RuntimeError('down')
        with self.assertLogs('Ftrack', 'ERROR'):
            self.assertEqual(ftrack.query_version_lists(Bad(), 'pid'), [])
        with self.assertLogs('Ftrack', 'ERROR'):
            self.assertEqual(ftrack.query_list_versions(Bad(), 'L'), [])


class ListVersionsTest(unittest.TestCase):

    def setUp(self):
        self.versions = [_version('v2', 12, asset='plate'), _version('v1', 3)]
        self.objects = [{'list_id': 'L1', 'entity_id': 'v1'}, {'list_id': 'L1', 'entity_id': 'v2'}]

    def test_rows(self):
        s = FakeSession(list_objects=self.objects, versions=self.versions)
        rows = ftrack.query_list_versions(s, 'L1')
        self.assertEqual(rows[0], {
            'Version Link': 'proj/sq010/sh010/compMain_v003', 'Version': 3,
            'Version Status': 'Approved', 'Version Description': 'final',
            'Asset Type': 'Render', 'Published By': 'Jan Novak'})
        self.assertEqual(rows[1]['Version Link'], 'proj/sq010/sh010/plate_v012')
        self.assertEqual(list(rows[0]), list(ftrack.LIST_COLUMNS))

    def test_without_link_projection(self):
        s = FakeSession(list_objects=self.objects, versions=self.versions, refuse_link=True)
        rows = ftrack.query_list_versions(s, 'L1')
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]['Version Link'], 'proj/sq010/sh010/compMain_v003')

    def test_missing_values(self):
        v = _version('v1', None, user={'first_name': None, 'last_name': None, 'username': 'bot'})
        v['status'] = None
        v['asset']['parent'] = None
        v['comment'] = None
        row = ftrack.version_row(v)
        self.assertEqual(row['Version Link'], 'compMain_v')
        self.assertEqual(row['Version Status'], '')
        self.assertEqual(row['Version Description'], '')
        self.assertEqual(row['Published By'], 'bot')

    def test_chunks(self):
        versions = [_version(f'v{i}', i) for i in range(250)]
        objects = [{'list_id': 'L1', 'entity_id': f'v{i}'} for i in range(250)]
        s = FakeSession(list_objects=objects, versions=versions)
        rows = ftrack.query_list_versions(s, 'L1')
        self.assertEqual(len(rows), 250)
        self.assertEqual(sum(' from AssetVersion ' in q for q in s.queries), 3)

    def test_empty_list(self):
        self.assertEqual(ftrack.query_list_versions(FakeSession(), 'L1'), [])
        self.assertEqual(ftrack.query_list_versions(None, 'L1'), [])


if __name__ == '__main__':
    unittest.main()
