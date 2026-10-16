"""
Tooltips live in tooltips.py, keyed by widget objectName. These tests read
submission.ui directly (no Qt needed) and check that every control has a
tooltip, that no tooltip points at a widget that doesn't exist, and that no
tooltips are set in Qt Designer (they used to get copy-pasted between controls).
"""
import os
import xml.etree.ElementTree as ET

import tests._stubs  # noqa: F401  (repo on sys.path)
import tooltips

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UI_FILE = os.path.join(REPO, "submission.ui")

INTERACTIVE = {"QLineEdit", "QPlainTextEdit", "QCheckBox", "QRadioButton",
               "QSpinBox", "QComboBox", "QPushButton", "QTableWidget",
               "QTreeWidget", "QProgressBar"}
# text areas that need no tooltip (Log tab text, Help tab), and widgets that
# get their tooltip in code (submission_helper._add_ayon_controls)
NO_TOOLTIP = {"log", "textEdit", "ayon_output_folder"}
# parse rows beyond the .ui are added in code (submission_helper._add_parse_rows)
PARSE_ROWS = 48


def _ui_widgets():
    root = ET.parse(UI_FILE).getroot()
    return {w.get("name"): w.get("class") for w in root.iter("widget")}


def test_every_control_has_a_tooltip():
    missing = [name for name, cls in _ui_widgets().items()
               if cls in INTERACTIVE and name not in NO_TOOLTIP
               and tooltips.tooltip_for(name) is None]
    assert missing == []


def test_code_built_parse_rows_have_tooltips():
    for row in range(1, PARSE_ROWS + 1):
        for field in ("name", "pattern", "repl", "source", "filter"):
            assert tooltips.tooltip_for(f"parse_{field}_{row:02d}"), (field, row)


def test_tooltip_keys_are_real_widgets():
    widgets = _ui_widgets()
    unknown = [key for key in tooltips.TOOLTIPS if key not in widgets]
    assert unknown == []


def test_no_tooltips_in_designer_file():
    root = ET.parse(UI_FILE).getroot()
    with_tooltip = [w.get("name") for w in root.iter("widget")
                    if any(p.get("name") == "toolTip" for p in w.findall("property"))]
    assert with_tooltip == [], "move these tooltips to tooltips.py"


def test_tooltips_are_plain_text():
    texts = list(tooltips.TOOLTIPS.values()) + [t for _, t in tooltips.ROW_TOOLTIPS]
    for text in texts:
        assert "<html" not in text and "<p>" not in text and "<br" not in text
        assert text.strip() == text


def test_rich_text_escapes_angle_brackets():
    rich = tooltips.to_rich_text("{vendor_<Column>}\nnext")
    assert rich == "<qt>{vendor_&lt;Column&gt;}<br>next</qt>"


def test_apply_tooltips_sets_only_known_widgets():
    class Widget:
        tip = None

        def setToolTip(self, text):
            self.tip = text

    class Ui:
        pass

    ui = Ui()
    ui.package_folder = Widget()
    ui.parse_name_40 = Widget()
    ui.some_layout = object()          # no setToolTip: skipped
    ui.label_12 = Widget()             # no tooltip defined: untouched
    assert tooltips.apply_tooltips(ui) == 2
    assert ui.package_folder.tip.startswith("<qt>")
    assert ui.parse_name_40.tip.startswith("<qt>")
    assert ui.label_12.tip is None
