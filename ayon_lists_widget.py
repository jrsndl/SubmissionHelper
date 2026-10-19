"""
AYON tab > AYON Lists sub-tab (the queries are in ayon_lists.py).

Left: the project's AYON entity lists by list category (list folders are
not used). Right: the versions of the selected list - Folder Path, Task,
Product, Version. Same browser as Ftrack > Get Lists.

Package matching: the versions of every list are compared with the AYON
versions the package files matched (Match version). A list with exactly
those versions is green, one with at least Match % of them in common cyan;
version rows of the package are green. Create List makes a list of the
package's versions when there isn't one yet (asks first).
"""
import logging

from PySide2 import QtCore, QtGui, QtWidgets

import ayon_lists
import ftrack
from ftrack_lists_widget import FtrackListsTab, ID_ROLE

EXACT_COLOR = "darkgreen"
ALMOST_COLOR = "darkcyan"
ROW_COLOR = "darkgreen"


class AyonListsTab(FtrackListsTab):
    COLUMNS = ayon_lists.LIST_COLUMNS
    SYSTEM = "AYON"
    BUTTON_TIP = ("Read the lists of the AYON Project set in the Ayon group. "
                  "Uses the AYON sign-in of the Preferences tab (Accounts).")
    TREE_TIP = ("AYON lists by list category. Select a list to show its versions; "
                "items that aren't versions are not shown.\n"
                "Green: the list has exactly the package's versions. Cyan: at least Match % "
                "in common.")
    TREE_HEADER = "List Category / List"
    GROUPS = "categories"

    def __init__(self, connect, busy=None, parent=None, log=None):
        super().__init__(connect, busy, parent)
        self.log = log
        # settings (MainWindow puts them on ui, saved in presets)
        self.auto_chbx = QtWidgets.QCheckBox("auto-read", self)
        self.auto_chbx.setObjectName("ayon_lists_auto")
        self.auto_chbx.setChecked(True)
        self.auto_chbx.setToolTip(
            "Read the AYON lists right after Submission Helper connects to AYON "
            "(Scan, or a package load / Reload with Enable on). Again only when the "
            "Project changes; Get Lists reads them any time.")
        self.top_bar.insertWidget(1, self.auto_chbx)

        self.match_label = QtWidgets.QLabel("Match:", self)
        self.match_pct = QtWidgets.QSpinBox(self)
        self.match_pct.setObjectName("ayon_lists_match_pct")
        self.match_pct.setRange(1, 99)
        self.match_pct.setValue(75)
        self.match_pct.setSuffix(" %")
        self.match_pct.setToolTip(
            "A list is cyan (almost matching) when at least this share of the versions in "
            "the list or the package are in both. Exactly the package's versions: green.")
        self.match_pct.valueChanged.connect(self.update_matches)
        self.top_bar.insertWidget(2, self.match_label)
        self.top_bar.insertWidget(3, self.match_pct)

        self.create_butt = QtWidgets.QPushButton("Create List from Package", self)
        self.create_butt.setMinimumHeight(30)
        self.create_butt.setToolTip(
            "Create an AYON list with the versions the package files matched (Match "
            "version on the Ayon tab). Enabled when no list has exactly these versions. "
            "Asks for the name and category first.")
        self.create_butt.setEnabled(False)
        self.create_butt.clicked.connect(self.create_list)
        self.top_bar.addWidget(self.create_butt)

        self._auto_project = None
        self._project = None
        # callable -> (package name, [version ids in package order]), set by MainWindow
        self.package_source = None
        # callable -> (ftrack session, project id), for Create List in ftrack
        self.ftrack_connect = None
        self._list_versions = {}
        self._package_ids = set()

    # lists -------------------------------------------------------------------

    def auto_read(self, con, project):
        """after a successful AYON connection: read the lists once per project"""
        if not self.auto_chbx.isChecked() or con is None or not project:
            return
        if project == self._auto_project and self.tree.topLevelItemCount():
            return
        self._auto_project = project
        self.show_lists(con, project)

    def show_lists(self, session, project_id):
        super().show_lists(session, project_id)
        self._list_versions = {}
        lists = [{'id': i.data(0, ID_ROLE), 'name': i.text(0)} for i in self._list_items()]
        if session is not None and project_id and lists:
            self._list_versions = self._busy(
                lambda: ayon_lists.list_version_ids(session, project_id, lists),
                "Reading AYON list versions...") or {}
        self.update_matches()

    def _list_items(self):
        out = []
        for t in range(self.tree.topLevelItemCount()):
            top = self.tree.topLevelItem(t)
            for c in range(top.childCount()):
                out.append(top.child(c))
        return out

    def query_lists(self, con, project):
        return ayon_lists.query_lists(con, project)

    def query_versions(self, con, list_id):
        return ayon_lists.query_list_versions(con, self._project, list_id)

    # package matching -----------------------------------------------------------

    def _package(self):
        result = None
        if self.package_source is not None:
            try:
                result = self.package_source()
            except Exception as e:
                if self.log is not None:
                    self.log.debug(f"AYON Lists: package versions: {e}")
        return result or ('', [])

    def row_background(self, row):
        return ROW_COLOR if row.get('_id') in self._package_ids else None

    def update_matches(self, *args):
        """color the lists and version rows by the package's matched versions"""
        _, ids = self._package()
        self._package_ids = set(ids)
        threshold = self.match_pct.value() / 100.0
        exact, almost = [], []
        for item in self._list_items():
            versions = self._list_versions.get(item.data(0, ID_ROLE))
            kind = ayon_lists.match_kind(versions, self._package_ids, threshold)
            if kind == ayon_lists.EXACT:
                item.setBackground(0, QtGui.QColor(EXACT_COLOR))
                exact.append(item.text(0))
            elif kind == ayon_lists.ALMOST:
                item.setBackground(0, QtGui.QColor(ALMOST_COLOR))
                almost.append(item.text(0))
            else:
                item.setBackground(0, QtGui.QBrush())
            if versions is not None and self._package_ids:
                shared = len(set(versions) & self._package_ids)
                item.setToolTip(0, f"{shared} of the package's {len(self._package_ids)} versions, "
                                   f"{len(versions)} in the list "
                                   f"({ayon_lists.overlap(versions, self._package_ids):.0%} in common)")
            else:
                item.setToolTip(0, "")
        for r in range(self.table.rowCount()):
            first = self.table.item(r, 0)
            color = ROW_COLOR if first is not None and first.data(ID_ROLE) in self._package_ids else None
            for c in range(self.table.columnCount()):
                cell = self.table.item(r, c)
                if cell is not None:
                    cell.setBackground(QtGui.QColor(color) if color else QtGui.QBrush())
        self.create_butt.setEnabled(bool(self._package_ids) and not exact
                                    and self._session is not None and bool(self._project))
        if self._package_ids and self.tree.topLevelItemCount():
            if exact:
                text = f"Package matches list: {', '.join(exact)}"
            elif almost:
                text = f"Package almost matches: {', '.join(almost)}"
            else:
                text = "No list has the package's versions"
            self.status.setText(f"{text} ({len(self._package_ids)} package versions)")

    # create ---------------------------------------------------------------------

    def _categories(self):
        names = []
        for t in range(self.tree.topLevelItemCount()):
            name = self.tree.topLevelItem(t).text(0)
            if name != ayon_lists.NO_CATEGORY:
                names.append(name)
        return names

    def create_list(self):
        """
        Create List from Package: name, category and where (AYON, or ftrack
        - the AYON ftrack sync then brings the list to AYON too), asked first
        """
        name, ids = self._package()
        ids = list(dict.fromkeys(ids))
        if not ids or self._session is None or not self._project:
            return
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("Create List from Package")
        form = QtWidgets.QFormLayout(dialog)
        name_edit = QtWidgets.QLineEdit(name or '', dialog)
        name_edit.setMinimumWidth(300)
        # AYON category: the attribute's options (enum) when it has them,
        # plus the categories of the lists shown; typing a new one is allowed
        options = []
        try:
            options = self._busy(lambda: ayon_lists.category_options(self._session),
                                 "Reading AYON list categories...") or []
        except Exception:
            options = []
        category = QtWidgets.QComboBox(dialog)
        category.setEditable(True)
        category.addItems([''] + options + [c for c in self._categories() if c not in options])
        category.setToolTip("Category of the AYON list" + (
            f" (AYON options: {', '.join(options)})" if options else ""))
        ftrack_category = QtWidgets.QComboBox(dialog)
        ftrack_category.setToolTip("Category of the ftrack list (ftrack requires one)")
        to_ftrack = QtWidgets.QCheckBox("push to Ftrack too", dialog)
        to_ftrack.setChecked(False)
        to_ftrack.setToolTip(
            "Create the list in ftrack (project of the Ftrack tab, Shots sub-tab) and the same "
            "list in AYON, paired by the ftrack list id (ftrackId), so the AYON ftrack sync "
            "keeps them together. Uses the ftrack ids AYON keeps for the versions.")
        where = QtWidgets.QLabel(dialog)
        ftrack_state = {'session': None, 'project_id': None, 'categories': None}

        def same_ayon_category(text):
            """the AYON category with the ftrack category's name, when the AYON one is empty"""
            if category.currentText().strip():
                return
            for i in range(category.count()):
                if category.itemText(i).lower() == str(text).lower():
                    category.setCurrentIndex(i)
                    return

        ftrack_category.currentTextChanged.connect(same_ayon_category)
        ftrack_label = QtWidgets.QLabel("ftrack category:", dialog)

        def fill_categories():
            on = to_ftrack.isChecked()
            ftrack_category.setVisible(on)
            ftrack_label.setVisible(on)
            if on:
                if ftrack_state['categories'] is None:
                    session, project_id = (self._busy(self.ftrack_connect, "Connecting to ftrack...")
                                           if self.ftrack_connect else (None, None)) or (None, None)
                    ftrack_state.update(session=session, project_id=project_id,
                                        categories=ftrack.list_categories(session) if session else [])
                if not ftrack_category.count():
                    ftrack_category.addItems(ftrack_state['categories'])
                if ftrack_state['session'] is None or not ftrack_state['project_id']:
                    where.setText("No ftrack connection or project (Ftrack tab, see the Log tab)")
                else:
                    where.setText(f"AYON project {self._project} and ftrack")
            else:
                where.setText(f"AYON project {self._project}")

        to_ftrack.toggled.connect(fill_categories)
        form.addRow("", to_ftrack)
        form.addRow("Create in:", where)
        form.addRow("List name:", name_edit)
        form.addRow("AYON category:", category)
        form.addRow(ftrack_label, ftrack_category)
        form.addRow("", QtWidgets.QLabel(f"{len(ids)} versions matched by the package files", dialog))
        buttons = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel, dialog)
        buttons.button(QtWidgets.QDialogButtonBox.Ok).setText("Create List")
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        form.addRow(buttons)
        fill_categories()
        if dialog.exec_() != QtWidgets.QDialog.Accepted:
            return
        label = name_edit.text().strip()
        if not label:
            self.status.setText("Create List: the list name is empty, nothing created")
            return
        cat = category.currentText().strip()
        if to_ftrack.isChecked():
            self._create_in_ftrack(label, cat, ftrack_category.currentText().strip(), ids,
                                   ftrack_state)
        else:
            self._create_in_ayon(label, cat, ids)

    def _log(self, level, msg, exc_info=False):
        if self.log is not None:
            self.log.log(level, msg, exc_info=exc_info)

    def _create_in_ayon(self, label, cat, ids, also=''):
        """
        :return: the AYON list id - new, or an existing list with this label
        (AYON labels are unique) the package's versions were added to - None
        when it failed or was cancelled (logged)
        """
        session, project = self._session, self._project
        try:
            existing = self._busy(lambda: ayon_lists.find_list_by_label(session, project, label),
                                  "Looking for the AYON list...")
        except Exception as e:
            self._log(logging.DEBUG, f"Looking for AYON list '{label}' failed: {e}")
            existing = None
        if existing:
            have = len(self._list_versions.get(existing) or ())
            answer = QtWidgets.QMessageBox.question(
                self, "AYON list exists",
                f"The AYON list '{label}' already exists ({have} versions). Add the package's "
                f"versions it doesn't have to it?")
            if answer != QtWidgets.QMessageBox.Yes:
                self.status.setText(f"AYON list '{label}' exists: nothing changed")
                return None
            try:
                added = self._busy(lambda: ayon_lists.add_missing_items(session, project, existing, ids),
                                   "Adding versions to the AYON list...")
            except Exception as e:
                self._log(logging.ERROR, f"{also}adding versions to AYON list '{label}' failed: {e}")
                self.status.setText(f"{also}adding to the AYON list failed (see the Log tab)")
                return None
            self._log(logging.INFO, f"AYON list '{label}' existed: {added} version(s) added")
            list_id = existing
        else:
            try:
                list_id = self._busy(
                    lambda: ayon_lists.create_version_list(session, project, label, ids, cat),
                    "Creating AYON list...")
            except Exception as e:
                self._log(logging.ERROR, f"{also}creating AYON list '{label}' failed: {e}")
                self.status.setText(f"{also}creating the AYON list failed (see the Log tab)")
                return None
            self._log(logging.INFO, f"AYON list '{label}' created in {project} with {len(ids)} versions")
        self.show_lists(session, project)
        for item in self._list_items():
            if item.data(0, ID_ROLE) == list_id:
                self.tree.setCurrentItem(item)
                break
        return list_id

    # seconds after creating the ftrack list: the AYON list is checked again
    RECHECK_AFTER = (5, 20)

    def _recheck_list(self, con, project, list_id, label, version_ids):
        """
        after the ftrack list was made: the AYON ftrack sync pairs it with the
        AYON list (by name) and may change its items; put back what's missing
        """
        try:
            added = ayon_lists.add_missing_items(con, project, list_id, version_ids)
        except Exception as e:
            self._log(logging.ERROR, f"AYON list '{label}': restoring its versions failed: {e}")
            return
        if added:
            self._log(logging.WARNING, f"AYON list '{label}' had lost {added} version(s) after the "
                                       f"ftrack list was created; they were added again")
            if self._project == project:
                self.show_lists(con, project)

    def _create_in_ftrack(self, label, cat, ftrack_cat, ids, ftrack_state):
        """
        push to Ftrack too: the ftrack list first (chosen category), then the
        AYON list with the same name - the ayon-ftrack sync pairs them by name
        """
        session, project_id = ftrack_state['session'], ftrack_state['project_id']
        if session is None or not project_id:
            self.status.setText("No ftrack connection or project: nothing created (see the Log tab)")
            return
        if not ftrack_cat:
            self.status.setText("ftrack lists need a category: nothing created")
            return
        con, project = self._session, self._project
        try:
            mapping = self._busy(lambda: ayon_lists.version_ftrack_ids(con, project, ids),
                                 "Reading ftrack ids from AYON...")
        except Exception as e:
            self._log(logging.ERROR, f"Reading the ftrack ids of the versions from AYON failed: {e}")
            self.status.setText("Reading ftrack ids failed: nothing created (see the Log tab)")
            return
        ayon_ids = [i for i in ids if i in mapping]
        ftrack_ids = [mapping[i] for i in ayon_ids]
        missing = len(ids) - len(ayon_ids)
        if not ayon_ids:
            self._log(logging.ERROR, "None of the package's versions has an ftrack id in AYON "
                                     "(not synced to ftrack): nothing created")
            self.status.setText("No version has an ftrack id: nothing created (see the Log tab)")
            return
        if missing:
            answer = QtWidgets.QMessageBox.question(
                self, "Create List in AYON and ftrack",
                f"{missing} of the {len(ids)} versions have no ftrack id in AYON (not in "
                f"ftrack). Create the list '{label}' with the other {len(ayon_ids)}?")
            if answer != QtWidgets.QMessageBox.Yes:
                return
        # 1. ftrack first, in the chosen category: when the AYON list appears,
        # the ayon-ftrack transmitter finds this list by name and uses it (it
        # creates its own ftrack list, in the first list category, otherwise)
        try:
            self._busy(lambda: ftrack.create_version_list(session, project_id, label, ftrack_cat,
                                                          ftrack_ids),
                       "Creating ftrack list...")
        except Exception as e:
            self._log(logging.ERROR, f"Creating ftrack list '{label}' failed: {e}; the AYON list "
                                     f"was not created", exc_info=True)
            self.status.setText("Creating the ftrack list failed: nothing created in AYON (see the Log tab)")
            return
        self._log(logging.INFO, f"ftrack list '{label}' ({ftrack_cat}) has the {len(ftrack_ids)} "
                                f"versions")
        # 2. AYON (checked, missing versions added item by item)
        list_id = self._create_in_ayon(label, cat, ayon_ids, also=f"ftrack list '{label}' is done, ")
        if list_id is None:
            return
        self.status.setText(f"List '{label}' created in ftrack and AYON ({len(ayon_ids)} versions)")
        # 3. the syncs react to the new lists: check the AYON list again
        for seconds in self.RECHECK_AFTER:
            QtCore.QTimer.singleShot(
                seconds * 1000,
                lambda: self._recheck_list(con, project, list_id, label, list(ayon_ids)))
