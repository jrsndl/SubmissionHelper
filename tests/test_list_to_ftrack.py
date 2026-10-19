"""Create List from Package in ftrack: AYON -> ftrack ids, ftrack list creation."""
import unittest

from tests import _stubs  # noqa: F401
import ayon_lists as al
import ftrack


class _Result:
    def __init__(self, items):
        self.items = items

    def all(self):
        return self.items


class FakeFtrack:
    def __init__(self, fail_commit=False):
        self.created = []
        self.committed = False
        self.rolled_back = False
        self.fail_commit = fail_commit

    def query(self, q):
        assert 'ListCategory' in q
        return _Result([{'id': 'c1', 'name': 'Dailies'}, {'id': 'c2', 'name': 'Client'}])

    def create(self, entity_type, data):
        entity = dict(data, id=f"{entity_type}-{len(self.created)}")
        self.created.append((entity_type, data))
        return entity

    def commit(self):
        if self.fail_commit:
            raise RuntimeError('permission denied')
        self.committed = True

    def rollback(self):
        self.rolled_back = True


class FtrackCreate(unittest.TestCase):

    def test_list_and_objects(self):
        s = FakeFtrack()
        list_id = ftrack.create_version_list(s, 'P', 'sub0012', 'Client', ['f2', 'f1'])
        self.assertTrue(s.committed)
        etype, data = s.created[0]
        self.assertEqual(etype, 'List')
        self.assertEqual(data, {'project_id': 'P', 'name': 'sub0012', 'is_open': True,
                                'category_id': 'c2', 'system_type': 'assetversion'})
        self.assertEqual([d['entity_id'] for t, d in s.created[1:]], ['f2', 'f1'])
        self.assertTrue(all(d['list_id'] == list_id for t, d in s.created[1:]))

    def test_unknown_category(self):
        s = FakeFtrack()
        with self.assertRaises(ValueError):
            ftrack.create_version_list(s, 'P', 'x', 'Nope', ['f1'])
        self.assertEqual(s.created, [])

    def test_failed_commit_rolls_back(self):
        s = FakeFtrack(fail_commit=True)
        with self.assertRaises(RuntimeError):
            ftrack.create_version_list(s, 'P', 'x', 'Client', ['f1'])
        self.assertTrue(s.rolled_back)

    def test_categories(self):
        self.assertEqual(ftrack.list_categories(FakeFtrack()), ['Client', 'Dailies'])
        self.assertEqual(ftrack.list_categories(None), [])


class FtrackIds(unittest.TestCase):

    def test_mapping_skips_unsynced(self):
        class Con:
            def get_versions(self, project, version_ids, fields):
                data = {'a': {'id': 'a', 'attrib': {'ftrackId': 'F-A'}},
                        'b': {'id': 'b', 'attrib': {}},
                        'c': {'id': 'c', 'attrib': {'ftrackId': 'F-C', 'ftrackPath': '/x'}}}
                return [data[i] for i in version_ids if i in data]
        self.assertEqual(al.version_ftrack_ids(Con(), 'p', ['a', 'b', 'c', 'a']),
                         {'a': 'F-A', 'c': 'F-C'})

    def test_falls_back_to_all_attrib(self):
        class Con:
            def __init__(self):
                self.fields = []

            def get_versions(self, project, version_ids, fields):
                self.fields.append(fields)
                if 'attrib.ftrackId' in fields:
                    raise RuntimeError('unknown field')
                return [{'id': 'a', 'attrib': '{"ftrackId": "F-A"}'}]
        con = Con()
        self.assertEqual(al.version_ftrack_ids(con, 'p', ['a']), {'a': 'F-A'})
        self.assertEqual(len(con.fields), 2)


if __name__ == '__main__':
    unittest.main()
