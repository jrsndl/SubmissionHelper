"""
The command line mode must run without Qt: sh_cli, ui_defaults and the
Sequencer import and run with PySide2 blocked. Runs in a subprocess, so the
Qt stubs of the other tests don't hide an import.
"""
import csv
import glob
import json
import os
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RUNNER = r"""
import sys, types
sys.modules['PySide2'] = None          # any Qt import fails
class _Any(types.ModuleType):
    def __getattr__(self, n):
        if n.startswith('__'):
            raise AttributeError(n)
        return _Any(n)
    def __call__(self, *a, **k):
        return _Any('x')
# optional services, not installed in every test environment
for m in ('ftrack_api', 'ftrack_api.exception', 'ayon_api', 'httpx', 'xlsxwriter'):
    try:
        __import__(m)
    except Exception:
        sys.modules[m] = _Any(m)
try:
    import unidecode
except Exception:
    sys.modules['unidecode'] = types.SimpleNamespace(unidecode=lambda s: s)
sys.path.insert(0, sys.argv[1])
import sh_cli
rc = sh_cli.main(sys.argv[2:])
assert not any(k.startswith('PySide2') and sys.modules[k] is not None for k in sys.modules), 'Qt was imported'
sys.exit(rc)
"""


class CliWithoutQt(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.pkg = os.path.join(self.tmp.name, 'pkg_v001')
        os.makedirs(os.path.join(self.pkg, 'sh010'))
        for n in (1001, 1002, 1003):
            with open(os.path.join(self.pkg, 'sh010', f'sh010_comp_v003.{n}.jpg'), 'wb') as f:
                f.write(b'x' * 100)
        self.preset = os.path.join(self.tmp.name, 'preset.json')
        with open(self.preset, 'w') as f:
            # partial preset: everything else comes from submission.ui
            json.dump({'name_rename_auto': {'category': 'checkbox', 'value': False}}, f)
        self.runner = os.path.join(self.tmp.name, 'run.py')
        with open(self.runner, 'w') as f:
            f.write(RUNNER)

    def _run(self, *argv):
        return subprocess.run([sys.executable, self.runner, REPO, *argv],
                              capture_output=True, text=True, timeout=300,
                              env={**os.environ, 'PATH': ''})   # no ffprobe: faster, still runs

    def test_headless_go_without_qt(self):
        r = self._run('-i', self.pkg, '-p', self.preset, '--actions', 'ftg',
                      '--settings', 'export_sub_csv=true,export_sub_excel=false')
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn('Headless run finished: 0 error(s)', r.stdout + r.stderr)
        files = glob.glob(os.path.join(self.pkg, '*.csv'))
        self.assertTrue(files, r.stdout + r.stderr)
        with open([f for f in files if not f.endswith('_log.csv')][0], newline='') as f:
            rows = list(csv.reader(f))
        self.assertEqual(len(rows), 2)          # title + the one sequence
        self.assertIn('sh010_comp_v003.%04d.jpg', rows[1])

    def test_bad_arguments(self):
        self.assertEqual(self._run('-i', self.pkg).returncode, 2)
        self.assertEqual(self._run('-i', self.pkg, '-p', self.preset, '--actions', 'q').returncode, 2)


class UiDefaults(unittest.TestCase):

    def test_defaults_from_ui_file(self):
        sys.path.insert(0, REPO)
        import ui_defaults
        d = ui_defaults.load_defaults()
        self.assertGreater(len(d), 400)
        # same shape as MainWindow.settings_from_gui
        self.assertEqual(d['package_folder']['category'], 'lineedit')
        self.assertIsInstance(d['name_rename_auto']['value'], bool)
        self.assertIsInstance(d['prefs_counter_start']['value'], int)
        combo = next(v for v in d.values() if v['category'] == 'combobox')
        self.assertIn(combo['value'], combo['all_items'] + [''])
        self.assertNotIn('log', d)


class HandOver(unittest.TestCase):

    def test_wants_headless(self):
        sys.path.insert(0, REPO)
        import sh_cli
        self.assertTrue(sh_cli.wants_headless(['-i', 'x', '-p', 'y']))
        self.assertTrue(sh_cli.wants_headless(['--input=x']))
        self.assertFalse(sh_cli.wants_headless([]))
        self.assertFalse(sh_cli.wants_headless(['--log-level', 'debug']))


if __name__ == '__main__':
    unittest.main()
