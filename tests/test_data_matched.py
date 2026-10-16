"""Data tab: Show Matched Only (data_rows_to_show)"""
import unittest

from tests import _stubs  # noqa: F401
import sequencer


def seq(values, rows):
    s = sequencer.Sequencer.__new__(sequencer.Sequencer)
    s.settings = {k: {'value': v} for k, v in values.items()}
    s.csv_data = rows
    return s


class DataMatchedOnly(unittest.TestCase):
    rows = [{'shot': 'a', '_matched': True}, {'shot': 'b'}, {'shot': 'c', '_matched': False}]

    def test_on_by_default(self):
        self.assertEqual([r['shot'] for r in seq({}, self.rows).data_rows_to_show()], ['a'])

    def test_off_shows_all(self):
        s = seq({'data_filter_matched': False}, self.rows)
        self.assertEqual(len(s.data_rows_to_show()), 3)

    def test_no_data(self):
        self.assertEqual(seq({}, None).data_rows_to_show(), [])


if __name__ == '__main__':
    unittest.main()
