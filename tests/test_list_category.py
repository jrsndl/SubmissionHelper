"""AYON list category: the attribute's options, and a category that only lands in data."""
import unittest

from tests import _stubs  # noqa: F401
import ayon_lists as al


class Options(unittest.TestCase):

    def test_enum_dicts_and_strings(self):
        class Con:
            def get_attributes_for_type(self, scope):
                assert scope == 'list'
                return {'category': {'type': 'string', 'enum': [
                    {'value': 'Submissions', 'label': 'Submissions'}, 'Finals', {'value': ''}]},
                    'ftrackId': {'type': 'string', 'enum': None}}
        self.assertEqual(al.category_options(Con()), ['Submissions', 'Finals'])

    def test_no_attribute_or_error(self):
        class NoCat:
            def get_attributes_for_type(self, scope):
                return {'ftrackId': {}}

        class Old:
            pass
        self.assertEqual(al.category_options(NoCat()), [])
        self.assertEqual(al.category_options(Old()), [])


class Warning(unittest.TestCase):

    def test_category_only_in_data_is_logged(self):
        class Con:
            items = []

            def create_entity_list(self, project, etype, label, **kw):
                if 'category' in kw.get('attrib', {}):
                    raise RuntimeError('400 value not in enum')
                self.items = kw.get('items')
                return 'L'

            def get_entity_lists(self, project, list_ids=None, fields=None, active=None):
                return iter([{'id': 'L', 'entityType': 'version', 'items': self.items}])
        with self.assertLogs('AyonLists', 'WARNING') as cm:
            al.create_version_list(Con(), 'p', 'sub', ['a'], 'Client')
        self.assertIn("'Client' is not accepted", cm.output[0])


if __name__ == '__main__':
    unittest.main()
