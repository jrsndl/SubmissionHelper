import os
import tempfile
import unittest
from unittest import mock

from tests import _stubs  # noqa: F401
import submission_helper as sh
import sh_cli


def args(*argv):
    return vars(sh.get_args(list(argv)))


class CliParseTest(unittest.TestCase):
    def test_defaults_start_gui(self):
        a = args()
        self.assertEqual(a['actions'], 'ftg')
        self.assertEqual(sh.check_cli_args(a), (False, None))

    def test_long_aliases(self):
        a = args('--input', 'x', '--preset', 'y')
        self.assertEqual((a['i'], a['p']), ('x', 'y'))

    def test_help_lists_every_action(self):
        for letter in sh.CLI_ACTIONS:
            self.assertRegex(sh.CLI_EPILOG, rf"\n  {letter}  ")


class CliCheckTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.preset = os.path.join(self.tmp.name, 'p.json')
        with open(self.preset, 'w') as f:
            f.write('{}')

    def test_only_one_of_i_p_is_error_2(self):
        self.assertEqual(sh.check_cli_args(args('-i', self.tmp.name)), (True, 2))
        self.assertEqual(sh.check_cli_args(args('-p', self.preset)), (True, 2))

    def test_missing_input_is_error_1(self):
        a = args('-i', os.path.join(self.tmp.name, 'nope'), '-p', self.preset)
        self.assertEqual(sh.check_cli_args(a), (True, 1))

    def test_unknown_action_is_error_2(self):
        a = args('-i', self.tmp.name, '-p', self.preset, '--actions', 'ftq')
        self.assertEqual(sh.check_cli_args(a), (True, 2))

    def test_valid_headless(self):
        a = args('-i', self.tmp.name, '-p', self.preset, '--actions', 'ftrdsgx')
        self.assertEqual(sh.check_cli_args(a), (True, None))

    def test_preset_by_name(self):
        found = mock.Mock(current_settings_name='clientX')
        missing = mock.Mock(current_settings_name='default')
        with mock.patch.object(sh_cli, 'Settings', return_value=found):
            self.assertEqual(sh.check_cli_args(args('-i', self.tmp.name, '-p', 'clientX')), (True, None))
        with mock.patch.object(sh_cli, 'Settings', return_value=missing):
            self.assertEqual(sh.check_cli_args(args('-i', self.tmp.name, '-p', 'clientX')), (True, 1))


class SettingsOverrideTest(unittest.TestCase):
    def test_types_and_unknown_keys(self):
        w = sh.MainWindow.__new__(sh.MainWindow)
        w.settings = {
            'name_rename_auto': {'category': 'checkbox', 'value': True},
            'prefs_counter_start': {'category': 'spinbox', 'value': 1},
            'name_template': {'category': 'lineedit', 'value': 'a'},
        }
        w.apply_settings_overrides(
            'name_rename_auto=off, prefs_counter_start=5,name_template={shot}_v,bogus=1,prefs_counter_start=x')
        self.assertIs(w.settings['name_rename_auto']['value'], False)
        self.assertEqual(w.settings['prefs_counter_start']['value'], 5)
        self.assertEqual(w.settings['name_template']['value'], '{shot}_v')
        self.assertNotIn('bogus', w.settings)


if __name__ == '__main__':
    unittest.main()
