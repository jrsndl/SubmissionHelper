import glob
import logging
import os
import re
import unittest

from tests import _stubs  # noqa: F401
import sequencer

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class SettingsKeysExistTest(unittest.TestCase):
    """
    Every gui setting the code reads must be a widget of the window (or one
    created in code). Settings are rebuilt from the widgets, so a key without
    a widget is missing at runtime: KeyError 'ftrack_include' was one.
    """
    # keys that are not widgets: window geometry, install.json settings
    NOT_WIDGETS = {'size', 'position', 'panel_splitter', 'global_prefs_enabled', 'global_prefs_path'}

    def test_all_literal_keys_have_widgets(self):
        ui = open(os.path.join(REPO, 'ui_Submission.py'), encoding='utf-8').read()
        sh = open(os.path.join(REPO, 'submission_helper.py'), encoding='utf-8').read()
        known = set(re.findall(r'self\.(\w+) = Q\w+\(', ui)) | set(re.findall(r'ui\.(\w+) = ', sh))
        known |= self.NOT_WIDGETS
        missing = {}
        for path in glob.glob(os.path.join(REPO, '*.py')):
            name = os.path.basename(path)
            if name.startswith('ui_'):
                continue
            src = open(path, encoding='utf-8').read()
            pattern = r"settings\s*(?:\[\s*['\"]([\w-]+)['\"]\s*\]|\.get\(\s*['\"]([\w-]+)['\"])"
            for m in re.finditer(pattern, src):
                key = m.group(1) or m.group(2)
                if key not in known:
                    missing.setdefault(key, []).append(f"{name}:{src.count(chr(10), 0, m.start()) + 1}")
        # ftrack_include stays as a fallback for older presets
        missing.pop('ftrack_include', None)
        self.assertEqual(missing, {})


class FtrackSessionSettingsTest(unittest.TestCase):
    def bare(self, settings):
        s = sequencer.Sequencer.__new__(sequencer.Sequencer)
        s.log = logging.getLogger('test')
        s.settings = settings
        s.ftrack = {}
        s.paths = {}
        return s

    def test_missing_keys_do_not_crash(self):
        s = self.bare({'ftrack_use': {'value': False}})
        s.get_ftrack_session()
        self.assertEqual(s.ftrack['include'], [])
        self.assertFalse(s.ftrack['do_ftrack'])

    def test_extensions_field_and_old_name(self):
        s = self.bare({'ftrack_use': {'value': False}, 'ftrack_include_2': {'value': 'mov, .EXR  dpx'}})
        s.get_ftrack_session()
        self.assertEqual(s.ftrack['include'], ['mov', 'exr', 'dpx'])
        s = self.bare({'ftrack_use': {'value': False}, 'ftrack_include': {'value': 'mov'}})
        s.get_ftrack_session()
        self.assertEqual(s.ftrack['include'], ['mov'])
