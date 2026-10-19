"""AYON tab > AYON Lists queries (ayon_lists.py) on fake ayon_api connections."""
import unittest

from tests import _stubs  # noqa: F401
import ayon_lists as al

VERSIONS = {'v1': {'id': 'v1', 'name': 'v003', 'version': 3, 'productId': 'p1', 'taskId': 't1'},
            'v2': {'id': 'v2', 'name': 'v012', 'version': 12, 'productId': 'p2', 'taskId': None}}
PRODUCTS = {'p1': {'id': 'p1', 'name': 'renderCompMain', 'folderId': 'f1'},
            'p2': {'id': 'p2', 'name': 'plateMain', 'folderId': 'f2'}}
FOLDERS = {'f1': {'id': 'f1', 'path': '/sq01/sh010'}, 'f2': {'id': 'f2', 'path': '/sq01/sh020'}}
TASKS = {'t1': {'id': 't1', 'name': 'comp'}}
ITEMS = [{'entityId': 'v2', 'entityType': 'version', 'position': 1},
         {'entityId': 'v1', 'entityType': 'version', 'position': 0},
         {'entityId': 'x', 'entityType': 'folder', 'position': 2}]


class _Getters:
    def _get(self, table, ids):
        return [table[i] for i in ids if i in table]

    def get_versions(self, project, version_ids, fields):
        return self._get(VERSIONS, version_ids)

    def get_products(self, project, product_ids, fields):
        return self._get(PRODUCTS, product_ids)

    def get_folders(self, project, folder_ids, fields):
        return self._get(FOLDERS, folder_ids)

    def get_tasks(self, project, task_ids, fields):
        return self._get(TASKS, task_ids)


class NewApi(_Getters):
    """ayon_api with the entity list helpers"""

    def __init__(self, folders_field=True):
        self.folders_field = folders_field

    def get_entity_list_folders(self, project):
        return [{'id': 'A', 'label': 'Client', 'parentId': None},
                {'id': 'B', 'label': 'Week 42', 'parentId': 'A'}]

    def get_entity_lists(self, project, list_ids=None, fields=None, active=None):
        if 'entityListFolderId' in (fields or ()) and not self.folders_field:
            raise RuntimeError("Cannot query field entityListFolderId")
        if list_ids:
            return iter([{'id': list_ids[0], 'entityType': 'version', 'items': ITEMS}])
        if 'data' in (fields or ()) and not self.folders_field:
            raise RuntimeError("Cannot query field data")
        lists = [
            {'id': 'L1', 'label': 'sub0012', 'active': True, 'entityListFolderId': 'B',
             'attrib': {'category': 'Submissions'}, 'data': {}},
            {'id': 'L2', 'label': 'loose', 'active': True, 'attrib': {}, 'data': {}},
            {'id': 'L3', 'label': 'old', 'active': False, 'attrib': {'category': 'X'}},
            {'id': 'L4', 'label': 'approved', 'active': True, 'entityListFolderId': 'A',
             'attrib': {'category': None}, 'data': {'category': 'Client'}},
        ]
        # only the fields asked for
        return iter([{k: v for k, v in one.items() if k in fields} for one in lists])


class _Response:
    def __init__(self, data, errors=None):
        self.data = data
        self.errors = errors

    def raise_for_status(self):
        pass


class OldApi(_Getters):
    """ayon_api without the helpers: plain GraphQL / REST"""

    def __init__(self):
        self.pages = 0

    def query_graphql(self, query, variables):
        assert 'entityListFolderId' not in query or True
        self.pages += 1
        if variables.get('after') is None:
            return _Response({'data': {'project': {'entityLists': {
                'pageInfo': {'hasNextPage': True, 'endCursor': 'c1'},
                'edges': [{'node': {'id': 'L1', 'label': 'b', 'active': True}}]}}}})
        return _Response({'data': {'project': {'entityLists': {
            'pageInfo': {'hasNextPage': False},
            'edges': [{'node': {'id': 'L2', 'label': 'a', 'active': True}}]}}}})

    def get(self, endpoint):
        if endpoint.endswith('entityListFolders'):
            raise RuntimeError('404')
        return _Response({'entityType': 'version', 'items': ITEMS})


class Lists(unittest.TestCase):

    def test_by_category_not_folder_inactive_dropped(self):
        out = al.query_lists(NewApi(), 'proj')
        self.assertEqual([(d['folder'], d['name']) for d in out],
                         [('Client', 'approved'), ('Submissions', 'sub0012'),
                          (al.NO_CATEGORY, 'loose')])

    def test_server_refusing_data_field(self):
        out = al.query_lists(NewApi(folders_field=False), 'proj')
        self.assertEqual([(d['folder'], d['name']) for d in out],
                         [('Submissions', 'sub0012'), (al.NO_CATEGORY, 'approved'),
                          (al.NO_CATEGORY, 'loose')])

    def test_category_from_json_strings(self):
        self.assertEqual(al.list_category({'allAttrib': '{"category": "Dailies"}'}), 'Dailies')
        self.assertEqual(al.list_category({'data': '{"category": "Final"}'}), 'Final')
        self.assertEqual(al.list_category({'allAttrib': 'not json'}), '')

    def test_old_api_graphql_pages(self):
        con = OldApi()
        out = al.query_lists(con, 'proj')
        self.assertEqual([d['name'] for d in out], ['a', 'b'])
        self.assertEqual({d['folder'] for d in out}, {al.NO_CATEGORY})

    def test_no_connection(self):
        self.assertEqual(al.query_lists(None, 'proj'), [])
        self.assertEqual(al.query_list_versions(NewApi(), '', 'L1'), [])


class Versions(unittest.TestCase):

    def check(self, con):
        with self.assertLogs('AyonLists', 'INFO'):
            rows = al.query_list_versions(con, 'proj', 'L1')
        self.assertEqual(rows, [
            {'_id': 'v1', 'Folder Path': '/sq01/sh010', 'Task': 'comp',
             'Product': 'renderCompMain', 'Version': 3},
            {'_id': 'v2', 'Folder Path': '/sq01/sh020', 'Task': '', 'Product': 'plateMain',
             'Version': 12},
        ])
        # the columns shown; _id is for the package match colors
        self.assertEqual([k for k in rows[0] if not k.startswith('_')], list(al.LIST_COLUMNS))

    def test_new_api(self):
        self.check(NewApi())

    def test_old_api_rest(self):
        self.check(OldApi())



class ConnectedHook(unittest.TestCase):
    """Sequencer.ayon_data_read calls Sequencer.on_ayon_connected after a good connection"""

    def test_hook_called_with_connection_and_project(self):
        import logging
        from unittest import mock
        import sequencer
        s = sequencer.Sequencer.__new__(sequencer.Sequencer)
        s.log = logging.getLogger('test')
        s.ui = object()
        s.paths = {}
        s.ayon_gui = {'project': 'proj', 'do_shotlist': True}
        s.ayon_collect_gui = lambda: None
        fake = mock.Mock(error=None, ayon='CON')
        fake.get_shotlist.return_value = [{'a': 1}]
        calls = []
        with mock.patch.object(sequencer, 'AyonShotlist', return_value=fake), \
                mock.patch.object(sequencer.credentials, 'ensure_ayon'), \
                mock.patch.object(sequencer.Sequencer, 'on_ayon_connected',
                                  staticmethod(lambda con, project: calls.append((con, project))),
                                  create=True):
            s.ayon_data_read(force=True)
            fake.error = 'down'
            s.ayon_data_read(force=True)
        self.assertEqual(calls, [('CON', 'proj')])


if __name__ == '__main__':
    unittest.main()
