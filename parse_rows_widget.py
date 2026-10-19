"""
Parsing tab as a table (the row logic is in parse_rows.py).

One table row per parsing row, titles on top: Name, Pattern, Repl, Source,
Filter. Only the rows in use are shown. Rows can be added, inserted,
duplicated, deleted, moved up / down, copied and pasted (tab separated text,
also to / from Excel).

Presets and the Sequencer still use the parse_<field>_01..48 line edits of
the .ui file (and _add_parse_rows): they are hidden and are the storage of
this table. A table edit writes all rows back to them, compacted from row 01;
their change (preset load) fills the table again.
"""
from PySide2 import QtCore, QtGui, QtWidgets

import parse_rows
from tooltips import tooltip_for, to_rich_text

INVALID_COLOR = "maroon"
SKIPPED_COLOR = "sienna"

HELP = ("Rows run top to bottom. Double click a cell to edit. "
        "Del deletes the selected rows, Ins inserts a row above, Ctrl+D duplicates, "
        "Ctrl+Up / Ctrl+Down moves, Ctrl+C copies the rows, Ctrl+V pastes them below "
        "(tab separated text, also from Excel; a single value goes to the selected cells).")


class ParseRowsTable(QtWidgets.QWidget):

    def __init__(self, ui, max_rows, parent=None, log=None):
        """
        :param ui: Ui_submission with parse_<field>_01 .. parse_<field>_<max_rows>
        """
        super().__init__(parent)
        self.ui = ui
        self.max_rows = max_rows
        self.log = log
        self._syncing = False

        layout = QtWidgets.QVBoxLayout(self)
        bar = QtWidgets.QHBoxLayout()
        layout.addLayout(bar)

        def button(text, tip, slot):
            b = QtWidgets.QPushButton(text, self)
            b.setToolTip(tip)
            b.setMinimumHeight(26)
            b.clicked.connect(slot)
            bar.addWidget(b)
            return b

        self.add_butt = button("Add", "Add an empty row at the end.", self.add_row)
        self.insert_butt = button("Insert", "Insert an empty row above the selected row (Ins).",
                                  self.insert_row)
        self.dup_butt = button("Duplicate", "Duplicate the selected rows below them (Ctrl+D).",
                               self.duplicate_rows)
        self.delete_butt = button("Delete", "Delete the selected rows (Del).", self.delete_rows)
        bar.addSpacing(12)
        self.up_butt = button("Move Up", "Move the selected rows up (Ctrl+Up).",
                              lambda: self.move_rows(-1))
        self.down_butt = button("Move Down", "Move the selected rows down (Ctrl+Down).",
                                lambda: self.move_rows(1))
        bar.addSpacing(12)
        self.copy_butt = button("Copy", "Copy the selected rows as tab separated text (Ctrl+C).",
                                self.copy_rows)
        self.paste_butt = button("Paste", "Paste rows (tab separated text) below the selected "
                                 "row, or at the end (Ctrl+V).", self.paste)
        bar.addSpacing(12)
        # not a setting (not on ui): presets don't change by looking at a preview
        self.preview_chbx = QtWidgets.QCheckBox("Preview", self)
        self.preview_chbx.setToolTip(
            "Show a Preview column: what each row gives for the first selected row of the "
            "Submission table (load a package, select a row there). Empty: the row didn't run "
            "for that file (Filter, or Name / Pattern / Source empty).")
        self.preview_chbx.toggled.connect(self.update_preview)
        bar.addWidget(self.preview_chbx)
        bar.addStretch(1)
        self.count_label = QtWidgets.QLabel("", self)
        bar.addWidget(self.count_label)

        # the field columns, then the read only Preview column
        self.preview_col = len(parse_rows.FIELDS)
        self.table = QtWidgets.QTableWidget(0, len(parse_rows.FIELDS) + 1, self)
        self.table.setHorizontalHeaderLabels(list(parse_rows.TITLES) + ["Preview"])
        for c, field in enumerate(parse_rows.FIELDS):
            tip = tooltip_for(f"parse_{field}_01")
            header = self.table.horizontalHeaderItem(c)
            if tip and header is not None:
                header.setToolTip(to_rich_text(tip))
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked |
                                   QtWidgets.QAbstractItemView.EditKeyPressed |
                                   QtWidgets.QAbstractItemView.AnyKeyPressed)
        self.table.verticalHeader().setDefaultSectionSize(24)
        self.table.verticalHeader().setToolTip("Row order: rows run top to bottom. "
                                               "Click to select whole rows.")
        hh = self.table.horizontalHeader()
        hh.setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        hh.setStretchLastSection(True)
        for c, width in enumerate((140, 360, 140, 220, 120, 200)):
            self.table.setColumnWidth(c, width)
        self.table.setColumnHidden(self.preview_col, True)
        # table row -> parse row number (1..) the Sequencer knows it by
        self._slots = []
        # callable -> (label, {'01': value, ...}) or None, set by MainWindow
        self.preview_source = None
        self.table.setToolTip(HELP)
        self.table.installEventFilter(self)
        self.table.itemChanged.connect(self._table_edited)
        self.table.itemSelectionChanged.connect(self._update_buttons)
        layout.addWidget(self.table, 1)

        # the hidden line edits: a preset load (settings_to_gui) fills them
        self._reload_timer = QtCore.QTimer(self)
        self._reload_timer.setSingleShot(True)
        self._reload_timer.setInterval(0)
        self._reload_timer.timeout.connect(self.load_from_fields)
        for edit in self._all_fields():
            edit.textChanged.connect(self._field_changed)

        self.load_from_fields()

    # storage: the parse_* line edits -------------------------------------------

    def _field(self, row, field):
        return getattr(self.ui, f"parse_{field}_{row:02d}", None)

    def _all_fields(self):
        for row in range(1, self.max_rows + 1):
            for field in parse_rows.FIELDS:
                edit = self._field(row, field)
                if edit is not None:
                    yield edit

    def _field_rows(self):
        rows = []
        for row in range(1, self.max_rows + 1):
            rows.append(tuple((self._field(row, f).text() if self._field(row, f) is not None else '')
                              for f in parse_rows.FIELDS))
        return rows

    def _field_changed(self, *args):
        if not self._syncing:
            self._reload_timer.start()

    def set_from_settings(self, settings, defaults=None):
        """
        A preset was applied (MainWindow.settings_to_gui fills the fields with
        signals blocked, so the table doesn't see it): the fields get the
        preset's values as saved - missing fields their .ui default - and the
        table shows the rows in use. Nothing is compacted or written back
        until the table is edited, so the preset stays as it is.
        """
        values = parse_rows.slot_values(settings, defaults, self.max_rows)
        self._syncing = True
        try:
            for row, row_values in enumerate(values, start=1):
                for field, value in zip(parse_rows.FIELDS, row_values):
                    edit = self._field(row, field)
                    if edit is not None and edit.text() != value:
                        edit.blockSignals(True)
                        edit.setText(value)
                        edit.blockSignals(False)
        finally:
            self._syncing = False
        self._reload_timer.stop()
        self.load_from_fields()

    def load_from_fields(self):
        """the table from the line edits: the rows in use, in order"""
        field_rows = self._field_rows()
        slots = [i for i, row in enumerate(field_rows, start=1) if not parse_rows.is_empty(row)]
        self._slots = slots
        self._set_rows([field_rows[i - 1] for i in slots])

    def write_to_fields(self):
        """
        all table rows to the line edits, from row 01 on; their textChanged
        refreshes the parsing as before
        """
        slots = parse_rows.to_slots(self.rows(), self.max_rows)
        self._slots = list(range(1, min(self.table.rowCount(), self.max_rows) + 1))
        self._syncing = True
        try:
            for row, values in enumerate(slots, start=1):
                for field, value in zip(parse_rows.FIELDS, values):
                    edit = self._field(row, field)
                    if edit is not None and edit.text() != value:
                        edit.setText(value)
        finally:
            self._syncing = False

    # table ---------------------------------------------------------------------

    def rows(self):
        out = []
        for r in range(self.table.rowCount()):
            values = []
            for c in range(len(parse_rows.FIELDS)):
                item = self.table.item(r, c)
                values.append(item.text() if item is not None else '')
            out.append(tuple(values))
        return out

    def _set_rows(self, rows, select=None):
        table = self.table
        table.blockSignals(True)
        try:
            table.setRowCount(len(rows))
            for r, row in enumerate(rows):
                for c, value in enumerate(parse_rows.clean(row)):
                    table.setItem(r, c, QtWidgets.QTableWidgetItem(value))
                self._mark_row(r)
        finally:
            table.blockSignals(False)
        if select:
            self._select_rows(select)
        self._update_buttons()
        self.update_preview()

    # preview -------------------------------------------------------------------

    def update_preview(self, *args):
        """
        Preview column: the value each row gives for the item of preview_source
        (the first selected Submission row); empty when the row didn't run
        """
        on = self.preview_chbx.isChecked()
        self.table.setColumnHidden(self.preview_col, not on)
        if not on:
            return
        result = None
        if self.preview_source is not None:
            try:
                result = self.preview_source()
            except Exception as e:
                if self.log is not None:
                    self.log.debug(f"Parsing preview: {e}")
        label, values = result if result else ("select a Submission row", None)
        header = self.table.horizontalHeaderItem(self.preview_col)
        if header is not None:
            header.setText(f"Preview: {label}")
        values = values or {}
        self.table.blockSignals(True)
        try:
            for r in range(self.table.rowCount()):
                slot = self._slots[r] if r < len(self._slots) else None
                text = values.get(f"{slot:02d}") if slot else None
                item = QtWidgets.QTableWidgetItem('' if text is None else str(text))
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                font = item.font()
                font.setItalic(True)
                item.setFont(font)
                self.table.setItem(r, self.preview_col, item)
        finally:
            self.table.blockSignals(False)

    def _mark_row(self, r):
        """colors: invalid pattern red, skipped row (Name / Pattern / Source empty) brown"""
        row = tuple((self.table.item(r, c).text() if self.table.item(r, c) else '')
                    for c in range(len(parse_rows.FIELDS)))
        problem = parse_rows.row_problem(row)
        bad_pattern = bool(parse_rows.pattern_error(row[1]))
        for c in range(len(parse_rows.FIELDS)):
            item = self.table.item(r, c)
            if item is None:
                continue
            if bad_pattern and c == 1:
                item.setBackground(QtGui.QColor(INVALID_COLOR))
            elif problem and not bad_pattern:
                item.setBackground(QtGui.QColor(SKIPPED_COLOR))
            else:
                item.setBackground(QtGui.QBrush())
            item.setToolTip(problem)

    def _table_edited(self, item):
        if item.column() >= self.preview_col:
            return
        self.table.blockSignals(True)
        try:
            self._mark_row(item.row())
        finally:
            self.table.blockSignals(False)
        self.write_to_fields()

    def _apply(self, rows, select=None):
        """new rows: table and line edits"""
        self._set_rows(rows, select)
        self.write_to_fields()

    def _selected_rows(self):
        rows = {i.row() for i in self.table.selectedIndexes()}
        if not rows and self.table.currentRow() >= 0:
            rows = {self.table.currentRow()}
        return sorted(rows)

    def _select_rows(self, indexes):
        table = self.table
        table.clearSelection()
        model = table.model()
        selection = QtCore.QItemSelection()
        for r in indexes:
            if 0 <= r < table.rowCount():
                selection.select(model.index(r, 0), model.index(r, table.columnCount() - 1))
        table.selectionModel().select(selection, QtCore.QItemSelectionModel.Select)
        if indexes:
            table.setCurrentCell(indexes[0], max(0, table.currentColumn()),
                                 QtCore.QItemSelectionModel.NoUpdate)

    def _update_buttons(self):
        n = self.table.rowCount()
        has_sel = bool(self._selected_rows())
        full = n >= self.max_rows
        self.add_butt.setEnabled(not full)
        self.insert_butt.setEnabled(not full)
        self.paste_butt.setEnabled(not full)
        self.dup_butt.setEnabled(has_sel and not full)
        for b in (self.delete_butt, self.up_butt, self.down_butt, self.copy_butt):
            b.setEnabled(has_sel)
        self.count_label.setText(f"{n} / {self.max_rows} rows")

    def _warn_dropped(self, dropped):
        if dropped and self.log is not None:
            self.log.warning(f"Parsing: {dropped} row(s) not added, the limit is {self.max_rows} rows")

    # operations ----------------------------------------------------------------

    def add_row(self):
        rows, idx, dropped = parse_rows.insert(self.rows(), self.table.rowCount(),
                                               [parse_rows.EMPTY], self.max_rows)
        self._warn_dropped(dropped)
        self._apply(rows, idx)
        if idx:
            self.table.setCurrentCell(idx[0], 0)

    def insert_row(self):
        sel = self._selected_rows()
        at = sel[0] if sel else 0
        rows, idx, dropped = parse_rows.insert(self.rows(), at, [parse_rows.EMPTY], self.max_rows)
        self._warn_dropped(dropped)
        self._apply(rows, idx)

    def duplicate_rows(self):
        sel = self._selected_rows()
        if not sel:
            return
        current = self.rows()
        rows, idx, dropped = parse_rows.insert(current, sel[-1] + 1, [current[i] for i in sel],
                                               self.max_rows)
        self._warn_dropped(dropped)
        self._apply(rows, idx)

    def delete_rows(self):
        sel = self._selected_rows()
        if not sel:
            return
        rows = parse_rows.delete(self.rows(), sel)
        nxt = min(sel[0], len(rows) - 1)
        self._apply(rows, [nxt] if nxt >= 0 else None)

    def move_rows(self, delta):
        rows, idx = parse_rows.move(self.rows(), self._selected_rows(), delta)
        self._apply(rows, idx)

    def copy_rows(self):
        sel = self._selected_rows()
        if not sel:
            return
        current = self.rows()
        QtWidgets.QApplication.clipboard().setText(parse_rows.to_tsv([current[i] for i in sel]))

    def paste(self):
        text = QtWidgets.QApplication.clipboard().text()
        if not text:
            return
        if not parse_rows.is_rows_text(text):
            # one value: into the selected cells
            value = text.strip("\r\n")
            items = [i for i in self.table.selectedItems() if i.column() < self.preview_col]
            if not items:
                return
            self.table.blockSignals(True)
            try:
                for item in items:
                    item.setText(value)
                for r in {i.row() for i in items}:
                    self._mark_row(r)
            finally:
                self.table.blockSignals(False)
            self.write_to_fields()
            return
        new_rows = parse_rows.from_tsv(text)
        if not new_rows:
            return
        sel = self._selected_rows()
        at = sel[-1] + 1 if sel else self.table.rowCount()
        rows, idx, dropped = parse_rows.insert(self.rows(), at, new_rows, self.max_rows)
        self._warn_dropped(dropped)
        self._apply(rows, idx)

    # keys ----------------------------------------------------------------------

    def eventFilter(self, obj, event):
        if obj is self.table and event.type() == QtCore.QEvent.KeyPress \
                and QtWidgets.QApplication.focusWidget() is self.table:
            # (a cell being edited has the focus in its editor: keys stay there)
            key = event.key()
            ctrl = bool(event.modifiers() & QtCore.Qt.ControlModifier)
            if event.matches(QtGui.QKeySequence.Copy):
                self.copy_rows()
                return True
            if event.matches(QtGui.QKeySequence.Paste):
                self.paste()
                return True
            if key == QtCore.Qt.Key_Delete and not ctrl:
                self.delete_rows()
                return True
            if key == QtCore.Qt.Key_Insert:
                self.insert_row()
                return True
            if ctrl and key == QtCore.Qt.Key_D:
                self.duplicate_rows()
                return True
            if ctrl and key == QtCore.Qt.Key_Up:
                self.move_rows(-1)
                return True
            if ctrl and key == QtCore.Qt.Key_Down:
                self.move_rows(1)
                return True
        return super().eventFilter(obj, event)
