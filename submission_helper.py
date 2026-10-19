import pprint
import argparse

import sys
import os
import subprocess
import inspect
from functools import partial
import logging
import time
import getpass

if __name__ == "__main__":
    # command line mode (-i / -p) runs without Qt: hand over to sh_cli before
    # PySide2 is imported, so it works on machines without Qt or a display
    import sh_cli as _sh_cli
    if _sh_cli.wants_headless(sys.argv[1:]):
        sys.exit(_sh_cli.main())

from PySide2 import QtCore, QtGui, QtWidgets

from ui_Submission import Ui_submission
from tooltips import apply_tooltips

from sequencer import Sequencer, PARSE_ROWS, PARSE_FIELDS
from settings import Settings
import parse_file_name
import sh_logging
from log_view import LogView
import grouping
from grouping_widget import GroupingTab
from ftrack_lists_widget import FtrackListsTab
from sh_cli import (CLI_ACTIONS, CLI_DESCRIPTION, CLI_EPILOG, setting_to_bool,  # noqa: F401
                    get_args, console_level_from_args, check_cli_args)
import sh_cli
import credentials

# bookkeeping keys of the Sequencer, not tokens: not shown in the Inspector
INSPECTOR_HIDDEN_KEYS = ('_parse_orig', '_data_keys')


class ImgWidget1(QtWidgets.QLabel):

    def __init__(self, parent=None, image_path=None):
        super(ImgWidget1, self).__init__(parent)
        pix = QtGui.QPixmap(image_path)
        pix_resized = pix.scaledToHeight(50, QtCore.Qt.SmoothTransformation)
        if pix_resized:
            self.setPixmap(pix_resized)
        else:
            log.error("Can't display image in a table: " + image_path)


class ImgWidget2(QtWidgets.QWidget):

    def __init__(self, parent=None, image_path=None):
        super(ImgWidget2, self).__init__(parent)
        if os.path.exists(image_path):
            self.pic = QtGui.QPixmap(image_path).scaledToHeight(
                50, QtCore.Qt.SmoothTransformation)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        if hasattr(self, 'pic'):
            painter.drawPixmap(0, 0, self.pic)


class MainWindow(QtWidgets.QMainWindow, Ui_submission):

    # widgets that hold output, not settings: never saved to / loaded from presets
    NOT_SETTINGS = ('log',)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()

    def dropEvent(self, e):
        for url in e.mimeData().urls():
            file_name = url.toLocalFile()
            self.ui.package_folder.setText(str(file_name))
            #print("Dropped file: " + file_name)

    def __init__(self, no_gui=False, s=None, package_path=None, args=None):
        super().__init__()

        self.log = logging.getLogger("MainWindow")
        self.bare_title = "Submission Helper"
        self.package_path = package_path

        self.ui = Ui_submission()
        self.ui.setupUi(self)
        self.no_gui = no_gui

        # top / bottom tab panels in a draggable splitter
        self.panel_splitter = self._setup_panel_splitter()
        self._tune_top_tab_layouts()
        # Parsing tab rows beyond the 32 from the .ui file
        self._add_parse_rows()
        # Ayon tab: Scan button, version / product filter controls
        self._add_ayon_controls()
        # Data tab: Show Matched Only
        self._add_data_controls()
        # tooltips of the .ui widgets and the parse rows added above
        apply_tooltips(self.ui)
        # Sequencer used by the Ayon tab when no package is loaded
        self.ayon_only = None

        # Log tab: shows everything logged by any module
        self.log_view = None
        if not self.no_gui:
            self.log_view = LogView(self.ui, self.ui.TopTab, self.ui.tab_21, parent=self)

        # Settings to gui
        # Top Tabs show / hide: Presets checkbox name: [tab index, tab name]
        self.tab_pairs = {
            "preset_mod_package": [0, "Package"],
            "preset_mod_parsing": [1, "Parsing"],
            "preset_mod_sidecar": [2, "Sidecar Files"],
            "preset_mod_rename": [3, "Rename"],
            "preset_mod_data": [4, "Data"],
            "preset_mod_ftrack": [5, "Ftrack"],
            "preset_mod_vendor": [6, "Vendor"],
            "preset_mod_replace": [7, "Replace"],
            "preset_mod_convert": [8, "Convert"],
            "preset_mod_spreadsheet": [9, "Spreadsheet"],
            "preset_mod_checks": [10, "Checks"],
            "preset_mod_publish": [11, "Ayon Publish"],
            "preset_mod_ayon": [12, "Ayon"],
            "preset_mod_preferences": [13, "Preferences"],
            "preset_mod_exports": [14, "Exports"],
            "preset_mod_log": [16, "Log"],
            "preset_mod_help": [17, "Help"]
        }
        self.tab_pairs_bottom = {
            "preset_mod_submission": [0, "Submission"],
            "preset_mod_drivelog": [1, "Drive Log"],
            "preset_mod_text": [2, "Text"],
            "preset_mod_sidecar": [3, "Sidecar Files"],
            "preset_mod_rename": [4, "Rename"],
            "preset_mod_inspector": [5, "Inspector"],
            "preset_mod_files": [6, "Files"]
        }
        # tab pages of the checkboxes above: tabs added in code (Grouping)
        # shift the indexes
        self.tab_pages = {k: self.ui.TopTab.widget(v[0]) for k, v in self.tab_pairs.items()}
        self.tab_pages_bottom = {k: self.ui.BottomTab.widget(v[0]) for k, v in self.tab_pairs_bottom.items()}
        # Grouping tab after Spreadsheet, replaces Merge By (Preferences tab)
        self.grouping_tab = self._add_grouping_tab()
        # Ftrack tab: Shots and Get Lists sub-tabs
        self.ftrack_lists_tab = self._add_ftrack_lists_tab()
        # Presets tab: Modules below the Presets group, full width
        self._arrange_preset_modules()
        self.ui_start = True
        self.settings_obj = s
        self.settings = self.settings_obj.settings or {}
        self.settings_inst = self.settings_obj.install_settings
        self.args = args or {}

        # personal ftrack / Ayon sign-in (credentials.py): the dialog asks when
        # there are no credentials, headless runs never ask
        self.accounts_group = None
        if not self.no_gui:
            self._setup_accounts()

        if not self.no_gui:
            self.apply_settings_overrides(self.args.get('settings', ''))
            self.settings_to_gui()
            self.log_view.rerender()
            # fill keys missing from an old / partial preset with the gui defaults
            self.settings_from_gui()
            self.settings_update_app_title()
            self.settings_update_dropbox()
            self.gui_show_hide_modules()
        else:
            # headless: start from the gui defaults, overlay the preset, so
            # older or partial presets don't raise KeyError later
            preset = self.settings
            self.settings_from_gui()
            self.settings.update(preset)
            self.apply_settings_overrides(self.args.get('settings', ''))
        self.ui_start = False

        # Other inits
        self.regexes = {}
        self.data = None

        # ---------------- Below is only connecting signals

        # Package Folder
        self.ui.package_folder.textChanged.connect(
            partial(self._handler_later, 'package_folder', 'source_change'))
        self.ui.package_browse.clicked.connect(
            partial(self.handler, 'package_browse', 'browse'))
        self.ui.package_explore.clicked.connect(
            partial(self.handler, 'package_explore', 'explore'))
        self.ui.reload.clicked.connect(
            partial(self.handler, 'package_reload', 'source_change'))

        # File Age
        self.ui.age_enabled.clicked.connect(
            partial(self.handler, 'age_enabled', 'refresh_spreadsheets_age'))
        self.ui.age_number.valueChanged.connect(
            partial(self.handler, 'age_number', 'refresh_spreadsheets_age'))
        self.ui.age_unit.currentIndexChanged.connect(
            partial(self.handler, 'age_unit', 'refresh_spreadsheets_age'))
        self.ui.age_type.currentIndexChanged.connect(
            partial(self.handler, 'age_type', 'refresh_spreadsheets_age'))
        self.ui.age_exclude.textChanged.connect(
            partial(self._handler_later, 'age_exclude', 'refresh_spreadsheets_age'))
        self.ui.age_include.textChanged.connect(
            partial(self._handler_later, 'age_include', 'refresh_spreadsheets_age'))

        # Rename Package
        self.ui.name_template.textChanged.connect(
            partial(self._handler_later, 'name_template', 'package_rename'))
        self.ui.name_date_regex.textChanged.connect(
            partial(self._handler_later, 'name_date_regex', 'package_rename'))
        self.ui.name_version_per_date.clicked.connect(
            partial(self.handler, 'name_version_per_date', 'package_rename'))
        self.ui.name_version_zeroes.valueChanged.connect(
            partial(self.handler, 'name_version_zeroes', 'package_rename'))
        self.ui.name_version_use_letters.clicked.connect(
            partial(self.handler,
                    'name_version_use_letters', 'package_rename'))
        self.ui.name_version_letters_uppercase.clicked.connect(
            partial(self.handler,
                    'name_version_letters_uppercase', 'package_rename'))
        self.ui.name_from_template.clicked.connect(
            partial(self.handler, 'name_from_template', 'package_rename'))
        self.ui.name_from_folder.clicked.connect(
            partial(self.handler, 'name_from_folder', 'package_rename'))

        self.ui.name_rename.clicked.connect(
            partial(self.handler, 'name_rename', 'package_rename'))
        self.ui.name_rename_auto.clicked.connect(
            partial(self.handler, 'name_rename_auto', 'package_rename'))

        # Parsing Tab
        # every field of every row refreshes the parsing
        for row in range(1, PARSE_ROWS + 1):
            for field in PARSE_FIELDS:
                name = f"parse_{field}_{row:02d}"
                getattr(self.ui, name).textChanged.connect(
                    partial(self._handler_later, name, 'refresh_parsing'))

        # Sidecar Tab
        self.ui.side_folder.textChanged.connect(
            partial(self._handler_later, 'side_folder', 'refresh_side_files'))
        self.ui.package_browse_2.clicked.connect(
            partial(self.browse_line_edit, self.ui.side_folder, 'dir', "Select Sidecar Search Folder"))
        self.ui.package_explore_2.clicked.connect(
            partial(self.explore_line_edit, self.ui.side_folder))
        self.ui.side_exclude.textChanged.connect(
            partial(self._handler_later, 'side_exclude', 'refresh_side_files'))
        self.ui.side_include.textChanged.connect(
            partial(self._handler_later, 'side_include', 'refresh_side_files'))

        self.ui.side_sub_only.clicked.connect(
            partial(self.handler, 'side_sub_only', 'refresh_side'))
        self.ui.side_log_only.clicked.connect(
            partial(self.handler, 'side_log_only', 'refresh_side'))
        self.ui.side_all.clicked.connect(
            partial(self.handler, 'side_all', 'refresh_side'))

        self.ui.side_pattern_1.textChanged.connect(
            partial(self._handler_later, 'side_pattern_1', 'refresh_side'))
        self.ui.side_repl_1.textChanged.connect(
            partial(self._handler_later, 'side_repl_1', 'refresh_side'))
        self.ui.side_match_1.textChanged.connect(
            partial(self._handler_later, 'side_match_1', 'refresh_side'))
        self.ui.side_dest_1.textChanged.connect(
            partial(self._handler_later, 'side_dest_1', 'refresh_side'))
        self.ui.side_filter_1.textChanged.connect(
            partial(self._handler_later, 'side_filter_1', 'refresh_side'))
        self.ui.side_pattern_2.textChanged.connect(
            partial(self._handler_later, 'side_pattern_2', 'refresh_side'))
        self.ui.side_repl_2.textChanged.connect(
            partial(self._handler_later, 'side_repl_2', 'refresh_side'))
        self.ui.side_match_2.textChanged.connect(
            partial(self._handler_later, 'side_match_2', 'refresh_side'))
        self.ui.side_dest_2.textChanged.connect(
            partial(self._handler_later, 'side_dest_2', 'refresh_side'))
        self.ui.side_filter_2.textChanged.connect(
            partial(self._handler_later, 'side_filter_2', 'refresh_side'))
        self.ui.side_pattern_3.textChanged.connect(
            partial(self._handler_later, 'side_pattern_3', 'refresh_side'))
        self.ui.side_repl_3.textChanged.connect(
            partial(self._handler_later, 'side_repl_3', 'refresh_side'))
        self.ui.side_match_3.textChanged.connect(
            partial(self._handler_later, 'side_match_3', 'refresh_side'))
        self.ui.side_dest_3.textChanged.connect(
            partial(self._handler_later, 'side_dest_3', 'refresh_side'))
        self.ui.side_filter_3.textChanged.connect(
            partial(self._handler_later, 'side_filter_3', 'refresh_side'))
        self.ui.side_pattern_4.textChanged.connect(
            partial(self._handler_later, 'side_pattern_4', 'refresh_side'))
        self.ui.side_repl_4.textChanged.connect(
            partial(self._handler_later, 'side_repl_4', 'refresh_side'))
        self.ui.side_match_4.textChanged.connect(
            partial(self._handler_later, 'side_match_4', 'refresh_side'))
        self.ui.side_dest_4.textChanged.connect(
            partial(self._handler_later, 'side_dest_4', 'refresh_side'))
        self.ui.side_filter_4.textChanged.connect(
            partial(self._handler_later, 'side_filter_4', 'refresh_side'))
        self.ui.side_pattern_5.textChanged.connect(
            partial(self._handler_later, 'side_pattern_5', 'refresh_side'))
        self.ui.side_repl_5.textChanged.connect(
            partial(self._handler_later, 'side_repl_5', 'refresh_side'))
        self.ui.side_match_5.textChanged.connect(
            partial(self._handler_later, 'side_match_5', 'refresh_side'))
        self.ui.side_dest_5.textChanged.connect(
            partial(self._handler_later, 'side_dest_5', 'refresh_side'))
        self.ui.side_filter_5.textChanged.connect(
            partial(self._handler_later, 'side_filter_5', 'refresh_side'))
        self.ui.side_pattern_6.textChanged.connect(
            partial(self._handler_later, 'side_pattern_6', 'refresh_side'))
        self.ui.side_repl_6.textChanged.connect(
            partial(self._handler_later, 'side_repl_6', 'refresh_side'))
        self.ui.side_match_6.textChanged.connect(
            partial(self._handler_later, 'side_match_6', 'refresh_side'))
        self.ui.side_dest_6.textChanged.connect(
            partial(self._handler_later, 'side_dest_6', 'refresh_side'))
        self.ui.side_filter_6.textChanged.connect(
            partial(self._handler_later, 'side_filter_6', 'refresh_side'))

        # copy files button
        self.ui.side_copy.clicked.connect(
            partial(self.handler, 'side_copy', 'side_copy'))

        # RENAME
        self.ui.Rename_go.clicked.connect(
            partial(self.handler, 'Rename_go', 'Rename_go'))
        self.ui.rename_reload_after.clicked.connect(
            partial(self.handler, 'rename_reload_after', ''))
        # bottom Rename tab: how the paths are shown
        for _radio in ('rename_tab_relative', 'rename_tab_absolute', 'rename_tab_names_only'):
            getattr(self.ui, _radio).clicked.connect(
                partial(self.handler, _radio, 'rename_display'))

        self.ui.rename_filter_01.textChanged.connect(
            partial(self._handler_later, 'rename_filter_01', 'refresh_rename'))
        self.ui.rename_pattern_01.textChanged.connect(
            partial(self._handler_later, 'rename_pattern_01', 'refresh_rename'))
        self.ui.rename_repl_01.textChanged.connect(
            partial(self._handler_later, 'rename_repl_01', 'refresh_rename'))
        self.ui.rename_source_01.valueChanged.connect(
            partial(self.handler, 'rename_source_01', 'refresh_rename'))

        self.ui.rename_filter_02.textChanged.connect(
            partial(self._handler_later, 'rename_filter_02', 'refresh_rename'))
        self.ui.rename_pattern_02.textChanged.connect(
            partial(self._handler_later, 'rename_pattern_02', 'refresh_rename'))
        self.ui.rename_repl_02.textChanged.connect(
            partial(self._handler_later, 'rename_repl_02', 'refresh_rename'))
        self.ui.rename_source_02.valueChanged.connect(
            partial(self.handler, 'rename_source_02', 'refresh_rename'))

        self.ui.rename_filter_03.textChanged.connect(
            partial(self._handler_later, 'rename_filter_03', 'refresh_rename'))
        self.ui.rename_pattern_03.textChanged.connect(
            partial(self._handler_later, 'rename_pattern_03', 'refresh_rename'))
        self.ui.rename_repl_03.textChanged.connect(
            partial(self._handler_later, 'rename_repl_03', 'refresh_rename'))
        self.ui.rename_source_03.valueChanged.connect(
            partial(self.handler, 'rename_source_03', 'refresh_rename'))

        self.ui.rename_filter_04.textChanged.connect(
            partial(self._handler_later, 'rename_filter_04', 'refresh_rename'))
        self.ui.rename_pattern_04.textChanged.connect(
            partial(self._handler_later, 'rename_pattern_04', 'refresh_rename'))
        self.ui.rename_repl_04.textChanged.connect(
            partial(self._handler_later, 'rename_repl_04', 'refresh_rename'))
        self.ui.rename_source_04.valueChanged.connect(
            partial(self.handler, 'rename_source_04', 'refresh_rename'))

        self.ui.rename_filter_05.textChanged.connect(
            partial(self._handler_later, 'rename_filter_05', 'refresh_rename'))
        self.ui.rename_pattern_05.textChanged.connect(
            partial(self._handler_later, 'rename_pattern_05', 'refresh_rename'))
        self.ui.rename_repl_05.textChanged.connect(
            partial(self._handler_later, 'rename_repl_05', 'refresh_rename'))
        self.ui.rename_source_05.valueChanged.connect(
            partial(self.handler, 'rename_source_05', 'refresh_rename'))

        self.ui.rename_filter_06.textChanged.connect(
            partial(self._handler_later, 'rename_filter_06', 'refresh_rename'))
        self.ui.rename_pattern_06.textChanged.connect(
            partial(self._handler_later, 'rename_pattern_06', 'refresh_rename'))
        self.ui.rename_repl_06.textChanged.connect(
            partial(self._handler_later, 'rename_repl_06', 'refresh_rename'))
        self.ui.rename_source_06.valueChanged.connect(
            partial(self.handler, 'rename_source_06', 'refresh_rename'))

        self.ui.rename_filter_07.textChanged.connect(
            partial(self._handler_later, 'rename_filter_07', 'refresh_rename'))
        self.ui.rename_pattern_07.textChanged.connect(
            partial(self._handler_later, 'rename_pattern_07', 'refresh_rename'))
        self.ui.rename_repl_07.textChanged.connect(
            partial(self._handler_later, 'rename_repl_07', 'refresh_rename'))
        self.ui.rename_source_07.valueChanged.connect(
            partial(self.handler, 'rename_source_07', 'refresh_rename'))

        self.ui.rename_filter_08.textChanged.connect(
            partial(self._handler_later, 'rename_filter_08', 'refresh_rename'))
        self.ui.rename_pattern_08.textChanged.connect(
            partial(self._handler_later, 'rename_pattern_08', 'refresh_rename'))
        self.ui.rename_repl_08.textChanged.connect(
            partial(self._handler_later, 'rename_repl_08', 'refresh_rename'))
        self.ui.rename_source_08.valueChanged.connect(
            partial(self.handler, 'rename_source_08', 'refresh_rename'))

        # Ftrack Tab
        self.ui.ftrack_use.clicked.connect(
            partial(self.handler, 'ftrack_use', 'refresh_ftrack'))
        self.ui.ftrack_project.textChanged.connect(
            partial(self._handler_later, 'ftrack_project', 'refresh_ftrack'))
        self.ui.ftrack_shot.textChanged.connect(
            partial(self._handler_later, 'ftrack_shot', 'refresh_ftrack'))
        self.ui.ftrack_task.textChanged.connect(
            partial(self._handler_later, 'ftrack_task', 'refresh_ftrack'))
        # Extensions (only these get ftrack notes); was never connected
        self.ui.ftrack_include_2.textChanged.connect(
            partial(self._handler_later, 'ftrack_include_2', 'refresh_ftrack'))
        self.ui.ftrack_label_use.clicked.connect(
            partial(self.handler, 'ftrack_label_use', 'refresh_ftrack'))
        self.ui.ftrack_label.textChanged.connect(
            partial(self._handler_later, 'ftrack_label', 'refresh_ftrack'))
        self.ui.ftrack_version_use.clicked.connect(
            partial(self.handler, 'ftrack_version_use', 'refresh_ftrack'))
        self.ui.ftrack_version.textChanged.connect(
            partial(self._handler_later, 'ftrack_version', 'refresh_ftrack'))
        self.ui.ftrack_note_pattern.textChanged.connect(
            partial(self._handler_later, 'ftrack_note_pattern', 'select_ftrack'))
        self.ui.ftrack_note_repl.textChanged.connect(
            partial(self._handler_later, 'ftrack_note_repl', 'select_ftrack'))
        self.ui.ftrack_do_op.clicked.connect(
            partial(self.handler, 'ftrack_do_op', 'refresh_ftrack'))
        # Query Notes was never connected: toggling it did nothing until a re-read
        self.ui.ftrack_do_notes.clicked.connect(
            partial(self.handler, 'ftrack_do_notes', 'refresh_ftrack'))
        self.ui.ftrack_export.clicked.connect(
            partial(self.handler, 'ftrack_export', 'ftrack_export'))

        # vendor
        self.ui.vendor_csv_path.textChanged.connect(
            partial(self._handler_later, 'vendor_csv_path', 'refresh_vendor'))
        self.ui.vendor_csv_explore.clicked.connect(
            partial(self.explore_line_edit, self.ui.vendor_csv_path))
        self.ui.vendor_csv_browse.clicked.connect(
            partial(self.browse_line_edit, self.ui.vendor_csv_path, 'csv', "Select Vendor CSV"))

        self.ui.vendor_csv_package_key.textChanged.connect(
            partial(self._handler_later, 'vendor_csv_package_key', 'refresh_vendor'))
        self.ui.vendor_csv_vendor_key.textChanged.connect(
            partial(self._handler_later, 'vendor_csv_vendor_key', 'refresh_vendor'))

        self.ui.vendor_csv_ignore.clicked.connect(
            partial(self.handler, 'vendor_csv_ignore', 'refresh_vendor'))
        self.ui.vendor_csv_ftrack.clicked.connect(
            partial(self.handler, 'vendor_csv_ftrack', 'refresh_vendor'))
        self.ui.vendor_csv_skip.clicked.connect(
            partial(self.handler, 'vendor_csv_skip', 'refresh_vendor'))
        self.ui.vendor_csv_skip_by.textChanged.connect(
            partial(self._handler_later, 'vendor_csv_skip_by', 'refresh_vendor'))
        self.ui.vendor_csv_skip_what.textChanged.connect(
            partial(self._handler_later, 'vendor_csv_skip_what', 'refresh_vendor'))

        self.ui.vendor_csv_prefs_spreadsheet.textChanged.connect(
            partial(self._handler_later, 'vendor_csv_prefs_spreadsheet',
                    'refresh_vendor'))
        self.ui.vendor_csv_prefs_repres.textChanged.connect(
            partial(self._handler_later, 'vendor_csv_prefs_repres',
                    'refresh_vendor'))

        # Convert
        # copy files button
        self.ui.thumbs_convert_now.clicked.connect(
            partial(self.handler, 'thumbs_convert_now', 'thumbs_convert_now'))

        # Spreadsheet
        self.ui.sub_columns.textChanged.connect(
            partial(self._handler_later, 'sub_columns', 'refresh_spreadsheets'))
        self.ui.sub_exclude.textChanged.connect(
            partial(self._handler_later, 'sub_exclude', 'refresh_spreadsheets'))
        self.ui.sub_include.textChanged.connect(
            partial(self._handler_later, 'sub_include', 'refresh_spreadsheets'))

        self.ui.log_columns.textChanged.connect(
            partial(self._handler_later, 'log_columns', 'refresh_spreadsheets'))
        self.ui.log_exclude.textChanged.connect(
            partial(self._handler_later, 'log_exclude', 'refresh_spreadsheets'))
        self.ui.log_include.textChanged.connect(
            partial(self._handler_later, 'log_include', 'refresh_spreadsheets'))

        self.ui.txt_columns.textChanged.connect(
            partial(self._handler_later, 'txt_columns', 'refresh_spreadsheets'))
        self.ui.txt_exclude.textChanged.connect(
            partial(self._handler_later, 'txt_exclude', 'refresh_spreadsheets'))
        self.ui.txt_include.textChanged.connect(
            partial(self._handler_later, 'txt_include', 'refresh_spreadsheets'))

        # Checks Tab
        # the size checks need the sizes read again
        self.ui.check_sequence_size_consistency.clicked.connect(
            partial(self.handler,
                    'check_sequence_size_consistency', 'refresh_size_checks'))
        self.ui.check_sequence_holes.clicked.connect(
            partial(self.handler, 'check_sequence_holes', 'refresh_size_checks'))

        self.ui.check_if_01.textChanged.connect(
            partial(self._handler_later, 'check_if_01', 'refresh_checks'))
        self.ui.check_check_01.textChanged.connect(
            partial(self._handler_later, 'check_check_01', 'refresh_checks'))
        self.ui.check_warning_01.clicked.connect(
            partial(self.handler, 'check_warning_01', 'refresh_checks'))
        self.ui.check_error_01.clicked.connect(
            partial(self.handler, 'check_error_01', 'refresh_checks'))
        self.ui.check_message_01.textChanged.connect(
            partial(self._handler_later, 'check_message_01', 'refresh_checks'))

        self.ui.check_if_02.textChanged.connect(
            partial(self._handler_later, 'check_if_02', 'refresh_checks'))
        self.ui.check_check_02.textChanged.connect(
            partial(self._handler_later, 'check_check_02', 'refresh_checks'))
        self.ui.check_warning_02.clicked.connect(
            partial(self.handler, 'check_warning_02', 'refresh_checks'))
        self.ui.check_error_02.clicked.connect(
            partial(self.handler, 'check_error_02', 'refresh_checks'))
        self.ui.check_message_02.textChanged.connect(
            partial(self._handler_later, 'check_message_02', 'refresh_checks'))

        self.ui.check_if_03.textChanged.connect(
            partial(self._handler_later, 'check_if_03', 'refresh_checks'))
        self.ui.check_check_03.textChanged.connect(
            partial(self._handler_later, 'check_check_03', 'refresh_checks'))
        self.ui.check_warning_03.clicked.connect(
            partial(self.handler, 'check_warning_03', 'refresh_checks'))
        self.ui.check_error_03.clicked.connect(
            partial(self.handler, 'check_error_03', 'refresh_checks'))
        self.ui.check_message_03.textChanged.connect(
            partial(self._handler_later, 'check_message_03', 'refresh_checks'))

        self.ui.check_if_04.textChanged.connect(
            partial(self._handler_later, 'check_if_04', 'refresh_checks'))
        self.ui.check_check_04.textChanged.connect(
            partial(self._handler_later, 'check_check_04', 'refresh_checks'))
        self.ui.check_warning_04.clicked.connect(
            partial(self.handler, 'check_warning_04', 'refresh_checks'))
        self.ui.check_error_04.clicked.connect(
            partial(self.handler, 'check_error_04', 'refresh_checks'))
        self.ui.check_message_04.textChanged.connect(
            partial(self._handler_later, 'check_message_04', 'refresh_checks'))

        self.ui.check_if_05.textChanged.connect(
            partial(self._handler_later, 'check_if_05', 'refresh_checks'))
        self.ui.check_check_05.textChanged.connect(
            partial(self._handler_later, 'check_check_05', 'refresh_checks'))
        self.ui.check_warning_05.clicked.connect(
            partial(self.handler, 'check_warning_05', 'refresh_checks'))
        self.ui.check_error_05.clicked.connect(
            partial(self.handler, 'check_error_05', 'refresh_checks'))
        self.ui.check_message_05.textChanged.connect(
            partial(self._handler_later, 'check_message_05', 'refresh_checks'))

        self.ui.check_if_06.textChanged.connect(
            partial(self._handler_later, 'check_if_06', 'refresh_checks'))
        self.ui.check_check_06.textChanged.connect(
            partial(self._handler_later, 'check_check_06', 'refresh_checks'))
        self.ui.check_warning_06.clicked.connect(
            partial(self.handler, 'check_warning_06', 'refresh_checks'))
        self.ui.check_error_06.clicked.connect(
            partial(self.handler, 'check_error_06', 'refresh_checks'))
        self.ui.check_message_06.textChanged.connect(
            partial(self._handler_later, 'check_message_06', 'refresh_checks'))

        self.ui.check_if_07.textChanged.connect(
            partial(self._handler_later, 'check_if_07', 'refresh_checks'))
        self.ui.check_check_07.textChanged.connect(
            partial(self._handler_later, 'check_check_07', 'refresh_checks'))
        self.ui.check_warning_07.clicked.connect(
            partial(self.handler, 'check_warning_07', 'refresh_checks'))
        self.ui.check_error_07.clicked.connect(
            partial(self.handler, 'check_error_07', 'refresh_checks'))
        self.ui.check_message_07.textChanged.connect(
            partial(self._handler_later, 'check_message_07', 'refresh_checks'))

        self.ui.check_if_08.textChanged.connect(
            partial(self._handler_later, 'check_if_08', 'refresh_checks'))
        self.ui.check_check_08.textChanged.connect(
            partial(self._handler_later, 'check_check_08', 'refresh_checks'))
        self.ui.check_warning_08.clicked.connect(
            partial(self.handler, 'check_warning_08', 'refresh_checks'))
        self.ui.check_error_08.clicked.connect(
            partial(self.handler, 'check_error_08', 'refresh_checks'))
        self.ui.check_message_08.textChanged.connect(
            partial(self._handler_later, 'check_message_08', 'refresh_checks'))

        self.ui.check_if_09.textChanged.connect(
            partial(self._handler_later, 'check_if_09', 'refresh_checks'))
        self.ui.check_check_09.textChanged.connect(
            partial(self._handler_later, 'check_check_09', 'refresh_checks'))
        self.ui.check_warning_09.clicked.connect(
            partial(self.handler, 'check_warning_09', 'refresh_checks'))
        self.ui.check_error_09.clicked.connect(
            partial(self.handler, 'check_error_09', 'refresh_checks'))
        self.ui.check_message_09.textChanged.connect(
            partial(self._handler_later, 'check_message_09', 'refresh_checks'))

        self.ui.check_if_10.textChanged.connect(
            partial(self._handler_later, 'check_if_10', 'refresh_checks'))
        self.ui.check_check_10.textChanged.connect(
            partial(self._handler_later, 'check_check_10', 'refresh_checks'))
        self.ui.check_warning_10.clicked.connect(
            partial(self.handler, 'check_warning_10', 'refresh_checks'))
        self.ui.check_error_10.clicked.connect(
            partial(self.handler, 'check_error_10', 'refresh_checks'))
        self.ui.check_message_10.textChanged.connect(
            partial(self._handler_later, 'check_message_10', 'refresh_checks'))

        self.ui.check_if_11.textChanged.connect(
            partial(self._handler_later, 'check_if_11', 'refresh_checks'))
        self.ui.check_check_11.textChanged.connect(
            partial(self._handler_later, 'check_check_11', 'refresh_checks'))
        self.ui.check_warning_11.clicked.connect(
            partial(self.handler, 'check_warning_11', 'refresh_checks'))
        self.ui.check_error_11.clicked.connect(
            partial(self.handler, 'check_error_11', 'refresh_checks'))
        self.ui.check_message_11.textChanged.connect(
            partial(self._handler_later, 'check_message_11', 'refresh_checks'))

        self.ui.check_if_12.textChanged.connect(
            partial(self._handler_later, 'check_if_12', 'refresh_checks'))
        self.ui.check_check_12.textChanged.connect(
            partial(self._handler_later, 'check_check_12', 'refresh_checks'))
        self.ui.check_warning_12.clicked.connect(
            partial(self.handler, 'check_warning_12', 'refresh_checks'))
        self.ui.check_error_12.clicked.connect(
            partial(self.handler, 'check_error_12', 'refresh_checks'))
        self.ui.check_message_12.textChanged.connect(
            partial(self._handler_later, 'check_message_12', 'refresh_checks'))

        self.ui.check_if_13.textChanged.connect(
            partial(self._handler_later, 'check_if_13', 'refresh_checks'))
        self.ui.check_check_13.textChanged.connect(
            partial(self._handler_later, 'check_check_13', 'refresh_checks'))
        self.ui.check_warning_13.clicked.connect(
            partial(self.handler, 'check_warning_13', 'refresh_checks'))
        self.ui.check_error_13.clicked.connect(
            partial(self.handler, 'check_error_13', 'refresh_checks'))
        self.ui.check_message_13.textChanged.connect(
            partial(self._handler_later, 'check_message_13', 'refresh_checks'))

        # check rows 14-21 (rows 1-13 are connected one by one above)
        for _row in range(14, 22):
            for _field, _signal in (('if', 'textChanged'), ('check', 'textChanged'),
                                    ('message', 'textChanged'), ('warning', 'clicked'),
                                    ('error', 'clicked')):
                _name = f"check_{_field}_{_row:02d}"
                getattr(getattr(self.ui, _name), _signal).connect(
                    partial(self._handler_later if _signal == 'textChanged' else self.handler,
                            _name, 'refresh_checks'))

        # Package name: Version Regex
        self.ui.name_version_regex.textChanged.connect(
            partial(self._handler_later, 'name_version_regex', 'package_rename'))

        # Data tab: Column Prefix and the match rules
        self.ui.name_date_prefix.textChanged.connect(
            partial(self._handler_later, 'name_date_prefix', 'refresh_data_csv'))
        for _n in (1, 2, 3):
            for _name in (f"data_package{_n}", f"data_data{_n}"):
                getattr(self.ui, _name).textChanged.connect(
                    partial(self._handler_later, _name, 'refresh_data_csv'))
            getattr(self.ui, f"data_package{_n}_chbx").clicked.connect(
                partial(self.handler, f"data_package{_n}_chbx", 'refresh_data_csv'))

        # Grouping tab (replaces Merge By): typed text refreshes after a pause
        self.grouping_tab.changed_later.connect(
            lambda key: self._handler_later(key, 'refresh_grouping'))
        self.grouping_tab.changed_now.connect(
            lambda key: self.handler(key, 'refresh_grouping'))
        self.ui.preset_mod_grouping.clicked.connect(
            partial(self.handler, 'preset_mod_grouping', 'tab_pairs'))

        # Convert rows: the convert_pathNN keys in the spreadsheets
        for _row in range(1, 9):
            for _field in ('if', 'exe', 'args', 'name'):
                _name = f"thumbs_{_field}_{_row:02d}"
                getattr(self.ui, _name).textChanged.connect(
                    partial(self._handler_later, _name, 'refresh_spreadsheets'))



        # Preferences Tab

        self.ui.prefs_size_scan.clicked.connect(
            partial(self.handler, 'prefs_size_scan', 'refresh_size_checks'))
        self.ui.prefs_size_ignore_first.valueChanged.connect(
            partial(self.handler, 'prefs_size_ignore_first', 'refresh_size_checks'))
        self.ui.prefs_size_neighborhood.valueChanged.connect(
            partial(self.handler, 'prefs_size_neighborhood', 'refresh_size_checks'))
        self.ui.prefs_size_threshold.valueChanged.connect(
            partial(self.handler, 'prefs_size_threshold', 'refresh_size_checks'))

        self.ui.prefs_tc_from_meta.clicked.connect(
            partial(self.handler, 'prefs_tc_from_meta', 'refresh_parsing'))
        self.ui.prefs_tc_from_counter.clicked.connect(
            partial(self.handler, 'prefs_tc_from_counter', 'refresh_parsing'))
        self.ui.prefs_tc_default.textChanged.connect(
            partial(self._handler_later, 'prefs_tc_default', 'refresh_parsing'))

        self.ui.prefs_counter_start.valueChanged.connect(
            partial(self.handler, 'prefs_counter_start', 'refresh_parsing'))
        self.ui.prefs_counter_step.valueChanged.connect(
            partial(self.handler, 'prefs_counter_step', 'refresh_parsing'))
        self.ui.prefs_counter_zeroes.valueChanged.connect(
            partial(self.handler, 'prefs_counter_zeroes', 'refresh_parsing'))


        # Exports Tab
        self.ui.export_sub_excel.clicked.connect(
            partial(self.handler, 'export_sub_excel', 'refresh_export_prep'))
        self.ui.export_sub_csv.clicked.connect(
            partial(self.handler, 'export_sub_csv', 'refresh_export_prep'))
        self.ui.export_sub_root.clicked.connect(
            partial(self.handler, 'export_sub_root', 'refresh_export_prep'))
        self.ui.export_sub_above.clicked.connect(
            partial(self.handler, 'export_sub_above', 'refresh_export_prep'))
        self.ui.export_sub_custom.clicked.connect(
            partial(self.handler, 'export_sub_custom', 'refresh_export_prep'))
        self.ui.export_sub_custom_path.textChanged.connect(
            partial(self._handler_later,
                    'export_sub_custom_path', 'refresh_export_prep'))

        self.ui.export_log_excel.clicked.connect(
            partial(self.handler, 'export_log_excel', 'refresh_export_prep'))
        self.ui.export_log_csv.clicked.connect(
            partial(self.handler, 'export_log_csv', 'refresh_export_prep'))
        self.ui.export_log_root.clicked.connect(
            partial(self.handler, 'export_log_root', 'refresh_export_prep'))
        self.ui.export_log_above.clicked.connect(
            partial(self.handler, 'export_log_above', 'refresh_export_prep'))
        self.ui.export_log_custom.clicked.connect(
            partial(self.handler, 'export_log_custom', 'refresh_export_prep'))
        self.ui.export_log_custom_path.textChanged.connect(
            partial(self._handler_later,
                    'export_log_custom_path', 'refresh_export_prep'))

        # Text Tab
        self.ui.text_txt.clicked.connect(
            partial(self.handler, 'text_txt', 'refresh_text'))
        self.ui.text_root.clicked.connect(
            partial(self.handler, 'text_root', 'refresh_text'))
        self.ui.text_above.clicked.connect(
            partial(self.handler, 'text_above', 'refresh_text'))
        self.ui.text_custom.clicked.connect(
            partial(self.handler, 'text_custom', 'refresh_text'))
        self.ui.text_custom_path.textChanged.connect(
            partial(self._handler_later, 'text_custom_path', 'refresh_text'))

        self.ui.text_add_titles.clicked.connect(
            partial(self.handler, 'text_add_titles', 'refresh_text'))
        self.ui.text_sep_tab.clicked.connect(
            partial(self.handler, 'text_sep_tab', 'refresh_text'))
        self.ui.text_sep_fixed.clicked.connect(
            partial(self.handler, 'text_sep_fixed', 'refresh_text'))

        self.ui.text_header.textChanged.connect(
            partial(self._handler_later, 'text_header', 'refresh_text'))
        self.ui.text_footer.textChanged.connect(
            partial(self._handler_later, 'text_footer', 'refresh_text'))

        # Presets Tab
        self.ui.load_preset_button.clicked.connect(
            partial(self.handler, 'load_preset_button', 'load_preset'))
        self.ui.save_preset_name.textChanged.connect(
            partial(self._handler_later, 'save_preset_text', 'save_presets'))
        self.ui.save_preset_button.clicked.connect(
            partial(self.handler, 'save_preset_button', 'save_presets'))
        self.ui.preset_explore.clicked.connect(
            partial(self.handler, 'preset_explore', 'preset_explore'))

        self.ui.preset_mod_package.clicked.connect(
            partial(self.handler, 'preset_mod_package', 'tab_pairs'))
        self.ui.preset_mod_parsing.clicked.connect(
            partial(self.handler, 'preset_mod_parsing', 'tab_pairs'))
        self.ui.preset_mod_sidecar.clicked.connect(
            partial(self.handler, 'preset_mod_sidecar', 'tab_pairs'))
        self.ui.preset_mod_rename.clicked.connect(
            partial(self.handler, 'preset_mod_rename', 'tab_pairs'))
        self.ui.preset_mod_data.clicked.connect(
            partial(self.handler, 'preset_mod_data', 'tab_pairs'))
        self.ui.preset_mod_ftrack.clicked.connect(
            partial(self.handler, 'preset_mod_ftrack', 'tab_pairs'))
        self.ui.preset_mod_vendor.clicked.connect(
            partial(self.handler, 'preset_mod_vendor', 'tab_pairs'))
        self.ui.preset_mod_replace.clicked.connect(
            partial(self.handler, 'preset_mod_replace', 'tab_pairs'))
        self.ui.preset_mod_convert.clicked.connect(
            partial(self.handler, 'preset_mod_convert', 'tab_pairs'))
        self.ui.preset_mod_spreadsheet.clicked.connect(
            partial(self.handler, 'preset_mod_spreadsheet', 'tab_pairs'))
        self.ui.preset_mod_text.clicked.connect(
            partial(self.handler, 'preset_mod_text', 'tab_pairs'))
        self.ui.preset_mod_checks.clicked.connect(
            partial(self.handler, 'preset_mod_checks', 'tab_pairs'))
        self.ui.preset_mod_publish.clicked.connect(
            partial(self.handler, 'preset_mod_publish', 'tab_pairs'))
        self.ui.preset_mod_ayon.clicked.connect(
            partial(self.handler, 'preset_mod_ayon', 'tab_pairs'))
        self.ui.preset_mod_preferences.clicked.connect(
            partial(self.handler, 'preset_mod_preferences', 'tab_pairs'))
        self.ui.preset_mod_exports.clicked.connect(
            partial(self.handler, 'preset_mod_exports', 'tab_pairs'))
        self.ui.preset_mod_log.clicked.connect(
            partial(self.handler, 'preset_mod_log', 'tab_pairs'))
        self.ui.preset_mod_help.clicked.connect(
            partial(self.handler, 'preset_mod_help', 'tab_pairs'))

        self.ui.preset_mod_submission.clicked.connect(
            partial(self.handler, 'preset_mod_submission', 'tab_pairs'))
        self.ui.preset_mod_drivelog.clicked.connect(
            partial(self.handler, 'preset_mod_drivelog', 'tab_pairs'))
        self.ui.preset_mod_inspector.clicked.connect(
            partial(self.handler, 'preset_mod_inspector', 'tab_pairs'))
        self.ui.preset_mod_files.clicked.connect(
            partial(self.handler, 'preset_mod_files', 'tab_pairs'))

        # Data Tab
        self.ui.tree_filter_file.textChanged.connect(
            partial(self._handler_later, 'tree_filter_file', 'data_filter'))
        self.ui.tree_filter_key.textChanged.connect(
            partial(self._handler_later, 'tree_filter_key', 'data_filter'))
        self.ui.tree_filter_value.textChanged.connect(
            partial(self._handler_later, 'tree_filter_value', 'data_filter'))


        # Ayon Tab
        self.ui.ayon_project.textChanged.connect(
            partial(self._handler_later, 'ayon_project', 'ayon_changed'))
        self.ui.ayon_prefix.textChanged.connect(
            partial(self._handler_later, 'ayon_prefix', 'ayon_rematch'))
        self.ui.ayon_output_folder.textChanged.connect(
            partial(self._handler_later, 'ayon_output_folder', 'ayon_changed'))
        self.ui.ayon_path_browse_2.clicked.connect(
            partial(self.browse_line_edit, self.ui.ayon_output_folder, 'dir', "Select Ayon List Output Folder"))

        # Data CSV (Data tab)
        self.ui.data_csv_browse.clicked.connect(self.browse_data_csv)
        self.ui.data_csv_path.textChanged.connect(
            partial(self._handler_later, 'data_csv_path', 'refresh_data_csv'))
        self.ui.data_csv_latest.clicked.connect(
            partial(self.handler, 'data_csv_latest', 'refresh_data_csv'))
        self.ui.data_enable.clicked.connect(
            partial(self.handler, 'data_enable', 'refresh_data_csv'))
        self.ui.data_filter_matched.clicked.connect(
            partial(self.handler, 'data_filter_matched', 'data_matched_filter'))

        # Search and Replace CSV
        self.ui.data_csv_browse_2.clicked.connect(
            partial(self.browse_line_edit, self.ui.replace_csv_path, 'csv', "Select Search and Replace CSV"))
        self.ui.replace_csv_path.textChanged.connect(
            partial(self._handler_later, 'replace_csv_path', 'refresh_replace_csv'))
        self.ui.replace_enable.clicked.connect(
            partial(self.handler, 'replace_enable', 'refresh_replace_csv'))
        self.ui.replace_button.clicked.connect(
            partial(self.handler, 'replace_button', 'replace_apply'))

        self.ui.ayon_do_shotlist.clicked.connect(
            partial(self.handler, 'ayon_do_shotlist', 'ayon_changed'))
        self.ui.ayon_export_csv.clicked.connect(
            partial(self.handler, 'ayon_export_csv', 'ayon_changed'))
        self.ui.ayon_export_excel.clicked.connect(
            partial(self.handler, 'ayon_export_excel', 'ayon_changed'))
        self.ui.ayon_thumbnails.clicked.connect(
            partial(self.handler, 'ayon_thumbnails', 'ayon_changed'))

        self.ui.ayon_filter_assets.clicked.connect(
            partial(self.handler, 'ayon_filter_assets', 'ayon_changed_filter'))
        self.ui.ayon_filter_shots.clicked.connect(
            partial(self.handler, 'ayon_filter_shots', 'ayon_changed_filter'))
        self.ui.ayon_filter_tasks.clicked.connect(
            partial(self.handler, 'ayon_filter_tasks', 'ayon_changed_filter'))
        self.ui.ayon_filter_other.clicked.connect(
            partial(self.handler, 'ayon_filter_other', 'ayon_changed_filter'))
        self.ui.ayon_filter_matched.clicked.connect(
            partial(self.handler, 'ayon_filter_matched', 'ayon_changed_filter'))
        self.ui.ayon_filter_tasktype_chbx.clicked.connect(
            partial(self.handler, 'ayon_filter_tasktype_chbx', 'ayon_changed_filter'))
        self.ui.ayon_filter_assignee_chbx.clicked.connect(
            partial(self.handler, 'ayon_filter_assignee_chbx', 'ayon_changed_filter'))
        self.ui.ayon_filter_tasktypes.textChanged.connect(
            partial(self._handler_later, 'ayon_filter_tasktypes', 'ayon_changed_filter'))
        self.ui.ayon_filter_taskname_chbx.clicked.connect(
            partial(self.handler, 'ayon_filter_taskname_chbx', 'ayon_changed_filter'))
        self.ui.ayon_filter_tasknames.textChanged.connect(
            partial(self._handler_later, 'ayon_filter_tasknames', 'ayon_changed_filter'))
        self.ui.ayon_filter_assignees.textChanged.connect(
            partial(self._handler_later, 'ayon_filter_assignees', 'ayon_changed_filter'))

        self.ui.ayon_package1_chbx.clicked.connect(
            partial(self.handler, 'ayon_package1_chbx', 'ayon_rematch'))
        self.ui.ayon_package2_chbx.clicked.connect(
            partial(self.handler, 'ayon_package2_chbx', 'ayon_rematch'))
        self.ui.ayon_package3_chbx.clicked.connect(
            partial(self.handler, 'ayon_package3_chbx', 'ayon_rematch'))
        self.ui.ayon_package1.textChanged.connect(
            partial(self._handler_later, 'ayon_package1',
                    'ayon_rematch'))
        self.ui.ayon_list1.textChanged.connect(
            partial(self._handler_later, 'ayon_list1',
                    'ayon_rematch'))
        self.ui.ayon_package2.textChanged.connect(
            partial(self._handler_later, 'ayon_package2',
                    'ayon_rematch'))
        self.ui.ayon_list2.textChanged.connect(
            partial(self._handler_later, 'ayon_list2',
                    'ayon_rematch'))
        self.ui.ayon_package3.textChanged.connect(
            partial(self._handler_later, 'ayon_package3',
                    'ayon_rematch'))
        self.ui.ayon_list3.textChanged.connect(
            partial(self._handler_later, 'ayon_list3',
                    'ayon_rematch'))
        self.ui.ayon_export_butt.clicked.connect(
            partial(self.handler, 'ayon_export_butt', 'ayon_export_butt'))
        self.ui.ayon_scan_butt.clicked.connect(
            partial(self.handler, 'ayon_scan_butt', 'ayon_scan'))
        self.ui.ayon_record_butt.clicked.connect(
            partial(self.handler, 'ayon_record_butt', 'ayon_record'))
        self.ui.ayon_versions_matched_only.clicked.connect(
            partial(self.handler, 'ayon_versions_matched_only', 'ayon_changed_filter'))
        # Match version uses the cached Matched Versions: no Ayon query, just refresh
        self.ui.ayon_version_match_chbx.clicked.connect(
            partial(self.handler, 'ayon_version_match_chbx', 'refresh_spreadsheets'))
        self.ui.ayon_version_match_pkg.textChanged.connect(
            partial(self._handler_later, 'ayon_version_match_pkg', 'refresh_spreadsheets'))
        self.ui.ayon_version_match_data.textChanged.connect(
            partial(self._handler_later, 'ayon_version_match_data', 'refresh_spreadsheets'))

        # preset name is empty, disable save button
        #self.ui.save_preset_button.setEnabled(False)

        # GO button
        self.ui.write_button.clicked.connect(
            partial(self.handler, 'write_button', 'write'))

        # FARM button
        self.ui.publish_farm_button.clicked.connect(
            partial(self.handler, 'publish_farm_button', 'publish'))

        # Publish Ayon LOCAL
        self.ui.publish_local_button.clicked.connect(
            partial(self.handler, 'publish_local_button', 'publish'))

        # For Headless operation, just run what is needed in init
        if self.no_gui and self.package_path is not None:
            self.settings_update("package_folder", self.ui.package_folder,
                                 value=os.path.dirname(self.package_path).replace('\\', '/'))
            if self.package_path.lower().endswith('.csv'):
                if bool(self.settings.get('vendor_csv_path_detect', {}).get('value', False)):
                    self.settings_update("vendor_csv_path",
                                         self.ui.vendor_csv_path,
                                         value=self.package_path)

            # get args
            #args

            self.data = Sequencer(self.package_path, sequence_mode='holes_allowed',
                                  gui=self.settings,
                                  more_settings=self.settings_obj, ui=self.ui, headless=self.no_gui)
            # the --actions string (default "ftg") already ran inside Sequencer,
            # including export ("g"), so don't export a second time here
            _c = sh_logging.LOG_BUFFER.counts
            self.log.info(f"Headless run finished: {_c.get('error', 0)} error(s), "
                          f"{_c.get('warning', 0)} warning(s).")
            # exit properly after headless go
            sys.exit()

    def handler(self, sender, group, *more):
        """

        """
        # every keystroke lands here: TRACE, so it doesn't flood the log buffer
        log.log(sh_logging.TRACE, "-> handler sender: {}, group: {}".format(
            str(sender), str(group)))

        # this refresh runs now with the current values: a deferred one of
        # the same kind would only repeat it
        self._cancel_later(group)

        # refresh self.settings
        self.settings_from_gui()

        # update settings from gui
        if self.data is not None:
            self.data.settings = self.settings

        if group == 'browse':
            if sender == 'package_browse':
                pth_to_browse = str(self.settings['package_folder']['value']).replace('\\', '/')
                browsed = self.browse(start_path=pth_to_browse)
                if browsed is not None:
                    self.settings_update("package_folder", self.ui.package_folder, value=browsed)
                    group = 'source_change'

        if group == 'source_change':
            pth = str(self.settings['package_folder']['value']).replace('\\', '/')
            if os.path.isfile(pth):
                self.settings_update("package_folder", self.ui.package_folder,
                                     value=os.path.dirname(pth).replace('\\', '/'))
                if pth.endswith('.csv'):
                    if bool(self.settings['vendor_csv_path_detect']['value']):
                        self.settings_update("vendor_csv_path",
                                             self.ui.vendor_csv_path,
                                             value=pth)
            self.data = Sequencer(pth, sequence_mode='holes_allowed', gui=self.settings, more_settings=self.settings_obj, ui=self.ui, headless=self.no_gui)
            self.show_all()

        if sender == 'name_rename':
            if self.data:
                pth = self.data.static_keywords['package_name_root'] + '/'
                dst = self.data.static_keywords['package_name']
                renamed = (pth + dst).replace('\\', '/')
                self.data.manual_rename()
                if os.path.isdir(renamed):
                    # signals blocked: the text change would scan the folder
                    # again (it was scanned three times after a rename)
                    self.ui.package_folder.blockSignals(True)
                    self.ui.package_folder.setText(renamed)
                    self.ui.package_folder.blockSignals(False)
                    self.settings_from_gui()
                    self.data = Sequencer(renamed, sequence_mode='holes_allowed',
                                          gui=self.settings,
                                          more_settings=self.settings_obj, ui=self.ui, headless=self.no_gui)
                    self.show_all()
                    return

        if group == 'package_rename':
            if self.data:
                self.data.transform_data()
                self.show_all()

        if group == 'refresh_parsing':
            if self.data:
                self.data.transform_data()
                self.show_all()

        if group == 'refresh_spreadsheets':
            if self.data:
                self.data.transform_data()
                self.show_all()

        if group == 'refresh_spreadsheets_age':
            if self.data:
                self.data.filter_items_add_counters()
                self.data.prepare_all_columns()
                self.data.prepare_tables()
                self.show_all()

        if group == 'refresh_age':
            if self.data:
                self.data.prepare_all_columns()
                self.data.prepare_tables()
                self.show_all()

        if group == 'refresh_text':
            if self.data:
                self.data.transform_data()
                self.show_all()

        if group == 'refresh_checks':
            if self.data:
                self.data.transform_data()
                self.show_all()

        if group == 'refresh_size_checks':
            if self.data:
                #self.data.clear_errors()
                self.data.get_file_sizes()
                self.data.transform_data()
                self.show_all()

        if group == 'refresh_side_files':
            if self.data:
                self.data.sidecar_files_find()
                # sidecar files filter
                self.data.sidecar_files_filter()
                # parse table headers
                self.data.prepare_all_columns()
                # fill tables for export and display
                self.data.prepare_tables()
                self.show_all()

        if group == 'refresh_side':
            if self.data:
                # sidecar files filter
                self.data.sidecar_files_filter()
                # parse table headers
                self.data.prepare_all_columns()
                # fill tables for export and display
                self.data.prepare_tables()
                self.show_all()

        if group == 'refresh_rename':
            if self.data:
                self.data.rename_prepare()
                self.data.rename_preprocess()
                # fill tables for export and display
                self.data.prepare_tables()
                self.show_all()

        if group == 'refresh_ftrack':
            if self.data:
                self._ayon_busy(self.data.ftrack_query, "Reading data from Ftrack...")
                self.data.select_ftrack_note()
                self.data.display_ftrack_table()
                self.data.prepare_all_columns()
                self.data.prepare_tables()
                self.show_all()
            else:
                log.debug("Ftrack: load a package first, the ftrack tab queries the loaded files")

        if group == 'select_ftrack':
            # Skipping ftrack queries for speed
            if self.data:
                self.data.select_ftrack_note()
                self.data.display_ftrack_table()
                self.data.prepare_all_columns()
                self.data.prepare_tables()
                self.show_all()

        if group == 'refresh_grouping':
            if self.data:
                # group tokens for the checks, then the tables (grouped again
                # with the check results)
                self.data.group_items()
                self.data.run_checks()
                self.data.prepare_all_columns()
                self.data.prepare_tables()
                self.show_all()

        if group == 'refresh_vendor':
            if self.data:
                # transform_data reads the vendor csv and builds the tables
                # (the vendor csv was processed three times per edit)
                self.data.transform_data()
                self.show_all()

        if group == 'refresh_data_csv':
            if self.data:
                self.data.csv_data = []
                self.data.csv_data_read()
                self.data.transform_data()
                self.show_all()

        if group == 'refresh_replace_csv':
            if self.data:
                self.data.replace_data = []
                self.data.csv_replace_data_read()
                self.data.csv_replace_prepare()
                self.data.display_replace_table()

        if group == 'publish':
            if self.data and self.data.column_titles_sub:
                if sender == 'publish_farm_button':
                    self.data.publish_ayon(mode="farm")
                elif sender == 'publish_local_button':
                    self.data.publish_ayon(mode="local")

        if sender == 'side_copy':
            if self.data:
                # sidecar files filter
                self.data.sidecar_files_copy()

        if sender == 'Rename_go':
            if self.data:
                self.data.rename_execute()
                if bool(self.settings.get('rename_reload_after', {}).get('value')):
                    # read the renamed files again
                    self._reload_package()

        if sender == 'write_button':
            # read column widths from tablewidget for excel column sizes
            # there is no way to change excel column sizes by content
            # Go also works with no Submission columns: the Drive Log, text,
            # sidecars, converts and rename don't need them
            if self.data:
                column_widths_sub = [
                    float(self.ui.sub_table.columnWidth(column_number))
                    for column_number, _ in enumerate(self.data.column_titles_sub or [])]
                column_widths_log = [
                    float(self.ui.log_table.columnWidth(column_number))
                    for column_number, _ in enumerate(self.data.column_titles_log or [])]

                self.data.export_all(column_widths_sub, column_widths_log)

        if group == 'ftrack_export':
            target = self._ayon_target()
            self._ayon_busy(target.ftrack_export, "Exporting Ftrack shot list...")

        if sender == 'ayon_export_butt':
            target = self._ayon_target()

            self._ayon_busy(target.ayon_export, "Exporting Ayon shot list...")
            if target is self.data and self.data.merged_list:
                # a first read also matches files: refresh the spreadsheets
                self.data.prepare_all_columns()
                self.data.prepare_tables()
                self.show_all()

        if group == 'ayon_scan':
            target = self._ayon_target()
            self._ayon_busy(target.ayon_scan, "Scanning Ayon...")
            if target is self.data and self.data.merged_list:
                self.data.prepare_all_columns()
                self.data.prepare_tables()
                self.show_all()

        if group == 'replace_apply':
            if self.data is None or not self.data.merged_list:
                self.log.error("Search and Replace: load a package first.")
            else:
                self._ayon_busy(self.data.replace_execute, "Replacing in text files...")

        if group == 'ayon_record':
            if self.data is None or not self.data.merged_list:
                self.log.error("Record package: load a package first.")
            else:
                self._ayon_busy(self.data.ayon_record_packages, "Recording package to Ayon...")

        if sender == 'preset_explore':
            self.expore_local_presets()

        if sender == 'package_explore':
            self.expore_package()

        if group == 'save_presets':
            preset_name = str(self.ui.save_preset_name.displayText())
            if preset_name is not None and preset_name != '':
                    #self.ui.save_preset_button.setEnabled(True)
                    if sender == 'save_preset_button':
                        try:
                            self.settings_from_gui()
                            self.settings_obj.settings = self.settings
                            self.settings_obj.write(preset_name)

                            self.settings_update_app_title()
                            self.settings_update_dropbox()
                        except Exception as e:
                            log.error('Error saving preset {}: {}'.format(preset_name, e))
            else:
                #self.ui.save_preset_button.setEnabled(False)
                pass

        if group == 'load_preset':
            preset_to_load = ''
            """
            try:
            """
            index = int(self.ui.load_preset_combobox.currentIndex())
            if index < 0 or index >= len(self.settings_obj.preset_names):
                log.warning("No preset selected to load.")
                return
            preset_to_load = str(self.settings_obj.preset_names[index])

            self.settings_obj.read(preset_to_load)
            self.settings = self.settings_obj.settings
            self.settings_to_gui()
            if self.log_view is not None:
                self.log_view.rerender()
            self.settings_update_app_title()
            self.settings_update_dropbox()
            self.gui_show_hide_modules()
            self.settings_update("save_preset_name",
                                 self.ui.save_preset_name,
                                 value=preset_to_load)
            # edits made before the load are superseded by the preset
            self._cancel_later()
            # the tables were cleared: build them again with the new preset,
            # so Go doesn't export the data of the previous one
            if self.data is not None:
                self._reload_package()
            """
            except Exception:
                log.error('Error reading preset {}'.format(preset_to_load))
            """

        if group == "thumbs_convert_now":
            if self.data is not None:
                # commands from the current Convert rows
                self.data.prepare_converts()
                self.data.run_converts()
                self.data.prepare_all_columns()
                self.data.prepare_tables()
                self.show_all()

        if group == "data_filter":
            self.show_data()

        if group == "data_matched_filter":
            # only the Data tab table changes, no new matching
            if self.data is not None:
                self.data.display_data_table()

        if group == "rename_display":
            if self.data:
                self.show_all()

        if group == "ayon_rematch":
            # match rules or prefix changed: match the loaded list again, no
            # new Ayon query (Project, Enable, Thumbnails apply on Scan / Reload)
            if self.data is not None and self.data.ayon_data:
                self.data.ayon_collect_gui()
                self.data.ayon_data_assign()
                self.data.ayon_versions_update()
                self.data.ayon_versions_assign()
                self.data.ayon_data_filter()
                self.data.prepare_all_columns()
                self.data.prepare_tables()
                self.show_all()
            elif self.ayon_only is not None:
                self.ayon_only.settings = self.settings
                self.ayon_only.ayon_data_filter()

        if group == "ayon_changed_filter":
            if self.data is not None:
                self.data.ayon_data_filter()
            elif self.ayon_only is not None:
                self.ayon_only.settings = self.settings
                self.ayon_only.ayon_data_filter()

        if group == "tab_pairs":
            self.gui_show_hide_modules()

    # typing pause before a text field refreshes the tables (ms)
    TYPING_DELAY_MS = 350

    def _handler_later(self, sender, group, *more):
        """
        Text fields: refresh once typing pauses instead of on every keystroke
        (every keystroke used to read all ~1000 widgets and rebuild the data).
        Different refresh kinds typed one after the other all run, in order.
        """
        pending = self.__dict__.setdefault('_pending_refresh', {})
        pending.pop(group, None)
        pending[group] = (sender, more)
        timer = self.__dict__.get('_refresh_timer')
        if timer is None:
            timer = QtCore.QTimer(self)
            timer.setSingleShot(True)
            timer.timeout.connect(self._run_pending)
            self._refresh_timer = timer
        timer.start(self.TYPING_DELAY_MS)

    def _run_pending(self):
        pending = self.__dict__.get('_pending_refresh') or {}
        while pending:
            group = next(iter(pending))
            sender, more = pending.pop(group)
            self.handler(sender, group, *more)

    def _cancel_later(self, group=None):
        """forget deferred refreshes: of one group, or all (group None)"""
        pending = self.__dict__.get('_pending_refresh')
        if not pending:
            return
        if group is None:
            pending.clear()
        else:
            pending.pop(group, None)

    def show_data(self):

        if self.data and self.settings:
            _1 = str(self.settings['tree_filter_file']['value'] or '')
            _2 = str(self.settings['tree_filter_key']['value'] or '')
            _3 = str(self.settings['tree_filter_value']['value'] or '')

            # Display merged items as a data tree
            self.ui.data_tree.clear()
            self.ui.data_tree.setColumnCount(3)
            self.ui.data_tree.setHeaderLabels(["#", "key", "value"])
            if self.data.merged_list is not None:
                for index, one_itm in enumerate(self.data.merged_list):
                    _fn = one_itm.get('part1', '')
                    _fp = one_itm.get('part2', '')
                    if _fp:
                        _l = _fp + '/' + _fn
                    else:
                        _l = _fn
                    _n = "{}: {}".format(str(index), _l)
                    if _1 and _1 not in _n:
                        continue
                    rows = [(str(k), str(v)) for k, v in sorted(one_itm.items())
                            if k not in INSPECTOR_HIDDEN_KEYS
                            and (not _2 or _2 in str(k)) and (not _3 or _3 in str(v))]
                    if (_2 or _3) and not rows:
                        # no token matches the key / value filter: skip the file
                        continue
                    _ti = QtWidgets.QTreeWidgetItem(self.ui.data_tree)
                    _ti.setText(0, _n)
                    for k, v in rows:
                        _tii = QtWidgets.QTreeWidgetItem(_ti)
                        _tii.setText(1, k)
                        _tii.setText(2, v)

    def _reload_package(self):
        """read the package folder again, like the Reload button"""
        self.settings_from_gui()
        pth = str(self.settings['package_folder']['value'] or '').replace('\\', '/')
        if not pth:
            return
        self.data = Sequencer(pth, sequence_mode='holes_allowed', gui=self.settings,
                              more_settings=self.settings_obj, ui=self.ui,
                              headless=self.no_gui)
        self.show_all()

    def _rename_rows_for_display(self, rows):
        """
        Rename table rows (full source / destination paths) as chosen by the
        radio buttons above the bottom Rename table
        """
        if not rows:
            return rows

        def _on(name):
            return bool(self.settings.get(name, {}).get('value'))

        if _on('rename_tab_names_only'):
            return [[str(p).replace('\\', '/').rsplit('/', 1)[-1] for p in row] for row in rows]
        if _on('rename_tab_relative'):
            root = str(self.settings.get('package_folder', {}).get('value') or '')
            root = root.replace('\\', '/').rstrip('/') + '/'

            def _rel(p):
                p = str(p).replace('\\', '/')
                return p[len(root):] if root != '/' and p.startswith(root) else p
            return [[_rel(p) for p in row] for row in rows]
        return rows

    def show_all(self):
        """
        Fill Submission table, drive log table and text with data
        :return:
        """

        if self.data:
            # tables are filled again: Go back to its normal look (it is
            # grey while the tables are cleared)
            self.ui.write_button.setStyleSheet("")
            # fill all tables
            self.display_table(
                self.data.table_sub,
                self.ui.sub_table,
                self.data.column_titles_sub
            )
            #self.ui.sub_table.update()
            self.display_table(
                self.data.table_log,
                self.ui.log_table,
                self.data.column_titles_log
            )
            #self.ui.log_table.update()
            self.ui.txt_table.setPlainText(self.data.table_txt)

            if self.data.table_side is not None:
                self.display_table(
                    self.data.table_side,
                    self.ui.side_table,
                    self.data.columns_side
                )
                #self.ui.side_table.update()

            self.display_table(
                self._rename_rows_for_display(self.data.table_rename),
                self.ui.rename_table,
                ['source', 'destination']
            )

            # display Package name
            _preview = self.data.output.get('package_name', '')
            self.ui.name_preview.setText(_preview)

            # Present data for each item
            self.show_data()


    def explore(self, path):

        log.debug('-> explore')

        platform = 'win'
        if sys.platform.startswith('darwin'):
            platform = 'mac'
        elif str(os.name).startswith('posix'):
            platform = 'nix'

        if path and path != '' and os.path.exists(path):
            if platform == 'win':
                win_path = os.path.normpath(path)
                if os.path.isdir(win_path):
                    os.startfile(win_path)
                else:
                    # open the parent folder with the file selected
                    subprocess.Popen(['explorer', '/select,', win_path])
            if platform == 'mac':
                if os.path.isdir(path):
                    subprocess.Popen(['open', path])
                else:
                    subprocess.Popen(['open', '-R', path])
            if platform == 'nix':
                if not os.path.isdir(path):
                    path = os.path.dirname(path)
                subprocess.Popen(['xdg-open', path])

    def browse(self, start_path):

        log.debug('-> browse')

        if start_path is None or not os.path.exists(start_path):
            start_path = os.path.expanduser('~')
            if start_path is None:
                start_path = ''
        dir_name = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder", start_path,
                                                              QtWidgets.QFileDialog.ShowDirsOnly)
        if not dir_name:
            # dialog cancelled
            return None
        return dir_name.replace('\\', '/')

    @staticmethod
    def _existing_start_dir(path):
        """
        Return the closest existing folder for a path typed in the gui,
        or the home folder. Used as the starting point of file dialogs.
        """
        path = (path or '').strip().replace('\\', '/')
        while path:
            if os.path.isdir(path):
                return path
            parent = os.path.dirname(path.rstrip('/'))
            if parent == path.rstrip('/'):
                break
            path = parent
        return os.path.expanduser('~')

    def browse_line_edit(self, line_edit, mode='dir', title="Select", *args):
        """
        Browse button handler: pick a folder or file and put it to the line edit.
        Setting the text fires the line edit's textChanged, which refreshes the data.
        :param line_edit: QLineEdit to read the start path from and write the result to
        :param mode: 'dir' for folders, 'csv' for csv files
        """
        start = self._existing_start_dir(line_edit.text())
        if mode == 'csv':
            picked, _ = QtWidgets.QFileDialog.getOpenFileName(
                self, title, start, "CSV files (*.csv *.CSV);;All files (*)")
        else:
            picked = QtWidgets.QFileDialog.getExistingDirectory(
                self, title, start, QtWidgets.QFileDialog.ShowDirsOnly)
        if picked:
            line_edit.setText(picked.replace('\\', '/'))

    def browse_data_csv(self, *args):
        """
        Data CSV can be a file, or a folder when 'Latest in Folder' is checked
        """
        if self.ui.data_csv_latest.isChecked():
            self.browse_line_edit(self.ui.data_csv_path, 'dir', "Select Data CSV Folder")
        else:
            self.browse_line_edit(self.ui.data_csv_path, 'csv', "Select Data CSV")

    def explore_line_edit(self, line_edit, *args):
        """
        Explore button handler: open the path from the line edit in the file manager.
        Falls back to the closest existing parent folder.
        """
        path = line_edit.text().strip().replace('\\', '/')
        if not (path and os.path.exists(path)):
            path = self._existing_start_dir(path)
        self.explore(path)

    def expore_local_presets(self):
        """
        Open user presets button
        :return:
        """
        self.explore(self.settings_obj.get_settings_path())

    def expore_package(self):
        _p = str(self.settings['package_folder']['value'])
        if _p:
            self.explore(_p.replace('\\', '/'))



    def go_button(self):

        log.debug('-> save_submission')
        self.data.export_all()

    def submission_name_from_path(self):

        log.debug('-> submission_name_from_path')

        last_dir = ""
        try:
            pth = str(self.ui.shots_path.displayText())
            if pth is not None and pth != "":
                prs = parse_file_name.parse(pth)
                last_dir = prs["parts"][-1]
        except Exception:
            pass

        return last_dir

    def display_table(self, table, table_ui, titles):
        """
        table data to ui
        """
        # display table
        table_ui.clear()
        table_ui.setColumnCount(0)
        table_ui.setRowCount(0)
        if table and titles:
            table_ui.setSortingEnabled(False)
            table_ui.setColumnCount(len(titles))
            table_ui.setHorizontalHeaderLabels(titles)
            table_ui.setRowCount(len(table))
            group_colors = setting_to_bool((self.settings.get('group_on') or {}).get('value')) and \
                setting_to_bool((self.settings.get('group_colors') or {}).get('value', True))

            for row, line in enumerate(table):
                # sub and log tables have merged list data
                # stored as a last item
                one_item = line[-1]
                if not isinstance(one_item, dict):
                    one_item = None

                for column_number, one_column in enumerate(titles):
                    my_title = str(one_column).lstrip().rstrip()
                    try:
                        table_ui.setItem(row,
                                         column_number,
                                         QtWidgets.QTableWidgetItem(str(line[column_number]))
                                         )
                    except Exception:
                        log.error("can't display table row")

                    if one_item:
                        # colorize: error, warning, size warning, then the
                        # Grouping tab group color, else the default grey
                        itm = table_ui.item(row, column_number)
                        if itm:
                            color = grouping.gui_color(one_item, use_groups=group_colors)
                            itm.setBackground(QtGui.QColor(color or "#4d4d4d"))

            table_ui.resizeColumnsToContents()
            table_ui.resizeRowsToContents()


    def clear_all_tables(self):
        """
        table data to ui
        """
        self.ui.sub_table.clear()
        self.ui.sub_table.setRowCount(0)
        self.ui.log_table.clear()
        self.ui.log_table.setRowCount(0)
        self.ui.txt_table.setPlainText('')

        # set go to gray
        self.ui.write_button.setStyleSheet("""
                QPushButton {background:rgb(81,81,81); color: white;} 
            """)


    def settings_update_dropbox(self):
        if not self.no_gui:
            self.ui.load_preset_combobox.blockSignals(True)
            self.ui.load_preset_combobox.clear()
            self.ui.load_preset_combobox.addItems(self.settings_obj.preset_names)

            try:
                index = self.settings_obj.preset_names.index(
                    self.settings_obj.current_settings_name)
                if index <= -1 or index > len(self.settings_obj.preset_names):
                    pass
                else:
                    # preselect a combobox value by index
                    self.ui.load_preset_combobox.setCurrentIndex(index)
            except Exception:
                log.error("Failed to set settings dropbox index.")

            self.ui.load_preset_combobox.blockSignals(False)

    def settings_update_app_title(self):
        self.setWindowTitle(self.bare_title + ": " +
                            self.settings_obj.current_settings_name)

    def settings_from_gui(self):
        """
        Stores gui values to self.settings
        """

        # Save geometry
        self.log.debug('-> settings_from_gui')
        self.settings = {}
        xs = str(self.geometry().width())
        ys = str(self.geometry().height())
        self.settings.update({'size': {
                                        'category': 'mainwindow_size',
                                        'size_x': xs,
                                        'size_y': ys}})
        x = str(self.geometry().x())
        y = str(self.geometry().y())
        self.settings.update({'position': {
                                        'category': 'mainwindow_position',
                                        'position_x': x,
                                        'position_y': y}})
        if getattr(self, 'panel_splitter', None) is not None:
            self.settings.update({'panel_splitter': {
                                        'category': 'splitter',
                                        'sizes': [int(v) for v in self.panel_splitter.sizes()]}})
        for my_name, obj in inspect.getmembers(self.ui):
            name = my_name
            if name in self.NOT_SETTINGS:
                continue
            if isinstance(obj, QtWidgets.QComboBox):
                all_items = [obj.itemText(i) for i in range(obj.count())]
                # get current index from combobox
                index = int(obj.currentIndex())
                text = str(obj.currentText())
                self.settings.update({name: {
                                            'category': 'combobox',
                                            'value': text,
                                            'all_items': all_items}})
            elif isinstance(obj, QtWidgets.QLineEdit):
                value = obj.displayText()
                self.settings.update({name: {
                                            'category': 'lineedit',
                                            'value': value}})
            elif isinstance(obj, QtWidgets.QPlainTextEdit):
                value = obj.toPlainText()
                self.settings.update({name: {
                                            'category': 'plaintextedit',
                                            'value': value}})
            elif isinstance(obj, QtWidgets.QCheckBox):
                state = bool(obj.isChecked())
                self.settings.update({name: {
                                            'category': 'checkbox',
                                            'value': state}})
            elif isinstance(obj, QtWidgets.QRadioButton):
                value = bool(obj.isChecked())
                self.settings.update({name: {
                                            'category': 'radiobutton',
                                            'value': value}})
            elif isinstance(obj, QtWidgets.QSpinBox):
                value = int(obj.value())
                self.settings.update({name: {
                                            'category': 'spinbox',
                                            'value': value}})
            elif isinstance(obj, QtWidgets.QSlider):
                value = str(obj.value())
                self.settings.update({name: {
                                            'category': 'slider',
                                            'value': value}})
        # Grouping tab definitions: one setting, a list of dicts
        if getattr(self, 'grouping_tab', None) is not None:
            self.settings['group_definitions'] = {
                'category': 'group_definitions',
                'value': self.grouping_tab.definitions()}

    def gui_show_hide_modules(self):
        # show / hide tabs
        for tabs, pages in ((self.ui.TopTab, self.tab_pages),
                            (self.ui.BottomTab, self.tab_pages_bottom)):
            for checkbox, page in pages.items():
                chbx = self.settings.get(checkbox)
                index = tabs.indexOf(page)
                if chbx and index >= 0:
                    tabs.setTabVisible(index, setting_to_bool(chbx.get('value', False)))

    def settings_to_gui(self):
        """
        Applies values from self.settings to gui
        """
        str_to_bool = setting_to_bool

        self.log.debug('-> settings_to_gui')
        skip_names = [
            'package_folder',
            'name_preview',
            'load_preset_combobox',
            'save_preset_name',
            'global_prefs_path',
            'global_prefs_enabled',
            'ffprobe_path',
            'vendor_csv_path'
        ] + list(self.NOT_SETTINGS)
        # indicate to user that reload or browse for package folder is needed
        self.clear_all_tables()

        # Restore main window geometry only if it is app start, not preset load
        if self.ui_start:
            setting_size = self.settings.get("size")
            if setting_size:
                self.resize(
                    int(setting_size['size_x']),
                    int(setting_size['size_y']))
            setting_pos = self.settings.get("position")
            if setting_pos:
                self.move(
                    int(setting_pos['position_x']),
                    int(setting_pos['position_y']))
            setting_split = self.settings.get("panel_splitter")
            if setting_split and getattr(self, 'panel_splitter', None) is not None:
                try:
                    sizes = [int(v) for v in setting_split.get('sizes', [])]
                    if len(sizes) == 2 and min(sizes) > 0:
                        self.panel_splitter.setSizes(sizes)
                except (TypeError, ValueError):
                    self.log.warning("Ignoring invalid saved panel sizes")
            self.ui_start = False

        for my_name, obj in inspect.getmembers(self.ui):
            one_setting = self.settings.get(my_name)
            if my_name in skip_names:
                continue
            if one_setting is None:
                continue

            obj.blockSignals(True)
            if isinstance(obj, QtWidgets.QComboBox):
                obj.clear()
                try:
                    obj.addItems(one_setting['all_items'])
                    _index = str(one_setting['value'])
                    if _index in one_setting['all_items']:
                        # the saved value is the item text (also when it is a number)
                        obj.setCurrentText(_index)
                    elif _index.isdigit() and int(_index) < len(one_setting['all_items']):
                        # preselect a combobox value by index
                        obj.setCurrentIndex(int(_index))
                    else:
                        obj.setCurrentText(_index)
                except Exception:
                    self.log.error("Error restoring QComboBox {}".format(
                        str(obj.objectName())))
            elif isinstance(obj, QtWidgets.QLineEdit):
                try:
                    obj.setText(one_setting['value'])
                except Exception:
                    self.log.error("Error restoring QLineEdit {}".format(
                        str(obj.objectName())))
            elif isinstance(obj, QtWidgets.QCheckBox):
                try:
                    # "False" saved as text is unchecked
                    obj.setChecked(str_to_bool(one_setting['value']))
                except Exception:
                    self.log.error("Error restoring QCheckBox {}".format(
                        str(obj.objectName())))
            elif isinstance(obj, QtWidgets.QRadioButton):
                try:
                    if one_setting['value']:
                        obj.setChecked(str_to_bool(one_setting['value']))
                except Exception:
                    self.log.error("Error restoring QRadioButton {}".format(
                        str(obj.objectName())))
            elif isinstance(obj, QtWidgets.QSpinBox):
                try:
                    # 0 is a value too
                    if one_setting['value'] is not None and one_setting['value'] != '':
                        obj.setValue(int(float(one_setting['value'])))
                except Exception:
                    self.log.error("Error restoring QSpinBox {}".format(
                        str(obj.objectName())))
            elif isinstance(obj, QtWidgets.QSlider):
                try:
                    if one_setting['value'] is not None and one_setting['value'] != '':
                        obj.setValue(int(float(one_setting['value'])))
                except Exception:
                    self.log.error("Error restoring QSlider {}".format(
                        str(obj.objectName())))
            elif isinstance(obj, QtWidgets.QPlainTextEdit):
                try:
                    obj.setPlainText(one_setting['value'])
                except Exception:
                    self.log.error("Error restoring QPlainTextEdit {}".format(
                        str(obj.objectName())))
            else:
                self.log.warning("Error restoring {} {}".format(
                    str(one_setting['category']), str(obj.objectName())))
            obj.blockSignals(False)

        # Grouping tab definitions (kept as they are when the preset has none)
        group_defs = self.settings.get('group_definitions')
        if isinstance(group_defs, dict) and getattr(self, 'grouping_tab', None) is not None:
            self.grouping_tab.set_definitions(group_defs.get('value'))

    def settings_update(self, knob_name, ui, value, val2=None):
        one_setting = self.settings.get(knob_name)
        if one_setting:
            if one_setting["category"]:
                # keep the type of the category: str(False) is "False", which
                # every later bool() check read as on
                if one_setting["category"] in ("checkbox", "radiobutton"):
                    one_setting["value"] = setting_to_bool(value)
                elif one_setting["category"] == "spinbox":
                    try:
                        one_setting["value"] = int(value)
                    except (TypeError, ValueError):
                        one_setting["value"] = value
                else:
                    one_setting["value"] = str(value)
                if one_setting["category"] == "lineedit" or\
                        one_setting["category"] == "plaintextedit":
                    if not self.no_gui:
                        ui.blockSignals(True)
                        ui.setText(value)
                        ui.blockSignals(False)
                elif one_setting["category"] == "checkbox" or\
                        one_setting["category"] == "radiobutton":
                    if not self.no_gui:
                        ui.blockSignals(True)
                        ui.setChecked(setting_to_bool(value))
                        ui.blockSignals(False)
                elif one_setting["category"] == "spinbox":
                    if not self.no_gui:
                        ui.blockSignals(True)
                        ui.setValue(int(value))
                        ui.blockSignals(False)
                elif one_setting["category"] == "combobox":
                    pass

    def apply_settings_overrides(self, overrides):
        """
        Apply --settings overrides "key1=value1,key2=value2" to self.settings.
        Values are converted by the category of the existing setting.
        """
        sh_cli.apply_settings_overrides(self.settings, overrides)

    # default height of the top tabs panel, it was fixed to this before
    TOP_PANEL_DEFAULT = 350
    TOP_PANEL_MIN = 350
    BOTTOM_PANEL_MIN = 120

    def _setup_panel_splitter(self):
        """
        Put TopTab and BottomTab into a vertical QSplitter, so the user can drag
        the border between them. Done in code so ui_Submission.py can still be
        regenerated from submission.ui.
        Double click on the handle restores the default height.
        :return: the splitter
        """
        top = self.ui.TopTab
        bottom = self.ui.BottomTab
        top_layout = self.ui.verticalLayout_15      # [TopTab, verticalLayout_10]
        bottom_layout = self.ui.verticalLayout_10   # [BottomTab, buttons, progress]

        top_layout.removeWidget(top)
        bottom_layout.removeWidget(bottom)

        splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical, self.ui.centralwidget)
        splitter.setObjectName("panel_splitter")
        splitter.setChildrenCollapsible(False)
        splitter.setHandleWidth(7)
        splitter.addWidget(top)
        splitter.addWidget(bottom)
        # window resizing goes to the bottom panel, as before
        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)
        splitter.setStyleSheet(
            "QSplitter::handle:vertical { background: #3a3a3a; margin: 1px 40px; border-radius: 2px; }"
            "QSplitter::handle:vertical:hover { background: #ffa02f; }")
        handle = splitter.handle(1)
        handle.setToolTip("Drag to resize the panels, double click to reset")
        handle.installEventFilter(self)

        # was a fixed 350 px, now 350 px minimum and free to grow
        top.setMinimumHeight(self.TOP_PANEL_MIN)
        top.setMaximumHeight(16777215)
        bottom.setMinimumHeight(self.BOTTOM_PANEL_MIN)

        top_layout.insertWidget(0, splitter, 1)
        self._reset_panel_splitter(splitter)
        return splitter

    def _tune_top_tab_layouts(self):
        """
        Layout fixes for a top panel taller than the old fixed 350 px.
        Done in code so ui_Submission.py can still be regenerated.
        """
        ui = self.ui
        no_limit = 16777215
        fixed_v = QtWidgets.QSizePolicy.Fixed

        def keep_horizontal(widget, vertical):
            pol = widget.sizePolicy()
            pol.setVerticalPolicy(vertical)
            widget.setSizePolicy(pol)

        # Package: the file age group stays compact, extra height is empty
        # space below all the controls
        keep_horizontal(ui.groupBox_5, fixed_v)
        ui.verticalLayout_128.addStretch(1)

        # Parsing: the scroll area grows with the panel (was max 350 px),
        # rows stay at the top
        ui.scrollArea.setMaximumHeight(no_limit)
        ui.verticalLayout_31.addStretch(1)

        # Rename: Rename button as high as the Go button instead of
        # stretching, extra height is empty space below
        go_h = ui.write_button.minimumHeight() or 40
        ui.Rename_go.setMinimumHeight(go_h)
        ui.Rename_go.setMaximumHeight(go_h)
        keep_horizontal(ui.Rename_go, fixed_v)
        ui.verticalLayout_66.addStretch(1)

        # Vendor: the scroll area (was max 450 px) and the two json editors
        # (were max 400 px) grow with the panel
        ui.scrollArea_4.setMaximumHeight(no_limit)
        ui.vendor_csv_prefs_spreadsheet.setMaximumHeight(no_limit)
        ui.vendor_csv_prefs_repres.setMaximumHeight(no_limit)

        # Convert: controls at the top, extra height below them
        ui.verticalLayout_35.addStretch(1)

        # Presets: the group boxes were vertically centered, keep them at the top
        ui.verticalLayout_95.addStretch(1)

        # Spreadsheet: the column editors (were max 300 px) use the full height
        for edit in (ui.sub_columns, ui.log_columns, ui.txt_columns):
            edit.setMaximumHeight(no_limit)

    def _add_grouping_tab(self):
        """
        Grouping tab (grouping_widget.py) after the Spreadsheet tab and its
        Modules checkbox on the Presets tab. Grouping replaces Merge By (the
        Merge Lines group of the Preferences tab).
        :return: the GroupingTab
        """
        ui = self.ui
        tab = GroupingTab(ui.TopTab)
        index = ui.TopTab.indexOf(ui.tab_2)
        ui.TopTab.insertTab(index + 1 if index >= 0 else ui.TopTab.count(), tab, "Grouping")
        # top controls are ordinary settings: settings_from_gui finds them on ui
        for name, widget in tab.settings_widgets.items():
            setattr(ui, name, widget)
        ui.tab_grouping = tab

        mod = QtWidgets.QCheckBox("Grouping", ui.groupBox_18)
        mod.setObjectName("preset_mod_grouping")
        mod.setSizePolicy(ui.preset_mod_spreadsheet.sizePolicy())
        mod.setMinimumSize(ui.preset_mod_spreadsheet.minimumSize())
        mod.setMaximumSize(ui.preset_mod_spreadsheet.maximumSize())
        mod.setChecked(True)
        mod.setToolTip("Show the Grouping tab. Hiding it doesn't switch grouping off.")
        ui.preset_mod_grouping = mod
        layout = ui.verticalLayout_72
        layout.insertWidget(layout.indexOf(ui.preset_mod_spreadsheet) + 1, mod)
        self.tab_pages['preset_mod_grouping'] = tab
        return tab

    def _add_ftrack_lists_tab(self):
        """
        The Ftrack tab gets sub-tabs: Shots (the Ftrack tab of the .ui file)
        and Get Lists (ftrack_lists_widget.py).
        :return: the FtrackListsTab
        """
        ui = self.ui
        top = ui.TopTab
        index = top.indexOf(ui.tab_11)
        if index < 0:
            return None
        label = top.tabText(index)
        was_current = top.currentIndex() == index
        container = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        sub_tabs = QtWidgets.QTabWidget(container)
        sub_tabs.setObjectName("ftrack_sub_tabs")
        layout.addWidget(sub_tabs)
        top.removeTab(index)
        sub_tabs.addTab(ui.tab_11, "Shots")
        lists = FtrackListsTab(self._ftrack_lists_connect, self._ayon_busy, sub_tabs)
        sub_tabs.addTab(lists, "Get Lists")
        top.insertTab(index, container, label)
        if was_current:
            top.setCurrentIndex(index)
        # Modules checkbox (Presets tab) shows / hides the whole Ftrack tab
        self.tab_pages['preset_mod_ftrack'] = container
        self.ftrack_sub_tabs = sub_tabs
        return lists

    def _ftrack_lists_connect(self):
        """
        Get Lists: ftrack session and the id of the Project of the Shots
        sub-tab. :return: (session, project_id), None items when missing (logged)
        """
        import ftrack
        paths = self._credential_paths()
        credentials.ensure_ftrack(paths)
        session = ftrack.open_session(paths.get('FTRACK_SERVER', ''),
                                      paths.get('FTRACK_API_USER', ''),
                                      paths.get('FTRACK_API_KEY', ''))
        project = str(self.ui.ftrack_project.displayText()).strip()
        if session is not None and not project:
            self.log.warning("Get Lists: set the ftrack Project on the Ftrack > Shots sub-tab")
            return session, None
        return session, ftrack.find_project_id(session, project)

    # Presets tab, Modules group: tabs in the order of the window
    MODULES_TOP = ('package', 'parsing', 'sidecar', 'rename', 'data', 'ftrack', 'vendor',
                   'replace', 'convert', 'spreadsheet', 'grouping', 'checks', 'publish',
                   'ayon', 'preferences', 'exports', 'log', 'help')
    MODULES_BOTTOM = ('submission', 'drivelog', 'text', 'inspector', 'files')
    MODULES_COLUMNS = 6

    def _arrange_preset_modules(self):
        """
        Presets tab: the Modules group (a narrow 3-column box next to the
        Presets group, texts cut off) goes below the Presets group, full
        width, with the checkboxes in a grid wide enough for their texts.
        Top and bottom tabs are listed separately. Done in code so
        ui_Submission.py can still be regenerated.
        """
        ui = self.ui
        old = ui.groupBox_18
        ui.horizontalLayout_67.removeWidget(old)

        box = QtWidgets.QGroupBox("Modules", ui.tab_3)
        box.setObjectName("groupBox_18")
        box.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        outer = QtWidgets.QVBoxLayout(box)
        outer.setContentsMargins(9, 6, 9, 9)
        outer.setSpacing(2)

        placed = set()

        def section(title, keys):
            boxes = []
            for key in keys:
                cb = getattr(ui, f"preset_mod_{key}", None)
                if cb is not None and cb not in placed:
                    boxes.append(cb)
                    placed.add(cb)
            if not boxes:
                return
            label = QtWidgets.QLabel(title, box)
            label.setStyleSheet("color: #a0a0a0;")
            outer.addWidget(label)
            grid = QtWidgets.QGridLayout()
            grid.setHorizontalSpacing(16)
            grid.setVerticalSpacing(2)
            for i, cb in enumerate(boxes):
                cb.setParent(box)
                cb.setMinimumSize(cb.sizeHint().width() + 8, 25)
                cb.setMaximumSize(16777215, 25)
                grid.addWidget(cb, i // self.MODULES_COLUMNS, i % self.MODULES_COLUMNS)
            for c in range(self.MODULES_COLUMNS):
                grid.setColumnMinimumWidth(c, 130)
            grid.setColumnStretch(self.MODULES_COLUMNS, 1)
            outer.addLayout(grid)

        section("Top tabs", self.MODULES_TOP)
        section("Bottom tabs", self.MODULES_BOTTOM)
        # checkboxes added later that the lists above don't know yet
        rest = sorted(n for n in dir(ui) if n.startswith("preset_mod_"))
        section("Other", [n[len("preset_mod_"):] for n in rest])

        old.setParent(None)
        old.deleteLater()
        ui.groupBox_18 = box

        # the Presets group was 270 px high to match the old Modules box
        presets = ui.groupBox_31
        presets.setMinimumHeight(0)
        presets.setMaximumHeight(16777215)
        presets.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        layout = ui.verticalLayout_95
        # right below the row with the Presets group (a stretch follows)
        idx = 0
        for i in range(layout.count()):
            if layout.itemAt(i).layout() is ui.horizontalLayout_67:
                idx = i
                break
        layout.insertWidget(idx + 1, box)

    def _add_data_controls(self):
        """Data tab: Show Matched Only checkbox after Latest in Folder"""
        ui = self.ui
        cb = QtWidgets.QCheckBox("Show Matched Only", ui.groupBox_25)
        cb.setObjectName("data_filter_matched")
        cb.setChecked(True)
        cb.setMinimumSize(QtCore.QSize(cb.sizeHint().width() + 8, 25))
        cb.setToolTip("Show only the Data CSV rows paired with a package file (green). "
                      "Off: all rows of the csv. Only changes the table on this tab.")
        ui.data_filter_matched = cb
        ui.horizontalLayout_162.addWidget(cb)

    def _add_parse_rows(self):
        """
        Add Parsing tab rows up to PARSE_ROWS, copying the look of the last
        row from the .ui file. The new fields are set on self.ui with the same
        naming (parse_name_33 ...), so they are saved in presets like the others.
        """
        ui = self.ui
        labels = {'name': "Name:", 'pattern': "Pattern:", 'repl': "Repl:",
                  'source': "Source:", 'filter': "Filter:"}
        # last row that exists in the ui file
        last = 0
        while hasattr(ui, f"parse_name_{last + 1:02d}"):
            last += 1
        if last == 0 or last >= PARSE_ROWS:
            return
        template_row = ui.hl_parse032 if hasattr(ui, 'hl_parse032') else None
        template_labels = []
        if template_row is not None:
            for i in range(template_row.count()):
                w = template_row.itemAt(i).widget()
                if isinstance(w, QtWidgets.QLabel):
                    template_labels.append(w)
        parent = ui.scrollAreaWidgetContents

        def copy_look(dst, src):
            dst.setSizePolicy(src.sizePolicy())
            dst.setMinimumSize(src.minimumSize())
            dst.setMaximumSize(src.maximumSize())
            dst.setToolTip(src.toolTip())

        for row in range(last + 1, PARSE_ROWS + 1):
            hl = QtWidgets.QHBoxLayout()
            hl.setObjectName(f"hl_parse{row:03d}")
            for idx, field in enumerate(PARSE_FIELDS):
                label = QtWidgets.QLabel(labels[field], parent)
                if idx < len(template_labels):
                    copy_look(label, template_labels[idx])
                hl.addWidget(label)
                edit = QtWidgets.QLineEdit(parent)
                name = f"parse_{field}_{row:02d}"
                edit.setObjectName(name)
                src = getattr(ui, f"parse_{field}_{last:02d}", None)
                if src is not None:
                    copy_look(edit, src)
                    edit.setPlaceholderText(src.placeholderText())
                setattr(ui, name, edit)
                hl.addWidget(edit)
            setattr(ui, hl.objectName(), hl)
            ui.verticalLayout_30.addLayout(hl)

    def _add_ayon_controls(self):
        """
        Ayon tab additions, built in code so ui_Submission.py can be regenerated:
        - Scan button: read the Ayon list now, also without a package
        - Versions group: Pull versions checkbox and Product filters
        New widgets are set on self.ui, so they are saved in presets.
        """
        ui = self.ui
        parent = ui.tab_25

        scan = QtWidgets.QPushButton("Scan", parent)
        scan.setObjectName("ayon_scan_butt")
        scan.setMinimumSize(QtCore.QSize(120, ui.ayon_export_butt.minimumHeight() or 35))
        scan.setMaximumHeight(ui.ayon_export_butt.maximumHeight())
        scan.setToolTip("Read the Ayon list now (also without a loaded package) "
                        "and match it to the files, if any.")
        ui.ayon_scan_butt = scan
        ui.horizontalLayout_212.insertWidget(0, scan)

        group = QtWidgets.QGroupBox("Versions", parent)
        group.setObjectName("ayon_versions_group")
        group.setMinimumSize(QtCore.QSize(350, 112))
        group.setMaximumHeight(112)
        pol = group.sizePolicy()
        pol.setVerticalPolicy(QtWidgets.QSizePolicy.Fixed)
        group.setSizePolicy(pol)
        rows = QtWidgets.QVBoxLayout(group)
        rows.setContentsMargins(6, 2, 6, 2)
        rows.setSpacing(4)
        row = QtWidgets.QHBoxLayout()
        rows.addLayout(row)

        chbx = QtWidgets.QCheckBox("Pull versions", group)
        chbx.setObjectName("ayon_versions_chbx")
        chbx.setMinimumSize(QtCore.QSize(110, 25))
        chbx.setToolTip("Add version info of the preferred product to every Ayon shot / asset row "
                        "(and its task rows). Used with the next Scan or package load.")
        ui.ayon_versions_chbx = chbx
        row.addWidget(chbx)

        label = QtWidgets.QLabel("Product filters:", group)
        row.addWidget(label)

        filters = QtWidgets.QLineEdit(group)
        filters.setObjectName("ayon_product_filters")
        filters.setMinimumSize(QtCore.QSize(100, 25))
        filters.setPlaceholderText("comp:renderCompMain:exr, :platePl01:exr")
        filters.setToolTip(
            "<p>task:product:representation, separated by commas. The task is optional.</p>"
            "<p><b>comp:renderCompMain:exr</b> - representation exr of product renderCompMain "
            "published from task comp<br>"
            "<b>:platePl01:exr</b> - any task<br>"
            "<b>:renderCompMain:</b> - product only: any task, any representation. Match version "
            "then pairs each file with a representation by its extension, then by its size.</p>"
            "<p>Filters are tried in order, the first one with a match is used, so list the "
            "preferred product first. The latest version of the product is used. "
            "Wildcards * ? are allowed, names are not case sensitive.</p>"
            "<p>Columns added: Product, Product Type, Version, Version Name, Version Status, "
            "Version Author, Version Date, Version Comment, Version Task, Representation, "
            "Repre Path, Version Filter, Version Frame Start / End, Version Handle Start / End, "
            "Version FPS, Version Width / Height, Version Pixel Aspect, Version Step, Version Host, "
            "Version Colorspace (keywords with the Ayon Column Prefix, e.g. {list_Version} with the default list_).</p>")
        ui.ayon_product_filters = filters
        row.addWidget(filters, 1)

        # second row: match a concrete version of Matched Versions to each file
        row2 = QtWidgets.QHBoxLayout()
        rows.addLayout(row2)
        match = QtWidgets.QCheckBox("Match version", group)
        match.setObjectName("ayon_version_match_chbx")
        match.setMinimumSize(QtCore.QSize(110, 25))
        match_tip = (
            "<p>For every file matched to an Ayon folder, find the Matched Versions row "
            "(same folder) whose <b>Version key</b> equals the file's <b>Package key</b>, "
            "e.g. Package <b>{version}</b> and Version <b>{Version}</b>. Numbers compare by "
            "value, so 007 equals 7.</p>"
            "<p>The row's columns are added to the file with the Column Prefix and "
            "<b>Matched</b>, e.g. {list_Matched Version}, {list_Matched Version Status}, "
            "{list_Matched Version Comment}, {list_Matched Repre Path}. "
            "Matched rows are teal in Matched Versions.</p>"
            "<p>For checks every file matched to an Ayon folder also gets "
            "{list_Matched Version Exists} (True / False) and "
            "{list_Matched Max Existing Version}, also when its version is not in Ayon yet.</p>")
        match.setToolTip(match_tip)
        ui.ayon_version_match_chbx = match
        row2.addWidget(match)
        row2.addWidget(QtWidgets.QLabel("Package:", group))
        mpkg = QtWidgets.QLineEdit(group)
        mpkg.setObjectName("ayon_version_match_pkg")
        mpkg.setMinimumSize(QtCore.QSize(100, 25))
        mpkg.setPlaceholderText("{version}")
        mpkg.setToolTip(match_tip)
        ui.ayon_version_match_pkg = mpkg
        row2.addWidget(mpkg, 1)
        row2.addWidget(QtWidgets.QLabel("Version:", group))
        mdata = QtWidgets.QLineEdit(group)
        mdata.setObjectName("ayon_version_match_data")
        mdata.setMinimumSize(QtCore.QSize(100, 25))
        mdata.setPlaceholderText("{Version}")
        mdata.setToolTip(match_tip)
        ui.ayon_version_match_data = mdata
        row2.addWidget(mdata, 1)

        # third row: record which package includes the matched versions
        row3 = QtWidgets.QHBoxLayout()
        rows.addLayout(row3)
        record_tip = (
            "<p>Write to Ayon which package includes each version and representation. "
            "Needs Pull versions and Match version: every Submission file matched to a "
            "version is paired with one of its representations, by file extension first, "
            "then by file size (Ayon keeps the size of every published file). The paired "
            "representation is {list_Matched Representation}, how it was found "
            "{list_Matched Representation By}.</p>"
            "<p>Version data gets <b>submissionHelper / packages / &lt;package name&gt;</b> with "
            "the representations in the package, representation data gets "
            "<b>submissionHelper / packages / &lt;package name&gt;</b>, both with date and user. "
            "Recording the same package again only writes what changed; other data stays.</p>")
        rec_go = QtWidgets.QCheckBox("Record Package with Go", group)
        rec_go.setObjectName("ayon_record_go")
        rec_go.setMinimumSize(QtCore.QSize(170, 25))
        rec_go.setToolTip(record_tip)
        ui.ayon_record_go = rec_go
        row3.addWidget(rec_go)
        row3.addStretch(1)
        rec_butt = QtWidgets.QPushButton("Record Package to Ayon", group)
        rec_butt.setObjectName("ayon_record_butt")
        rec_butt.setMinimumSize(QtCore.QSize(170, 25))
        rec_butt.setToolTip(record_tip)
        ui.ayon_record_butt = rec_butt
        row3.addWidget(rec_butt)

        idx = ui.verticalLayout_116.indexOf(ui.groupBox_33)
        ui.verticalLayout_116.insertWidget(idx + 1 if idx >= 0 else -1, group)

        # List Filters: Task Names row, below Task Types, same look
        name_row = QtWidgets.QHBoxLayout()
        tn_chbx = QtWidgets.QCheckBox("Task Names:", ui.groupBox_34)
        tn_chbx.setObjectName("ayon_filter_taskname_chbx")
        tn_chbx.setSizePolicy(ui.ayon_filter_tasktype_chbx.sizePolicy())
        tn_chbx.setMinimumSize(ui.ayon_filter_tasktype_chbx.minimumSize())
        tn_chbx.setMaximumSize(ui.ayon_filter_tasktype_chbx.maximumSize())
        tn_tip = ("Show only tasks with these names, separated by commas, e.g. comp, compFinal. "
                  "Wildcards * ? allowed, not case sensitive. Works together with Task Types "
                  "and Assignees: a task must pass all enabled filters.")
        tn_chbx.setToolTip(tn_tip)
        ui.ayon_filter_taskname_chbx = tn_chbx
        name_row.addWidget(tn_chbx)
        tn_edit = QtWidgets.QLineEdit(ui.groupBox_34)
        tn_edit.setObjectName("ayon_filter_tasknames")
        tn_edit.setSizePolicy(ui.ayon_filter_tasktypes.sizePolicy())
        tn_edit.setMinimumSize(ui.ayon_filter_tasktypes.minimumSize())
        tn_edit.setMaximumSize(ui.ayon_filter_tasktypes.maximumSize())
        tn_edit.setPlaceholderText("comp, compFinal")
        tn_edit.setToolTip(tn_tip)
        ui.ayon_filter_tasknames = tn_edit
        name_row.addWidget(tn_edit)
        pos = ui.verticalLayout_114.indexOf(ui.horizontalLayout_208)
        ui.verticalLayout_114.insertLayout(pos + 1 if pos >= 0 else -1, name_row)

        ui.ayon_output_folder.setToolTip(
            "<p>Folder where <b>Export Shot List</b> saves ayon-list.csv, ayon-list-versions.csv "
            "(with Versions CSV). With Thumbnails on, the thumbnails are downloaded to "
            "_thumbsDownload in it when the list is read (Scan or package load).</p>")

        # export checkbox for the Matched Versions csv, next to the CSV / Excel ones
        vcsv = QtWidgets.QCheckBox("Versions CSV", parent)
        vcsv.setObjectName("ayon_export_versions_csv")
        vcsv.setMinimumSize(QtCore.QSize(110, 25))
        vcsv.setToolTip("Also write the Matched Versions list to ayon-list-versions.csv, "
                        "in the same folder as ayon-list.csv")
        ui.ayon_export_versions_csv = vcsv
        pos = ui.horizontalLayout_68.indexOf(ui.ayon_export_excel)
        ui.horizontalLayout_68.insertWidget(pos + 1 if pos >= 0 else -1, vcsv)

        # sub tabs: Shot List (the existing table) and Matched Versions
        tabs = QtWidgets.QTabWidget(parent)
        tabs.setObjectName("ayon_tables_tab")
        list_page = QtWidgets.QWidget()
        list_layout = QtWidgets.QVBoxLayout(list_page)
        list_layout.setContentsMargins(0, 0, 0, 0)
        table_index = ui.verticalLayout_118.indexOf(ui.ayon_table)
        ui.verticalLayout_118.removeWidget(ui.ayon_table)
        list_layout.addWidget(ui.ayon_table)
        tabs.addTab(list_page, "Shot List")

        versions_page = QtWidgets.QWidget()
        versions_layout = QtWidgets.QVBoxLayout(versions_page)
        versions_layout.setContentsMargins(0, 0, 0, 0)
        vtable = QtWidgets.QTableWidget(versions_page)
        vtable.setObjectName("ayon_versions_table")
        vtable.setSizePolicy(ui.ayon_table.sizePolicy())
        vtable.setMinimumSize(ui.ayon_table.minimumSize())
        vtable.setToolTip("All versions of the configured products (Product filters) of the Ayon folders "
                          "matched to the package files, sorted by folder path and version "
                          "(needs Pull versions). Preferred = picked by the product filters.")
        vbar = QtWidgets.QHBoxLayout()
        vmatched = QtWidgets.QCheckBox("Show matched only", versions_page)
        vmatched.setObjectName("ayon_versions_matched_only")
        vmatched.setToolTip("Only the versions a package file matched (teal, Match version). "
                            "Versions CSV exports what is shown.")
        ui.ayon_versions_matched_only = vmatched
        vbar.addWidget(vmatched)
        vbar.addStretch(1)
        versions_layout.addLayout(vbar)
        versions_layout.addWidget(vtable)
        tabs.addTab(versions_page, "Matched Versions")
        ui.ayon_versions_table = vtable
        ui.ayon_versions_page = versions_page
        ui.ayon_tables_tab = tabs
        ui.verticalLayout_118.insertWidget(table_index if table_index >= 0 else -1, tabs, 1)

    def _ayon_target(self):
        """
        Sequencer for Ayon operations: the loaded package, or an Ayon only
        one when no package is loaded
        """
        if self.data is not None:
            return self.data
        if self.ayon_only is None:
            self.ayon_only = Sequencer(None, sequence_mode='holes_allowed', gui=self.settings,
                                       more_settings=self.settings_obj, ui=self.ui,
                                       headless=self.no_gui)
        self.ayon_only.settings = self.settings
        return self.ayon_only

    def _ayon_busy(self, fn, message):
        """run fn with a wait cursor and a status bar message"""
        self.ui.statusBar.showMessage(message)
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        try:
            return fn()
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()
            self.ui.statusBar.clearMessage()

    def _setup_accounts(self):
        """sign-in dialog for credentials.prompt, Accounts group on the Preferences tab"""
        import credentials_dialog
        def ask(kind, url):
            ok = credentials_dialog.ask_sign_in(kind, url, parent=self)
            if self.accounts_group is not None:
                self.accounts_group.refresh()
            return ok
        credentials.set_prompt_handler(ask)
        self.accounts_group = credentials_dialog.AccountsGroup(
            self._credential_paths, self._credentials_changed, parent=self.ui.tab_4)
        row = QtWidgets.QHBoxLayout()
        row.addWidget(self.accounts_group)
        self.ui.verticalLayout_40.addLayout(row)

    def _credential_paths(self):
        """the credentials in use: of the loaded package, else resolved now"""
        for target in (getattr(self, 'data', None), getattr(self, 'ayon_only', None)):
            if target is not None and getattr(target, 'paths', None):
                return target.paths
        return credentials.resolve({}, credentials.startup_env(), self.settings_inst)

    def _credentials_changed(self):
        """after a sign-in / sign-out: use the new credentials from now on"""
        for target in (getattr(self, 'data', None), getattr(self, 'ayon_only', None)):
            if target is not None and getattr(target, 'paths', None) is not None:
                credentials.resolve(target.paths, credentials.startup_env(), self.settings_inst)

    def _reset_panel_splitter(self, splitter=None):
        splitter = splitter or self.panel_splitter
        total = max(sum(splitter.sizes()), self.TOP_PANEL_DEFAULT + self.BOTTOM_PANEL_MIN)
        splitter.setSizes([self.TOP_PANEL_DEFAULT, total - self.TOP_PANEL_DEFAULT])

    def eventFilter(self, obj, event):
        splitter = getattr(self, 'panel_splitter', None)
        if splitter is not None and obj is splitter.handle(1) \
                and event.type() == QtCore.QEvent.MouseButtonDblClick:
            self._reset_panel_splitter()
            return True
        return super().eventFilter(obj, event)

    def get_user_name(self):
        return getpass.getuser()

    def closeEvent(self, event):
        if self.log_view is not None:
            self.log_view.detach()
        self.settings_from_gui()
        self.settings_obj.settings = self.settings
        _last_prefs = 'last_' + self.get_user_name()
        self.settings_obj.write(_last_prefs)
        log.info('Writing {}'.format(_last_prefs))
        log.info('Finished')
        # Qt messages during teardown must not reach python logging
        sh_logging.uninstall_qt_message_handler(QtCore)
        # prevents second call
        sys.exit()

# log
# logging is configured in __main__ by sh_logging.setup_logging()
log = logging.getLogger("SubmissionHelper")


if __name__ == "__main__":
    # the windowed exe has no console: stdout / stderr are None there, a
    # stray print or argparse message must not crash the app
    if sys.stdout is None:
        sys.stdout = open(os.devnull, 'w')
    if sys.stderr is None:
        sys.stderr = open(os.devnull, 'w')
    args = vars(get_args())
    input_path = args['i']
    input_preset = args['p']

    try:
        sh_logging.setup_logging(console_level_from_args(args), args.get('log_file'))
    except OSError as e:
        sh_logging.setup_logging(console_level_from_args(args))
        log.error(f"Can't open log file '{args.get('log_file')}': {e}")
    sh_logging.install_excepthook()
    sh_logging.install_qt_message_handler(QtCore)
    log.debug(f"Command line: {sys.argv}")

    headless, exit_code = check_cli_args(args)
    if exit_code is not None:
        sys.exit(exit_code)
    if headless:
        # -i / -p are normally handed to sh_cli at the top of this file
        sys.exit(sh_cli.run_headless(args))

    app = QtWidgets.QApplication.instance()  # checks if QApplication already exists
    if not app:  # create QApplication if it doesn't exist
        app = QtWidgets.QApplication(sys.argv)

    log.debug('Starting GUI')
    settings_obj = Settings('last_' + getpass.getuser(), args)
    main = MainWindow(no_gui=False, s=settings_obj, args=args)
    main.show()
    rc = app.exec_()
    sh_logging.uninstall_qt_message_handler(QtCore)
    sys.exit(rc)
