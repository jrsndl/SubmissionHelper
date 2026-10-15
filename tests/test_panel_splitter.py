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
