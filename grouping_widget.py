"""
Grouping tab of the gui (the logic is in grouping.py).

Built in code, like the other code-built controls, so ui_Submission.py can
still be regenerated from submission.ui. The top controls are ordinary
settings widgets (MainWindow puts them on self.ui, so presets save them like
any other widget); the group definitions are saved as one setting,
'group_definitions', a list of dicts.
"""
from functools import partial

from PySide2 import QtCore, QtWidgets

import grouping

LABEL_WIDTH = 170

TIPS = {
    'group_on':
        "Group the files that are sent together, e.g. the exr sequence, the mp4 review and the "
        "thumbnail of one version. Replaces Merge By (Preferences tab).",
    'group_by':
        "Token template of the group key: files with the same key are one group, e.g. "
        "{shot}{task}{version} or {folder_name}{task_name}{variant}{version}. "
        "Files where a token is unknown are not in a group.",
    'group_repre':
        "Representation name of each file, compared (not case sensitive) with the Repres fields "
        "below. Default {extension}; e.g. {list_Matched Representation} for the Ayon "
        "representation matched on the Ayon tab.",
    'group_task_type':
        "Task type of each file, compared with Task Type(s) of the group definitions.",
    'group_task_name':
        "Task name of each file, compared with Task Name(s) of the group definitions.",
    'group_no_export_missing':
        "Leave the files of groups with a missing required representation out of the "
        "Submission export (Excel, CSV and the Ayon publish CSV). They stay in the Submission "
        "table, in red. The Drive Log is exported in full.",
    'group_together':
        "List the rows of a group one below the other, at the place of the group's first row.",
    'group_colors':
        "Give the rows of each group the same muted background in the Submission and Drive Log "
        "tables. Errors and warnings keep their colors.",
    'group_colors_excel':
        "Color the rows in the Excel exports too: groups in light colors, errors red, warnings "
        "orange. Off: no colors in Excel.",
    'group_collapse_sub':
        "Show each group as one Submission row: in every column equal values are shown once, "
        "different values are joined by Separator.",
    'group_collapse_log':
        "Show each group as one Drive Log row, like Collapse Submission.",
    'group_collapse_sep':
        "Text between the different values of a collapsed column, e.g. \", \" or \" / \".",
}

DEF_TIPS = {
    'name': "Name of the group definition, available as {group_name}.",
    'task_types':
        "The definition is used for a group with a file of one of these task types "
        "(Task Type field above), separated by commas or spaces. Wildcards * ? allowed, "
        "not case sensitive. Empty: any task type.",
    'task_names':
        "The definition is used for a group with a file of one of these task names "
        "(Task Name field above). Wildcards * ? allowed. Empty: any task name.",
    'always_repres':
        "Required representations that must be in the package, e.g. exr. A missing one is an "
        "error on every row of the group.",
    'always_or_convert_repres':
        "Required representations that are in the package or are made by a Convert row from a "
        "file of the group (the extension of its File Name), e.g. mp4. {group_to_convert} lists "
        "the ones that will be converted.",
    'optional_repres':
        "Representations that may be in the group. With any Repres field filled in, a file with "
        "another representation gets a warning.",
    'inheritance_repre_priority':
        "Order in which files give their values to Inherit Columns, e.g. exr mp4. Files with "
        "other representations come after, in table order.",
    'review_repre':
        "File of the group whose tokens every file of the group gets as {group_review_<token>}, "
        "e.g. mp4 mov: {group_review_full_path} is the review movie. The first one found counts.",
    'thumb_source_repre':
        "File of the group whose tokens every file gets as {group_thumb_<token>}, e.g. exr: "
        "{group_thumb_convert_path01} is the thumbnail Convert row 01 made from the exr.",
    'inherit_columns':
        "Submission column titles, separated by commas. A cell that is empty or has an unknown "
        "{token} takes the value of the same column from another file of the group "
        "(Inheritance Repre Priority order).",
}


class GroupDefinitionWidget(QtWidgets.QFrame):
    """one group definition: header with Enable, name, move and remove buttons, then the fields"""
    changed = QtCore.Signal(bool)          # True: typed text (refresh later)
    move_up = QtCore.Signal(object)
    move_down = QtCore.Signal(object)
    remove = QtCore.Signal(object)

    FIELDS = (
        # (key, label, row, column, span)
        ('name', "Group Name:", 0, 0, 2),
        ('task_types', "Task Type(s):", 1, 0, 1),
        ('task_names', "Task Name(s):", 1, 1, 1),
        ('always_repres', "Always Repres:", 2, 0, 1),
        ('always_or_convert_repres', "Always/Convert Repres:", 2, 1, 1),
        ('optional_repres', "Optional Repres:", 3, 0, 1),
        ('inheritance_repre_priority', "Inheritance Repre Priority:", 3, 1, 1),
        ('review_repre', "Review Repre:", 4, 0, 1),
        ('thumb_source_repre', "Thumbnail Source Repre:", 4, 1, 1),
        ('inherit_columns', "Inherit Columns:", 5, 0, 2),
    )

    def __init__(self, data=None, parent=None):
        super().__init__(parent)
        self.setObjectName("GroupDefinition")
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setStyleSheet(
            "QFrame#GroupDefinition { border: 1px solid #3a3a3a; border-radius: 3px; }"
            "QFrame#GroupDefHeader { background: #3a3a3a; }")
        main = QtWidgets.QVBoxLayout(self)
        main.setContentsMargins(0, 0, 0, 0)
        main.setSpacing(0)

        header = QtWidgets.QFrame(self)
        header.setObjectName("GroupDefHeader")
        hl = QtWidgets.QHBoxLayout(header)
        hl.setContentsMargins(6, 3, 6, 3)
        self.toggle = self._small_button("▼", "Show / hide the fields")
        self.toggle.clicked.connect(self.toggle_collapsed)
        self.enabled = QtWidgets.QCheckBox("Enable", header)
        self.enabled.setChecked(True)
        self.enabled.setToolTip("Off: the definition is skipped.")
        self.title = QtWidgets.QLabel(header)
        self.title.setStyleSheet("font-weight: bold;")
        self.up = self._small_button("▲", "Move up: definitions are tried from the top, "
                                               "the first one that matches a group is used")
        self.down = self._small_button("▼", "Move down")
        self.delete = self._small_button("✕", "Remove this group definition")
        self.up.clicked.connect(lambda *_a: self.move_up.emit(self))
        self.down.clicked.connect(lambda *_a: self.move_down.emit(self))
        self.delete.clicked.connect(lambda *_a: self.remove.emit(self))
        for w in (self.toggle, self.enabled, self.title):
            hl.addWidget(w)
        hl.addStretch(1)
        for w in (self.up, self.down, self.delete):
            hl.addWidget(w)
        main.addWidget(header)

        self.body = QtWidgets.QWidget(self)
        grid = QtWidgets.QGridLayout(self.body)
        grid.setContentsMargins(12, 6, 12, 8)
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(4)
        self.edits = {}
        for key, label, row, col, span in self.FIELDS:
            lbl = QtWidgets.QLabel(label, self.body)
            lbl.setMinimumWidth(LABEL_WIDTH)
            edit = QtWidgets.QLineEdit(self.body)
            edit.setMinimumHeight(25)
            edit.setToolTip(DEF_TIPS[key])
            lbl.setToolTip(DEF_TIPS[key])
            grid.addWidget(lbl, row, col * 2)
            grid.addWidget(edit, row, col * 2 + 1, 1, span * 2 - 1)
            edit.textChanged.connect(lambda *_a: self.changed.emit(True))
            self.edits[key] = edit
        grid.setColumnStretch(1, 1)
        grid.setColumnStretch(3, 1)
        main.addWidget(self.body)

        self.edits['name'].textChanged.connect(self._update_title)
        self.enabled.toggled.connect(lambda *_a: self.changed.emit(False))
        self.set_data(data or grouping.new_definition())

    def _small_button(self, text, tip):
        b = QtWidgets.QPushButton(text, self)
        b.setFixedSize(22, 22)
        b.setToolTip(tip)
        b.setStyleSheet("QPushButton { min-height: 0px; padding: 0px; font-size: 10px; }")
        return b

    def _update_title(self, text=None):
        text = self.edits['name'].text() if text is None else text
        self.title.setText(text.strip() or "Untitled Group")

    def toggle_collapsed(self, _checked=False):
        visible = not self.body.isVisible()
        self.body.setVisible(visible)
        self.toggle.setText("▼" if visible else "▶")

    def set_data(self, data):
        d = grouping.clean_definitions([data])[0] if data else grouping.new_definition()
        self.blockSignals(True)
        self.enabled.setChecked(bool(d['enabled']))
        for key, edit in self.edits.items():
            edit.setText(str(d.get(key, '')))
        self.blockSignals(False)
        self._update_title()

    def data(self):
        d = {key: edit.text().strip() for key, edit in self.edits.items()}
        d['enabled'] = self.enabled.isChecked()
        return {k: d[k] for k in grouping.DEFINITION_FIELDS}


class GroupingTab(QtWidgets.QWidget):
    """
    The Grouping tab. Signals: changed_now (a checkbox, a definition added,
    moved...), changed_later (typed text). MainWindow refreshes on both.
    """
    changed_now = QtCore.Signal(str)
    changed_later = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("tab_grouping")
        self.settings_widgets = {}
        self.definition_widgets = []

        outer = QtWidgets.QVBoxLayout(self)
        outer.setContentsMargins(6, 6, 6, 6)
        outer.setSpacing(4)

        d = grouping.DEFAULTS
        # row 1: enable + group by
        r1 = QtWidgets.QHBoxLayout()
        r1.addWidget(self._check('group_on', "Enable Grouping", d['group_on']))
        r1.addSpacing(12)
        r1.addWidget(self._label("Group by:", 'group_by'))
        r1.addWidget(self._edit('group_by', d['group_by']), 1)
        outer.addLayout(r1)

        # row 2: where representation / task come from
        r2 = QtWidgets.QHBoxLayout()
        for key, label in (('group_repre', "Representation:"), ('group_task_type', "Task Type:"),
                           ('group_task_name', "Task Name:")):
            r2.addWidget(self._label(label, key))
            r2.addWidget(self._edit(key, d[key]), 1)
            r2.addSpacing(8)
        outer.addLayout(r2)

        # row 3: export / view options
        r3 = QtWidgets.QHBoxLayout()
        r3.addWidget(self._check('group_no_export_missing',
                                 "Do not export items in group with missing Representations",
                                 d['group_no_export_missing']))
        r3.addSpacing(12)
        r3.addWidget(self._check('group_together', "Keep Group Rows Together", d['group_together']))
        r3.addSpacing(12)
        r3.addWidget(self._check('group_colors', "Color Group Rows", d['group_colors']))
        r3.addWidget(self._check('group_colors_excel', "Color Rows in Excel", d['group_colors_excel']))
        r3.addStretch(1)
        outer.addLayout(r3)

        # row 4: collapse
        r4 = QtWidgets.QHBoxLayout()
        r4.addWidget(QtWidgets.QLabel("Collapse Groups:", self))
        r4.addWidget(self._check('group_collapse_sub', "Submission", d['group_collapse_sub']))
        r4.addWidget(self._check('group_collapse_log', "Drive Log", d['group_collapse_log']))
        r4.addSpacing(12)
        r4.addWidget(self._label("Separator:", 'group_collapse_sep', width=None))
        sep = self._edit('group_collapse_sep', d['group_collapse_sep'])
        sep.setMaximumWidth(80)
        r4.addWidget(sep)
        r4.addStretch(1)
        add = QtWidgets.QPushButton("Add Group Definition", self)
        add.setObjectName("group_add_butt")
        add.setMinimumSize(QtCore.QSize(170, 25))
        add.setToolTip("Add a group definition at the end. Definitions are tried from the top: "
                       "the first enabled one whose Task Type(s) and Task Name(s) match is used.")
        add.clicked.connect(self._add_clicked)
        self.add_button = add
        r4.addWidget(add)
        outer.addLayout(r4)

        # group definitions
        scroll = QtWidgets.QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QtWidgets.QFrame.NoFrame)
        holder = QtWidgets.QWidget(scroll)
        self.list_layout = QtWidgets.QVBoxLayout(holder)
        self.list_layout.setContentsMargins(0, 4, 0, 0)
        self.list_layout.setSpacing(6)
        self.list_layout.addStretch(1)
        scroll.setWidget(holder)
        self.scroll = scroll
        outer.addWidget(scroll, 1)

    # ---------------------------------------------------------------- helpers
    @staticmethod
    def _emit(signal, key, *_args):
        # Qt slots: PySide2 may call with or without the signal's arguments
        signal.emit(key)

    def _label(self, text, key, width=110):
        lbl = QtWidgets.QLabel(text, self)
        if width:
            lbl.setMinimumWidth(width)
        lbl.setToolTip(TIPS[key])
        return lbl

    def _edit(self, key, value):
        e = QtWidgets.QLineEdit(self)
        e.setObjectName(key)
        e.setText(value)
        e.setMinimumHeight(25)
        e.setToolTip(TIPS[key])
        e.textChanged.connect(partial(self._emit, self.changed_later, key))
        self.settings_widgets[key] = e
        return e

    def _check(self, key, text, value):
        c = QtWidgets.QCheckBox(text, self)
        c.setObjectName(key)
        c.setChecked(bool(value))
        c.setMinimumHeight(25)
        c.setToolTip(TIPS[key])
        c.clicked.connect(partial(self._emit, self.changed_now, key))
        self.settings_widgets[key] = c
        return c

    # ------------------------------------------------------------ definitions
    def _add_clicked(self, _checked=False):
        n = len(self.definition_widgets) + 1
        self.add_definition(grouping.new_definition(f"Group {n}"))
        self.changed_now.emit('group_definitions')

    def add_definition(self, data=None):
        w = GroupDefinitionWidget(data, self)
        w.changed.connect(self._definition_changed)
        w.move_up.connect(partial(self._move, step=-1))
        w.move_down.connect(partial(self._move, step=1))
        w.remove.connect(self._remove)
        self.definition_widgets.append(w)
        self.list_layout.insertWidget(self.list_layout.count() - 1, w)
        return w

    def _definition_changed(self, typed=False):
        if typed:
            self.changed_later.emit('group_definitions')
        else:
            self.changed_now.emit('group_definitions')

    def _move(self, widget, step):
        i = self.definition_widgets.index(widget)
        j = i + step
        if not 0 <= j < len(self.definition_widgets):
            return
        lst = self.definition_widgets
        lst[i], lst[j] = lst[j], lst[i]
        self._relayout()
        self.changed_now.emit('group_definitions')

    def _remove(self, widget):
        name = widget.data().get('name') or "this group definition"
        answer = QtWidgets.QMessageBox.question(
            self, "Remove Group Definition", f"Remove {name}?")
        if answer != QtWidgets.QMessageBox.Yes:
            return
        self.definition_widgets.remove(widget)
        self.list_layout.removeWidget(widget)
        widget.deleteLater()
        self.changed_now.emit('group_definitions')

    def _relayout(self):
        for w in self.definition_widgets:
            self.list_layout.removeWidget(w)
        for i, w in enumerate(self.definition_widgets):
            self.list_layout.insertWidget(i, w)

    def definitions(self):
        return [w.data() for w in self.definition_widgets]

    def set_definitions(self, value):
        """replace all definitions (preset load); no change signals"""
        for w in self.definition_widgets:
            self.list_layout.removeWidget(w)
            w.deleteLater()
        self.definition_widgets = []
        for d in grouping.clean_definitions(value):
            self.add_definition(d)
