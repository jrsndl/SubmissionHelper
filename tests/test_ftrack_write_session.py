"""ftrack list write: a new session, and an error after the save that left the list complete."""
import unittest
from unittest import mock

from tests import _stubs  # noqa: F401
import ftrack


class _Result:
    def __init__(self, items):
        self.items = items

    def all(self):
        return self.items

    def first(self):
        return self.items[0] if self.items else None


class Fake:
    """saves on commit, then raises like the recursion error"""

    def __init__(self, raise_after_commit=False, save=True):
        self.lists = {}
        self.objects = []
        self.pending = []
        self.raise_after_commit = raise_after_commit
        self.save = save
        self.closed = False

    def query(self, q):
        if 'ListCategory' in q:
            return _Result([{'id': 'c1', 'name': 'Client'}])
        if q.startswith('select id, name, category_id from List'):
            return _Result([{'id': i, 'name': d['name'], 'category_id': d['category_id']}
                            for i, d in self.lists.items()])
        if 'ListObject' in q:
            return _Result([{'entity_id': e} for _, e in self.objects])
        raise AssertionError(q)

    def create(self, etype, data):
        self.pending.append((etype, data))
        return dict(data, id='L1')

    def commit(self):
        if self.save:
            for etype, data in self.pending:
                if etype == 'List':
                    self.lists['L1'] = data
                else:
                    self.objects.append((data['list_id'], data['entity_id']))
        self.pending = []
        if self.raise_after_commit:
            raise RecursionError('maximum recursion depth exceeded')

    def rollback(self):
        self.pending = []

    def close(self):
        self.closed = True


class WriteSession(unittest.TestCase):

    def test_error_after_save_counts_as_done(self):
        s = Fake(raise_after_commit=True)
        with self.assertLogs('Ftrack', 'WARNING'):
            self.assertEqual(ftrack.create_version_list(s, 'P', 'sub', 'Client', ['a', 'b']), 'L1')

    def test_error_without_save_raises(self):
        s = Fake(raise_after_commit=True, save=False)
        with self.assertRaises(RecursionError):
            ftrack.create_version_list(s, 'P', 'sub', 'Client', ['a'])

    def test_new_session_used_and_closed(self):
        shared = mock.Mock(server_url='https://ft', api_user='me', api_key='k')
        fresh = Fake()
        with mock.patch.object(ftrack.ftrack_api, 'Session', return_value=fresh) as S:
            ftrack.create_version_list(shared, 'P', 'sub', 'Client', ['a'])
        S.assert_called_once()
        self.assertTrue(fresh.closed)
        shared.create.assert_not_called()
        self.assertEqual(fresh.objects, [('L1', 'a')])


if __name__ == '__main__':
    unittest.main()
