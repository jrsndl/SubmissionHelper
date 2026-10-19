"""AYON Lists: matching lists to the package's versions, creating a list (ayon_lists.py)."""
import unittest

from tests import _stubs  # noqa: F401
import ayon_lists as al


class Match(unittest.TestCase):

    def test_exact_almost_none(self):
        pkg = {'a', 'b', 'c', 'd'}
        self.assertEqual(al.match_kind({'d', 'c', 'b', 'a'}, pkg, 0.75), al.EXACT)
        # 3 shared of 4 in either: 75 %
        self.assertEqual(al.match_kind({'a', 'b', 'c'}, pkg, 0.75), al.ALMOST)
        # 3 shared of 5 in either: 60 %
        self.assertIsNone(al.match_kind({'a', 'b', 'c', 'x'}, pkg, 0.75))
        self.assertEqual(al.match_kind({'a', 'b', 'c', 'x'}, pkg, 0.6), al.ALMOST)

    def test_empty_sides_never_match(self):
        self.assertIsNone(al.match_kind(set(), {'a'}, 0.1))
        self.assertIsNone(al.match_kind({'a'}, set(), 0.1))
        self.assertIsNone(al.match_kind(None, None, 0.1))
        self.assertEqual(al.overlap(set(), set()), 0.0)


class _Resp:
    def __init__(self, data=None, fail=False):
        self.data = data
        self.fail = fail

    def raise_for_status(self):
        if self.fail:
            raise RuntimeError('400 attribute category does not exist')


class OldCon:
    """ayon_api without the list helpers: REST, with a small list store"""

    def __init__(self, attrib_ok=True, ignore_items=False):
        self.attrib_ok = attrib_ok
        self.ignore_items = ignore_items
        self.posts = []
        self.lists = {'L1': [{'entityId': 'a', 'entityType': 'version'},
                             {'entityId': 'f', 'entityType': 'folder'}],
                      'L2': []}

    def get(self, endpoint):
        lid = endpoint.rsplit('/', 1)[-1]
        items = self.lists.get(lid)
        if items is None:
            raise RuntimeError('404')
        return _Resp({'entityType': 'version', 'items': items})

    def post(self, endpoint, **kwargs):
        self.posts.append((endpoint, kwargs))
        if endpoint.endswith('/items'):
            lid = endpoint.split('/')[-2]
            self.lists[lid].append({'entityId': kwargs['entityId'], 'entityType': 'version',
                                    'position': kwargs.get('position')})
            return _Resp()
        if 'attrib' in kwargs and not self.attrib_ok:
            return _Resp(fail=True)
        self.lists[kwargs['id']] = [] if self.ignore_items else [
            dict(i, entityType='version') for i in kwargs.get('items') or []]
        return _Resp()


class NewCon:
    def __init__(self):
        self.calls = []
        self.lists = {}

    def create_entity_list(self, project, entity_type, label, **kwargs):
        self.calls.append((project, entity_type, label, kwargs))
        self.lists['NEW'] = [dict(i, entityType='version') for i in kwargs.get('items') or []]
        return 'NEW'

    def get_entity_lists(self, project, list_ids=None, fields=None, active=None):
        return iter([{'id': i, 'entityType': 'version', 'items': self.lists[i]}
                     for i in list_ids or [] if i in self.lists])


class ListVersions(unittest.TestCase):

    def test_versions_per_list(self):
        lists = [{'id': 'L1', 'name': 'one', 'entity_type': 'version'},
                 {'id': 'L2', 'name': 'empty'},
                 {'id': 'L3', 'name': 'folders', 'entity_type': 'folder'},
                 {'id': 'L4', 'name': 'broken'}]
        with self.assertLogs('AyonLists', 'WARNING'):
            out = al.list_version_ids(OldCon(), 'proj', lists)
        self.assertEqual(out, {'L1': {'a'}, 'L2': set()})


class Create(unittest.TestCase):

    def test_new_api_with_category(self):
        con = NewCon()
        self.assertEqual(al.create_version_list(con, 'proj', 'sub0012', ['b', 'a'], 'Subs'), 'NEW')
        project, etype, label, kwargs = con.calls[0]
        self.assertEqual((project, etype, label), ('proj', 'version', 'sub0012'))
        self.assertEqual(kwargs['items'], [{'entityId': 'b', 'position': 0},
                                           {'entityId': 'a', 'position': 1}])
        self.assertEqual(kwargs['attrib'], {'category': 'Subs'})

    def test_rest_category_falls_back_to_data(self):
        con = OldCon(attrib_ok=False)
        list_id = al.create_version_list(con, 'proj', 'sub0012', ['a'], 'Subs')
        # attrib refused, data accepted; the items came with the list
        self.assertEqual(len(con.posts), 2)
        endpoint, kwargs = con.posts[-1]
        self.assertEqual(endpoint, 'projects/proj/lists')
        self.assertEqual(kwargs['data'], {'category': 'Subs'})
        self.assertEqual(kwargs['id'], list_id)
        self.assertEqual(kwargs['entityType'], 'version')

    def test_no_category_one_try(self):
        con = OldCon()
        al.create_version_list(con, 'proj', 'x', ['a'])
        self.assertEqual(len(con.posts), 1)
        self.assertNotIn('attrib', con.posts[0][1])

    def test_server_ignoring_items_gets_them_one_by_one(self):
        con = OldCon(ignore_items=True)
        with self.assertLogs('AyonLists', 'INFO'):
            list_id = al.create_version_list(con, 'proj', 'sub0012', ['b', 'a', 'b'], 'Subs')
        self.assertEqual([i['entityId'] for i in con.lists[list_id]], ['b', 'a'])
        self.assertEqual([i['position'] for i in con.lists[list_id]], [0, 1])

    def test_items_that_cant_be_added_raise(self):
        con = OldCon(ignore_items=True)
        original = con.post

        def post(endpoint, **kwargs):
            if endpoint.endswith('/items'):
                return _Resp(fail=True)
            return original(endpoint, **kwargs)
        con.post = post
        with self.assertRaises(RuntimeError):
            al.create_version_list(con, 'proj', 'x', ['a'])

    def test_failure_raises(self):
        class Bad:
            def create_entity_list(self, *a, **k):
                raise RuntimeError('denied')
        with self.assertRaises(RuntimeError):
            al.create_version_list(Bad(), 'proj', 'x', ['a'], 'Subs')


if __name__ == '__main__':
    unittest.main()
