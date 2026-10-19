"""Parsing tab Preview: Sequencer.fill_regexes keeps each row's result per file."""
import logging
import unittest

from tests import _stubs  # noqa: F401
import sequencer


def seq(rows):
    s = sequencer.Sequencer.__new__(sequencer.Sequencer)
    st = {}
    for n, (name, pattern, repl, source, fltr) in rows.items():
        for field, value in zip(('name', 'pattern', 'repl', 'source', 'filter'),
                                (name, pattern, repl, source, fltr)):
            st[f'parse_{field}_{n:02d}'] = {'value': value}
    s.settings = st
    s.log = logging.getLogger('test')
    s.static_keywords = {}
    s.prepare_regex()
    return s


class Preview(unittest.TestCase):

    def test_results_by_row_and_filtered_rows_missing(self):
        s = seq({1: ('shot', r'^([a-z]+\d+)_', '', '{name}', ''),
                 3: ('task', r'_([a-z]+)_', '', '{name}', '.exr'),
                 4: ('up', r'(.+)', 'lambda m: m.group(1).upper()', '{shot}', '')})
        exr = {'name': 'sh010_comp_v001', 'path': '/p/sh010_comp_v001.1001.exr'}
        mov = {'name': 'sh020_comp_v001', 'path': '/p/sh020_comp_v001.mov'}
        s.merged_list = [exr, mov]
        s.fill_regexes()
        self.assertEqual(exr['_parse_preview'], {'01': 'sh010', '03': 'comp', '04': 'SH010'})
        # the .exr Filter: row 03 didn't run for the mov
        self.assertEqual(mov['_parse_preview'], {'01': 'sh020', '04': 'SH020'})

    def test_refresh_drops_old_results(self):
        s = seq({1: ('shot', r'^(\w+?)_', '', '{name}', '')})
        item = {'name': 'sh010_comp', 'path': '/p/sh010_comp.exr'}
        s.merged_list = [item]
        s.fill_regexes()
        self.assertIn('01', item['_parse_preview'])
        s = seq({2: ('task', r'_(\w+)$', '', '{name}', '')})
        s.merged_list = [item]
        s.fill_regexes()
        self.assertEqual(item['_parse_preview'], {'02': 'comp'})


if __name__ == '__main__':
    unittest.main()
