"""Push to Ftrack too: the AYON list is created as well, paired by the ftrack list id."""
import unittest

from tests import _stubs  # noqa: F401
import ayon_lists as al


class Tries(unittest.TestCase):

    def test_order_attrib_first_no_duplicates(self):
        tries = al._create_tries('Subs', 'FT1')
        self.assertEqual(tries[0], {'attrib': {'category': 'Subs', 'ftrackId': 'FT1'}})
        self.assertIn({'data': {'category': 'Subs', 'ftrackId': 'FT1'}}, tries)
        self.assertEqual(len(tries), 4)
        self.assertEqual(al._create_tries('', None), [{}])
        self.assertEqual(al._create_tries('', 'FT1'),
                         [{'attrib': {'ftrackId': 'FT1'}}, {'data': {'ftrackId': 'FT1'}}])


class Create(unittest.TestCase):

    def test_ftrack_id_stays_in_attrib_when_category_attrib_is_refused(self):
        class Con:
            def __init__(self):
                self.calls = []

            def create_entity_list(self, project, etype, label, **kw):
                self.calls.append(kw)
                if 'category' in kw.get('attrib', {}):
                    raise RuntimeError('400 unknown attribute category')
                self.items = kw.get('items')
                return 'L'

            def get_entity_lists(self, project, list_ids=None, fields=None, active=None):
                return iter([{'id': 'L', 'entityType': 'version', 'items': self.items}])
        con = Con()
        self.assertEqual(al.create_version_list(con, 'p', 'sub', ['a'], 'Subs', ftrack_id='FT1'), 'L')
        last = con.calls[-1]
        self.assertEqual(last['attrib'], {'ftrackId': 'FT1'})
        self.assertEqual(last['data'], {'category': 'Subs'})


if __name__ == '__main__':
    unittest.main()
