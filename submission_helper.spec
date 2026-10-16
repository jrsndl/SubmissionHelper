# -*- mode: python ; coding: utf-8 -*-
#
# PyInstaller spec for Submission Helper. Build with build_exe.bat, or:
#     .venv\Scripts\python -m PyInstaller --noconfirm --clean submission_helper.spec
#
# One folder build (dist\SubmissionHelper) with two executables that share
# all files:
#   SubmissionHelper.exe      GUI, no console window
#   SubmissionHelper-cli.exe  same app with a console, for headless / command
#                             line use (-i -p --actions ...) and log output
#
# The app looks for install.json, presets and the oiio / ocio / ffmpeg
# folders next to the exe; build_exe.bat copies them there.

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

hiddenimports = collect_submodules('ftrack_api') + collect_submodules('ayon_api')
# submission.ui: the command line mode reads its default settings from it
# (ui_defaults.py), without Qt
datas = collect_data_files('ftrack_api') + [('submission.ui', '.')]

a = Analysis(
    ['submission_helper.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    # dev tools installed in the venv, not needed in the app
    excludes=['tkinter', 'pytest', '_pytest', 'sphinx', 'docutils', 'ruff', 'IPython'],
    noarchive=False,
)
pyz = PYZ(a.pure)

common = dict(
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    # UPX can break Qt dlls
    upx=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

exe_gui = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='SubmissionHelper',
    console=False,          # no cmd window
    **common,
)

exe_cli = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='SubmissionHelper-cli',
    console=True,
    **common,
)

coll = COLLECT(
    exe_gui,
    exe_cli,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='SubmissionHelper',
)
