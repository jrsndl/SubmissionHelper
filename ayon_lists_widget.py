"""
AYON tab > AYON Lists sub-tab (the queries are in ayon_lists.py).

Left: the project's AYON entity lists by list category (list folders are
not used). Right: the versions of the selected list - Folder Path, Task,
Product, Version. Same browser as Ftrack > Get Lists.
Nothing here is saved in presets.
"""
from PySide2 import QtWidgets

import ayon_lists
from ftrack_lists_widget import FtrackListsTab


class AyonListsTab(FtrackListsTab):
    COLUMNS = ayon_lists.LIST_COLUMNS
    SYSTEM = "AYON"
    BUTTON_TIP = ("Read the lists of the AYON Project set in the Ayon group. "
                  "Uses the AYON sign-in of the Preferences tab (Accounts).")
    TREE_TIP = ("AYON lists by list category. Select a list to show its versions; "
                "items that aren't versions are not shown.")
    TREE_HEADER = "List Category / List"
    GROUPS = "categories"

    def __init__(self, connect, busy=None, parent=None):
        super().__init__(connect, busy, parent)
        # setting (MainWindow puts it on ui, saved in presets), default on
        self.auto_chbx = QtWidgets.QCheckBox("auto-read", self)
        self.auto_chbx.setObjectName("ayon_lists_auto")
        self.auto_chbx.setChecked(True)
        self.auto_chbx.setToolTip(
            "Read the AYON lists right after Submission Helper connects to AYON "
            "(Scan, or a package load / Reload with Enable on). Again only when the "
            "Project changes; Get Lists reads them any time.")
        self.top_bar.insertWidget(1, self.auto_chbx)
        self._auto_project = None

    def auto_read(self, con, project):
        """after a successful AYON connection: read the lists once per project"""
        if not self.auto_chbx.isChecked() or con is None or not project:
            return
        if project == self._auto_project and self.tree.topLevelItemCount():
            return
        self._auto_project = project
        self.show_lists(con, project)

    def query_lists(self, con, project):
        return ayon_lists.query_lists(con, project)

    def query_versions(self, con, list_id):
        return ayon_lists.query_list_versions(con, self._project, list_id)
