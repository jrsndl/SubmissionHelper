"""
Ftrack tab > Get Lists sub-tab (the queries are in ftrack.py).

Left: the project's ftrack version lists, by list folder (category).
Right: the versions of the selected list - Version Link (ftrack hierarchy
path and version name), Version, Version Status, Version Description,
Asset Type, Published By.

Built in code, like the other code-built controls, so ui_Submission.py can
still be regenerated from submission.ui. Nothing here is saved in presets.
"""
from PySide2 import QtCore, QtGui, QtWidgets

import ftrack

ID_ROLE = QtCore.Qt.UserRole


class _CopyTable(QtWidgets.QTableWidget):
    """Ctrl+C calls on_copy (the item view's own copy takes only one cell)"""
    on_copy = None

    def keyPressEvent(self, event):
        if event.matches(QtGui.QKeySequence.Copy) and self.on_copy is not None:
            self.on_copy()
            event.accept()
            return
        super().keyPressEvent(event)


class FtrackListsTab(QtWidgets.QWidget):
    """
    Lists browser; the AYON Lists sub-tab (ayon_lists_widget.py) is a subclass
    with its own COLUMNS, texts and queries.
    """
    COLUMNS = ftrack.LIST_COLUMNS
    SYSTEM = "ftrack"
    BUTTON_TIP = ("Read the version lists of the ftrack Project set on the Shots sub-tab. "
                  "Uses the ftrack sign-in of the Preferences tab (Accounts).")
    TREE_TIP = "ftrack list folders and their version lists. Select a list to show its versions."
    TREE_HEADER = "List Folder / List"
    GROUPS = "folders"

    def query_lists(self, session, project):
        """[{'id', 'name', 'folder'}]"""
        return ftrack.query_version_lists(session, project)

    def query_versions(self, session, list_id):
        """rows: dicts with COLUMNS keys"""
        return ftrack.query_list_versions(session, list_id)

    def __init__(self, connect, busy=None, parent=None):
        """
        :param connect: callable -> (session, project_id); (None, None) or a
            None item when there is no connection / project (it logs why)
        :param busy: callable(fn, message) running fn with a wait cursor
        """
        super().__init__(parent)
        self._connect = connect
        self._busy = busy or (lambda fn, message: fn())
        self._session = None

        layout = QtWidgets.QVBoxLayout(self)
        top = QtWidgets.QHBoxLayout()
        self.top_bar = top
        layout.addLayout(top)
        self.get_butt = QtWidgets.QPushButton("Get Lists", self)
        self.get_butt.setMinimumSize(QtCore.QSize(120, 30))
        self.get_butt.setToolTip(self.BUTTON_TIP)
        top.addWidget(self.get_butt)
        self.status = QtWidgets.QLabel("", self)
        top.addWidget(self.status, 1)

        splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal, self)
        self.splitter = splitter
        layout.addWidget(splitter, 1)

        self.tree = QtWidgets.QTreeWidget(splitter)
        self.tree.setHeaderLabels([self.TREE_HEADER])
        self.tree.setToolTip(self.TREE_TIP)
        self.table = _CopyTable(0, len(self.COLUMNS), splitter)
        self.table.setHorizontalHeaderLabels(list(self.COLUMNS))
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setToolTip("Versions of the selected list. Ctrl+C copies the selected "
                              "rows (tab separated, for Excel).")
        splitter.addWidget(self.tree)
        splitter.addWidget(self.table)
        # the list tree only as wide as its names (_fit_tree), the table gets the rest
        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([200, 1000])

        self.table.on_copy = self.copy_selection

        self.get_butt.clicked.connect(self.get_lists)
        self.tree.currentItemChanged.connect(self._list_selected)

    # lists -------------------------------------------------------------------

    def get_lists(self):
        result = self._busy(self._connect, f"Connecting to {self.SYSTEM}...") or (None, None)
        session, project_id = result
        self.show_lists(session, project_id)

    def show_lists(self, session, project_id):
        """the lists of the project, with a connection made elsewhere"""
        self.tree.clear()
        self._fill_table([])
        self._session = session
        self._project = project_id
        if session is None or not project_id:
            self.status.setText(f"No {self.SYSTEM} connection or project (see the Log tab).")
            return
        lists = self._busy(lambda: self.query_lists(session, project_id),
                           f"Reading {self.SYSTEM} lists...")
        folders = {}
        for one in lists:
            folder = folders.get(one['folder'])
            if folder is None:
                folder = QtWidgets.QTreeWidgetItem(self.tree, [one['folder']])
                folder.setFlags(folder.flags() & ~QtCore.Qt.ItemIsSelectable)
                folders[one['folder']] = folder
            item = QtWidgets.QTreeWidgetItem(folder, [one['name']])
            item.setData(0, ID_ROLE, one['id'])
        self.tree.expandAll()
        self._fit_tree()
        self.status.setText(f"{len(lists)} lists in {len(folders)} {self.GROUPS}")

    def _fit_tree(self):
        """tree as wide as its longest name (160..450 px)"""
        self.tree.resizeColumnToContents(0)
        width = self.tree.sizeHintForColumn(0) + self.tree.indentation() + 40
        width = max(160, min(width, 450))
        total = sum(self.splitter.sizes()) or (width + 800)
        self.splitter.setSizes([width, max(total - width, 200)])

    def _list_selected(self, current, previous=None):
        list_id = current.data(0, ID_ROLE) if current is not None else None
        if not list_id:
            return
        session = self._session
        rows = self._busy(lambda: self.query_versions(session, list_id),
                          f"Reading {self.SYSTEM} list versions...")
        self._fill_table(rows)
        self.status.setText(f"{current.text(0)}: {len(rows)} versions")

    # table -------------------------------------------------------------------

    def _fill_table(self, rows):
        table = self.table
        table.setSortingEnabled(False)
        table.setRowCount(len(rows))
        for r, row in enumerate(rows):
            for c, column in enumerate(self.COLUMNS):
                value = row.get(column, '')
                item = QtWidgets.QTableWidgetItem()
                # numbers sort as numbers
                item.setData(QtCore.Qt.DisplayRole, value if isinstance(value, int) else str(value))
                table.setItem(r, c, item)
        table.setSortingEnabled(True)
        if rows:
            table.resizeColumnsToContents()

    def copy_selection(self):
        rows = sorted({i.row() for i in self.table.selectedIndexes()})
        if not rows:
            return
        lines = ["\t".join(self.COLUMNS)]
        for r in rows:
            cells = []
            for c in range(self.table.columnCount()):
                item = self.table.item(r, c)
                cells.append(item.text().replace("\t", " ").replace("\n", " ") if item else "")
            lines.append("\t".join(cells))
        QtWidgets.QApplication.clipboard().setText("\n".join(lines))
