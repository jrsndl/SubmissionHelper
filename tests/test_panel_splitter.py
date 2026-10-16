import os
import unittest

from tests import _stubs  # noqa: F401
import submission_helper as sh


class FakeSplitter:
    def __init__(self, sizes):
        self._s = list(sizes)

    def sizes(self):
        return list(self._s)

    def setSizes(self, s):
        self._s = list(s)


class PanelSplitterResetTest(unittest.TestCase):
    def test_reset_keeps_total_and_sets_default_top(self):
        w = sh.MainWindow.__new__(sh.MainWindow)
        w.panel_splitter = FakeSplitter([600, 300])
        w._reset_panel_splitter()
        self.assertEqual(w.panel_splitter.sizes(), [sh.MainWindow.TOP_PANEL_DEFAULT, 900 - sh.MainWindow.TOP_PANEL_DEFAULT])

    def test_reset_before_window_is_shown(self):
        # before show() a splitter reports [0, 0]
        w = sh.MainWindow.__new__(sh.MainWindow)
        s = FakeSplitter([0, 0])
        w._reset_panel_splitter(s)
        top, bottom = s.sizes()
        self.assertEqual(top, sh.MainWindow.TOP_PANEL_DEFAULT)
        self.assertGreaterEqual(bottom, sh.MainWindow.BOTTOM_PANEL_MIN)


if __name__ == '__main__':
    unittest.main()


class LayoutTuningNamesTest(unittest.TestCase):
    def test_widgets_used_by_layout_code_exist_in_ui(self):
        # guards against regenerating ui_Submission.py with renamed objects
        import re
        here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        src = open(os.path.join(here, 'submission_helper.py'), encoding='utf-8').read()
        ui = open(os.path.join(here, 'ui_Submission.py'), encoding='utf-8').read()
        body = src[src.index('def _setup_panel_splitter'):src.index('def _reset_panel_splitter')]
        names = set(re.findall(r'(?:ui|self\.ui)\.(\w+)', body))
        # widgets the code creates itself
        names -= set(re.findall(r'(?:ui|self\.ui)\.(\w+) = ', body))
        self.assertTrue(names)
        missing = sorted(n for n in names if f'self.{n} = ' not in ui)
        self.assertEqual(missing, [])


class PresetModulesTest(unittest.TestCase):
    def test_widgets_used_exist_in_ui(self):
        import re
        here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        src = open(os.path.join(here, 'submission_helper.py'), encoding='utf-8').read()
        ui = open(os.path.join(here, 'ui_Submission.py'), encoding='utf-8').read()
        start = src.index('def _arrange_preset_modules')
        body = src[start:src.index('\n    def ', start)]
        names = set(re.findall(r'(?:ui|self\.ui)\.(\w+)', body)) - {'groupBox_18'}
        missing = sorted(n for n in names if f'self.{n} = ' not in ui)
        self.assertEqual(missing, [])
        self.assertIn('self.groupBox_18 = ', ui)

    def test_every_module_checkbox_is_listed(self):
        import re
        here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ui = open(os.path.join(here, 'ui_Submission.py'), encoding='utf-8').read()
        in_ui = set(re.findall(r'self\.preset_mod_(\w+) = QCheckBox', ui)) | {'grouping'}
        listed = set(sh.MainWindow.MODULES_TOP) | set(sh.MainWindow.MODULES_BOTTOM)
        self.assertEqual(in_ui - listed, set())
        self.assertEqual(listed - in_ui, set())
