"""
Default settings read straight from submission.ui, without Qt.

The gui builds its settings from the widgets (MainWindow.settings_from_gui).
The command line mode must run without Qt, so it reads the same defaults from
the Qt Designer file: same keys, same categories, same value types.

Widgets added in code (Parsing rows 33-48, some Ayon controls) are not in the
.ui file; they all default to empty / unchecked and the Sequencer reads them
with defaults.
"""
import logging
import os
import sys
import xml.etree.ElementTree as ET

log = logging.getLogger("ui_defaults")

UI_FILE_NAME = "submission.ui"

# settings_from_gui skips these widgets
NOT_SETTINGS = ('log',)


def ui_file_path():
    """submission.ui next to the scripts, or next to / inside the frozen exe"""
    candidates = []
    if getattr(sys, 'frozen', False):
        candidates.append(os.path.dirname(sys.executable))
        meipass = getattr(sys, '_MEIPASS', None)
        if meipass:
            candidates.append(meipass)
    candidates.append(os.path.dirname(os.path.abspath(__file__)))
    for folder in candidates:
        path = os.path.join(folder, UI_FILE_NAME)
        if os.path.isfile(path):
            return path
    return None


def _prop(widget, name):
    """<property name=...> child element's value element, or None"""
    for p in widget.findall('property'):
        if p.get('name') == name and len(p):
            return p[0]
    return None


def _text(widget, name, default=''):
    el = _prop(widget, name)
    if el is None:
        return default
    if el.tag == 'string':
        return el.text or ''
    return el.text if el.text is not None else default


def _bool(widget, name, default=False):
    el = _prop(widget, name)
    if el is None:
        return default
    return (el.text or '').strip().lower() == 'true'


def _int(widget, name, default=0):
    el = _prop(widget, name)
    try:
        return int(el.text) if el is not None else default
    except (TypeError, ValueError):
        return default


def _setting(widget):
    cls = widget.get('class')
    if cls == 'QLineEdit':
        return {'category': 'lineedit', 'value': _text(widget, 'text')}
    if cls == 'QPlainTextEdit':
        return {'category': 'plaintextedit', 'value': _text(widget, 'plainText')}
    if cls == 'QCheckBox':
        return {'category': 'checkbox', 'value': _bool(widget, 'checked')}
    if cls == 'QRadioButton':
        return {'category': 'radiobutton', 'value': _bool(widget, 'checked')}
    if cls == 'QSpinBox':
        minimum = _int(widget, 'minimum', 0)
        maximum = _int(widget, 'maximum', 99)
        value = _int(widget, 'value', minimum)
        return {'category': 'spinbox', 'value': max(minimum, min(maximum, value))}
    if cls == 'QSlider':
        minimum = _int(widget, 'minimum', 0)
        return {'category': 'slider', 'value': str(_int(widget, 'value', minimum))}
    if cls == 'QComboBox':
        items = []
        for item in widget.findall('item'):
            el = _prop(item, 'text')
            items.append((el.text or '') if el is not None else '')
        index = _int(widget, 'currentIndex', 0)
        value = items[index] if 0 <= index < len(items) else ''
        return {'category': 'combobox', 'value': value, 'all_items': items}
    return None


def load_defaults(path=None):
    """
    :param path: the .ui file, default: submission.ui next to the app
    :return: settings dict like MainWindow.settings_from_gui gives
             ({} when the file can't be read, logged)
    """
    path = path or ui_file_path()
    if not path:
        log.warning(f"{UI_FILE_NAME} not found: command line mode starts from the preset only")
        return {}
    try:
        tree = ET.parse(path)
    except (OSError, ET.ParseError) as e:
        log.error(f"Reading default settings from {path} failed: {e}")
        return {}
    settings = {}
    for widget in tree.iter('widget'):
        name = widget.get('name')
        if not name or name in NOT_SETTINGS:
            continue
        one = _setting(widget)
        if one is not None:
            settings[name] = one
    return settings
