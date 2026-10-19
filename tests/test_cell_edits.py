"""Spreadsheet tab: Title=*value columns, edits kept over table rebuilds."""
import unittest

from tests import _stubs  # noqa: F401
import sequencer


def make():
    s = sequencer.Sequencer.__new__(sequencer.Sequencer)
    s.column_editable_sub = []
    s.column_editable_log = []
    s.cell_edits = {'sub': {}, 'log': {}}
    s.column_titles_sub, s.column_expressions_sub = s.prepare_columns(
        "Shot = {shot}, Notes = *{note}, Status=* fixed", s.column_editable_sub)
    s.column_titles_log, s.column_expressions_log = s.prepare_columns(
        "File = {file}", s.column_editable_log)
    return s


def rows(*items):
    return [[it['shot'], it.get('note', ''), 'fixed', it] for it in items]


class Columns(unittest.TestCase):

    def test_star_marks_editable_and_is_not_in_expression(self):
        s = make()
        self.assertEqual(s.column_titles_sub, ['Shot', 'Notes', 'Status'])
        self.assertEqual(s.column_expressions_sub, ['{shot}', '{note}', 'fixed'])
        self.assertEqual(s.column_editable_sub, [False, True, True])
        self.assertEqual(s.column_editable_log, [False])

    def test_without_flags_list_unchanged(self):
        s = make()
        self.assertEqual(s.prepare_columns("Note = *{n}"), (['Note'], ['{n}']))


class Edits(unittest.TestCase):

    def setUp(self):
        self.s = make()
        self.a = {'shot': 'sh010', 'note': 'old', 'path': '/p/a.exr'}
        self.b = {'shot': 'sh020', 'note': 'x', 'path': '/p/b.exr'}
        self.s.table_sub = rows(self.a, self.b)
        self.s.table_log = [['f', self.a]]

    def test_only_editable_columns(self):
        s = self.s
        self.assertFalse(s.set_cell_edit('sub', 0, 0, 'hack'))
        self.assertEqual(s.table_sub[0][0], 'sh010')
        self.assertFalse(s.set_cell_edit('log', 0, 0, 'hack'))
        self.assertFalse(s.set_cell_edit('sub', 5, 1, 'out of range'))

    def test_edit_goes_to_table_and_survives_rebuild(self):
        s = self.s
        self.assertTrue(s.set_cell_edit('sub', 1, 1, 'send this one'))
        self.assertEqual(s.table_sub[1][1], 'send this one')
        # refresh: rows rebuilt in another order
        s.table_sub = rows(self.b, self.a)
        s.apply_cell_edits('sub')
        self.assertEqual(s.table_sub[0][1], 'send this one')
        self.assertEqual(s.table_sub[1][1], 'old')

    def test_column_no_longer_editable_drops_to_normal_value(self):
        s = self.s
        s.set_cell_edit('sub', 0, 1, 'new')
        s.column_editable_sub = []
        s.column_titles_sub, s.column_expressions_sub = s.prepare_columns(
            "Shot = {shot}, Notes = {note}, Status = fixed", s.column_editable_sub)
        s.table_sub = rows(self.a, self.b)
        s.apply_cell_edits('sub')
        self.assertEqual(s.table_sub[0][1], 'old')

    def test_new_sequencer_has_no_edits(self):
        self.s.set_cell_edit('sub', 0, 1, 'new')
        fresh = make()
        fresh.table_sub = rows(self.a, self.b)
        fresh.apply_cell_edits('sub')
        self.assertEqual(fresh.table_sub[0][1], 'old')

    def test_collapsed_group_row(self):
        s = self.s
        summary = {'_group_members': [self.a, self.b], 'group_key': 'sh010comp'}
        s.table_sub = [['sh010, sh020', 'old, x', 'fixed', summary]]
        self.assertTrue(s.set_cell_edit('sub', 0, 1, 'group note'))
        s.table_sub = [['sh010, sh020', 'old, x', 'fixed',
                        {'_group_members': [self.a, self.b], 'group_key': 'sh010comp'}]]
        s.apply_cell_edits('sub')
        self.assertEqual(s.table_sub[0][1], 'group note')

    def test_row_without_file_cannot_keep_edit(self):
        s = self.s
        s.table_sub = [['sh', 'n', 'fixed', {'shot': 'sh'}]]
        self.assertFalse(s.set_cell_edit('sub', 0, 1, 'x'))

    def test_without_init_attributes(self):
        s = sequencer.Sequencer.__new__(sequencer.Sequencer)
        s.table_sub, s.column_titles_sub = [], []
        s.apply_cell_edits('sub')   # no AttributeError


if __name__ == '__main__':
    unittest.main()
