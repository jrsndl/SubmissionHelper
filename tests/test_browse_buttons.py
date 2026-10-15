import os
import tempfile
import unittest
from unittest import mock

from tests import _stubs  # noqa: F401
import submission_helper as sh


class FakeLineEdit:
    def __init__(self, text=''):
        self._t = text
        self.set_calls = []

    def text(self):
        return self._t

    def setText(self, t):
        self._t = t
        self.set_calls.append(t)


class FakeCheck:
    def __init__(self, on):
        self.on = on

    def isChecked(self):
        return self.on


def window():
    return sh.MainWindow.__new__(sh.MainWindow)


class BrowseLineEditTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def test_pick_folder_sets_text_with_forward_slashes(self):
        le = FakeLineEdit()
        dlg = mock.Mock()
        dlg.getExistingDirectory.return_value = 'C:\\shots\\side'
        with mock.patch.object(sh.QtWidgets, 'QFileDialog', dlg):
            window().browse_line_edit(le, 'dir', 't', False)  # False = clicked(checked)
        self.assertEqual(le.text(), 'C:/shots/side')

    def test_cancel_keeps_text(self):
        le = FakeLineEdit('keep/me')
        dlg = mock.Mock()
        dlg.getOpenFileName.return_value = ('', '')
        with mock.patch.object(sh.QtWidgets, 'QFileDialog', dlg):
            window().browse_line_edit(le, 'csv', 't')
        self.assertEqual(le.set_calls, [])

    def test_csv_dialog_starts_in_existing_parent(self):
        sub = os.path.join(self.tmp.name, 'a')
        os.makedirs(sub)
        le = FakeLineEdit(os.path.join(sub, 'missing', 'x.csv'))
        dlg = mock.Mock()
        dlg.getOpenFileName.return_value = (sub + '/v.csv', 'CSV')
        with mock.patch.object(sh.QtWidgets, 'QFileDialog', dlg):
            window().browse_line_edit(le, 'csv', 't')
        start = dlg.getOpenFileName.call_args[0][2]
        self.assertEqual(start, sub.replace('\\', '/'))
        self.assertEqual(le.text(), sub + '/v.csv')

    def test_data_csv_uses_folder_dialog_when_latest(self):
        w = window()
        w.ui = mock.Mock()
        w.ui.data_csv_path = FakeLineEdit()
        dlg = mock.Mock()
        dlg.getExistingDirectory.return_value = '/data'
        for latest, expect in ((True, 'getExistingDirectory'), (False, 'getOpenFileName')):
            w.ui.data_csv_latest = FakeCheck(latest)
            dlg.reset_mock()
            dlg.getOpenFileName.return_value = ('/data/a.csv', '')
            with mock.patch.object(sh.QtWidgets, 'QFileDialog', dlg):
                w.browse_data_csv(False)
            self.assertTrue(getattr(dlg, expect).called, expect)

    def test_explore_falls_back_to_existing_parent(self):
        w = window()
        w.explore = mock.Mock()
        w.explore_line_edit(FakeLineEdit(os.path.join(self.tmp.name, 'nope', 'f.csv')), False)
        w.explore.assert_called_once_with(self.tmp.name.replace('\\', '/'))


if __name__ == '__main__':
    unittest.main()
