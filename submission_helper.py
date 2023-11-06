import pprint

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

from sequencer import Sequencer
from settings import Settings
import parse_file_name


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

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()

    def dropEvent(self, e):
        for url in e.mimeData().urls():
            file_name = url.toLocalFile()
            self.ui.package_folder.setText(str(file_name))
            #print("Dropped file: " + file_name)

    def __init__(self, no_gui=False, s=None):
        super().__init__()
        self.bare_title = "Submission Helper"

        self.ui = Ui_submission()
        self.ui.setupUi(self)
        self.no_gui = no_gui

        # Settings to gui
        self.ui_start = True
        self.settings_obj = s
        self.settings = self.settings_obj.settings
        self.settings_inst = self.settings_obj.install_settings

        self.settings_to_gui()
        self.settings_update_app_title()
        self.settings_update_dropbox()
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
        self.ui.parse_name_01.textChanged.connect(
            partial(self.handler, 'parse_name_01', 'refresh_parsing'))
        self.ui.parse_name_02.textChanged.connect(
            partial(self.handler, 'parse_name_02', 'refresh_parsing'))
        self.ui.parse_name_03.textChanged.connect(
            partial(self.handler, 'parse_name_03', 'refresh_parsing'))
        self.ui.parse_name_04.textChanged.connect(
            partial(self.handler, 'parse_name_04', 'refresh_parsing'))
        self.ui.parse_name_05.textChanged.connect(
            partial(self.handler, 'parse_name_05', 'refresh_parsing'))
        self.ui.parse_name_06.textChanged.connect(
            partial(self.handler, 'parse_name_06', 'refresh_parsing'))
        self.ui.parse_name_07.textChanged.connect(
            partial(self.handler, 'parse_name_07', 'refresh_parsing'))
        self.ui.parse_name_08.textChanged.connect(
            partial(self.handler, 'parse_name_08', 'refresh_parsing'))
        self.ui.parse_name_09.textChanged.connect(
            partial(self.handler, 'parse_name_09', 'refresh_parsing'))
        self.ui.parse_name_10.textChanged.connect(
            partial(self.handler, 'parse_name_10', 'refresh_parsing'))
        self.ui.parse_name_11.textChanged.connect(
            partial(self.handler, 'parse_name_11', 'refresh_parsing'))
        self.ui.parse_name_12.textChanged.connect(
            partial(self.handler, 'parse_name_12', 'refresh_parsing'))
        self.ui.parse_name_13.textChanged.connect(
            partial(self.handler, 'parse_name_13', 'refresh_parsing'))
        self.ui.parse_name_14.textChanged.connect(
            partial(self.handler, 'parse_name_14', 'refresh_parsing'))
        self.ui.parse_name_15.textChanged.connect(
            partial(self.handler, 'parse_name_15', 'refresh_parsing'))
        self.ui.parse_name_16.textChanged.connect(
            partial(self.handler, 'parse_name_16', 'refresh_parsing'))
        self.ui.parse_name_17.textChanged.connect(
            partial(self.handler, 'parse_name_01', 'refresh_parsing'))
        self.ui.parse_name_18.textChanged.connect(
            partial(self.handler, 'parse_name_02', 'refresh_parsing'))
        self.ui.parse_name_19.textChanged.connect(
            partial(self.handler, 'parse_name_03', 'refresh_parsing'))
        self.ui.parse_name_20.textChanged.connect(
            partial(self.handler, 'parse_name_04', 'refresh_parsing'))
        self.ui.parse_name_21.textChanged.connect(
            partial(self.handler, 'parse_name_05', 'refresh_parsing'))
        self.ui.parse_name_22.textChanged.connect(
            partial(self.handler, 'parse_name_06', 'refresh_parsing'))
        self.ui.parse_name_23.textChanged.connect(
            partial(self.handler, 'parse_name_07', 'refresh_parsing'))
        self.ui.parse_name_24.textChanged.connect(
            partial(self.handler, 'parse_name_08', 'refresh_parsing'))
        self.ui.parse_name_25.textChanged.connect(
            partial(self.handler, 'parse_name_09', 'refresh_parsing'))
        self.ui.parse_name_26.textChanged.connect(
            partial(self.handler, 'parse_name_10', 'refresh_parsing'))
        self.ui.parse_name_27.textChanged.connect(
            partial(self.handler, 'parse_name_11', 'refresh_parsing'))
        self.ui.parse_name_28.textChanged.connect(
            partial(self.handler, 'parse_name_12', 'refresh_parsing'))
        self.ui.parse_name_29.textChanged.connect(
            partial(self.handler, 'parse_name_13', 'refresh_parsing'))
        self.ui.parse_name_30.textChanged.connect(
            partial(self.handler, 'parse_name_14', 'refresh_parsing'))
        self.ui.parse_name_31.textChanged.connect(
            partial(self.handler, 'parse_name_15', 'refresh_parsing'))
        self.ui.parse_name_32.textChanged.connect(
            partial(self.handler, 'parse_name_16', 'refresh_parsing'))

        self.ui.parse_pattern_01.textChanged.connect(
            partial(self.handler, 'parse_pattern_01', 'refresh_parsing'))
        self.ui.parse_pattern_02.textChanged.connect(
            partial(self.handler, 'parse_pattern_02', 'refresh_parsing'))
        self.ui.parse_pattern_03.textChanged.connect(
            partial(self.handler, 'parse_pattern_03', 'refresh_parsing'))
        self.ui.parse_pattern_04.textChanged.connect(
            partial(self.handler, 'parse_pattern_04', 'refresh_parsing'))
        self.ui.parse_pattern_05.textChanged.connect(
            partial(self.handler, 'parse_pattern_05', 'refresh_parsing'))
        self.ui.parse_pattern_06.textChanged.connect(
            partial(self.handler, 'parse_pattern_06', 'refresh_parsing'))
        self.ui.parse_pattern_07.textChanged.connect(
            partial(self.handler, 'parse_pattern_07', 'refresh_parsing'))
        self.ui.parse_pattern_08.textChanged.connect(
            partial(self.handler, 'parse_pattern_08', 'refresh_parsing'))
        self.ui.parse_pattern_09.textChanged.connect(
            partial(self.handler, 'parse_pattern_09', 'refresh_parsing'))
        self.ui.parse_pattern_10.textChanged.connect(
            partial(self.handler, 'parse_pattern_10', 'refresh_parsing'))
        self.ui.parse_pattern_11.textChanged.connect(
            partial(self.handler, 'parse_pattern_11', 'refresh_parsing'))
        self.ui.parse_pattern_12.textChanged.connect(
            partial(self.handler, 'parse_pattern_12', 'refresh_parsing'))
        self.ui.parse_pattern_13.textChanged.connect(
            partial(self.handler, 'parse_pattern_13', 'refresh_parsing'))
        self.ui.parse_pattern_14.textChanged.connect(
            partial(self.handler, 'parse_pattern_14', 'refresh_parsing'))
        self.ui.parse_pattern_15.textChanged.connect(
            partial(self.handler, 'parse_pattern_15', 'refresh_parsing'))
        self.ui.parse_pattern_16.textChanged.connect(
            partial(self.handler, 'parse_pattern_16', 'refresh_parsing'))
        self.ui.parse_pattern_17.textChanged.connect(
            partial(self.handler, 'parse_pattern_01', 'refresh_parsing'))
        self.ui.parse_pattern_18.textChanged.connect(
            partial(self.handler, 'parse_pattern_02', 'refresh_parsing'))
        self.ui.parse_pattern_19.textChanged.connect(
            partial(self.handler, 'parse_pattern_03', 'refresh_parsing'))
        self.ui.parse_pattern_20.textChanged.connect(
            partial(self.handler, 'parse_pattern_04', 'refresh_parsing'))
        self.ui.parse_pattern_21.textChanged.connect(
            partial(self.handler, 'parse_pattern_05', 'refresh_parsing'))
        self.ui.parse_pattern_22.textChanged.connect(
            partial(self.handler, 'parse_pattern_06', 'refresh_parsing'))
        self.ui.parse_pattern_23.textChanged.connect(
            partial(self.handler, 'parse_pattern_07', 'refresh_parsing'))
        self.ui.parse_pattern_24.textChanged.connect(
            partial(self.handler, 'parse_pattern_08', 'refresh_parsing'))
        self.ui.parse_pattern_25.textChanged.connect(
            partial(self.handler, 'parse_pattern_09', 'refresh_parsing'))
        self.ui.parse_pattern_26.textChanged.connect(
            partial(self.handler, 'parse_pattern_10', 'refresh_parsing'))
        self.ui.parse_pattern_27.textChanged.connect(
            partial(self.handler, 'parse_pattern_11', 'refresh_parsing'))
        self.ui.parse_pattern_28.textChanged.connect(
            partial(self.handler, 'parse_pattern_12', 'refresh_parsing'))
        self.ui.parse_pattern_29.textChanged.connect(
            partial(self.handler, 'parse_pattern_13', 'refresh_parsing'))
        self.ui.parse_pattern_30.textChanged.connect(
            partial(self.handler, 'parse_pattern_14', 'refresh_parsing'))
        self.ui.parse_pattern_32.textChanged.connect(
            partial(self.handler, 'parse_pattern_15', 'refresh_parsing'))
        self.ui.parse_pattern_32.textChanged.connect(
            partial(self.handler, 'parse_pattern_16', 'refresh_parsing'))

        self.ui.parse_repl_01.textChanged.connect(
            partial(self.handler, 'parse_repl_01', 'refresh_parsing'))
        self.ui.parse_repl_02.textChanged.connect(
            partial(self.handler, 'parse_repl_02', 'refresh_parsing'))
        self.ui.parse_repl_03.textChanged.connect(
            partial(self.handler, 'parse_repl_03', 'refresh_parsing'))
        self.ui.parse_repl_04.textChanged.connect(
            partial(self.handler, 'parse_repl_04', 'refresh_parsing'))
        self.ui.parse_repl_05.textChanged.connect(
            partial(self.handler, 'parse_repl_05', 'refresh_parsing'))
        self.ui.parse_repl_06.textChanged.connect(
            partial(self.handler, 'parse_repl_06', 'refresh_parsing'))
        self.ui.parse_repl_07.textChanged.connect(
            partial(self.handler, 'parse_repl_07', 'refresh_parsing'))
        self.ui.parse_repl_08.textChanged.connect(
            partial(self.handler, 'parse_repl_08', 'refresh_parsing'))
        self.ui.parse_repl_09.textChanged.connect(
            partial(self.handler, 'parse_repl_09', 'refresh_parsing'))
        self.ui.parse_repl_10.textChanged.connect(
            partial(self.handler, 'parse_repl_10', 'refresh_parsing'))
        self.ui.parse_repl_11.textChanged.connect(
            partial(self.handler, 'parse_repl_11', 'refresh_parsing'))
        self.ui.parse_repl_12.textChanged.connect(
            partial(self.handler, 'parse_repl_12', 'refresh_parsing'))
        self.ui.parse_repl_13.textChanged.connect(
            partial(self.handler, 'parse_repl_13', 'refresh_parsing'))
        self.ui.parse_repl_14.textChanged.connect(
            partial(self.handler, 'parse_repl_14', 'refresh_parsing'))
        self.ui.parse_repl_15.textChanged.connect(
            partial(self.handler, 'parse_repl_15', 'refresh_parsing'))
        self.ui.parse_repl_16.textChanged.connect(
            partial(self.handler, 'parse_repl_16', 'refresh_parsing'))
        self.ui.parse_repl_17.textChanged.connect(
            partial(self.handler, 'parse_repl_01', 'refresh_parsing'))
        self.ui.parse_repl_18.textChanged.connect(
            partial(self.handler, 'parse_repl_02', 'refresh_parsing'))
        self.ui.parse_repl_19.textChanged.connect(
            partial(self.handler, 'parse_repl_03', 'refresh_parsing'))
        self.ui.parse_repl_20.textChanged.connect(
            partial(self.handler, 'parse_repl_04', 'refresh_parsing'))
        self.ui.parse_repl_21.textChanged.connect(
            partial(self.handler, 'parse_repl_05', 'refresh_parsing'))
        self.ui.parse_repl_22.textChanged.connect(
            partial(self.handler, 'parse_repl_06', 'refresh_parsing'))
        self.ui.parse_repl_23.textChanged.connect(
            partial(self.handler, 'parse_repl_07', 'refresh_parsing'))
        self.ui.parse_repl_24.textChanged.connect(
            partial(self.handler, 'parse_repl_08', 'refresh_parsing'))
        self.ui.parse_repl_25.textChanged.connect(
            partial(self.handler, 'parse_repl_09', 'refresh_parsing'))
        self.ui.parse_repl_26.textChanged.connect(
            partial(self.handler, 'parse_repl_10', 'refresh_parsing'))
        self.ui.parse_repl_27.textChanged.connect(
            partial(self.handler, 'parse_repl_11', 'refresh_parsing'))
        self.ui.parse_repl_28.textChanged.connect(
            partial(self.handler, 'parse_repl_12', 'refresh_parsing'))
        self.ui.parse_repl_29.textChanged.connect(
            partial(self.handler, 'parse_repl_13', 'refresh_parsing'))
        self.ui.parse_repl_30.textChanged.connect(
            partial(self.handler, 'parse_repl_14', 'refresh_parsing'))
        self.ui.parse_repl_31.textChanged.connect(
            partial(self.handler, 'parse_repl_15', 'refresh_parsing'))
        self.ui.parse_repl_32.textChanged.connect(
            partial(self.handler, 'parse_repl_16', 'refresh_parsing'))

        self.ui.parse_source_01.textChanged.connect(
            partial(self.handler, 'parse_source_01', 'refresh_parsing'))
        self.ui.parse_source_02.textChanged.connect(
            partial(self.handler, 'parse_source_02', 'refresh_parsing'))
        self.ui.parse_source_03.textChanged.connect(
            partial(self.handler, 'parse_source_03', 'refresh_parsing'))
        self.ui.parse_source_04.textChanged.connect(
            partial(self.handler, 'parse_source_04', 'refresh_parsing'))
        self.ui.parse_source_05.textChanged.connect(
            partial(self.handler, 'parse_source_05', 'refresh_parsing'))
        self.ui.parse_source_06.textChanged.connect(
            partial(self.handler, 'parse_source_06', 'refresh_parsing'))
        self.ui.parse_source_07.textChanged.connect(
            partial(self.handler, 'parse_source_07', 'refresh_parsing'))
        self.ui.parse_source_08.textChanged.connect(
            partial(self.handler, 'parse_source_08', 'refresh_parsing'))
        self.ui.parse_source_09.textChanged.connect(
            partial(self.handler, 'parse_source_09', 'refresh_parsing'))
        self.ui.parse_source_10.textChanged.connect(
            partial(self.handler, 'parse_source_10', 'refresh_parsing'))
        self.ui.parse_source_11.textChanged.connect(
            partial(self.handler, 'parse_source_11', 'refresh_parsing'))
        self.ui.parse_source_12.textChanged.connect(
            partial(self.handler, 'parse_source_12', 'refresh_parsing'))
        self.ui.parse_source_13.textChanged.connect(
            partial(self.handler, 'parse_source_13', 'refresh_parsing'))
        self.ui.parse_source_14.textChanged.connect(
            partial(self.handler, 'parse_source_14', 'refresh_parsing'))
        self.ui.parse_source_15.textChanged.connect(
            partial(self.handler, 'parse_source_15', 'refresh_parsing'))
        self.ui.parse_source_16.textChanged.connect(
            partial(self.handler, 'parse_source_16', 'refresh_parsing'))
        self.ui.parse_source_17.textChanged.connect(
            partial(self.handler, 'parse_source_01', 'refresh_parsing'))
        self.ui.parse_source_18.textChanged.connect(
            partial(self.handler, 'parse_source_02', 'refresh_parsing'))
        self.ui.parse_source_19.textChanged.connect(
            partial(self.handler, 'parse_source_03', 'refresh_parsing'))
        self.ui.parse_source_20.textChanged.connect(
            partial(self.handler, 'parse_source_04', 'refresh_parsing'))
        self.ui.parse_source_21.textChanged.connect(
            partial(self.handler, 'parse_source_05', 'refresh_parsing'))
        self.ui.parse_source_22.textChanged.connect(
            partial(self.handler, 'parse_source_06', 'refresh_parsing'))
        self.ui.parse_source_23.textChanged.connect(
            partial(self.handler, 'parse_source_07', 'refresh_parsing'))
        self.ui.parse_source_24.textChanged.connect(
            partial(self.handler, 'parse_source_08', 'refresh_parsing'))
        self.ui.parse_source_25.textChanged.connect(
            partial(self.handler, 'parse_source_09', 'refresh_parsing'))
        self.ui.parse_source_26.textChanged.connect(
            partial(self.handler, 'parse_source_10', 'refresh_parsing'))
        self.ui.parse_source_27.textChanged.connect(
            partial(self.handler, 'parse_source_11', 'refresh_parsing'))
        self.ui.parse_source_28.textChanged.connect(
            partial(self.handler, 'parse_source_12', 'refresh_parsing'))
        self.ui.parse_source_29.textChanged.connect(
            partial(self.handler, 'parse_source_13', 'refresh_parsing'))
        self.ui.parse_source_30.textChanged.connect(
            partial(self.handler, 'parse_source_14', 'refresh_parsing'))
        self.ui.parse_source_31.textChanged.connect(
            partial(self.handler, 'parse_source_15', 'refresh_parsing'))
        self.ui.parse_source_32.textChanged.connect(
            partial(self.handler, 'parse_source_16', 'refresh_parsing'))

        # Sidecar Tab
        self.ui.side_folder.textChanged.connect(
            partial(self.handler, 'side_folder', 'refresh_side_files'))
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
            partial(self.handler, 'vendor_csv_explore', 'refresh_vendor'))
        self.ui.vendor_csv_browse.clicked.connect(
            partial(self.handler, 'vendor_csv_browse', 'refresh_vendor'))

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

        self.ui.check_if_1.textChanged.connect(
            partial(self.handler, 'check_if_1', 'refresh_checks'))
        self.ui.check_check_1.textChanged.connect(
            partial(self.handler, 'check_check_1', 'refresh_checks'))
        self.ui.check_warning_1.clicked.connect(
            partial(self.handler, 'check_warning_1', 'refresh_checks'))
        self.ui.check_error_1.clicked.connect(
            partial(self.handler, 'check_error_1', 'refresh_checks'))
        self.ui.check_message_1.textChanged.connect(
            partial(self.handler, 'check_message_1', 'refresh_checks'))

        self.ui.check_if_2.textChanged.connect(
            partial(self.handler, 'check_if_2', 'refresh_checks'))
        self.ui.check_check_2.textChanged.connect(
            partial(self.handler, 'check_check_2', 'refresh_checks'))
        self.ui.check_warning_2.clicked.connect(
            partial(self.handler, 'check_warning_2', 'refresh_checks'))
        self.ui.check_error_2.clicked.connect(
            partial(self.handler, 'check_error_2', 'refresh_checks'))
        self.ui.check_message_2.textChanged.connect(
            partial(self.handler, 'check_message_2', 'refresh_checks'))

        self.ui.check_if_3.textChanged.connect(
            partial(self.handler, 'check_if_3', 'refresh_checks'))
        self.ui.check_check_3.textChanged.connect(
            partial(self.handler, 'check_check_3', 'refresh_checks'))
        self.ui.check_warning_3.clicked.connect(
            partial(self.handler, 'check_warning_3', 'refresh_checks'))
        self.ui.check_error_3.clicked.connect(
            partial(self.handler, 'check_error_3', 'refresh_checks'))
        self.ui.check_message_3.textChanged.connect(
            partial(self.handler, 'check_message_3', 'refresh_checks'))

        self.ui.check_if_4.textChanged.connect(
            partial(self.handler, 'check_if_4', 'refresh_checks'))
        self.ui.check_check_4.textChanged.connect(
            partial(self.handler, 'check_check_4', 'refresh_checks'))
        self.ui.check_warning_4.clicked.connect(
            partial(self.handler, 'check_warning_4', 'refresh_checks'))
        self.ui.check_error_4.clicked.connect(
            partial(self.handler, 'check_error_4', 'refresh_checks'))
        self.ui.check_message_4.textChanged.connect(
            partial(self.handler, 'check_message_4', 'refresh_checks'))

        self.ui.check_if_5.textChanged.connect(
            partial(self.handler, 'check_if_5', 'refresh_checks'))
        self.ui.check_check_5.textChanged.connect(
            partial(self.handler, 'check_check_5', 'refresh_checks'))
        self.ui.check_warning_5.clicked.connect(
            partial(self.handler, 'check_warning_5', 'refresh_checks'))
        self.ui.check_error_5.clicked.connect(
            partial(self.handler, 'check_error_5', 'refresh_checks'))
        self.ui.check_message_5.textChanged.connect(
            partial(self.handler, 'check_message_5', 'refresh_checks'))

        self.ui.check_if_6.textChanged.connect(
            partial(self.handler, 'check_if_6', 'refresh_checks'))
        self.ui.check_check_6.textChanged.connect(
            partial(self.handler, 'check_check_6', 'refresh_checks'))
        self.ui.check_warning_6.clicked.connect(
            partial(self.handler, 'check_warning_6', 'refresh_checks'))
        self.ui.check_error_6.clicked.connect(
            partial(self.handler, 'check_error_6', 'refresh_checks'))
        self.ui.check_message_6.textChanged.connect(
            partial(self.handler, 'check_message_6', 'refresh_checks'))

        self.ui.check_if_7.textChanged.connect(
            partial(self.handler, 'check_if_7', 'refresh_checks'))
        self.ui.check_check_7.textChanged.connect(
            partial(self.handler, 'check_check_7', 'refresh_checks'))
        self.ui.check_warning_7.clicked.connect(
            partial(self.handler, 'check_warning_7', 'refresh_checks'))
        self.ui.check_error_7.clicked.connect(
            partial(self.handler, 'check_error_7', 'refresh_checks'))
        self.ui.check_message_7.textChanged.connect(
            partial(self.handler, 'check_message_7', 'refresh_checks'))

        self.ui.check_if_8.textChanged.connect(
            partial(self.handler, 'check_if_8', 'refresh_checks'))
        self.ui.check_check_8.textChanged.connect(
            partial(self.handler, 'check_check_8', 'refresh_checks'))
        self.ui.check_warning_8.clicked.connect(
            partial(self.handler, 'check_warning_8', 'refresh_checks'))
        self.ui.check_error_8.clicked.connect(
            partial(self.handler, 'check_error_8', 'refresh_checks'))
        self.ui.check_message_8.textChanged.connect(
            partial(self.handler, 'check_message_8', 'refresh_checks'))

        self.ui.check_if_9.textChanged.connect(
            partial(self.handler, 'check_if_9', 'refresh_checks'))
        self.ui.check_check_9.textChanged.connect(
            partial(self.handler, 'check_check_9', 'refresh_checks'))
        self.ui.check_warning_9.clicked.connect(
            partial(self.handler, 'check_warning_9', 'refresh_checks'))
        self.ui.check_error_9.clicked.connect(
            partial(self.handler, 'check_error_9', 'refresh_checks'))
        self.ui.check_message_9.textChanged.connect(
            partial(self.handler, 'check_message_9', 'refresh_checks'))

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

        # GO button
        self.ui.write_button.clicked.connect(
            partial(self.handler, 'write_button', 'write'))

        # preset name is empty, disable save button
        self.ui.save_preset_button.setEnabled(False)


    def handler(self, sender, group, *more):
        """

        """
        log.debug("-> handler sender: {}, group: {}".format(
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
            #self.ui.setUpdatesEnabled(False)
            pth = str(self.settings['package_folder']['value']).replace('\\', '/')
            if os.path.isfile(pth):
                self.settings_update("package_folder", self.ui.package_folder,
                                     value=os.path.dirname(pth).replace('\\', '/'))
                if pth.endswith('.csv'):
                    if bool(self.settings['vendor_csv_path_detect']['value']):
                        self.settings_update("vendor_csv_path",
                                             self.ui.vendor_csv_path,
                                             value=pth)
            #self.ui.setUpdatesEnabled(True)
            self.data = Sequencer(pth, sequence_mode='holes_allowed', gui=self.settings, more_settings=self.settings_inst)
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
                                          more_settings=self.settings_inst)
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

        if group == 'refresh_text':
            if self.data:
                self.data.transform_data()
                self.show_all()

        if group == 'refresh_checks':
            if self.data:
                self.data.run_checks()
                self.show_all()

        if group == 'refresh_size_checks':
            if self.data:
                self.data.clear_errors()
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

        if sender == 'side_copy':
            if self.data:
                # sidecar files filter
                self.data.sidecar_files_copy()

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

        if sender == 'preset_explore':
            self.expore_local_presets()

        if sender == 'package_explore':
            self.expore_package()

        if group == 'save_presets':
            preset_name = str(self.ui.save_preset_name.displayText())
            if preset_name and preset_name != '':
                self.ui.save_preset_button.setEnabled(True)
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
                self.ui.save_preset_button.setEnabled(False)

        if group == 'load_preset':
            preset_to_load = ''
            """
            try:
            """
            index = int(self.ui.load_preset_combobox.currentIndex())
            preset_to_load = str(self.settings_obj.preset_names[index])

            self.settings_obj.read(preset_to_load)
            self.settings = self.settings_obj.settings
            self.settings_to_gui()
            self.settings_update_app_title()
            self.settings_update_dropbox()
            """
            except:
                log.error('Error reading preset {}'.format(preset_to_load))
            """

        if group == "thumbs_convert_now":
            self.data.run_converts()

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

            # display Package name
            _preview = self.data.output.get('package_name', '')
            self.ui.name_preview.setText(_preview)

            # Display merged items as a data tree
            self.ui.data_tree.clear()
            self.ui.data_tree.setColumnCount(3)
            self.ui.data_tree.setHeaderLabels(["#", "key", "value"])
            for one_itm in self.data.merged_list:
                _ti = QtWidgets.QTreeWidgetItem(self.ui.data_tree)
                _fn = one_itm.get('part1', '')
                _fp = one_itm.get('part2', '')
                if _fp:
                    _l = _fp + '/' + _fn
                else:
                    _l = _fn
                _n = "{}: {}".format(str(self.data.merged_list.index(one_itm)), _l)
                _ti.setText(0, _n)
                for k, v in one_itm.items():
                    _tii = QtWidgets.QTreeWidgetItem(self.ui.data_tree)
                    _tii.setText(1, str(k))
                    _tii.setText(2, str(v))
                    _ti.addChild(_tii)

    def explore(self, path):

        log.debug('-> explore')

        platform = 'win'
        if sys.platform.startswith('darwin'):
            platform = 'mac'
        elif str(os.name).startswith('posix'):
            platform = 'nix'

        if path and path != '' and os.path.exists(path):
            if platform == 'win':
                if os.path.isdir(path):
                    path = path + '/'
                subprocess.Popen('explorer /root,  \"' + path.replace('/', '\\') + '\"')
            if platform == 'mac':
                subprocess.call(['open', "-R", path])
            if platform == 'nix':
                subprocess.call(('xdg-open', path))

    def browse(self, start_path):

        log.debug('-> browse')

        if start_path is None or not os.path.exists(start_path):
            start_path = os.path.expanduser('~')
            if start_path is None:
                start_path = ''
        dir_name = QtWidgets.QFileDialog.getExistingDirectory(None, "Select Folder", start_path,
                                                              QtWidgets.QFileDialog.ShowDirsOnly)
        if dir_name:
            dir_name.replace('\\', '/')
        return dir_name

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
        logging.debug('-> settings_from_gui')
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
        for my_name, obj in inspect.getmembers(self.ui):
            name = my_name
            if isinstance(obj, QtWidgets.QComboBox):
                all_items = [obj.itemText(i) for i in range(obj.count())]
                # get current index from combobox
                index = int(obj.currentIndex())
                self.settings.update({name: {
                                            'category': 'combobox',
                                            'value': index,
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

        logging.debug('-> settings_to_gui')
        skip_names = [
            'package_folder',
            'name_preview',
            'load_preset_combobox',
            'save_preset_name',
            'global_prefs_path',
            'global_prefs_enabled',
            'ffprobe_path'
        ]
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
                    if _index <= -1 or _index > len(one_setting['all_items']):
                        pass
                    else:
                        # preselect a combobox value by index
                        obj.setCurrentIndex(_index)
                except:
                    logging.error("Error restoring QComboBox {}".format(
                        str(obj.objectName())))
            elif isinstance(obj, QtWidgets.QLineEdit):
                try:
                    obj.setText(one_setting['value'])
                except:
                    logging.error("Error restoring QLineEdit {}".format(
                        str(obj.objectName())))
            elif isinstance(obj, QtWidgets.QCheckBox):
                try:
                    if one_setting['value']:
                        # restore checkbox
                        obj.setChecked(True)
                    else:
                        obj.setChecked(False)
                except:
                    logging.error("Error restoring QCheckBox {}".format(
                        str(obj.objectName())))
            elif isinstance(obj, QtWidgets.QRadioButton):
                try:
                    if one_setting['value']:
                        obj.setChecked(str_to_bool(one_setting['value']))
                except:
                    logging.error("Error restoring QRadioButton {}".format(
                        str(obj.objectName())))
            elif isinstance(obj, QtWidgets.QSpinBox):
                try:
                    if one_setting['value']:
                        obj.setValue(int(one_setting['value']))
                except:
                    logging.error("Error restoring QSpinBox {}".format(
                        str(obj.objectName())))
            elif isinstance(obj, QtWidgets.QSlider):
                try:
                    if one_setting['value']:
                        obj.setValue(int(one_setting['value']))
                except:
                    logging.error("Error restoring QSlider {}".format(
                        str(obj.objectName())))
            elif isinstance(obj, QtWidgets.QPlainTextEdit):
                try:
                    obj.setPlainText(one_setting['value'])
                except:
                    logging.error("Error restoring QPlainTextEdit {}".format(
                        str(obj.objectName())))
            else:
                logging.warning("Error restoring {} {}".format(
                    str(one_setting['category']), str(obj.objectName())))
            obj.blockSignals(False)

    def settings_update(self, knob_name, ui, value, val2=None, no_gui=False):
        one_setting = self.settings.get(knob_name)
        if one_setting:
            if one_setting["category"]:
                one_setting["value"] = str(value)
                if one_setting["category"] == "lineedit" or\
                        one_setting["category"] == "plaintextedit":
                    if not no_gui:
                        ui.setText(value)
                elif one_setting["category"] == "checkbox" or\
                        one_setting["category"] == "radiobutton":
                    if not no_gui:
                        ui.setChecked(bool(value))
                elif one_setting["category"] == "spinbox":
                    if not no_gui:
                        ui.setValue(int(value))
                elif one_setting["category"] == "combobox":
                    pass

    def get_user_name(self):
        return getpass.getuser()

    def closeEvent(self, event):
        self.settings_from_gui()
        self.settings_obj.settings = self.settings
        _last_prefs = 'last_' + self.get_user_name()
        self.settings_obj.write(_last_prefs)
        log.info('Writing {}'.format(_last_prefs))
        log.info('Finished')
        # prevents second call
        sys.exit()

if __name__ == "__main__":
    # log
    log = logging.getLogger("mylog")
    log.setLevel(logging.DEBUG)
    """
    logging.basicConfig(filename=os.path.join(self.settings_get_user_settings_path(),
                                              'SubmissionHelperLog.log').replace('\\', '/'), level=logging.DEBUG)
    """
    log.info('Started at: ' + time.strftime("%Y-%m-%d, %H:%M"))


    # Settings
    settings_obj = Settings('last_' + getpass.getuser())

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Plastique")

    app = app.instance()  # checks if QApplication already exists
    if not app:  # create QApplication if it doesn't exist
        app = QtWidgets.QApplication([])
    main = MainWindow(no_gui=False, s=settings_obj)
    main.show()
    app.exec_()
