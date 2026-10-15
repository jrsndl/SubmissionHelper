import json
import os
import sys
import tempfile
import unittest

from tests import _stubs  # noqa: F401
import settings as settings_mod


def make_settings(script_dir, user_dir, name='last_test', install=None):
    """Build a Settings object whose app and user folders point to temp dirs."""
    S = settings_mod.Settings
    orig = (S._get_script_path, S.get_user_settings_path)
    S._get_script_path = lambda self: script_dir
    S.get_user_settings_path = lambda self: user_dir
    try:
        if install is not None:
            with open(os.path.join(script_dir, 'install.json'), 'w') as f:
                json.dump(install, f)
        return S(name, {})
    finally:
        S._get_script_path, S.get_user_settings_path = orig


class SettingsReadTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.script = os.path.join(self.tmp.name, 'app')
        self.user = os.path.join(self.tmp.name, 'user')
        os.makedirs(self.script)

    def tearDown(self):
        self.tmp.cleanup()

    def test_no_presets_at_all_gives_empty_dict(self):
        # fresh clone: no last_<user>.json and default.json is gitignored
        s = make_settings(self.script, self.user)
        self.assertEqual(s.settings, {})
        self.assertEqual(s.current_settings_name, 'default')

    def test_preset_in_app_folder_loads_by_name(self):
        with open(os.path.join(self.script, 'clientX.json'), 'w') as f:
            json.dump({'a': {'value': 1}}, f)
        s = make_settings(self.script, self.user, name='clientX')
        self.assertEqual(s.settings, {'a': {'value': 1}})
        self.assertEqual(s.current_settings_name, 'clientX')

    def test_missing_preset_falls_back_and_does_not_keep_name(self):
        with open(os.path.join(self.script, 'default.json'), 'w') as f:
            json.dump({'d': {'value': True}}, f)
        s = make_settings(self.script, self.user, name='doesnotexist')
        self.assertEqual(s.settings, {'d': {'value': True}})
        self.assertEqual(s.current_settings_name, 'default')

    def test_corrupt_preset_falls_back(self):
        with open(os.path.join(self.script, 'bad.json'), 'w') as f:
            f.write('{not json')
        s = make_settings(self.script, self.user, name='bad')
        self.assertEqual(s.settings, {})

    def test_missing_user_dir_does_not_list_parent_jsons(self):
        with open(os.path.join(self.tmp.name, 'unrelated.json'), 'w') as f:
            f.write('{}')
        s = make_settings(self.script, self.user)
        self.assertNotIn('unrelated', s.preset_names)

    def test_install_json_without_global_keys(self):
        s = make_settings(self.script, self.user, install={'ffprobe_path': ''})
        self.assertIsNone(s.get_global_settings_path())

    def test_global_prefs_string_false(self):
        gdir = os.path.join(self.tmp.name, 'global')
        os.makedirs(gdir)
        s = make_settings(self.script, self.user,
                          install={'global_prefs_enabled': 'false', 'global_prefs_path': gdir})
        self.assertIsNone(s.get_global_settings_path())

    @unittest.skipIf(sys.platform == 'win32', 'posix exe suffix handling')
    def test_relative_exe_path_suffix_removed_not_chars(self):
        s = make_settings(self.script, self.user,
                          install={'ffprobe_path': './ffmpeg/ffprobe.exe',
                                   'vfx-transcode_path': './vfx-transcode.exe'})
        self.assertTrue(s.install_settings['ffprobe_path'].endswith('/ffmpeg/ffprobe'))
        self.assertTrue(s.install_settings['vfx-transcode_path'].endswith('/vfx-transcode'))


if __name__ == '__main__':
    unittest.main()
