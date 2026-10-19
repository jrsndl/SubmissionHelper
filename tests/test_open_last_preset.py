"""Next gui start opens the preset loaded last when it was closed unchanged."""
import json
import os
import shutil
import tempfile
import unittest
from unittest import mock

from tests import _stubs  # noqa: F401
import settings as settings_mod
from settings import Settings, OPEN_PRESET_KEY, preset_changed


class Changed(unittest.TestCase):

    def test_geometry_and_package_are_no_change(self):
        a = {'sub_columns': {'value': 'Shot={shot}'}, 'size': {'size_x': '10'},
             'package_folder': {'value': 'a'}}
        b = {'sub_columns': {'value': 'Shot={shot}'}, 'size': {'size_x': '99'},
             'package_folder': {'value': 'b'}, OPEN_PRESET_KEY: 'x'}
        self.assertFalse(preset_changed(a, b))

    def test_value_change(self):
        self.assertTrue(preset_changed({'a': {'value': 1}}, {'a': {'value': 2}}))
        self.assertTrue(preset_changed({'a': {'value': 1}}, {}))

    def test_combobox_items_are_no_change(self):
        a = {'c': {'category': 'combobox', 'value': 'x', 'all_items': ['x']}}
        b = {'c': {'category': 'combobox', 'value': 'x', 'all_items': ['x', 'y']}}
        self.assertFalse(preset_changed(a, b))
        b['c']['value'] = 'y'
        self.assertTrue(preset_changed(a, b))

    def test_no_baseline_is_changed(self):
        self.assertTrue(preset_changed(None, {}))


class OpenLastPreset(unittest.TestCase):

    def setUp(self):
        self.dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.dir)
        p = mock.patch.object(Settings, 'get_settings_path', return_value=self.dir)
        p.start()
        self.addCleanup(p.stop)
        for name in ('get_user_settings_path', '_get_script_path'):
            p = mock.patch.object(Settings, name, return_value=self.dir)
            p.start()
            self.addCleanup(p.stop)
        p = mock.patch.object(Settings, 'get_global_settings_path', return_value=None)
        p.start()
        self.addCleanup(p.stop)

    def write(self, name, data):
        with open(os.path.join(self.dir, name + '.json'), 'w') as f:
            json.dump(data, f)

    def test_opens_pointed_preset_with_last_geometry(self):
        self.write('clientA', {'sub_columns': {'value': 'A'}, 'size': {'size_x': '1'}})
        self.write('last_me', {'sub_columns': {'value': 'A'}, 'size': {'size_x': '777'},
                               OPEN_PRESET_KEY: 'clientA'})
        s = Settings('last_me', {})
        self.assertEqual(s.open_last_preset(), 'clientA')
        self.assertEqual(s.current_settings_name, 'clientA')
        self.assertEqual(s.settings['size'], {'size_x': '777'})
        self.assertNotIn(OPEN_PRESET_KEY, s.settings)

    def test_without_pointer_stays_last(self):
        self.write('last_me', {'sub_columns': {'value': 'mine'}})
        s = Settings('last_me', {})
        self.assertIsNone(s.open_last_preset())
        self.assertEqual(s.current_settings_name, 'last_me')

    def test_missing_preset_stays_last(self):
        self.write('last_me', {'sub_columns': {'value': 'mine'}, OPEN_PRESET_KEY: 'gone'})
        s = Settings('last_me', {})
        self.assertIsNone(s.open_last_preset())
        self.assertEqual(s.current_settings_name, 'last_me')
        self.assertEqual(s.settings['sub_columns'], {'value': 'mine'})


if __name__ == '__main__':
    unittest.main()
