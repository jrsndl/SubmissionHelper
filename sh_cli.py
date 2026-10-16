"""
Command line mode of Submission Helper, without Qt.

    python sh_cli.py -i <package> -p <preset> [--actions ftg] ...
    python submission_helper.py -i ... -p ...     (hands over to this module
                                                   before importing Qt)

Nothing here imports PySide2: the headless run works on machines without Qt
or a display (render farm nodes). Default settings come from submission.ui
(ui_defaults), the preset is laid over them, then --settings overrides.
"""
import argparse
import logging
import os
import sys

import sh_logging
from settings import Settings

log = logging.getLogger("SubmissionHelper")

CLI_ACTIONS = "ftdgsrcpPax"

CLI_DESCRIPTION = """\
Submission Helper - check, rename and document vfx packages.

Without -i/-p the GUI starts. With both -i and -p it runs headless:
the preset is loaded, the --actions are run in order, and the app exits.
"""

CLI_EPILOG = """\
actions (letters for --actions, run left to right):
  f  read files      scan the package folder, read metadata, csv/ayon/ftrack data
  t  transform data  apply parsing, columns, naming and checks
                     (most actions below need f and t to run first)
  d  reload          same as f + t, use after r (rename) or c (convert)
  g  go              same as the Go button: export submission, drive log and
                     text as set in the preset. Also copies sidecars ("Copy
                     with Go"), runs converts ("Convert on Go") and renames
                     the package folder ("Auto Rename") when those are on.
                     Nothing is exported without g.
  s  sidecar files   copy sidecar files to their destinations
  r  rename          rename / move files using the Rename tab rules
  c  convert         run the Convert tab commands
  p  publish ayon    export submission csv and ingest it to Ayon locally
  P  publish farm    same as p, submitted as a Deadline job
  a  ayon shotlist   read, filter and write the Ayon shot list (Ayon tab)
  x  ftrack list     write the ftrack shot list to the Ftrack tab Export path

examples:
  # GUI
  python submission_helper.py

  # check a package and export spreadsheets with a preset file
  python submission_helper.py -i D:/out/pkg_v001 -p D:/presets/clientX.json

  # same, preset by name from the presets folder
  python submission_helper.py -i D:/out/pkg_v001 -p clientX

  # rename, reload, copy sidecars, export
  python submission_helper.py -i D:/out/pkg_v001 -p clientX --actions ftrdsg

  # override preset values for this run only
  python submission_helper.py -i D:/out/pkg_v001 -p clientX --settings name_rename_auto=false,prefs_counter_start=5

  # the same without Qt / PySide2 installed (render farm nodes)
  python sh_cli.py -i D:/out/pkg_v001 -p clientX

  (with the built exe, use SubmissionHelper-cli.exe instead of python submission_helper.py)

The command line mode doesn't use Qt: it runs without PySide2 and without a
display. Its default settings are read from submission.ui.

exit codes:
  0  finished
  1  input or preset not found, or an action crashed
     (many problems are only logged, check the log output)
  2  bad arguments (only one of -i/-p, unknown action letter)
"""


def setting_to_bool(value):
    """
    bool of a saved setting: "False" / "false" / "0" / "off" / "no" / "" are
    False (bool("False") is True, which turned unchecked boxes on)
    """
    if isinstance(value, str):
        return value.strip().lower() not in ('', 'false', '0', 'off', 'no', 'none')
    return bool(value)


def get_args(argv=None):

    parser = argparse.ArgumentParser(
        prog="submission_helper",
        description=CLI_DESCRIPTION,
        epilog=CLI_EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '-i', '--input',
        dest='i',
        metavar='PATH',
        help="Package folder, or a csv file inside it (with Vendor tab "
             "'Auto Detect' on in the preset, the csv is used as the vendor csv). "
             "Required for headless mode.",
        type=str,
        required=False
    )
    parser.add_argument(
        '-p', '--preset',
        dest='p',
        metavar='PRESET',
        help="Preset json file, or the name of a saved preset (without "
             ".json). Required for headless mode.",
        type=str,
        required=False
    )
    parser.add_argument(
        '--actions',
        metavar='LETTERS',
        help="Headless actions to run, in order. See the list below. "
             "Default: %(default)s",
        type=str,
        default="ftg"
    )
    parser.add_argument(
        '--settings',
        metavar='KEY=VALUE[,KEY=VALUE...]',
        help="Override preset values for this run. Keys are the setting names "
             "used in the preset json. Checkboxes take true/false (1/0, yes/no, "
             "on/off), number fields take integers, text fields take the text "
             "as is. Values can't contain commas.",
        type=str,
        default=""
    )
    log_group = parser.add_argument_group(
        'logging',
        "Console output (stderr), in GUI and headless mode. The GUI Log tab "
        "has its own level filter.")
    log_group.add_argument(
        '--log-level',
        choices=['debug', 'info', 'warning', 'error', 'none'],
        default='info',
        help="Console log level, 'none' turns console output off. Default: %(default)s")
    log_group.add_argument(
        '-v', '--verbose',
        action='store_true',
        help="Same as --log-level debug")
    log_group.add_argument(
        '-q', '--quiet',
        action='store_true',
        help="Same as --log-level warning")
    log_group.add_argument(
        '--log-file',
        metavar='PATH',
        help="Also append the full log (all levels, with dates) to this file")
    return parser.parse_args(argv)


def console_level_from_args(args):
    """
    :param args: dict from vars(get_args())
    :return: logging level for the console, None for no console output
    """
    if args.get('verbose'):
        return logging.DEBUG
    if args.get('quiet'):
        return logging.WARNING
    return sh_logging.level_from_name(args.get('log_level', 'info'))

def check_cli_args(args):
    """
    Validate command line arguments.
    :param args: dict from vars(get_args())
    :return: (headless, exit_code) - exit_code is None when the app should start
    """
    input_path = args.get('i')
    input_preset = args.get('p')
    if input_path is None and input_preset is None:
        return False, None

    # headless was requested, fail loudly instead of silently opening the gui
    if input_path is None or input_preset is None:
        log.error("Headless mode needs both -i and -p.")
        return True, 2
    bad = sorted(set(args.get('actions') or '') - set(CLI_ACTIONS))
    if bad:
        log.error(f"Unknown action letter(s) {', '.join(bad)} in --actions '{args['actions']}'. "
                  f"Valid: {CLI_ACTIONS}")
        return True, 2
    if not os.path.exists(input_path):
        log.error(f"Input path '{input_path}' does not exist.")
        return True, 1
    if not os.path.isfile(input_preset):
        # allow a preset name, resolved like the gui's preset list
        _probe = Settings(input_preset, args)
        if _probe.current_settings_name != input_preset:
            log.error(f"Preset '{input_preset}' not found (not a file, not a saved preset name).")
            return True, 1
    return True, None


def apply_settings_overrides(settings, overrides):
    """
    Apply --settings overrides "key1=value1,key2=value2" to settings.
    Values are converted by the category of the existing setting.
    """
    if not overrides:
        return
    for pair in overrides.split(','):
        pair = pair.strip()
        if not pair:
            continue
        if '=' not in pair:
            log.warning(f"Ignoring settings override '{pair}', expected key=value")
            continue
        key, value = [x.strip() for x in pair.split('=', 1)]
        one_setting = settings.get(key)
        if one_setting is None:
            log.warning(f"Ignoring settings override '{key}', unknown setting")
            continue
        category = one_setting.get('category', '')
        try:
            if category in ('checkbox', 'radiobutton'):
                value = value.lower() in ('1', 'true', 'yes', 'on')
            elif category == 'spinbox':
                value = int(value)
        except ValueError:
            log.warning(f"Ignoring settings override '{key}={value}', bad value for {category}")
            continue
        one_setting['value'] = value
        log.info(f"Settings override: {key} = {value!r}")


def headless_settings(settings_obj, input_path, overrides=''):
    """
    Settings for a headless run: submission.ui defaults, the preset over them
    (older or partial presets don't raise KeyError later), --settings last.
    """
    import ui_defaults
    settings = ui_defaults.load_defaults()
    settings.update(settings_obj.settings or {})
    apply_settings_overrides(settings, overrides)
    if str(input_path).lower().endswith('.csv') and \
            setting_to_bool((settings.get('vendor_csv_path_detect') or {}).get('value')):
        # -i points at the vendor csv inside the package folder
        settings.setdefault('vendor_csv_path', {'category': 'lineedit'})['value'] = \
            str(input_path).replace('\\', '/')
    return settings


def run_headless(args):
    """
    Run the --actions on the package without Qt.
    :param args: dict from vars(get_args()), already checked by check_cli_args
    :return: exit code
    """
    input_path = args['i']
    settings_obj = Settings(args['p'], args)
    settings = headless_settings(settings_obj, input_path, args.get('settings', ''))
    settings_obj.settings = settings
    log.debug(f"Headless run: {len(settings)} settings, preset '{settings_obj.current_settings_name}'")
    try:
        # imported here: --help and argument errors don't need ftrack, ayon...
        from sequencer import Sequencer
        # the --actions string runs inside Sequencer
        Sequencer(input_path, sequence_mode='holes_allowed', gui=settings,
                  more_settings=settings_obj, ui=None, headless=True)
    except Exception:
        log.exception("Headless run failed")
        return 1
    _c = sh_logging.LOG_BUFFER.counts
    log.info(f"Headless run finished: {_c.get('error', 0)} error(s), "
             f"{_c.get('warning', 0)} warning(s).")
    return 0


def wants_headless(argv):
    """True when the command line asks for the headless mode (-i or -p given)"""
    return any(a in ('-i', '-p', '--input', '--preset') or
               a.startswith(('-i', '-p', '--input=', '--preset='))
               for a in argv if not a.startswith('--log'))


def setup(args):
    """console / file logging and the exception hook, as the gui does"""
    # the windowed exe has no console: stdout / stderr are None there
    if sys.stdout is None:
        sys.stdout = open(os.devnull, 'w')
    if sys.stderr is None:
        sys.stderr = open(os.devnull, 'w')
    try:
        sh_logging.setup_logging(console_level_from_args(args), args.get('log_file'))
    except OSError as e:
        sh_logging.setup_logging(console_level_from_args(args))
        log.error(f"Can't open log file '{args.get('log_file')}': {e}")
    sh_logging.install_excepthook()


def main(argv=None):
    """command line entry: headless run, or an error when -i / -p are missing"""
    argv = sys.argv[1:] if argv is None else argv
    if sys.stdout is None:
        # argparse may print (--help, errors) before setup()
        sys.stdout = open(os.devnull, 'w')
    if sys.stderr is None:
        sys.stderr = open(os.devnull, 'w')
    args = vars(get_args(argv))
    setup(args)
    log.debug(f"Command line: {sys.argv}")
    headless, exit_code = check_cli_args(args)
    if exit_code is not None:
        return exit_code
    if not headless:
        log.error("Command line mode needs -i and -p (run submission_helper.py for the gui).")
        return 2
    return run_headless(args)


if __name__ == "__main__":
    sys.exit(main())
