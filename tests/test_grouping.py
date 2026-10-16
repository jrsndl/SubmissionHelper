"""
Grouping tab (grouping.py): group keys, definitions, required representations,
inheritance, collapse, colors, and the Sequencer wiring.
"""
import logging
import unittest

from tests import _stubs  # noqa: F401
import grouping
import sequencer


def item(name, ext, shot='sh010', task='comp', task_type='Compositing', version='v003', **more):
    it = {'name': name, 'extension': ext, 'shot': shot, 'task': task,
          'task_type': task_type, 'version': version,
          'error': '', 'warning': '', 'size_warning': ''}
    it.update(more)
    return it


def cfg(definitions=None, **values):
    settings = {'group_on': True, 'group_definitions': definitions or []}
    settings.update(values)
    return grouping.config(lambda k, d: settings.get(k, d))


def definition(**values):
    d = grouping.new_definition('Comp')
    d.update(values)
    return d


class Basics(unittest.TestCase):

    def test_split_list(self):
        self.assertEqual(grouping.split_list('exr, mp4  mov'), ['exr', 'mp4', 'mov'])
        self.assertEqual(grouping.split_list('Frame Range, Shot\nTask', commas_only=True),
                         ['Frame Range', 'Shot', 'Task'])
        self.assertEqual(grouping.repre_list('.EXR exr Mp4'), ['exr', 'mp4'])

    def test_config_defaults_and_string_bools(self):
        c = grouping.config(lambda k, d: {'group_on': 'False', 'group_collapse_sub': 'true'}.get(k, d))
        self.assertFalse(c['group_on'])
        self.assertTrue(c['group_collapse_sub'])
        self.assertEqual(c['group_repre'], '{extension}')
        self.assertEqual(c['group_by'], '{shot}{task}{version}')
        self.assertEqual(c['group_task_name'], '{task}')
        self.assertEqual(c['definitions'], [])

    def test_clean_definitions_drops_junk_and_fills_fields(self):
        out = grouping.clean_definitions([{'name': 'A', 'inheritance_priority': 'exr'}, 'junk', None])
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0]['inheritance_repre_priority'], 'exr')
        self.assertTrue(out[0]['enabled'])
        self.assertEqual(set(out[0]), set(grouping.DEFINITION_FIELDS))
        self.assertEqual(grouping.clean_definitions('nope'), [])


class Assign(unittest.TestCase):

    def test_off_gives_empty_tokens_and_restores_errors(self):
        a = item('a', 'exr', error='check failed')
        grouping.assign([a], cfg(group_on=False))
        self.assertEqual(a['group_key'], '')
        self.assertEqual(a['error'], 'check failed')

    def test_groups_by_key_in_order(self):
        items = [item('a', 'exr'), item('b', 'exr', shot='sh020'), item('c', 'mp4')]
        groups = grouping.assign(items, cfg())
        self.assertEqual([g['key'] for g in groups], ['sh010compv003', 'sh020compv003'])
        self.assertEqual(items[2]['group_number'], 1)
        self.assertEqual(items[0]['group_size'], 2)
        self.assertEqual(items[0]['group_repres'], 'exr, mp4')

    def test_unknown_token_means_no_group(self):
        a = item('a', 'exr')
        del a['shot']
        self.assertEqual(grouping.assign([a], cfg()), [])
        self.assertEqual(a['group_key'], '')
        self.assertEqual(a['_group_number'], 0)

    def test_vendor_skipped_items_are_not_grouped(self):
        a = item('a', 'exr', vendor_skip=True)
        self.assertEqual(grouping.assign([a], cfg()), [])

    def test_missing_required_is_error_on_all_rows(self):
        d = definition(always_repres='exr', always_or_convert_repres='mp4')
        items = [item('a', 'exr')]
        grouping.assign(items, cfg([d]))
        self.assertIn('missing representation(s) mp4', items[0]['error'])
        self.assertTrue(items[0]['_group_missing'])
        self.assertEqual(items[0]['group_missing'], 'mp4')

    def test_convert_satisfies_convertable_but_not_always(self):
        d = definition(always_repres='exr', always_or_convert_repres='mp4')
        a = item('a', 'exr', convert_path01='D:/pkg/_review/a.mp4')
        grouping.assign([a], cfg([d]))
        self.assertEqual(a['error'], '')
        self.assertEqual(a['group_to_convert'], 'mp4')

        d2 = definition(always_repres='mp4')
        grouping.assign([a], cfg([d2]))
        self.assertIn('missing representation(s) mp4', a['error'])

    def test_errors_are_not_doubled_on_refresh(self):
        d = definition(always_repres='mov')
        a = item('a', 'exr', check_error='bad res', error='bad res')
        for _ in range(3):
            grouping.assign([a], cfg([d]))
        self.assertEqual(a['error'], 'bad res; Group Comp: missing representation(s) mov')

    def test_definition_matching_by_task_type_and_name(self):
        lgt = definition(name='Lighting', task_types='Lighting', task_names='lgt*', always_repres='exr')
        comp = definition(name='Comp', task_types='compositing', always_repres='mov')
        a = item('a', 'exr', task='lgtMain', task_type='Lighting')
        b = item('b', 'exr')
        grouping.assign([a, b], cfg([lgt, comp]))
        self.assertEqual(a['group_name'], 'Lighting')
        self.assertEqual(a['error'], '')
        self.assertEqual(b['group_name'], 'Comp')     # type matched case insensitive
        self.assertIn('mov', b['error'])

    def test_disabled_definition_is_skipped(self):
        d = definition(enabled=False, always_repres='mov')
        a = item('a', 'exr')
        grouping.assign([a], cfg([d]))
        self.assertEqual(a['group_name'], '')
        self.assertEqual(a['error'], '')

    def test_required_with_check_error_fails_the_group(self):
        d = definition(always_repres='exr mp4')
        a = item('a', 'exr', check_error='holes', error='holes')
        b = item('b', 'mp4')
        grouping.assign([a, b], cfg([d]))
        self.assertIn('required representation(s) exr have error(s)', b['error'])
        self.assertEqual(a['error'], 'holes')

    def test_undefined_and_duplicate_repres_warn(self):
        d = definition(always_repres='exr', optional_repres='mp4')
        items = [item('a', 'exr'), item('b', 'exr'), item('c', 'mov')]
        grouping.assign(items, cfg([d]))
        self.assertIn('more than once', items[0]['warning'])
        self.assertIn('mov is not defined', items[2]['warning'])
        self.assertEqual(items[2]['error'], '')

    def test_review_and_thumb_tokens(self):
        d = definition(review_repre='mov mp4', thumb_source_repre='exr')
        a = item('a', 'exr', convert_path01='D:/t/a.jpg')
        b = item('b', 'mp4', full_path='D:/p/b.mp4')
        grouping.assign([a, b], cfg([d]))
        self.assertEqual(a['group_review_full_path'], 'D:/p/b.mp4')
        self.assertEqual(b['group_thumb_convert_path01'], 'D:/t/a.jpg')
        # removed again when the definition no longer asks for them
        grouping.assign([a, b], cfg([definition()]))
        self.assertNotIn('group_review_full_path', a)

    def test_custom_representation_template(self):
        d = definition(always_repres='review')
        a = item('a', 'mp4', repre_name='review')
        grouping.assign([a], cfg([d], group_repre='{repre_name}'))
        self.assertEqual(a['error'], '')


def rows_for(items, columns):
    return [[str(it.get(c, '{' + c + '}')) for c in columns] + [it] for it in items]


class Rows(unittest.TestCase):

    def test_inherit_fills_bad_cells_by_priority(self):
        d = definition(inherit_columns='Frames, Notes', inheritance_repre_priority='mp4 exr')
        a = item('a', 'exr', frames='1001-1100')
        b = item('b', 'mp4', frames='1001-1100x', notes='from mp4')
        c = item('c', 'jpg')
        groups = grouping.assign([a, b, c], cfg([d]))
        rows = rows_for([a, b, c], ['name', 'frames', 'notes'])
        filled = grouping.inherit(rows, ['File', 'Frames', 'Notes '], groups)
        self.assertEqual(rows[0][2], 'from mp4')
        self.assertEqual(rows[2][1], '1001-1100x')     # mp4 first in priority
        self.assertEqual(rows[0][1], '1001-1100')      # good values are kept
        self.assertEqual(filled, 3)

    def test_keep_together(self):
        a, b, c = item('a', 'exr'), item('b', 'exr', shot='sh020'), item('c', 'mp4')
        grouping.assign([a, b, c], cfg())
        rows = rows_for([a, b, c], ['name'])
        self.assertEqual([r[0] for r in grouping.keep_together(rows)], ['a', 'c', 'b'])

    def test_collapse(self):
        d = definition(always_repres='exr mp4 mov')
        a, b = item('a', 'exr'), item('b', 'mp4')
        u = {'name': 'loose', 'shot': 'x'}
        grouping.assign([a, b, u], cfg([d]))
        rows = rows_for([a, u, b], ['shot', 'extension'])
        out = grouping.collapse(rows, ' / ')
        self.assertEqual(len(out), 2)
        self.assertEqual(out[0][:2], ['sh010', 'exr / mp4'])
        self.assertTrue(out[0][-1]['_group_missing'])
        self.assertIn('mov', out[0][-1]['error'])
        self.assertIs(out[1][-1], u)

    def test_exportable_drops_missing_groups(self):
        d = definition(always_repres='mov')
        a, b = item('a', 'exr'), item('b', 'exr', shot='sh020')
        b['extension'] = 'mov'
        grouping.assign([a, b], cfg([d]))
        rows = rows_for([a, b], ['name'])
        self.assertEqual([r[0] for r in grouping.exportable(rows)], ['b'])

    def test_colors_errors_win(self):
        self.assertEqual(grouping.gui_color({'error': 'x', '_group_number': 1}), 'maroon')
        self.assertEqual(grouping.gui_color({'warning': 'x', '_group_number': 1}), 'sienna')
        self.assertEqual(grouping.gui_color({'_group_number': 2}), grouping.GUI_COLORS[1])
        self.assertIsNone(grouping.gui_color({'_group_number': 2}, use_groups=False))
        self.assertIsNone(grouping.gui_color({}))
        self.assertEqual(grouping.excel_color({'_group_number': 9}), grouping.EXCEL_COLORS[0])
        self.assertEqual(grouping.excel_color({'error': 'e'}), grouping.EXCEL_ERROR)


def make_seq(values, items):
    s = sequencer.Sequencer.__new__(sequencer.Sequencer)
    s.log = logging.getLogger('SubmissionHelper')
    s.headless = True
    s.ui = None
    s.output = {}
    s.static_keywords = {}
    s.settings = {k: {'value': v} for k, v in values.items()}
    s.merged_list = items
    s.paths = {}
    return s


class SequencerWiring(unittest.TestCase):

    def _seq(self, **values):
        base = {'group_on': True, 'sub_columns': 'File={name},Ext={extension},Notes={notes},Err={error}',
                'log_columns': 'File={name}', 'txt_columns': ''}
        base.update(values)
        items = [item('a', 'exr', hide_sub=False, hide_log=False, hide_txt=True, vendor_ignore_sub=False),
                 item('x', 'exr', shot='sh020', hide_sub=False, hide_log=False, hide_txt=True,
                      vendor_ignore_sub=False),
                 item('b', 'mp4', notes='n1', hide_sub=False, hide_log=False, hide_txt=True,
                      vendor_ignore_sub=False)]
        s = make_seq(base, items)
        s.prepare_all_columns()
        s.prepare_tables()
        return s

    def test_rows_together_and_group_error_in_columns(self):
        d = definition(always_repres='exr mov', inherit_columns='Notes')
        s = self._seq(group_definitions=[d])
        self.assertEqual([r[0] for r in s.table_sub], ['a', 'b', 'x'])
        self.assertIn('missing representation(s) mov', s.table_sub[0][3])
        self.assertEqual(s.table_sub[0][2], 'n1')        # inherited from the mp4
        self.assertEqual(s.table_log[1][0], 'b')

    def test_collapse_submission_only(self):
        s = self._seq(group_collapse_sub=True)
        self.assertEqual([r[0] for r in s.table_sub], ['a, b', 'x'])
        self.assertEqual(len(s.table_log), 3)
        s = self._seq(group_collapse_sub=True, group_collapse_log=True, group_collapse_sep='|')
        self.assertEqual(s.table_log[0][0], 'a|b')

    def test_grouping_off_keeps_order(self):
        s = self._seq(group_on=False)
        self.assertEqual([r[0] for r in s.table_sub], ['a', 'x', 'b'])
        self.assertEqual(s.table_sub[0][2], '{notes}')

    def test_export_leaves_out_missing_groups(self):
        d = definition(always_repres='mov', task_names='comp')
        s = self._seq(group_definitions=[d])
        self.assertEqual(len(s.submission_rows_for_export()), 0)
        s.settings['group_no_export_missing'] = {'value': False}
        self.assertEqual(len(s.submission_rows_for_export()), 3)


if __name__ == '__main__':
    unittest.main()


class ExcelColors(unittest.TestCase):

    def test_excel_rows_get_group_and_error_fills(self):
        import os
        import tempfile
        import zipfile
        d = definition(always_repres='exr mp4', task_names='comp')
        items = [item('a', 'exr', hide_sub=False, hide_log=True, hide_txt=True, vendor_ignore_sub=False),
                 item('b', 'mp4', hide_sub=False, hide_log=True, hide_txt=True, vendor_ignore_sub=False),
                 item('c', 'exr', shot='sh020', hide_sub=False, hide_log=True, hide_txt=True,
                      vendor_ignore_sub=False)]
        s = make_seq({'group_on': True, 'group_colors_excel': True, 'group_definitions': [d],
                      'sub_columns': 'File={name}', 'log_columns': '', 'txt_columns': ''}, items)
        s.prepare_all_columns()
        s.prepare_tables()
        with tempfile.TemporaryDirectory() as tmp:
            root = os.path.join(tmp, 'sub')
            s.export_file_names = {'sub': {'export_root': root, 'do_excel': True, 'do_csv': False,
                                           'do_skip': False, 'skip': '', 'do_split': False,
                                           'split': '', 'num': 3}}
            s.export_spreadsheet('sub', s.table_sub, s.column_titles_sub)
            with zipfile.ZipFile(root + '.xlsx') as z:
                styles = z.read('xl/styles.xml').decode()
        self.assertIn(grouping.EXCEL_COLORS[0].lstrip('#').upper(), styles.upper())
        self.assertIn(grouping.EXCEL_ERROR.lstrip('#').upper(), styles.upper())
