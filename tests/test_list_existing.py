"""Create List from Package when a list with that name exists: add the missing versions."""
import unittest

from tests import _stubs  # noqa: F401
import ayon_lists as al
import ftrack


class _Result:
    def __init__(self, items):
        self.items = items

    def all(self):
        return self.items

    def first(self):
        return self.items[0] if self.items else None


class FakeFtrack:
    def __init__(self, existing_objects=None, existing_category='c1'):
        self.existing_objects = existing_objects
        self.created = []
        self.existing = {'id': 'OLD', 'name': 'sub', 'category_id': existing_category}

    def query(self, q):
        if 'ListCategory' in q:
            return _Result([{'id': 'c1', 'name': 'Client'}])
        if q.startswith('select id, name, category_id from List'):
            assert 'category_id is' not in q   # any category
            return _Result([] if self.existing_objects is None else [self.existing])
        if 'ListObject' in q:
            return _Result([{'entity_id': e} for e in self.existing_objects or []])
        raise AssertionError(q)

    def create(self, etype, data):
        self.created.append((etype, data))
        return dict(data, id='NEW')

    def commit(self):
        pass

    def rollback(self):
        pass


class Ftrack(unittest.TestCase):

    def test_existing_list_gets_only_missing_versions(self):
        s = FakeFtrack(existing_objects=['f1', 'x9'])
        list_id = ftrack.create_version_list(s, 'P', 'sub', 'Client', ['f1', 'f2', 'f2'])
        self.assertEqual(list_id, 'OLD')
        self.assertEqual(s.created, [('ListObject', {'list_id': 'OLD', 'entity_id': 'f2'})])

    def test_list_in_another_category_is_moved(self):
        # e.g. made by the ayon-ftrack transmitter in the first list category
        s = FakeFtrack(existing_objects=[], existing_category='c9')
        self.assertEqual(ftrack.create_version_list(s, 'P', 'sub', 'Client', ['f1']), 'OLD')
        self.assertEqual(s.existing['category_id'], 'c1')
        self.assertEqual(s.created, [('ListObject', {'list_id': 'OLD', 'entity_id': 'f1'})])

    def test_new_list_when_none(self):
        s = FakeFtrack()
        self.assertEqual(ftrack.create_version_list(s, 'P', 'sub', 'Client', ['f1']), 'NEW')
        self.assertEqual(s.created[0][0], 'List')


class Ayon(unittest.TestCase):

    def test_find_by_label(self):
        class Con:
            def get_entity_lists(self, project, list_ids=None, fields=None, active=None):
                return iter([{'id': 'A', 'label': 'Sub0001'}, {'id': 'B', 'label': 'sub0001'},
                             {'id': 'C', 'label': 'other'}])
        con = Con()
        self.assertEqual(al.find_list_by_label(con, 'p', 'sub0001'), 'B')
        self.assertEqual(al.find_list_by_label(con, 'p', 'SUB0001'), 'A')
        self.assertIsNone(al.find_list_by_label(con, 'p', 'none'))
        self.assertIsNone(al.find_list_by_label(con, 'p', ''))

    def test_add_to_list_with_other_versions(self):
        class Con:
            def __init__(self):
                self.items = [{'entityId': 'x', 'entityType': 'version', 'position': 0},
                              {'entityId': 'a', 'entityType': 'version', 'position': 1}]

            def get_entity_lists(self, project, list_ids=None, fields=None, active=None):
                return iter([{'id': 'L', 'entityType': 'version', 'items': list(self.items)}])

            def create_entity_list_item(self, project, list_id, entity_id, position=None):
                self.items.append({'entityId': entity_id, 'entityType': 'version',
                                   'position': position})
        con = Con()
        with self.assertLogs('AyonLists', 'INFO'):
            self.assertEqual(al.add_missing_items(con, 'p', 'L', ['a', 'b', 'c']), 2)
        self.assertEqual([i['entityId'] for i in con.items], ['x', 'a', 'b', 'c'])
        self.assertEqual(al.add_missing_items(con, 'p', 'L', ['a', 'b']), 0)


if __name__ == '__main__':
    unittest.main()
