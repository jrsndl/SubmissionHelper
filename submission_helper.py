import sys
import os
import subprocess
import inspect
from functools import partial
import xlsxwriter
import logging
import time

from PySide2 import QtCore, QtGui, QtWidgets

from ui_Submission import Ui_submission

from sequencer import Sequencer
from settings import Settings
import parse_file_name
import pprint


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
            print("Dropped file: " + file_name)

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
            partial(self.handler, 'shot_explore', 'explore'))
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

        self.ui.name_rename_auto.clicked.connect(
            partial(self.handler, 'name_rename_auto', 'package_rename'))
        self.ui.name_rename_auto.clicked.connect(
            partial(self.handler, 'name_rename_auto', 'package_rename'))

        # Parsing Tab
        self.ui.parse_name_1.textChanged.connect(
            partial(self.handler, 'parse_name_1', 'refresh_parsing'))
        self.ui.parse_name_2.textChanged.connect(
            partial(self.handler, 'parse_name_2', 'refresh_parsing'))
        self.ui.parse_name_3.textChanged.connect(
            partial(self.handler, 'parse_name_3', 'refresh_parsing'))
        self.ui.parse_name_4.textChanged.connect(
            partial(self.handler, 'parse_name_4', 'refresh_parsing'))
        self.ui.parse_name_5.textChanged.connect(
            partial(self.handler, 'parse_name_5', 'refresh_parsing'))
        self.ui.parse_name_6.textChanged.connect(
            partial(self.handler, 'parse_name_6', 'refresh_parsing'))
        self.ui.parse_name_7.textChanged.connect(
            partial(self.handler, 'parse_name_7', 'refresh_parsing'))
        self.ui.parse_name_8.textChanged.connect(
            partial(self.handler, 'parse_name_8', 'refresh_parsing'))
        self.ui.parse_name_9.textChanged.connect(
            partial(self.handler, 'parse_name_9', 'refresh_parsing'))

        self.ui.parse_pattern_1.textChanged.connect(
            partial(self.handler, 'parse_pattern_1', 'refresh_parsing'))
        self.ui.parse_pattern_2.textChanged.connect(
            partial(self.handler, 'parse_pattern_2', 'refresh_parsing'))
        self.ui.parse_pattern_3.textChanged.connect(
            partial(self.handler, 'parse_pattern_3', 'refresh_parsing'))
        self.ui.parse_pattern_4.textChanged.connect(
            partial(self.handler, 'parse_pattern_4', 'refresh_parsing'))
        self.ui.parse_pattern_5.textChanged.connect(
            partial(self.handler, 'parse_pattern_5', 'refresh_parsing'))
        self.ui.parse_pattern_6.textChanged.connect(
            partial(self.handler, 'parse_pattern_6', 'refresh_parsing'))
        self.ui.parse_pattern_7.textChanged.connect(
            partial(self.handler, 'parse_pattern_7', 'refresh_parsing'))
        self.ui.parse_pattern_8.textChanged.connect(
            partial(self.handler, 'parse_pattern_8', 'refresh_parsing'))
        self.ui.parse_pattern_9.textChanged.connect(
            partial(self.handler, 'parse_pattern_9', 'refresh_parsing'))

        self.ui.parse_repl_1.textChanged.connect(
            partial(self.handler, 'parse_repl_1', 'refresh_parsing'))
        self.ui.parse_repl_2.textChanged.connect(
            partial(self.handler, 'parse_repl_2', 'refresh_parsing'))
        self.ui.parse_repl_3.textChanged.connect(
            partial(self.handler, 'parse_repl_3', 'refresh_parsing'))
        self.ui.parse_repl_4.textChanged.connect(
            partial(self.handler, 'parse_repl_4', 'refresh_parsing'))
        self.ui.parse_repl_5.textChanged.connect(
            partial(self.handler, 'parse_repl_5', 'refresh_parsing'))
        self.ui.parse_repl_6.textChanged.connect(
            partial(self.handler, 'parse_repl_6', 'refresh_parsing'))
        self.ui.parse_repl_7.textChanged.connect(
            partial(self.handler, 'parse_repl_7', 'refresh_parsing'))
        self.ui.parse_repl_8.textChanged.connect(
            partial(self.handler, 'parse_repl_8', 'refresh_parsing'))
        self.ui.parse_repl_9.textChanged.connect(
            partial(self.handler, 'parse_repl_9', 'refresh_parsing'))

        self.ui.parse_source_1.textChanged.connect(
            partial(self.handler, 'parse_source_1', 'refresh_parsing'))
        self.ui.parse_source_2.textChanged.connect(
            partial(self.handler, 'parse_source_2', 'refresh_parsing'))
        self.ui.parse_source_3.textChanged.connect(
            partial(self.handler, 'parse_source_3', 'refresh_parsing'))
        self.ui.parse_source_4.textChanged.connect(
            partial(self.handler, 'parse_source_4', 'refresh_parsing'))
        self.ui.parse_source_5.textChanged.connect(
            partial(self.handler, 'parse_source_5', 'refresh_parsing'))
        self.ui.parse_source_6.textChanged.connect(
            partial(self.handler, 'parse_source_6', 'refresh_parsing'))
        self.ui.parse_source_7.textChanged.connect(
            partial(self.handler, 'parse_source_7', 'refresh_parsing'))
        self.ui.parse_source_8.textChanged.connect(
            partial(self.handler, 'parse_source_8', 'refresh_parsing'))
        self.ui.parse_source_9.textChanged.connect(
            partial(self.handler, 'parse_source_9', 'refresh_parsing'))

        # Ftrack Tab
        self.ui.ftrack_use.clicked.connect(
            partial(self.handler, 'ftrack_use', 'refresh_ftrack'))
        self.ui.ftrack_server.textChanged.connect(
            partial(self.handler, 'ftrack_server', 'refresh_ftrack'))
        self.ui.ftrack_api_key.textChanged.connect(
            partial(self.handler, 'ftrack_api_key', 'refresh_ftrack'))
        self.ui.ftrack_project.textChanged.connect(
            partial(self.handler, 'ftrack_project', 'refresh_ftrack'))
        self.ui.ftrack_shot_use.clicked.connect(
            partial(self.handler, 'ftrack_shot_use', 'refresh_ftrack'))
        self.ui.ftrack_shot.textChanged.connect(
            partial(self.handler, 'ftrack_shot', 'refresh_ftrack'))
        self.ui.ftrack_label_use.clicked.connect(
            partial(self.handler, 'ftrack_label_use', 'refresh_ftrack'))
        self.ui.ftrack_label.textChanged.connect(
            partial(self.handler, 'ftrack_label', 'refresh_ftrack'))
        self.ui.ftrack_note.textChanged.connect(
            partial(self.handler, 'ftrack_note', 'refresh_ftrack'))

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
        self.ui.check_if_eq_1.textChanged.connect(
            partial(self.handler, 'check_if_eq_1', 'refresh_checks'))
        self.ui.check_check_1.textChanged.connect(
            partial(self.handler, 'check_check_1', 'refresh_checks'))
        self.ui.check_check_eq_1.textChanged.connect(
            partial(self.handler, 'check_check_eq_1', 'refresh_checks'))
        self.ui.check_warning_1.clicked.connect(
            partial(self.handler, 'check_warning_1', 'refresh_shots'))
        self.ui.check_error_1.clicked.connect(
            partial(self.handler, 'check_error_1', 'refresh_shots'))
        self.ui.check_message_1.textChanged.connect(
            partial(self.handler, 'check_message_1', 'refresh_checks'))

        self.ui.check_if_2.textChanged.connect(
            partial(self.handler, 'check_if_2', 'refresh_checks'))
        self.ui.check_if_eq_2.textChanged.connect(
            partial(self.handler, 'check_if_eq_2', 'refresh_checks'))
        self.ui.check_check_2.textChanged.connect(
            partial(self.handler, 'check_check_2', 'refresh_checks'))
        self.ui.check_check_eq_2.textChanged.connect(
            partial(self.handler, 'check_check_eq_2', 'refresh_checks'))
        self.ui.check_warning_2.clicked.connect(
            partial(self.handler, 'check_warning_2', 'refresh_shots'))
        self.ui.check_error_2.clicked.connect(
            partial(self.handler, 'check_error_2', 'refresh_shots'))
        self.ui.check_message_2.textChanged.connect(
            partial(self.handler, 'check_message_2', 'refresh_checks'))

        self.ui.check_if_3.textChanged.connect(
            partial(self.handler, 'check_if_3', 'refresh_checks'))
        self.ui.check_if_eq_3.textChanged.connect(
            partial(self.handler, 'check_if_eq_3', 'refresh_checks'))
        self.ui.check_check_3.textChanged.connect(
            partial(self.handler, 'check_check_3', 'refresh_checks'))
        self.ui.check_check_eq_3.textChanged.connect(
            partial(self.handler, 'check_check_eq_3', 'refresh_checks'))
        self.ui.check_warning_3.clicked.connect(
            partial(self.handler, 'check_warning_3', 'refresh_checks'))
        self.ui.check_error_3.clicked.connect(
            partial(self.handler, 'check_error_3', 'refresh_checks'))
        self.ui.check_message_3.textChanged.connect(
            partial(self.handler, 'check_message_3', 'refresh_checks'))

        # Preferences Tab
        # ignore fps for now?

        self.ui.prefs_size_scan.clicked.connect(
            partial(self.handler, 'prefs_size_scan', 'refresh_checks'))
        self.ui.prefs_size_ignore_first.valueChanged.connect(
            partial(self.handler, 'prefs_size_ignore_first', 'refresh_checks'))
        self.ui.prefs_size_neighborhood.valueChanged.connect(
            partial(self.handler, 'prefs_size_neighborhood', 'refresh_checks'))
        self.ui.prefs_size_threshold.valueChanged.connect(
            partial(self.handler, 'prefs_size_threshold', 'refresh_checks'))

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
            pth = str(self.settings['package_folder']['value']).replace('\\', '/')
            self.data = Sequencer(pth, sequence_mode='holes_allowed', gui=self.settings)
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

        if sender == 'write_button':
            # read column widths from tablewidget for excel column sizes
            # there is no way to change excel column sizes by content
            column_widths_sub = []
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
            self.display_table(
                self.data.table_log,
                self.ui.log_table,
                self.data.column_titles_log
            )
            self.ui.txt_table.setPlainText(self.data.table_txt)

            # display Package name
            _preview = self.data.output.get('package_name', '')
            self.ui.name_preview.setText(_preview)

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
                subprocess.Popen('explorer /select,  \"' + path.replace('/', '\\') + '\"')
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
        self.explore(self.settings_obj.get_user_settings_path())

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
                for column_number, one_column in enumerate(titles):
                    my_title = str(one_column).lstrip().rstrip()
                    try:
                        table_ui.setItem(row,
                                         column_number,
                                         QtWidgets.QTableWidgetItem(str(line[column_number]))
                                         )
                    except:
                        log.error("can't display table row")
            table_ui.resizeColumnsToContents()
            table_ui.resizeRowsToContents()

    def clear_all_tables(self):
        """
        table data to ui
        """
        self.ui.sub_table.setRowCount(0)
        self.ui.log_table.setRowCount(0)
        self.ui.txt_table.setPlainText('')

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
            else:
                _b = bool(my_str)
            return _b

        logging.debug('-> settings_to_gui')
        skip_names = [
            'package_folder',
            'name_preview',
            'load_preset_combobox',
            'save_preset_name'
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
                        obj.setChecked(str_to_bool(one_setting['value']))
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

    def closeEvent(self, event):
        self.settings_from_gui()
        self.settings_obj.settings = self.settings
        self.settings_obj.write('last')
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
    settings_obj = Settings("last")

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Plastique")

    app = app.instance()  # checks if QApplication already exists
    if not app:  # create QApplication if it doesn't exist
        app = QtWidgets.QApplication([])
    main = MainWindow(no_gui=False, s=settings_obj)
    main.show()
    app.exec_()
