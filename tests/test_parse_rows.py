import logging
import unittest

from tests import _stubs  # noqa: F401
import sequencer
import submission_helper as sh


class ParseRowsTest(unittest.TestCase):
    def bare(self, settings):
        s = sequencer.Sequencer.__new__(sequencer.Sequencer)
        s.settings = settings
        s.log = logging.getLogger('test')
        return s

    def test_48_rows(self):
        self.assertEqual(sequencer.PARSE_ROWS, 48)

    def test_rows_beyond_32_are_used(self):
        st = {}
        for f in sequencer.PARSE_FIELDS:
            st[f'parse_{f}_40'] = {'value': ''}
        st['parse_name_40'] = {'value': 'shot'}
        st['parse_pattern_40'] = {'value': r'(sh\d+)'}
        st['parse_source_40'] = {'value': '{name}'}
        s = self.bare(st)
        s.prepare_regex()
        self.assertIn('40', s.regexes)
        self.assertEqual(s.regexes['40']['key'], 'shot')

    def test_old_preset_without_new_rows_and_invalid_pattern(self):
        s = self.bare({'parse_name_01': {'value': 'a'}, 'parse_pattern_01': {'value': '(('},
                       'parse_source_01': {'value': '{name}'}})
        s.prepare_regex()   # used to raise KeyError for missing rows
        self.assertEqual(s.regexes, {})

    def test_connection_loop_covers_all_fields(self):
        import inspect
        src = inspect.getsource(sh.MainWindow.__init__)
        self.assertIn('for field in PARSE_FIELDS', src)
        self.assertIn('filter', sequencer.PARSE_FIELDS)


if __name__ == '__main__':
    unittest.main()
