"""
Old presets load into the Parsing table: rows as saved, missing fields
(rows 33-48, the Filter column) from the .ui defaults, never from the preset
loaded before; compacting the rows keeps the parsing result.
"""
import logging
import unittest

from tests import _stubs  # noqa: F401
import parse_rows as pr
import sequencer

COUNT = sequencer.PARSE_ROWS


def preset(rows, with_filter=True, count=32):
    """a preset as an older SH saved it: count rows, maybe without Filter"""
    st = {}
    for i in range(1, count + 1):
        values = rows.get(i, pr.EMPTY)
        for field, value in zip(pr.FIELDS, pr.clean(values)):
            if field == 'filter' and not with_filter:
                continue
            st[pr.field_key(i, field)] = {'category': 'lineedit', 'value': value}
    return st


DEFAULTS = {'parse_name_01': {'value': 'shot'},
            'parse_pattern_01': {'value': '([^_*]_[^_*]_)'},
            'parse_source_01': {'value': '{name}'}}


class SlotValues(unittest.TestCase):

    def test_old_preset_with_gaps_and_no_filter(self):
        old = preset({1: ('shot', r'^(\w+)_', '', '{name}'),
                      5: ('task', r'_(\w+)$', '', '{name}'),
                      20: ('ver', r'v(\d+)', '', '{name}')}, with_filter=False)
        values = pr.slot_values(old, DEFAULTS, COUNT)
        self.assertEqual(len(values), COUNT)
        self.assertEqual(values[4], ('task', r'_(\w+)$', '', '{name}', ''))
        self.assertEqual([r[0] for r in pr.used_rows(values)], ['shot', 'task', 'ver'])

    def test_missing_rows_are_not_kept_from_the_previous_preset(self):
        newer = preset({40: ('extra', 'x', '', '{name}', '')}, count=48)
        older = preset({1: ('shot', 'a', '', '{name}', '')}, count=32)
        pr.slot_values(newer, DEFAULTS, COUNT)
        values = pr.slot_values(older, DEFAULTS, COUNT)
        self.assertEqual(values[39], pr.EMPTY)

    def test_missing_row_one_gets_the_ui_default(self):
        values = pr.slot_values({}, DEFAULTS, COUNT)
        self.assertEqual(values[0], ('shot', '([^_*]_[^_*]_)', '', '{name}', ''))
        self.assertEqual(pr.slot_values(None, None, 3), [pr.EMPTY] * 3)

    def test_none_value(self):
        st = {'parse_name_01': {'value': None}}
        self.assertEqual(pr.slot_values(st, {}, 1)[0], pr.EMPTY)


class CompactedRowsParseTheSame(unittest.TestCase):

    def regexes(self, settings):
        s = sequencer.Sequencer.__new__(sequencer.Sequencer)
        s.settings = settings
        s.log = logging.getLogger('test')
        s.prepare_regex()
        return [(r['key'], r['pattern'], r['source']) for r in s.regexes.values()]

    def test_compacting_keeps_rows_and_order(self):
        old = preset({2: ('shot', r'^(\w+)_', '', '{name}'),
                      7: ('shot', r'^(\w+)_', '', '{part2}', '.exr'),
                      31: ('ver', r'v(\d+)', '', '{name}')})
        before = self.regexes(old)
        slots = pr.to_slots(pr.used_rows(pr.slot_values(old, {}, COUNT)), COUNT)
        compacted = {}
        for i, row in enumerate(slots, start=1):
            for field, value in zip(pr.FIELDS, row):
                compacted[pr.field_key(i, field)] = {'value': value}
        self.assertEqual(self.regexes(compacted), before)
        self.assertEqual(compacted['parse_filter_02']['value'], '.exr')


if __name__ == '__main__':
    unittest.main()
