"""Parsing table row operations (parse_rows.py)."""
import unittest

from tests import _stubs  # noqa: F401
import parse_rows as pr

A = ('shot', r'^(\w+)_', '', '{name}', '')
B = ('task', r'_(\w+)$', '', '{name}', '.exr')
C = ('ver', r'v(\d+)', '', '{name}', '')


class Ops(unittest.TestCase):

    def test_used_rows_compacts_and_slots_pad(self):
        rows = [pr.EMPTY, A, pr.EMPTY, B]
        self.assertEqual(pr.used_rows(rows), [A, B])
        slots = pr.to_slots([A, pr.EMPTY, B], 5)
        self.assertEqual(slots, [A, pr.EMPTY, B, pr.EMPTY, pr.EMPTY])
        self.assertEqual(len(pr.to_slots([A] * 9, 5)), 5)

    def test_move_block(self):
        rows, sel = pr.move([A, B, C], [1, 2], -1)
        self.assertEqual((rows, sel), ([B, C, A], [0, 1]))
        rows, sel = pr.move([A, B, C], [0, 1], 1)
        self.assertEqual((rows, sel), ([C, A, B], [1, 2]))
        # at the top / bottom: nothing moves
        self.assertEqual(pr.move([A, B, C], [0], -1), ([A, B, C], [0]))
        self.assertEqual(pr.move([A, B, C], [2], 1), ([A, B, C], [2]))

    def test_delete(self):
        self.assertEqual(pr.delete([A, B, C], [0, 2]), [B])

    def test_insert_limit(self):
        rows, idx, dropped = pr.insert([A, B], 1, [C, C, C], limit=4)
        self.assertEqual(rows, [A, C, C, B])
        self.assertEqual((idx, dropped), ([1, 2], 1))

    def test_tsv_round_trip(self):
        text = pr.to_tsv([A, ('x\ty', 'a\nb', '', '', '')])
        rows = pr.from_tsv(text)
        self.assertEqual(rows[0], A)
        self.assertEqual(rows[1], ('x y', 'a b', '', '', ''))

    def test_from_tsv_short_lines_header_and_blank(self):
        text = "Name\tPattern\tRepl\tSource\tFilter\r\nshot\t^(\\w+)\r\n\r\n"
        self.assertEqual(pr.from_tsv(text), [('shot', '^(\\w+)', '', '', '')])

    def test_is_rows_text(self):
        self.assertFalse(pr.is_rows_text("{name}\n"))
        self.assertTrue(pr.is_rows_text("a\tb"))
        self.assertTrue(pr.is_rows_text("a\nb"))

    def test_row_problem(self):
        self.assertEqual(pr.row_problem(A), '')
        self.assertEqual(pr.row_problem(pr.EMPTY), '')
        self.assertIn('Source', pr.row_problem(('n', 'p', '', '', '')))
        self.assertIn('Invalid', pr.row_problem(('n', '((', '', '{name}', '')))


if __name__ == '__main__':
    unittest.main()
