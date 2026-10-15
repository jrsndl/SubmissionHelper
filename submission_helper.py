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

from PySide2 import QtCore, QtGui, QtWidgets

from ui_Submission import Ui_submission

from sequencer import Sequencer, PARSE_ROWS, PARSE_FIELDS
from settings import Settings
import parse_file_name
import sh_logging
from log_view import LogView


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
        self.ui_start = True
        self.settings_obj = s
        self.settings = self.settings_obj.settings or {}
        self.settings_inst = self.settings_obj.install_settings
        self.args = args or {}

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
            partial(self.handler, 'package_folder', 'source_change'))
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
            partial(self.handler, 'age_exclude', 'refresh_spreadsheets_age'))
        self.ui.age_include.textChanged.connect(
            partial(self.handler, 'age_include', 'refresh_spreadsheets_age'))

        # Rename Package
        self.ui.name_template.textChanged.connect(
            partial(self.handler, 'name_template', 'package_rename'))
        self.ui.name_date_regex.textChanged.connect(
            partial(self.handler, 'name_date_regex', 'package_rename'))
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
                    partial(self.handler, name, 'refresh_parsing'))

        # Sidecar Tab
        self.ui.side_folder.textChanged.connect(
            partial(self.handler, 'side_folder', 'refresh_side_files'))
        self.ui.package_browse_2.clicked.connect(
            partial(self.browse_line_edit, self.ui.side_folder, 'dir', "Select Sidecar Search Folder"))
        self.ui.package_explore_2.clicked.connect(
            partial(self.explore_line_edit, self.ui.side_folder))
        self.ui.side_exclude.textChanged.connect(
            partial(self.handler, 'side_exclude', 'refresh_side_files'))
        self.ui.side_include.textChanged.connect(
            partial(self.handler, 'side_include', 'refresh_side_files'))

        self.ui.side_sub_only.clicked.connect(
            partial(self.handler, 'side_sub_only', 'refresh_side'))
        self.ui.side_log_only.clicked.connect(
            partial(self.handler, 'side_log_only', 'refresh_side'))
        self.ui.side_all.clicked.connect(
            partial(self.handler, 'side_all', 'refresh_side'))

        self.ui.side_pattern_1.textChanged.connect(
            partial(self.handler, 'side_pattern_1', 'refresh_side'))
        self.ui.side_repl_1.textChanged.connect(
            partial(self.handler, 'side_repl_1', 'refresh_side'))
        self.ui.side_match_1.textChanged.connect(
            partial(self.handler, 'side_match_1', 'refresh_side'))
        self.ui.side_dest_1.textChanged.connect(
            partial(self.handler, 'side_dest_1', 'refresh_side'))
        self.ui.side_filter_1.textChanged.connect(
            partial(self.handler, 'side_filter_1', 'refresh_side'))
        self.ui.side_pattern_2.textChanged.connect(
            partial(self.handler, 'side_pattern_2', 'refresh_side'))
        self.ui.side_repl_2.textChanged.connect(
            partial(self.handler, 'side_repl_2', 'refresh_side'))
        self.ui.side_match_2.textChanged.connect(
            partial(self.handler, 'side_match_2', 'refresh_side'))
        self.ui.side_dest_2.textChanged.connect(
            partial(self.handler, 'side_dest_2', 'refresh_side'))
        self.ui.side_filter_2.textChanged.connect(
            partial(self.handler, 'side_filter_2', 'refresh_side'))
        self.ui.side_pattern_3.textChanged.connect(
            partial(self.handler, 'side_pattern_3', 'refresh_side'))
        self.ui.side_repl_3.textChanged.connect(
            partial(self.handler, 'side_repl_3', 'refresh_side'))
        self.ui.side_match_3.textChanged.connect(
            partial(self.handler, 'side_match_3', 'refresh_side'))
        self.ui.side_dest_3.textChanged.connect(
            partial(self.handler, 'side_dest_3', 'refresh_side'))
        self.ui.side_filter_3.textChanged.connect(
            partial(self.handler, 'side_filter_3', 'refresh_side'))
        self.ui.side_pattern_4.textChanged.connect(
            partial(self.handler, 'side_pattern_4', 'refresh_side'))
        self.ui.side_repl_4.textChanged.connect(
            partial(self.handler, 'side_repl_4', 'refresh_side'))
        self.ui.side_match_4.textChanged.connect(
            partial(self.handler, 'side_match_4', 'refresh_side'))
        self.ui.side_dest_4.textChanged.connect(
            partial(self.handler, 'side_dest_4', 'refresh_side'))
        self.ui.side_filter_4.textChanged.connect(
            partial(self.handler, 'side_filter_4', 'refresh_side'))
        self.ui.side_pattern_5.textChanged.connect(
            partial(self.handler, 'side_pattern_5', 'refresh_side'))
        self.ui.side_repl_5.textChanged.connect(
            partial(self.handler, 'side_repl_5', 'refresh_side'))
        self.ui.side_match_5.textChanged.connect(
            partial(self.handler, 'side_match_5', 'refresh_side'))
        self.ui.side_dest_5.textChanged.connect(
            partial(self.handler, 'side_dest_5', 'refresh_side'))
        self.ui.side_filter_5.textChanged.connect(
            partial(self.handler, 'side_filter_5', 'refresh_side'))
        self.ui.side_pattern_6.textChanged.connect(
            partial(self.handler, 'side_pattern_6', 'refresh_side'))
        self.ui.side_repl_6.textChanged.connect(
            partial(self.handler, 'side_repl_6', 'refresh_side'))
        self.ui.side_match_6.textChanged.connect(
            partial(self.handler, 'side_match_6', 'refresh_side'))
        self.ui.side_dest_6.textChanged.connect(
            partial(self.handler, 'side_dest_6', 'refresh_side'))
        self.ui.side_filter_6.textChanged.connect(
            partial(self.handler, 'side_filter_6', 'refresh_side'))

        # copy files button
        self.ui.side_copy.clicked.connect(
            partial(self.handler, 'side_copy', 'side_copy'))

        # RENAME
        self.ui.Rename_go.clicked.connect(
            partial(self.handler, 'Rename_go', 'Rename_go'))
        self.ui.rename_reload_after.clicked.connect(
            partial(self.handler, 'rename_reload_after', ''))

        self.ui.rename_filter_01.textChanged.connect(
            partial(self.handler, 'rename_filter_01', 'refresh_rename'))
        self.ui.rename_pattern_01.textChanged.connect(
            partial(self.handler, 'rename_pattern_01', 'refresh_rename'))
        self.ui.rename_repl_01.textChanged.connect(
            partial(self.handler, 'rename_repl_01', 'refresh_rename'))
        self.ui.rename_source_01.valueChanged.connect(
            partial(self.handler, 'rename_source_01', 'refresh_rename'))

        self.ui.rename_filter_02.textChanged.connect(
            partial(self.handler, 'rename_filter_02', 'refresh_rename'))
        self.ui.rename_pattern_02.textChanged.connect(
            partial(self.handler, 'rename_pattern_02', 'refresh_rename'))
        self.ui.rename_repl_02.textChanged.connect(
            partial(self.handler, 'rename_repl_02', 'refresh_rename'))
        self.ui.rename_source_02.valueChanged.connect(
            partial(self.handler, 'rename_source_02', 'refresh_rename'))

        self.ui.rename_filter_03.textChanged.connect(
            partial(self.handler, 'rename_filter_03', 'refresh_rename'))
        self.ui.rename_pattern_03.textChanged.connect(
            partial(self.handler, 'rename_pattern_03', 'refresh_rename'))
        self.ui.rename_repl_03.textChanged.connect(
            partial(self.handler, 'rename_repl_03', 'refresh_rename'))
        self.ui.rename_source_03.valueChanged.connect(
            partial(self.handler, 'rename_source_03', 'refresh_rename'))

        self.ui.rename_filter_04.textChanged.connect(
            partial(self.handler, 'rename_filter_04', 'refresh_rename'))
        self.ui.rename_pattern_04.textChanged.connect(
            partial(self.handler, 'rename_pattern_04', 'refresh_rename'))
        self.ui.rename_repl_04.textChanged.connect(
            partial(self.handler, 'rename_repl_04', 'refresh_rename'))
        self.ui.rename_source_04.valueChanged.connect(
            partial(self.handler, 'rename_source_04', 'refresh_rename'))

        self.ui.rename_filter_05.textChanged.connect(
            partial(self.handler, 'rename_filter_05', 'refresh_rename'))
        self.ui.rename_pattern_05.textChanged.connect(
            partial(self.handler, 'rename_pattern_05', 'refresh_rename'))
        self.ui.rename_repl_05.textChanged.connect(
            partial(self.handler, 'rename_repl_05', 'refresh_rename'))
        self.ui.rename_source_05.valueChanged.connect(
            partial(self.handler, 'rename_source_05', 'refresh_rename'))

        self.ui.rename_filter_06.textChanged.connect(
            partial(self.handler, 'rename_filter_06', 'refresh_rename'))
        self.ui.rename_pattern_06.textChanged.connect(
            partial(self.handler, 'rename_pattern_06', 'refresh_rename'))
        self.ui.rename_repl_06.textChanged.connect(
            partial(self.handler, 'rename_repl_06', 'refresh_rename'))
        self.ui.rename_source_06.valueChanged.connect(
            partial(self.handler, 'rename_source_06', 'refresh_rename'))

        self.ui.rename_filter_07.textChanged.connect(
            partial(self.handler, 'rename_filter_07', 'refresh_rename'))
        self.ui.rename_pattern_07.textChanged.connect(
            partial(self.handler, 'rename_pattern_07', 'refresh_rename'))
        self.ui.rename_repl_07.textChanged.connect(
            partial(self.handler, 'rename_repl_07', 'refresh_rename'))
        self.ui.rename_source_07.valueChanged.connect(
            partial(self.handler, 'rename_source_07', 'refresh_rename'))

        self.ui.rename_filter_08.textChanged.connect(
            partial(self.handler, 'rename_filter_08', 'refresh_rename'))
        self.ui.rename_pattern_08.textChanged.connect(
            partial(self.handler, 'rename_pattern_08', 'refresh_rename'))
        self.ui.rename_repl_08.textChanged.connect(
            partial(self.handler, 'rename_repl_08', 'refresh_rename'))
        self.ui.rename_source_08.valueChanged.connect(
            partial(self.handler, 'rename_source_08', 'refresh_rename'))

        # Ftrack Tab
        self.ui.ftrack_use.clicked.connect(
            partial(self.handler, 'ftrack_use', 'refresh_ftrack'))
        self.ui.ftrack_project.textChanged.connect(
            partial(self.handler, 'ftrack_project', 'refresh_ftrack'))
        self.ui.ftrack_shot.textChanged.connect(
            partial(self.handler, 'ftrack_shot', 'refresh_ftrack'))
        self.ui.ftrack_task.textChanged.connect(
            partial(self.handler, 'ftrack_task', 'refresh_ftrack'))
        self.ui.ftrack_label_use.clicked.connect(
            partial(self.handler, 'ftrack_label_use', 'refresh_ftrack'))
        self.ui.ftrack_label.textChanged.connect(
            partial(self.handler, 'ftrack_label', 'refresh_ftrack'))
        self.ui.ftrack_version_use.clicked.connect(
            partial(self.handler, 'ftrack_version_use', 'refresh_ftrack'))
        self.ui.ftrack_version.textChanged.connect(
            partial(self.handler, 'ftrack_version', 'refresh_ftrack'))
        self.ui.ftrack_note_pattern.textChanged.connect(
            partial(self.handler, 'ftrack_note_pattern', 'select_ftrack'))
        self.ui.ftrack_note_repl.textChanged.connect(
            partial(self.handler, 'ftrack_note_repl', 'select_ftrack'))
        self.ui.ftrack_do_op.clicked.connect(
            partial(self.handler, 'ftrack_do_op', 'refresh_ftrack'))

        # vendor
        self.ui.vendor_csv_path.textChanged.connect(
            partial(self.handler, 'vendor_csv_path', 'refresh_vendor'))
        self.ui.vendor_csv_explore.clicked.connect(
            partial(self.explore_line_edit, self.ui.vendor_csv_path))
        self.ui.vendor_csv_browse.clicked.connect(
            partial(self.browse_line_edit, self.ui.vendor_csv_path, 'csv', "Select Vendor CSV"))

        self.ui.vendor_csv_package_key.textChanged.connect(
            partial(self.handler, 'vendor_csv_package_key', 'refresh_vendor'))
        self.ui.vendor_csv_vendor_key.textChanged.connect(
            partial(self.handler, 'vendor_csv_vendor_key', 'refresh_vendor'))

        self.ui.vendor_csv_ignore.clicked.connect(
            partial(self.handler, 'vendor_csv_ignore', 'refresh_vendor'))
        self.ui.vendor_csv_ftrack.clicked.connect(
            partial(self.handler, 'vendor_csv_ftrack', 'refresh_vendor'))
        self.ui.vendor_csv_skip.clicked.connect(
            partial(self.handler, 'vendor_csv_skip', 'refresh_vendor'))
        self.ui.vendor_csv_skip_by.textChanged.connect(
            partial(self.handler, 'vendor_csv_skip_by', 'refresh_vendor'))
        self.ui.vendor_csv_skip_what.textChanged.connect(
            partial(self.handler, 'vendor_csv_skip_what', 'refresh_vendor'))

        self.ui.vendor_csv_prefs_spreadsheet.textChanged.connect(
            partial(self.handler, 'vendor_csv_prefs_spreadsheet',
                    'refresh_vendor'))
        self.ui.vendor_csv_prefs_repres.textChanged.connect(
            partial(self.handler, 'vendor_csv_prefs_repres',
                    'refresh_vendor'))

        # Convert
        # copy files button
        self.ui.thumbs_convert_now.clicked.connect(
            partial(self.handler, 'thumbs_convert_now', 'thumbs_convert_now'))

        # Spreadsheet
        self.ui.sub_columns.textChanged.connect(
            partial(self.handler, 'sub_columns', 'refresh_spreadsheets'))
        self.ui.sub_exclude.textChanged.connect(
            partial(self.handler, 'sub_exclude', 'refresh_spreadsheets'))
        self.ui.sub_include.textChanged.connect(
            partial(self.handler, 'sub_include', 'refresh_spreadsheets'))

        self.ui.log_columns.textChanged.connect(
            partial(self.handler, 'log_columns', 'refresh_spreadsheets'))
        self.ui.log_exclude.textChanged.connect(
            partial(self.handler, 'log_exclude', 'refresh_spreadsheets'))
        self.ui.log_include.textChanged.connect(
            partial(self.handler, 'log_include', 'refresh_spreadsheets'))

        self.ui.txt_columns.textChanged.connect(
            partial(self.handler, 'txt_columns', 'refresh_spreadsheets'))
        self.ui.txt_exclude.textChanged.connect(
            partial(self.handler, 'txt_exclude', 'refresh_spreadsheets'))
        self.ui.txt_include.textChanged.connect(
            partial(self.handler, 'txt_include', 'refresh_spreadsheets'))

        # Checks Tab
        self.ui.check_sequence_size_consistency.clicked.connect(
            partial(self.handler,
                    'check_sequence_size_consistency', 'refresh_checks'))
        self.ui.check_sequence_holes.clicked.connect(
            partial(self.handler, 'check_sequence_holes', 'refresh_checks'))

        self.ui.check_if_01.textChanged.connect(
            partial(self.handler, 'check_if_01', 'refresh_checks'))
        self.ui.check_check_01.textChanged.connect(
            partial(self.handler, 'check_check_01', 'refresh_checks'))
        self.ui.check_warning_01.clicked.connect(
            partial(self.handler, 'check_warning_01', 'refresh_checks'))
        self.ui.check_error_01.clicked.connect(
            partial(self.handler, 'check_error_01', 'refresh_checks'))
        self.ui.check_message_01.textChanged.connect(
            partial(self.handler, 'check_message_01', 'refresh_checks'))

        self.ui.check_if_02.textChanged.connect(
            partial(self.handler, 'check_if_02', 'refresh_checks'))
        self.ui.check_check_02.textChanged.connect(
            partial(self.handler, 'check_check_02', 'refresh_checks'))
        self.ui.check_warning_02.clicked.connect(
            partial(self.handler, 'check_warning_02', 'refresh_checks'))
        self.ui.check_error_02.clicked.connect(
            partial(self.handler, 'check_error_02', 'refresh_checks'))
        self.ui.check_message_02.textChanged.connect(
            partial(self.handler, 'check_message_02', 'refresh_checks'))

        self.ui.check_if_03.textChanged.connect(
            partial(self.handler, 'check_if_03', 'refresh_checks'))
        self.ui.check_check_03.textChanged.connect(
            partial(self.handler, 'check_check_03', 'refresh_checks'))
        self.ui.check_warning_03.clicked.connect(
            partial(self.handler, 'check_warning_03', 'refresh_checks'))
        self.ui.check_error_03.clicked.connect(
            partial(self.handler, 'check_error_03', 'refresh_checks'))
        self.ui.check_message_03.textChanged.connect(
            partial(self.handler, 'check_message_03', 'refresh_checks'))

        self.ui.check_if_04.textChanged.connect(
            partial(self.handler, 'check_if_04', 'refresh_checks'))
        self.ui.check_check_04.textChanged.connect(
            partial(self.handler, 'check_check_04', 'refresh_checks'))
        self.ui.check_warning_04.clicked.connect(
            partial(self.handler, 'check_warning_04', 'refresh_checks'))
        self.ui.check_error_04.clicked.connect(
            partial(self.handler, 'check_error_04', 'refresh_checks'))
        self.ui.check_message_04.textChanged.connect(
            partial(self.handler, 'check_message_04', 'refresh_checks'))

        self.ui.check_if_05.textChanged.connect(
            partial(self.handler, 'check_if_05', 'refresh_checks'))
        self.ui.check_check_05.textChanged.connect(
            partial(self.handler, 'check_check_05', 'refresh_checks'))
        self.ui.check_warning_05.clicked.connect(
            partial(self.handler, 'check_warning_05', 'refresh_checks'))
        self.ui.check_error_05.clicked.connect(
            partial(self.handler, 'check_error_05', 'refresh_checks'))
        self.ui.check_message_05.textChanged.connect(
            partial(self.handler, 'check_message_05', 'refresh_checks'))

        self.ui.check_if_06.textChanged.connect(
            partial(self.handler, 'check_if_06', 'refresh_checks'))
        self.ui.check_check_06.textChanged.connect(
            partial(self.handler, 'check_check_06', 'refresh_checks'))
        self.ui.check_warning_06.clicked.connect(
            partial(self.handler, 'check_warning_06', 'refresh_checks'))
        self.ui.check_error_06.clicked.connect(
            partial(self.handler, 'check_error_06', 'refresh_checks'))
        self.ui.check_message_06.textChanged.connect(
            partial(self.handler, 'check_message_06', 'refresh_checks'))

        self.ui.check_if_07.textChanged.connect(
            partial(self.handler, 'check_if_07', 'refresh_checks'))
        self.ui.check_check_07.textChanged.connect(
            partial(self.handler, 'check_check_07', 'refresh_checks'))
        self.ui.check_warning_07.clicked.connect(
            partial(self.handler, 'check_warning_07', 'refresh_checks'))
        self.ui.check_error_07.clicked.connect(
            partial(self.handler, 'check_error_07', 'refresh_checks'))
        self.ui.check_message_07.textChanged.connect(
            partial(self.handler, 'check_message_07', 'refresh_checks'))

        self.ui.check_if_08.textChanged.connect(
            partial(self.handler, 'check_if_08', 'refresh_checks'))
        self.ui.check_check_08.textChanged.connect(
            partial(self.handler, 'check_check_08', 'refresh_checks'))
        self.ui.check_warning_08.clicked.connect(
            partial(self.handler, 'check_warning_08', 'refresh_checks'))
        self.ui.check_error_08.clicked.connect(
            partial(self.handler, 'check_error_08', 'refresh_checks'))
        self.ui.check_message_08.textChanged.connect(
            partial(self.handler, 'check_message_08', 'refresh_checks'))

        self.ui.check_if_09.textChanged.connect(
            partial(self.handler, 'check_if_09', 'refresh_checks'))
        self.ui.check_check_09.textChanged.connect(
            partial(self.handler, 'check_check_09', 'refresh_checks'))
        self.ui.check_warning_09.clicked.connect(
            partial(self.handler, 'check_warning_09', 'refresh_checks'))
        self.ui.check_error_09.clicked.connect(
            partial(self.handler, 'check_error_09', 'refresh_checks'))
        self.ui.check_message_09.textChanged.connect(
            partial(self.handler, 'check_message_09', 'refresh_checks'))

        self.ui.check_if_10.textChanged.connect(
            partial(self.handler, 'check_if_10', 'refresh_checks'))
        self.ui.check_check_10.textChanged.connect(
            partial(self.handler, 'check_check_10', 'refresh_checks'))
        self.ui.check_warning_10.clicked.connect(
            partial(self.handler, 'check_warning_10', 'refresh_checks'))
        self.ui.check_error_10.clicked.connect(
            partial(self.handler, 'check_error_10', 'refresh_checks'))
        self.ui.check_message_10.textChanged.connect(
            partial(self.handler, 'check_message_10', 'refresh_checks'))

        self.ui.check_if_11.textChanged.connect(
            partial(self.handler, 'check_if_11', 'refresh_checks'))
        self.ui.check_check_11.textChanged.connect(
            partial(self.handler, 'check_check_11', 'refresh_checks'))
        self.ui.check_warning_11.clicked.connect(
            partial(self.handler, 'check_warning_11', 'refresh_checks'))
        self.ui.check_error_11.clicked.connect(
            partial(self.handler, 'check_error_11', 'refresh_checks'))
        self.ui.check_message_11.textChanged.connect(
            partial(self.handler, 'check_message_11', 'refresh_checks'))

        self.ui.check_if_12.textChanged.connect(
            partial(self.handler, 'check_if_12', 'refresh_checks'))
        self.ui.check_check_12.textChanged.connect(
            partial(self.handler, 'check_check_12', 'refresh_checks'))
        self.ui.check_warning_12.clicked.connect(
            partial(self.handler, 'check_warning_12', 'refresh_checks'))
        self.ui.check_error_12.clicked.connect(
            partial(self.handler, 'check_error_12', 'refresh_checks'))
        self.ui.check_message_12.textChanged.connect(
            partial(self.handler, 'check_message_12', 'refresh_checks'))

        self.ui.check_if_13.textChanged.connect(
            partial(self.handler, 'check_if_13', 'refresh_checks'))
        self.ui.check_check_13.textChanged.connect(
            partial(self.handler, 'check_check_13', 'refresh_checks'))
        self.ui.check_warning_13.clicked.connect(
            partial(self.handler, 'check_warning_13', 'refresh_checks'))
        self.ui.check_error_13.clicked.connect(
            partial(self.handler, 'check_error_13', 'refresh_checks'))
        self.ui.check_message_13.textChanged.connect(
            partial(self.handler, 'check_message_13', 'refresh_checks'))



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
            partial(self.handler, 'prefs_tc_default', 'refresh_parsing'))

        self.ui.prefs_counter_start.valueChanged.connect(
            partial(self.handler, 'prefs_counter_start', 'refresh_parsing'))
        self.ui.prefs_counter_step.valueChanged.connect(
            partial(self.handler, 'prefs_counter_step', 'refresh_parsing'))
        self.ui.prefs_counter_zeroes.valueChanged.connect(
            partial(self.handler, 'prefs_counter_zeroes', 'refresh_parsing'))

        self.ui.prefs_merge_chbx.clicked.connect(
            partial(self.handler, 'prefs_merge_chbx', 'refresh_merge'))
        self.ui.prefs_merge_collapse.clicked.connect(
            partial(self.handler, 'prefs_merge_collapse', 'refresh_merge'))
        self.ui.prefs_merge_sep.textChanged.connect(
            partial(self.handler, 'prefs_merge_sep', 'refresh_merge'))
        self.ui.prefs_merge_sort.textChanged.connect(
            partial(self.handler, 'prefs_merge_sort', 'refresh_merge'))
        self.ui.prefs_merge_order.textChanged.connect(
            partial(self.handler, 'prefs_merge_order', 'refresh_merge'))
        self.ui.prefs_merge_hide.clicked.connect(
            partial(self.handler, 'prefs_merge_hide', 'refresh_merge'))


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
            partial(self.handler,
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
            partial(self.handler,
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
            partial(self.handler, 'text_custom_path', 'refresh_text'))

        self.ui.text_add_titles.clicked.connect(
            partial(self.handler, 'text_add_titles', 'refresh_text'))
        self.ui.text_sep_tab.clicked.connect(
            partial(self.handler, 'text_sep_tab', 'refresh_text'))
        self.ui.text_sep_fixed.clicked.connect(
            partial(self.handler, 'text_sep_fixed', 'refresh_text'))

        self.ui.text_header.textChanged.connect(
            partial(self.handler, 'text_header', 'refresh_text'))
        self.ui.text_footer.textChanged.connect(
            partial(self.handler, 'text_footer', 'refresh_text'))

        # Presets Tab
        self.ui.load_preset_button.clicked.connect(
            partial(self.handler, 'load_preset_button', 'load_preset'))
        self.ui.save_preset_name.textChanged.connect(
            partial(self.handler, 'save_preset_text', 'save_presets'))
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
            partial(self.handler, 'tree_filter_file', 'data_filter'))
        self.ui.tree_filter_key.textChanged.connect(
            partial(self.handler, 'tree_filter_key', 'data_filter'))
        self.ui.tree_filter_value.textChanged.connect(
            partial(self.handler, 'tree_filter_value', 'data_filter'))


        # Ayon Tab
        self.ui.ayon_project.textChanged.connect(
            partial(self.handler, 'ayon_project', 'ayon_changed'))
        self.ui.ayon_prefix.textChanged.connect(
            partial(self.handler, 'ayon_prefix', 'ayon_changed'))
        self.ui.ayon_output_folder.textChanged.connect(
            partial(self.handler, 'ayon_output_folder', 'ayon_changed'))
        self.ui.ayon_path_browse_2.clicked.connect(
            partial(self.browse_line_edit, self.ui.ayon_output_folder, 'dir', "Select Ayon List Output Folder"))

        # Data CSV (Data tab)
        self.ui.data_csv_browse.clicked.connect(self.browse_data_csv)
        self.ui.data_csv_path.textChanged.connect(
            partial(self.handler, 'data_csv_path', 'refresh_data_csv'))
        self.ui.data_csv_latest.clicked.connect(
            partial(self.handler, 'data_csv_latest', 'refresh_data_csv'))
        self.ui.data_enable.clicked.connect(
            partial(self.handler, 'data_enable', 'refresh_data_csv'))

        # Search and Replace CSV
        self.ui.data_csv_browse_2.clicked.connect(
            partial(self.browse_line_edit, self.ui.replace_csv_path, 'csv', "Select Search and Replace CSV"))
        self.ui.replace_csv_path.textChanged.connect(
            partial(self.handler, 'replace_csv_path', 'refresh_replace_csv'))
        self.ui.replace_enable.clicked.connect(
            partial(self.handler, 'replace_enable', 'refresh_replace_csv'))

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
            partial(self.handler, 'ayon_filter_tasktypes', 'ayon_changed_filter'))
        self.ui.ayon_filter_assignees.textChanged.connect(
            partial(self.handler, 'ayon_filter_assignees', 'ayon_changed_filter'))

        self.ui.ayon_package1_chbx.clicked.connect(
            partial(self.handler, 'ayon_package1_chbx', 'ayon_changed_filter'))
        self.ui.ayon_package2_chbx.clicked.connect(
            partial(self.handler, 'ayon_package2_chbx', 'ayon_changed_filter'))
        self.ui.ayon_package3_chbx.clicked.connect(
            partial(self.handler, 'ayon_package3_chbx', 'ayon_changed_filter'))
        self.ui.ayon_package1.textChanged.connect(
            partial(self.handler, 'ayon_package1',
                    'ayon_changed_filter'))
        self.ui.ayon_list1.textChanged.connect(
            partial(self.handler, 'ayon_list1',
                    'ayon_changed_filter'))
        self.ui.ayon_package2.textChanged.connect(
            partial(self.handler, 'ayon_package2',
                    'ayon_changed_filter'))
        self.ui.ayon_list2.textChanged.connect(
            partial(self.handler, 'ayon_list2',
                    'ayon_changed_filter'))
        self.ui.ayon_package3.textChanged.connect(
            partial(self.handler, 'ayon_package3',
                    'ayon_changed_filter'))
        self.ui.ayon_list3.textChanged.connect(
            partial(self.handler, 'ayon_list3',
                    'ayon_changed_filter'))
        self.ui.ayon_export_butt.clicked.connect(
            partial(self.handler, 'ayon_export_butt', 'ayon_export_butt'))
        self.ui.ayon_scan_butt.clicked.connect(
            partial(self.handler, 'ayon_scan_butt', 'ayon_scan'))


        self.ui.tree_filter_value.textChanged.connect(
            partial(self.handler, 'tree_filter_value', 'data_filter'))

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
                    self.ui.package_folder.setText(renamed)
                    self.settings_from_gui()
                    self.data = Sequencer(renamed, sequence_mode='holes_allowed',
                                          gui=self.settings,
                                          more_settings=self.settings_obj, ui=self.ui, headless=self.no_gui)
                    self.show_all()

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
                self.data.ftrack_query()
                self.data.select_ftrack_note()
                self.data.prepare_all_columns()
                self.data.prepare_tables()
                self.show_all()

        if group == 'select_ftrack':
            # Skipping ftrack queries for speed
            if self.data:
                self.data.select_ftrack_note()
                self.data.prepare_all_columns()
                self.data.prepare_tables()
                self.show_all()

        if group == 'refresh_merge':
            if self.data:
                self.data.prepare_all_columns()
                self.data.prepare_tables()
                self.show_all()

        if group == 'refresh_vendor':
            if self.data:

                self.data.vendor_csv_all()
                self.data.vendor_csv_all()
                self.data.transform_data()

                # parse table headers
                self.data.prepare_all_columns()
                # fill tables for export and display
                self.data.prepare_tables()
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
                # sidecar files filter
                self.data.rename_execute()

        if sender == 'write_button':
            # read column widths from tablewidget for excel column sizes
            # there is no way to change excel column sizes by content
            column_widths_sub = []
            if self.data and self.data.column_titles_sub:
                for column_number, one_column in enumerate(self.data.column_titles_sub):
                    column_widths_sub.append(
                        (float(self.ui.sub_table.columnWidth(column_number))))
                column_widths_log = []
                for column_number, one_column in enumerate(self.data.column_titles_log):
                    column_widths_log.append(
                        (float(self.ui.log_table.columnWidth(column_number))))

                self.data.export_all(column_widths_sub, column_widths_log)

        if sender == 'ayon_export_butt':
            target = self._ayon_target()

            def _export():
                target.ayon_data_read(force=True)
                target.ayon_data_filter()
                target.ayon_data_write()
            self._ayon_busy(_export, "Reading Ayon shot list...")

        if group == 'ayon_scan':
            target = self._ayon_target()
            self._ayon_busy(target.ayon_scan, "Scanning Ayon...")
            if target is self.data and self.data.merged_list:
                self.data.prepare_all_columns()
                self.data.prepare_tables()
                self.show_all()

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
                        except:
                            log.error('Error saving preset {}'.format(preset_name))
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
            """
            except:
                log.error('Error reading preset {}'.format(preset_to_load))
            """

        if group == "thumbs_convert_now":
            if self.data is not None:
                self.data.run_converts()

        if group == "data_filter":
            self.show_data()

        if group == "ayon_changed_filter":
            if self.data is not None:
                self.data.ayon_data_filter()
            elif self.ayon_only is not None:
                self.ayon_only.settings = self.settings
                self.ayon_only.ayon_data_filter()

        if group == "tab_pairs":
            self.gui_show_hide_modules()

    def show_data(self):

        if self.data and self.settings:
            _1 = str(self.settings['tree_filter_file']['value'])
            _2 = str(self.settings['tree_filter_key']['value'])
            _3 = str(self.settings['tree_filter_value']['value'])

            # Display merged items as a data tree
            self.ui.data_tree.clear()
            self.ui.data_tree.setColumnCount(3)
            self.ui.data_tree.setHeaderLabels(["#", "key", "value"])
            if self.data.merged_list is not None:
                for one_itm in self.data.merged_list:
                    _ti = QtWidgets.QTreeWidgetItem(self.ui.data_tree)
                    _fn = one_itm.get('part1', '')
                    _fp = one_itm.get('part2', '')
                    if _fp:
                        _l = _fp + '/' + _fn
                    else:
                        _l = _fn
                    _n = "{}: {}".format(str(self.data.merged_list.index(one_itm)), _l)

                    if (not _1) or _1 == "" or (str(_1) in _n):
                        _ti.setText(0, _n)
                        for k, v in sorted(one_itm.items()):
                            _tii = None
                            if (not _2) or _2 == "" or (str(_2) in str(k)):
                                if (not _3) or _3 == "" or (str(_3) in str(v)):
                                    _tii = QtWidgets.QTreeWidgetItem(self.ui.data_tree)
                                    _tii.setText(1, str(k))
                                    _tii.setText(2, str(v))
                                    _ti.addChild(_tii)

    def show_all(self):
        """
        Fill Submission table, drive log table and text with data
        :return:
        """

        if self.data:
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
                self.data.table_rename,
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
        except:
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

            for row, line in enumerate(table):
                # set row color by check list
                color = 'white'

                # sub and log tables have merged list data
                # stored as a last item
                one_item = line[-1]
                if type(one_item) is str:
                    one_item = None

                for column_number, one_column in enumerate(titles):
                    my_title = str(one_column).lstrip().rstrip()
                    try:
                        table_ui.setItem(row,
                                         column_number,
                                         QtWidgets.QTableWidgetItem(str(line[column_number]))
                                         )
                    except:
                        log.error("can't display table row")

                    if one_item:
                    #colorize
                        itm = table_ui.item(row, column_number)
                        color = 'white'
                        _size_warning = one_item.get('size_warning', '')
                        if _size_warning != '':
                            color = 'purple'
                        _warning = one_item.get('warning', '')
                        if _warning != '':
                            color = 'orange'
                        _error = one_item.get('error', '')
                        if _error != '':
                            color = 'red'
                        if itm:
                            if color == 'green':
                                itm.setBackground(QtGui.QColor('darkgreen'))
                            elif color == 'orange':
                                itm.setBackground(QtGui.QColor('sienna'))
                            elif color == 'red':
                                itm.setBackground(QtGui.QColor('maroon'))
                            elif color == 'purple':
                                itm.setBackground(QtGui.QColor('purple'))
                            else:
                                # white
                                itm.setBackground(QtGui.QColor("#4d4d4d"))

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
            except:
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

    def gui_show_hide_modules(self):
        # show / hide tabs
        for checkbox, val in self.tab_pairs.items():
            index = val[0]
            tab_name = val[1]
            chbx = self.settings.get(checkbox)
            if chbx:
                is_on = chbx.get('value', False)
                if is_on:
                    self.ui.TopTab.setTabVisible(index, True)
                else:
                    self.ui.TopTab.setTabVisible(index, False)

        for checkbox, val in self.tab_pairs_bottom.items():
            index = val[0]
            tab_name = val[1]
            chbx = self.settings.get(checkbox)
            if chbx:
                is_on = chbx.get('value', False)
                if is_on:
                    self.ui.BottomTab.setTabVisible(index, True)
                else:
                    self.ui.BottomTab.setTabVisible(index, False)

    def settings_to_gui(self):
        """
        Applies values from self.settings to gui
        """
        def str_to_bool(my_str):
            if my_str == "True":
                _b = True
            elif my_str == "False":
                _b = False
            if my_str == "true":
                _b = True
            elif my_str == "false":
                _b = False
            else:
                _b = bool(my_str)
            return _b

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
                    _index = one_setting['value']
                    if _index.isdigit():
                        if _index <= -1 or _index > len(one_setting['all_items']):
                            pass
                        else:
                            # preselect a combobox value by index
                            obj.setCurrentIndex(_index)
                    else:
                        obj.setCurrentText(_index)
                except:
                    self.log.error("Error restoring QComboBox {}".format(
                        str(obj.objectName())))
            elif isinstance(obj, QtWidgets.QLineEdit):
                try:
                    obj.setText(one_setting['value'])
                except:
                    self.log.error("Error restoring QLineEdit {}".format(
                        str(obj.objectName())))
            elif isinstance(obj, QtWidgets.QCheckBox):
                try:
                    if one_setting['value']:
                        # restore checkbox
                        obj.setChecked(True)
                    else:
                        obj.setChecked(False)
                except:
                    self.log.error("Error restoring QCheckBox {}".format(
                        str(obj.objectName())))
            elif isinstance(obj, QtWidgets.QRadioButton):
                try:
                    if one_setting['value']:
                        obj.setChecked(str_to_bool(one_setting['value']))
                except:
                    self.log.error("Error restoring QRadioButton {}".format(
                        str(obj.objectName())))
            elif isinstance(obj, QtWidgets.QSpinBox):
                try:
                    if one_setting['value']:
                        obj.setValue(int(one_setting['value']))
                except:
                    self.log.error("Error restoring QSpinBox {}".format(
                        str(obj.objectName())))
            elif isinstance(obj, QtWidgets.QSlider):
                try:
                    if one_setting['value']:
                        obj.setValue(int(one_setting['value']))
                except:
                    self.log.error("Error restoring QSlider {}".format(
                        str(obj.objectName())))
            elif isinstance(obj, QtWidgets.QPlainTextEdit):
                try:
                    obj.setPlainText(one_setting['value'])
                except:
                    self.log.error("Error restoring QPlainTextEdit {}".format(
                        str(obj.objectName())))
            else:
                self.log.warning("Error restoring {} {}".format(
                    str(one_setting['category']), str(obj.objectName())))
            obj.blockSignals(False)

    def settings_update(self, knob_name, ui, value, val2=None):
        one_setting = self.settings.get(knob_name)
        if one_setting:
            if one_setting["category"]:
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
                        ui.setChecked(bool(value))
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
            one_setting = self.settings.get(key)
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
        group.setMinimumSize(QtCore.QSize(350, 50))
        group.setMaximumHeight(50)
        pol = group.sizePolicy()
        pol.setVerticalPolicy(QtWidgets.QSizePolicy.Fixed)
        group.setSizePolicy(pol)
        row = QtWidgets.QHBoxLayout(group)
        row.setContentsMargins(6, 2, 6, 2)

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
            "<b>:platePl01:exr</b> - any task</p>"
            "<p>Filters are tried in order, the first one with a match is used, so list the "
            "preferred product first. The latest version of the product is used. "
            "Wildcards * ? are allowed, names are not case sensitive.</p>"
            "<p>Columns added: Product, Product Type, Version, Version Name, Version Status, "
            "Version Author, Version Date, Version Comment, Version Task, Representation, "
            "Repre Path, Version Filter, Version Frame Start / End, Version Handle Start / End, "
            "Version FPS, Version Width / Height, Version Pixel Aspect, Version Step, Version Host, "
            "Version Colorspace (keywords with the Ayon prefix, e.g. {ayon_Version}).</p>")
        ui.ayon_product_filters = filters
        row.addWidget(filters, 1)

        idx = ui.verticalLayout_116.indexOf(ui.groupBox_33)
        ui.verticalLayout_116.insertWidget(idx + 1 if idx >= 0 else -1, group)

        ui.ayon_output_folder.setToolTip(
            "<p>Folder where <b>Export Shot List</b> saves ayon-list.csv, ayon-list-versions.csv "
            "(with Versions CSV) and optionally the thumbnails.</p>")

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
        vtable.setToolTip("Every version of every product of the Ayon folders matched to the "
                          "package files (needs Pull versions). Preferred = picked by the product filters.")
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
  x  ftrack list     write ftrack_shotlist.csv next to the package

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

  (with the built exe, use submission_helper.exe instead of python submission_helper.py)

exit codes:
  0  finished
  1  input or preset not found, or an action crashed
     (many problems are only logged, check the log output)
  2  bad arguments (only one of -i/-p, unknown action letter)
"""


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

# log
# logging is configured in __main__ by sh_logging.setup_logging()
log = logging.getLogger("SubmissionHelper")

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


if __name__ == "__main__":
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
        # allow running on linux render nodes / farm without a display
        if sys.platform.startswith('linux') and not (os.environ.get('DISPLAY') or os.environ.get('WAYLAND_DISPLAY')):
            os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

    app = QtWidgets.QApplication.instance()  # checks if QApplication already exists
    if not app:  # create QApplication if it doesn't exist
        app = QtWidgets.QApplication(sys.argv)

    if headless:
        log.debug('Starting headless')
        settings_obj = Settings(input_preset, args)
        main = MainWindow(no_gui=True, s=settings_obj, package_path=input_path, args=args)
        #main.show()
        app.exec_()
    else:
        log.debug('Starting GUI')
        settings_obj = Settings('last_' + getpass.getuser(), args)
        main = MainWindow(no_gui=False, s=settings_obj, args=args)
        main.show()
        rc = app.exec_()
        sh_logging.uninstall_qt_message_handler(QtCore)
        sys.exit(rc)

