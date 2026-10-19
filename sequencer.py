import concurrent.futures
import csv
import json
import logging
import os
import pprint
import re
import shutil
import subprocess
import sys
import time
from operator import itemgetter

import ftrack_api
import xlsxwriter
try:
    # only the gui needs Qt; the command line mode runs without it
    from PySide2 import QtGui, QtWidgets, QtCore
except ImportError:
    QtGui = QtWidgets = QtCore = None
from unidecode import unidecode

import helpers
import parse_file_name
from ftrack import FtrackHelper, open_session, find_project_id
from metadata import MetaData
from ayon_shotlist import AyonShotlist, parse_product_filters
import ayon_packages
from ayon_publish import AyonPublish
import credentials

# number of rows on the Parsing tab (32 come from the .ui file, the rest are
# added by MainWindow._add_parse_rows)
PARSE_ROWS = 48
PARSE_FIELDS = ('name', 'pattern', 'repl', 'source', 'filter')


from sh_tokens import _KeepMissing, _TOKEN_RE, expand_tokens, format_keep, unresolved_tokens  # noqa: F401
import grouping


class Sequencer(object):
    def __init__(self, in_path, sequence_mode='to_subsequences', gui=None, more_settings=None, ui=None, headless=False):

        self.converts = None
        self.ui = ui
        self.headless = headless

        self.settings_obj = more_settings
        self.settings = self.settings_obj.settings
        self.settings_inst = self.settings_obj.install_settings
        self.settings_args = self.settings_obj.args

        self.log = logging.getLogger("Sequencer")
        self.sequence_mode = sequence_mode
        self.merged_list = None
        self.settings = gui
        self.regexes = None
        self.static_keywords = {}
        self.column_titles_sub = None
        self.column_expressions_sub = None
        self.column_titles_log = None
        self.column_expressions_log = None
        self.column_titles_txt = None
        self.column_expressions_txt = None
        # Spreadsheet tab: columns defined as Title=*value can be edited in
        # the Submission / Drive Log tables
        self.column_editable_sub = []
        self.column_editable_log = []
        # cell edits of those tables: {'sub' / 'log': {(row key, column title): text}}
        # kept over refreshes, a Reload (new Sequencer) drops them
        self.cell_edits = {'sub': {}, 'log': {}}
        self.table_sub = []
        self.table_log = []
        self.table_side = []
        self.table_rename = []
        self.columns_side = []
        self.table_txt = ""
        self.table_files = []
        self.columns_files = ['File', 'Size', 'Category', 'Missing', 'Path', 'Meta']

        self.paths = {}
        self._prep_paths_vars()

        self.my_ayon = None
        self.ayon_data = []
        # Grouping tab: groups of the last refresh (grouping.assign)
        self.groups = []
        self.ayon_gui = None
        # every version of the products of the Ayon folders matched to files
        self.ayon_matched_versions = []

        self.renames = []
        self.output = {}

        self.vendor_csv = []
        self.vendor_csv_transformed = []
        self.vendor_csv_prefs_spreadsheet = {}
        self.vendor_csv_prefs_repres = {}

        if in_path is None:
            # Ayon only: used by the Ayon tab Scan button before a package
            # is loaded, no files are read
            self.in_path = ''
            return
        if not os.path.exists(in_path):
            self.log.error(f"Package path '{in_path}' does not exist.")
        else:
            self.log.info(f"Package path '{in_path}")
        self.in_path = self._prepare_in_path(in_path)

        if self.headless:
            # HEADLESS MODE
            self.settings['package_folder']['value'] = self.in_path
            self._process_headless()
        else:
            # GUI MODE
            self.read_files()
            self.transform_data()
        #pprint.pprint(self.merged_list)

    def _process_headless(self):
        action_names = {
            "r": "Rename",
            "s": "Sidecar Files",
            "c": "Convert",
            "d": "Reload",
            "g": "Go",
            "f": "Read Files",
            "t": "Transform Data",
            "p": "Publish to Ayon - local",
            "P": "Publish to Ayon - Deadline",
            "a": "Export Ayon Shotlist",
            "k": "Record Package to Ayon",
            "e": "Search and Replace",
            "x": "Export Ftrack Shotlist"
        }
        if self.settings_args is not None:
            actions_arg = self.settings_args.get("actions", None)
            if actions_arg is not None:
                self.log.info(
                    'Started at: ' + time.strftime("%Y-%m-%d, %H:%M"))
                time_start = time.time()
                actions = list(actions_arg)
                action_count = 0
                action_lenght = len(actions_arg)
                self.log.info(
                    f"Running {action_lenght} headless actions: {actions_arg}")
                for action in actions:
                    action_count += 1
                    action_name = action_names.get(action, f"Unknown ({action})")
                    self.log.info(
                        f"Running headless action {action_count}/{action_lenght}: {action_name}")
                    if action == "g":
                        # GO
                        self.export_all()
                    elif action == "d":
                        # RELOAD
                        self.read_files()
                        self.transform_data()
                    elif action == "s":
                        # SIDECAR
                        self.sidecar_files_copy()
                    elif action == "r":
                        # RENAME
                        self.rename_execute()
                    elif action == "c":
                        # CONVERT
                        self.run_converts()
                    elif action == "f":
                        # READ FILES
                        self.read_files()
                    elif action == "t":
                        # TRANSFORM DATA
                        self.transform_data()
                    elif action == "p":
                        # Publish to Ayon - local
                        self.publish_ayon(mode="local")
                    elif action == "P":
                        # Publish to Ayon - Deadline
                        self.publish_ayon(mode="farm")
                    elif action == "a":
                        # Export Ayon Shotlist
                        self.ayon_export()
                    elif action == "k":
                        # Record Package to Ayon
                        self.ayon_record_packages()
                    elif action == "e":
                        # Search and Replace in text files
                        self.replace_execute()
                    elif action == "x":
                        # Export Ftrack Shotlist
                        self.ftrack_export()
                    else:
                        self.log.warning(f"Unknown action: {action}")
                    self.log.info(
                        f"Headless action {action_count}/{action_lenght}: {action_name} finished")
                self.log.info(
                    'Finished at: ' + time.strftime("%Y-%m-%d, %H:%M"))
                self.log.info(
                    f'Processing time {round(time.time() - time_start, 2)} seconds')
            else:
                self.log.error("Actions CLI argument is missing.")
        else:
            self.log.error("CLI arguments are missing.")

    def _prep_paths_vars(self):
        """
        Get paths and environment variables for executables
        sources are environment variables, install.json, and os paths
        :return:
        """
        def which(program):
            def is_exe(fpath):
                return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

            fpath, fname = os.path.split(program)
            if fpath:
                if is_exe(program):
                    return program
            else:
                for path in os.environ.get("PATH", "").split(os.pathsep):
                    exe_file = os.path.join(path, program)
                    if is_exe(exe_file):
                        return exe_file
            return None

        envs = dict(os.environ)
        deadline_command = 'deadlinecommand'
        if sys.platform == 'win32':
            usr = envs.get('USERNAME', '')
            deadline_command += '.exe'
            executables = ['ayon.exe', 'ffmpeg.exe', 'ffprobe.exe', 'ffplay.exe', 'oiiotool.exe', deadline_command]

        else:
            usr = envs.get('USER', '')
            executables = ['ayon', 'ffmpeg', 'ffprobe', 'ffplay', 'oiiotool', deadline_command]

        # paths are lowercase
        together = {
            'user': usr,
            'FTRACK_API_USER': envs.get('FTRACK_API_USER', ''),
            'FTRACK_SERVER': envs.get('FTRACK_SERVER', ''),
            'FTRACK_API_KEY': envs.get('FTRACK_API_KEY', ''),
            'AYON_SERVER_URL': envs.get('AYON_SERVER_URL', ''),
            'AYON_USERNAME': envs.get('AYON_USERNAME', ''),
            'AYON_API_KEY': envs.get('AYON_API_KEY', ''),
            'ayon': '',
            'ffmpeg': '',
            'ffprobe': '',
            'oiiotool': '',
            'ocio': envs.get('OCIO', ''),
            'deadline': '',
            'vfx-transcode': ''
        }

        # check if executables are available on path
        for one_exec in executables:
            exe_path = which(one_exec)
            k = os.path.splitext(one_exec)[0]
            if k == 'deadlinecommand':
                k = 'deadline'
            if exe_path:
                together[k] = exe_path
            elif k not in together:
                together[k] = ''

        # try to get deadline command from environment, overrides PATH
        dp = envs.get('DEADLINE_PATH', '')
        if dp != '':
            dp = dp.replace("\\", "/").rstrip('/')
            dp = f"{dp}/{deadline_command}"
            if os.path.exists(dp):
                together['deadline'] = dp

        # override executable paths by Submission Helper specific environment variables
        if envs.get('SH_FFMPEG'):
            together['ffmpeg'] = envs['SH_FFMPEG']
        if envs.get('SH_FFPROBE'):
            together['ffprobe'] = envs['SH_FFPROBE']
        if envs.get('SH_OIIOTOOL'):
            together['oiiotool'] = envs['SH_OIIOTOOL']
        if envs.get('SH_AYON'):
            together['ayon'] = envs['SH_AYON']
        if envs.get('SH_OCIO'):
            together['ocio'] = envs['SH_OCIO']

        # check if install.json config has valid stuff, use it if yes.
        # install.json overrides everything
        if self.settings_inst is not None:
            if self.settings_inst.get('ffprobe_path') and self.settings_inst.get('ffprobe_path') != "" and os.path.exists(self.settings_inst['ffprobe_path']):
                together['ffprobe'] = self.settings_inst['ffprobe_path']
            if self.settings_inst.get('ffmpeg_path') and self.settings_inst.get('ffmpeg_path') != "" and os.path.exists(self.settings_inst['ffmpeg_path']):
                together['ffmpeg'] = self.settings_inst['ffmpeg_path']
            if self.settings_inst.get('oiio_path') and self.settings_inst.get('oiio_path') != "" and os.path.exists(self.settings_inst['oiio_path']):
                together['oiiotool'] = self.settings_inst['oiio_path']
            if self.settings_inst.get('vfx-transcode_path') and self.settings_inst.get('vfx-transcode_path') != "" and os.path.exists(self.settings_inst['vfx-transcode_path']):
                together['vfx-transcode'] = self.settings_inst['vfx-transcode_path']
            if self.settings_inst.get('ayon_path') and  self.settings_inst.get('ayon_path') != "" and os.path.exists(self.settings_inst['ayon_path']):
                together['ayon'] = self.settings_inst['ayon_path']
            if self.settings_inst.get('ocio_path') and  self.settings_inst.get('ocio_path') != "" and os.path.exists(self.settings_inst['ocio_path']):
                together['ocio'] = self.settings_inst['ocio_path']
            if self.settings_inst.get('deadline') and  self.settings_inst.get('deadline') != "" and os.path.exists(self.settings_inst['deadline']):
                together['deadline'] = self.settings_inst['deadline']

            # ftrack: current names, then the names used until mid 2025
            # (server_url / api_key / api_user), still in older install.json files
            legacy_used = []
            for env_key, name, legacy in (('FTRACK_SERVER', 'ftrack_server_url', 'server_url'),
                                          ('FTRACK_API_KEY', 'ftrack_api_key', 'api_key'),
                                          ('FTRACK_API_USER', 'ftrack_api_user', 'api_user')):
                if self.settings_inst.get(name):
                    together[env_key] = self.settings_inst[name]
                elif self.settings_inst.get(legacy):
                    together[env_key] = self.settings_inst[legacy]
                    legacy_used.append(f"{legacy} -> {name}")
            if legacy_used:
                self.log.debug("install.json uses old ftrack key names, consider renaming: "
                               + ", ".join(legacy_used))

            if self.settings_inst.get('ayon_server_url') and  self.settings_inst.get('ayon_server_url') != "":
                together['AYON_SERVER_URL'] = self.settings_inst['ayon_server_url']
            if self.settings_inst.get('ayon_api_key') and  self.settings_inst.get('ayon_api_key') != "":
                together['AYON_API_KEY'] = self.settings_inst['ayon_api_key']
            if self.settings_inst.get('ayon_username') and  self.settings_inst.get('ayon_username') != "":
                together['AYON_USERNAME'] = self.settings_inst['ayon_username']


        # OCIO path from gui overrides everything
        if self.settings is not None:
            gui_pth = self.settings.get('prefs_oiio_custom_ocio_path')
            gui_pth_enabled = bool((self.settings.get('prefs_oiio_custom_ocio') or {}).get('value', False))
            if gui_pth and gui_pth['value'] and os.path.exists(gui_pth['value']) and gui_pth_enabled:
                together['ocio'] = gui_pth['value']

        # ftrack / Ayon credentials: environment, then the user's own (keyring),
        # then install.json (credentials.py)
        credentials.resolve(together, credentials.startup_env(), self.settings_inst)
        self.paths = together

    def _prepare_in_path(self, in_path):
        """
        Add trailing slash to folder path if it is existing folder
        Convert to forward slashes
        """

        if in_path is None:
            in_path = ''
        in_path = in_path.replace("\\", "/")
        if os.path.isdir(in_path.rstrip('/')):
            if in_path[-1] != '/':
                in_path = f"{in_path}/"
        return  in_path

    def read_files(self):
        """
        Do all the slow stuff like finding files
        and reading metadata
        :return:
        """
        if not self.headless:
            self.ui.statusBar.showMessage("Scanning files", 3000)

        # get list of all files
        file_list = self.walk_dirs(self.in_path)

        # get list of dirs of sequences
        self.merged_list = []
        self.merged_list = self.seq_list_from_file_list(
            file_list, mode=self.sequence_mode)

        # get list of dirs of multi-frame files
        self.merged_list.extend(self.multirames_from_file_list(file_list))

        # other (audio, office, graphics, other)
        self.merged_list.extend(self.other_files_from_file_list(file_list))

        _cats = {}
        for one_item in self.merged_list:
            _c = one_item.get('category', 'other')
            _cats[_c] = _cats.get(_c, 0) + 1
        self.log.info(f"Scanned {self.in_path}: {len(file_list)} file(s) in {len(self.merged_list)} item(s)"
                      + (" (" + ", ".join(f"{v} {k}" for k, v in sorted(_cats.items())) + ")" if _cats else ""))

        # make paths relative
        self.get_relative_paths(parse_file_name.parse(self.in_path))

        # get file sizes for merged list
        if not self.headless:
            self.ui.statusBar.showMessage("Calculating file sizes", 3000)
        self.get_file_sizes()

        # get file age
        if not self.headless:
            self.ui.statusBar.showMessage("Calculating file age", 3000)
        self.get_file_age()

        # sidecar files
        if not self.headless:
            self.ui.statusBar.showMessage("Processing Sidecar files", 3000)
        self.sidecar_files_find()

        # display found files
        if not self.headless:
            self.prepare_file_table()
            self.display_file_table()

        if not self.headless:
            self.ui.statusBar.showMessage("Reading CSV Data", 3000)
        self.csv_data = []
        self.csv_data_read()
        if not self.headless:
            self.display_data_table()

        if not self.headless:
            self.ui.statusBar.showMessage("Reading Replace Data", 3000)
        self.replace_data = []
        self.csv_replace_data_read()
        self.csv_replace_prepare()
        if not self.headless:
            self.display_replace_table()

        if not self.headless:
            self.ui.statusBar.showMessage("Reading Ayon Data", 3000)
        self.ayon_data = []
        self.ayon_data_read()
        if not self.headless:
            self.display_ayon_table()

        # metadata
        if not self.headless:
            self.ui.statusBar.showMessage("Gathering Metadata", 3000)
        self.get_metadata()

        # Ftrack shotlist export used to run here on every read and wrote to a
        # hardcoded D:/ftrack_shotlist.csv. It is now only done by the
        # headless 'x' action.


    def transform_data(self):
        """
        Transform file info and prepare data for export
        :return:
        """

        # this sets static keywords like date and package name
        if not self.headless:
            self.ui.statusBar.showMessage("Preparing Package Name", 3000)
        self.prepare_package_name()

        # make paths relative
        #self.get_relative_paths(parse_file_name.parse(self.in_path))

        # also adds totals to static keywords
        if not self.headless:
            self.ui.statusBar.showMessage("Parsing Keywords", 3000)
        self.filter_items_add_counters()

        # read from settings and compile
        self.prepare_regex()

        # for every found item prepare regex items
        self.fill_regexes()

        if not self.headless:
            self.ui.statusBar.showMessage("Reading data from Ftrack", 3000)
        self.ftrack = {}
        # notes and OpenPype attributes
        self.ftrack_query()
        self.select_ftrack_note()
        if not self.headless:
            self.display_ftrack_table()

        self.csv_data_assign()
        if not self.headless:
            self.display_data_table()
            pass

        self.ayon_data_assign()
        self.ayon_versions_update()
        self.ayon_versions_assign()
        if not self.headless:
            self.display_ayon_table()
            self.display_ayon_versions_table()

        # sidecar files filter
        if not self.headless:
            self.ui.statusBar.showMessage("Filtering Sidecar Files", 3000)
        self.sidecar_files_filter()

        # vendor ingest
        if not self.headless:
            self.ui.statusBar.showMessage("Processing Vendor CSV", 3000)
        self.vendor_csv_all()

        # prepare conversions
        if not self.headless:
            self.ui.statusBar.showMessage("Preparing Converts", 3000)
        self.prepare_converts()

        # Grouping tab: group tokens for the checks (grouped again with the
        # check results when the tables are built)
        self.group_items()

        #self.checks = []
        if not self.headless:
            self.ui.statusBar.showMessage("Running Checks", 3000)
        self.run_checks()

        self.rename_prepare()
        self.rename_preprocess()

        # parse table headers
        if not self.headless:
            self.ui.statusBar.showMessage("Preparing Tables", 3000)
        self.prepare_all_columns()

        # fill tables for export and display
        self.prepare_tables()

        self.select_ftrack_note()

    def get_metadata(self):

        def _get_one_meta(one):
            # runs in a worker thread: no gui calls here
            one.meta_get()
            return [one.item, one.meta_data]

        self.output['status'] = "Getting meta data"

        if self.merged_list and len(self.merged_list) > 0:
            _cnt = 0
            for one_item in self.merged_list:
                if one_item['category'] in\
                        ['still', 'video', 'sequence', 'audio']:
                    _cnt +=1
            self.log.info("Start Reading metadata for {} media files".format(_cnt))
            if _cnt > 0:
                progress_step = (1 / _cnt) * 100
            else:
                progress_step = 0

            # prepare meta objects
            meta_objs = []
            for one_item in self.merged_list:
                meta_objs.append(MetaData(one_item, self.settings, self.paths))

            # run threaded metadata load
            if not self.headless:
                self.ui.progressBar.setValue(0)
            done = 0
            # ffprobe / oiiotool are separate processes: run a few at once
            # (the workers make no gui calls, results are applied here in order)
            workers = max(1, min(8, os.cpu_count() or 1))
            with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
                for result in executor.map(_get_one_meta, meta_objs):
                    itm = result[0]
                    meta = result[1]
                    itm.update(meta)
                    done += 1
                    _name = itm.get('full_path') or itm.get('name', '')
                    self.log.debug(f"Metadata read: {_name}")
                    # gui updates in the gui thread
                    if not self.headless:
                        self.ui.progressBar.setValue(int(min(100, done * progress_step)))
                        self.ui.statusBar.showMessage(f"Gathering Metadata: {_name} done.", 3000)
            self.log.info(f"Metadata read for {done} item(s)")

            if not self.headless:
                self.ui.progressBar.setValue(100)

    def vendor_csv_all(self):

        self.vendor_csv_read()
        self.vendor_csv_prefs_spreadsheet_read()
        self.vendor_csv_prefs_repre_read()
        self.vendor_csv_transform()
        # self.vendor_csv_write()
        self.vendor_csv_add()
        self.vendor_csv_repre_checks()
        self.vendor_csv_add()

    def vendor_csv_read(self):
        """
        Read the csv from Vendor

        :return: self.vendor_csv dict
        """

        vendor_csv = []

        pth = ""
        if self.settings:
            if self.settings['vendor_csv_path']['value']:
                pth = self.settings['vendor_csv_path']['value']

        if pth and pth != '' and os.path.exists(pth):
            try:
                # utf-8-sig: Excel writes a BOM, which used to end up in the
                # first column name
                with open(pth, encoding='utf-8-sig', errors='replace', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        vendor_csv.append(dict(row))
            except (OSError, csv.Error) as e:
                self.log.error(f'Error opening vendor csv file {pth}: {e}')
        self.vendor_csv = vendor_csv

    def vendor_csv_prefs_spreadsheet_read(self):
        """
        Reads Json for spreadsheet configuration

        :return: self.vendor_csv_prefs_spreadsheet
        """
        vendor_csv_prefs_spreadsheet = {}

        prefs_spread = ""
        if self.settings:
            if self.settings['vendor_csv_prefs_spreadsheet']['value']:
                prefs_spread = self.settings['vendor_csv_prefs_spreadsheet']['value']

        if str(prefs_spread).strip():
            try:
                vendor_csv_prefs_spreadsheet = json.loads(prefs_spread)
            except ValueError as e:
                self.log.error(f'Error reading Vendor spreadsheet Json: {e}')
        if not isinstance(vendor_csv_prefs_spreadsheet, dict):
            self.log.error('Vendor spreadsheet Json must be an object {"column": {...}}')
            vendor_csv_prefs_spreadsheet = {}
        self.vendor_csv_prefs_spreadsheet = vendor_csv_prefs_spreadsheet

    def vendor_csv_prefs_repre_read(self):
        """
        Reads Json for preflight / validations

        :return: self.vendor_csv_prefs_repre
        """
        vendor_csv_prefs_repre = {}

        prefs_repre = ""
        if self.settings:
            if self.settings['vendor_csv_prefs_repres']['value']:
                prefs_repre = self.settings['vendor_csv_prefs_repres']['value']

        if str(prefs_repre).strip():
            try:
                vendor_csv_prefs_repre = json.loads(prefs_repre)
            except ValueError as e:
                self.log.error(f'Error reading Vendor representation Json: {e}')
        if not isinstance(vendor_csv_prefs_repre, dict):
            self.log.error('Vendor representation Json must be an object')
            vendor_csv_prefs_repre = {}
        # an old value must not stay when the json is now empty or invalid
        self.vendor_csv_prefs_repre = vendor_csv_prefs_repre

    def vendor_csv_transform(self):
        """
        Uses Vendor CSV and Json config to make a new CSV (list of dicts)
        Validates if columns exist (json required)
        Renames Columns (json column)
        Can make new columns with defaults (json default)
        Validates if existing column matches the regex (json validate)

        :return:self.vendor_csv_transformed
        """

        vendor_csv_transformed = []
        if self.vendor_csv and self.vendor_csv_prefs_spreadsheet:

            for row_index, one_row in enumerate(self.vendor_csv):

                row_keys = one_row.keys()
                trans_row = {}
                row_errors = []
                line = row_index + 2
                for k, v in self.vendor_csv_prefs_spreadsheet.items():
                    v = v if isinstance(v, dict) else {}
                    column = v.get('column') or k
                    default = v.get('default', '')
                    if k in row_keys:
                        # prefs column present in csv (a short row gives None)
                        cell = one_row[k] if one_row[k] is not None else ''
                        try:
                            valid = bool(re.match(v.get('validate') or '', cell))
                        except re.error as e:
                            self.log.warning(f"Vendor Json: invalid validate regex of {k}: {e}")
                            valid = True
                        if valid:
                            # store valid value to renamed column, default if empty
                            trans_row[column] = cell if cell else default
                        else:
                            row_errors.append(
                                "Row {} has invalid column {} = {}".format(line, k, cell))
                    else:
                        # prefs column NOT present in csv
                        if bool(v.get('required')):
                            row_errors.append(
                                "Row {} has missing column {}".format(line, k))
                        else:
                            # not required, let's fill with default
                            trans_row[column] = default

                json_keys = self.vendor_csv_prefs_spreadsheet.keys()
                for k, v in one_row.items():
                    if k in json_keys:
                        pass
                    else:
                        # some columns in vendor csv are not in json,
                        # let's copy under vendor_*
                        trans_row['vendor_' + str(k)] = v

                # keep errors as list for now
                trans_row['vendor_row_errors'] = row_errors
                vendor_csv_transformed.append(trans_row)

        self.vendor_csv_transformed = vendor_csv_transformed

    def vendor_csv_write(self):
        """
        Writes self.vendor_csv_transformed to csv od hdd
        For debug, not used

        :return:
        """

        pth = ""
        if self.settings:
            if self.settings['vendor_csv_path']['value']:
                pth = self.settings['vendor_csv_path']['value']
        pth = pth + '_transformed.csv'

        if self.vendor_csv_transformed:
            with open(pth, 'w', encoding='utf8',
                      newline='') as output_file:
                fc = csv.DictWriter(output_file, fieldnames=self.vendor_csv_transformed[0].keys())
                fc.writeheader()
                fc.writerows(self.vendor_csv_transformed)

    def vendor_csv_add(self):

        class Default(dict):
            def __missing__(self, key):
                return '{' + key + '}'

        p_key = ""
        v_key = ""
        _ignore = True
        _skip_by = ""
        _skip_what = ""
        _skip = False
        if self.settings:
            if self.settings['vendor_csv_package_key']['value']:
                p_key = self.settings['vendor_csv_package_key']['value']
            if self.settings['vendor_csv_vendor_key']['value']:
                v_key = self.settings['vendor_csv_vendor_key']['value']
            if self.settings['vendor_csv_ignore']['value'] is not None:
                _ignore = bool(self.settings['vendor_csv_ignore']['value'])
            if self.settings['vendor_csv_skip_by']['value']:
                _skip_by = self.settings['vendor_csv_skip_by']['value']
            if self.settings['vendor_csv_skip_what']['value']:
                _skip_what = str(self.settings['vendor_csv_skip_what']['value']).split()
            if self.settings['vendor_csv_skip']['value'] is not None:
                _skip = bool(self.settings['vendor_csv_skip']['value'])
                if (not _skip_what) or (not _skip_by):
                    _skip = False

            # no vendor csv (any more): nothing is left out because of it
            for one_item in self.merged_list or []:
                one_item['vendor_skip'] = False
                one_item['vendor_ignore_sub'] = bool(one_item.get('hide_sub'))

            if self.merged_list is not None and len(
                    self.merged_list) > 0 and self.vendor_csv_transformed:

                # a key without any {token} would pair every file with every row
                keys_ok = bool(unresolved_tokens(p_key)) and bool(unresolved_tokens(v_key))
                if not keys_ok and (p_key or v_key):
                    self.log.warning(
                        f"Vendor: Package key {p_key!r} and Vendor key {v_key!r} must both "
                        "use tokens, e.g. {name} and {vendor_Filename}; files are not paired")
                for one_item in self.merged_list if keys_ok else []:
                    package_key = format_keep(p_key, one_item)
                    if unresolved_tokens(package_key):
                        # the file doesn't have the token: can't pair it
                        continue
                    for one_row in self.vendor_csv_transformed:
                        vendor_key = format_keep(v_key, one_row)
                        if vendor_key == package_key:
                            # vendor csv row identification matches
                            # the package scan row identification
                            for k, v in one_row.items():
                                # add key from csv to the item; not the link
                                # back to an item (it made the item contain itself)
                                if k == 'merged_item':
                                    continue
                                one_item[k] = v
                            one_row['merged_item'] = one_item

                # now ignore unassigned items
                if _ignore:
                    all_vendor_keys = self.vendor_csv_transformed[0].keys()
                    one_vendor_key = list(all_vendor_keys)[0]
                    for one_item in self.merged_list:
                        # vendor_skip: left out because of the vendor csv,
                        # kept when the other filters (age...) run again
                        vendor_skip = not one_item.get(one_vendor_key, None)
                        if _skip:
                            item_skip_by = format_keep(_skip_by, one_item)
                            if item_skip_by in _skip_what:
                                vendor_skip = True
                        one_item['vendor_skip'] = vendor_skip
                        one_item['vendor_ignore_sub'] = bool(
                            one_item.get('hide_sub')) or vendor_skip


                else:
                    for one_item in self.merged_list:
                        one_item['vendor_skip'] = False
                        one_item['vendor_ignore_sub'] = bool(one_item.get('hide_sub'))


    def vendor_csv_repre_checks(self):

        class Default(dict):
            def __missing__(self, key):
                return '{' + key + '}'

        def substract_list(required, testing):
            return [x for x in required if x not in testing]


        if self.vendor_csv_transformed and self.vendor_csv_prefs_repre:
            prefs = self.vendor_csv_prefs_repre
            # find line merges
            merge_key = prefs.get('merge_repres_by', '')
            repres = prefs.get('repres') or []
            merge_groups = {}
            for current, one_row in enumerate(self.vendor_csv_transformed):

                # add merge key to the transformed csv
                # also keep track of grouped rows in merge_groups
                #print('current {}'.format(current))
                try:
                    #one_row['vendor_Merge_by'] = merge_key.format(**one_row)
                    one_row['vendor_Merge_by'] = format_keep(merge_key, one_row)
                    if '{' in one_row['vendor_Merge_by']:
                        raise Exception('failed to expand')
                    #print('merge by {}'.format(one_row['vendor_Merge_by']))
                except Exception:
                    #print('Vendor CSV failed to expand, line {}'.format(current+2))
                    continue

                if one_row['vendor_Merge_by']:
                    if one_row['vendor_Merge_by'] in merge_groups:
                        merge_groups[one_row['vendor_Merge_by']].append(current)
                        #pprint.pprint(merge_groups)
                    else:
                        _empty = []
                        _empty.append(current)
                        merge_groups[one_row['vendor_Merge_by']] = _empty
                        #pprint.pprint(merge_groups)

                    #current_repre_name = one_row['vendor_Output']
                    current_repre_name = one_row.get('vendor_Output')
                    if current_repre_name is None:
                        continue
                    current_line = current + 2

                    # REPRES check
                    # check if output name exists in REPRES
                    # if repre exists, does the file extension match the allowed ones?
                    # check if metadata_check matches
                    if not any(d.get('name') == current_repre_name for d in repres):
                        # repre does not exist in repre json, skip
                        one_row['vendor_row_errors'].append("Output Type {} not found in preferences for line {}".format(current_repre_name, current_line))
                    else:
                        for one_repre in repres:
                            if one_repre.get('name') == current_repre_name:
                                try:
                                    # check extension
                                    current_extension = one_row['merged_item']['extension']
                                    if current_extension in one_repre['extensions']:
                                        # check metadata
                                        for one_meta_key, one_meta_value in one_repre['metadata_check'].items():
                                            read_meta = one_row['merged_item'].get(
                                                one_meta_key, '')
                                            if one_meta_value:
                                                if read_meta and read_meta == one_meta_value:
                                                    pass
                                                else:
                                                    one_row['vendor_row_errors'].append(
                                                        "Metadata {} != {}, = {}".format(
                                                            one_meta_key, one_meta_value,
                                                            read_meta))
                                        # fill range
                                        _filled = {}
                                        for one_range_key, one_range_value in one_repre['frame_range'].items():
                                            if type(one_range_value) == str:
                                                try:
                                                    _filled[one_range_key] = one_range_value.format(**one_row['merged_item'])
                                                except Exception:
                                                    pass
                                        one_row['vendor_frame_range'] = _filled

                                        # fill tags, separate by space
                                        one_row['vendor_Tags'] = ' '.join(
                                            one_repre['vendor_Tags'])
                                    else:
                                        one_row['vendor_row_errors'].append(
                                            "File extension {} doesn't match the representation extension(s) {} for output {}".format(
                                                current_extension,
                                                ', '.join(one_repre['extensions']),
                                                current_repre_name
                                            ))
                                except (KeyError, TypeError, AttributeError) as e:
                                    # no file paired with the row, or incomplete repre Json
                                    self.log.debug(f"Vendor csv line {current_line}: repre check skipped ({e!r})")

            # -------------------------------- CHECK task_intent_repres
            """
            task_intent_repres = {
                "comp": [{
                    "intents": ["WIP", "wip", "CHECK", "check"],
                    "always": ["preview", "edit", "review"],
                    "optional": ["exr"]
                    },
                    {
                    "intents": ["PAF", "paf", "QC", "qc","FINAL", "final"],
                    "always": ["exr", "preview", "edit", "review"],
                    "optional": []
                    }
                ],
                "lay": [{
                    "intents": ["WIP", "wip", "CHECK", "check"],
                    "always": ["preview", "edit", "review"],
                    "optional": ["exr"]
                    }
                ]
            }
            """

            """
            merge_groups = {
                'mw_210_11_0270compMain1': [0, 1, 2, 3],
                'mw_210_12_0300compMain1': [4, 5, 6, 7]
            }
            """

            # get all tasks defined in json settings
            task_intent_repres = prefs.get('task_intent_repres') or {}
            all_tasks = task_intent_repres.keys()
            for one_merge_key, merge_list in merge_groups.items():
                task = self.vendor_csv_transformed[merge_list[0]].get(
                    'vendor_Task')
                intent = self.vendor_csv_transformed[merge_list[0]].get(
                    'vendor_Intent')

                # find all outputs for merge_group
                all_merged_outputs = []
                for one_index in merge_list:
                    _type = self.vendor_csv_transformed[one_index].get(
                        'vendor_Output')
                    if _type is None:
                        continue
                    all_merged_outputs.append(_type)

                # find json task + intent definition
                # this will get us required (always) and optional outputs for task + intent pair
                task_found = False
                intent_found = False
                json_task_defs = None
                _always = []
                _optional = []
                _always_and_optional = []
                if task in all_tasks:
                    json_task_defs = task_intent_repres[task]
                    task_found = True
                else:
                    # error for all group items
                    for one_index in merge_list:
                        self.vendor_csv_transformed[one_index][
                            'vendor_row_errors'].append(
                            "Task {} was not found in Json task_intent_repres section: {}.".format(
                                task, all_tasks))

                # find intent
                if task_found and json_task_defs is not None:
                    for one_task_def in json_task_defs:
                        if intent in one_task_def.get('intents', []):
                            # found the task & intent pair, we have output defs
                            intent_found = True
                            break
                if not intent_found:
                    # error for all group items
                    for one_index in merge_list:
                        self.vendor_csv_transformed[one_index][
                            'vendor_row_errors'].append(
                            "Intent {} was not found in Json task_intent_repres section for task: {}.".format(
                                intent, task))
                else:
                    _always = one_task_def.get('always') or []
                    _optional = one_task_def.get('optional') or []

                # remember the required / optional outputs on every row of the
                # group: the post-pass reads them (the key was never set, so
                # the whole post-pass failed)
                for one_index in merge_list:
                    self.vendor_csv_transformed[one_index]['vendor_One_task_set'] = {
                        'always': list(_always), 'optional': list(_optional)}

                # we have all_merged_outputs (all outputs found in current merge group)
                # and definition of _always and _optional outputs
                # do some checks

                # warn for duplicate outputs in all_merged_outputs
                duplicates = [number for number in all_merged_outputs if
                              all_merged_outputs.count(number) > 1]
                unique_duplicates = list(set(duplicates))
                if len(unique_duplicates) > 0:
                    for one_index in merge_list:
                        self.vendor_csv_transformed[one_index][
                            'vendor_row_errors'].append(
                            "Output type ({}) is present more than once in merged group {}".format(
                                ' '.join(unique_duplicates),
                                self.vendor_csv_transformed[one_index][
                                    'vendor_Merge_by']))

                # warn if required (always) output is missing
                if _always is not None:
                    required_but_missing = substract_list(_always, all_merged_outputs)
                    if required_but_missing is not None and len(
                            required_but_missing) > 0:
                        missing_count = len(required_but_missing)
                        for one_index in merge_list:
                            self.vendor_csv_transformed[one_index][
                                'vendor_row_errors'].append(
                                "{} required output(s) are missing: {}".format(
                                    missing_count,
                                    ' '.join(required_but_missing)))
                    if _optional is not None:
                        _always_and_optional = _always + _optional
                    else:
                        _always_and_optional = _always

                # warn if output exist in merged group, but is/are NOT defined
                if _always_and_optional is not None:
                    duplicates = [number for number in all_merged_outputs if
                                  all_merged_outputs.count(number) > 1]
                    _remove_dupes = substract_list(all_merged_outputs, duplicates)
                    if _remove_dupes is not None and len(_remove_dupes) > 0:
                        # outputs present in the group that the task / intent
                        # doesn't define (the arguments were the wrong way round:
                        # it listed defined outputs that are missing)
                        _udefined = substract_list(_remove_dupes, _always_and_optional)
                        if _udefined is not None and len(
                                _udefined) > 0:
                            undefined_count = len(_udefined)
                            for one_index in merge_list:
                                self.vendor_csv_transformed[one_index][
                                    'vendor_row_errors'].append(
                                    "{} output(s) are present but undefined in task_intent_repres: {}".format(
                                        undefined_count,
                                        ' '.join(_udefined)))

            # ------------------------------------------------------------------------------------------------------
            for mrg_key in merge_groups.keys():
                # make dicts where each length / tc / range serves as key,
                # with value being a list of indexes for self.vendor_csv_transformed
                # _ranges_no_slate = {'1001-1010': [1, 2, 3], '1001-1001': [4]}
                _lengths = {}
                _ranges_no_slate = {}
                _tcs_no_slate = {}
                for one_index in merge_groups[mrg_key]:
                    row = self.vendor_csv_transformed[one_index]
                    rng = row.get('vendor_frame_range') or {}
                    try:
                        ln = rng['length']
                        fs = int(rng['frame_start'])
                        fe = int(rng['frame_end'])
                        tc = str(rng['timecode'])
                        fps = str(rng['frame_rate'])
                        slate = bool(rng['slate_present'])
                        if tc and fps:
                            # fps can be 23.976: not int()
                            tc_to_num = helpers.tc_to_frames(tc, fps, '1') + 1
                            tc_no_slate = helpers.frames_to_tc(tc_to_num, fps, '1')
                            if slate:
                                tc = tc_no_slate
                    except (KeyError, TypeError, ValueError) as e:
                        self.log.debug(f"Vendor csv line {one_index + 2}: frame range not usable ({e!r})")
                        continue
                    if slate:
                        fs += 1
                    frame_range = '{}-{}'.format(fs, fe)
                    _lengths.setdefault(ln, []).append(one_index)
                    _ranges_no_slate.setdefault(frame_range, []).append(one_index)
                    _tcs_no_slate.setdefault(tc, []).append(one_index)

            # add errors to all rows in merged group if one or more output is required but have error(s)
            for mrg_key in merge_groups.keys():
                _failed_required_outputs = []
                indexes = merge_groups[mrg_key]
                for one_index in indexes:
                    row = self.vendor_csv_transformed[one_index]
                    required = (row.get('vendor_One_task_set') or {}).get('always') or []
                    if row.get('vendor_row_errors') and row.get('vendor_Output') in required:
                        _failed_required_outputs.append(row['vendor_Output'])

                if len(_failed_required_outputs) > 0:
                    _err = "Required outputs: {} ;have error(s)".format(", ".join(_failed_required_outputs))
                    for one_index in merge_groups[mrg_key]:
                        self.vendor_csv_transformed[one_index]['vendor_row_errors'].append(_err)

        # convert errors to string (also when the repre Json is not set)
        for one_row in self.vendor_csv_transformed or []:
            errors = one_row.get('vendor_row_errors')
            if isinstance(errors, list):
                one_row['vendor_row_errors'] = ', '.join(str(e) for e in errors)

    def get_relative_paths(self, parsed_in_path):

        self.output['status'] = "Getting relative paths" \
                                " (get_relative_paths)"

        root_dir = parsed_in_path['path']
        root_dir_length = len(root_dir)
        if self.merged_list and len(self.merged_list) > 0:
            for one_item in self.merged_list:
                relative_path = one_item['path'][root_dir_length:]
                relative_path = relative_path.lstrip('/')
                relative_folder = "/".join(relative_path.split('/')[:-1]) + '/'
                relative_folder = relative_folder.lstrip('/')
                one_item['relative_path'] = relative_path
                one_item['relative_folder'] = relative_folder

    def get_file_age(self):

        def get_age(file_path):
            """
            Retrieve the file age.

            :param file_path: Full path to the file.
            :return: A dictionary containing file age details:
                - age_created_minutes: Age of the file in minutes since creation.
                - age_created_hours: Age of the file in hours since creation.
                - age_created_days: Age of the file in days since creation.
                - age_modified_minutes: Age of the file in minutes since the last modification.
                - age_modified_hours: Age of the file in hours since the last modification.
                - age_modified_days: Age of the file in days since the last modification.
            """

            try:
                file_stats = os.stat(file_path)
                current_time = time.time()
                precision = 2

                # Calculate creation time differences
                created_time = file_stats.st_ctime
                age_created_seconds = current_time - created_time
                age_created_minutes = round(age_created_seconds / 60, precision)
                age_created_hours = round(age_created_minutes / 60, precision)
                age_created_days = round(age_created_hours / 24, precision)

                # Calculate modified time differences
                modified_time = file_stats.st_mtime
                age_modified_seconds = current_time - modified_time
                age_modified_minutes = round(age_modified_seconds / 60, precision)
                age_modified_hours = round(age_modified_minutes / 60, precision)
                age_modified_days = round(age_modified_hours / 24, precision)

                return {
                    'age_minutes_created': age_created_minutes,
                    'age_hours_created': age_created_hours,
                    'age_days_created': age_created_days,
                    'age_minutes_modified': age_modified_minutes,
                    'age_hours_modified': age_modified_hours,
                    'age_days_modified': age_modified_days,
                    'age_file_youngest': file_path,
                    'age_error': None
                }

            except Exception as e:
                return {
                    'age_minutes_created': 0,
                    'age_hours_created': 0,
                    'age_days_created': 0,
                    'age_minutes_modified': 0,
                    'age_hours_modified': 0,
                    'age_days_modified': 0,
                    'age_file_youngest': 0,
                    'age_error': str(e)
                }

        def is_younger(age_old, age_new, mode="auto"):

            if age_old['age_error'] is not None or age_new['age_error'] is not None:
                # Can't compare error
                return False

            if mode == "auto":
                if age_old['age_minutes_created'] < age_old['age_minutes_modified']:
                    mode = "modified"
                else:
                    mode = "created"

            if mode == "created":
                return age_new['age_minutes_modified'] < age_old['age_minutes_modified']
            elif mode == "modified":
                return age_new['age_minutes_modified'] < age_old['age_minutes_modified']

        if self.merged_list is not None and len(self.merged_list) > 0:
            for one_item in self.merged_list:
                if one_item['category'] == 'sequence':
                    youngest = {}
                    for one_frame in range(one_item['start_number'],
                                           one_item['end_number'] + 1):
                        one_file = one_item['path_prs'] + '/' + one_item[
                            'clean_name'] + str(one_frame).zfill(
                            one_item['padding']) + '.' + one_item['extension']

                        age_data = get_age(one_file)
                        if youngest == {}:
                            youngest = age_data
                        # find youngest file in the sequence
                        if is_younger(youngest, age_data):
                            youngest = age_data
                    one_item['file_age'] = youngest
                else:
                    one_item['file_age'] = get_age(one_item['path'])

            for one_item in self.merged_list:
                age_dict = one_item.get('file_age')
                if age_dict is not None:
                    one_item.update(age_dict)

    def get_file_sizes(self):

        def median(l):
            half = len(l) // 2
            l.sort()
            if not len(l) % 2:
                return (l[half - 1] + l[half]) / 2.0
            return l[half]

        def median_difference(lst, med):
            dif = []
            for one in lst:
                dif.append(float(one)/float(med))
            return dif

        def get_big_devs(difs, treshold=0.3, start = 0):
            dif = []
            low = 1.0 - treshold
            high = 1.0 + treshold
            for one in difs:
                if one < low or one > high:
                    dif.append(start)
                start += 1
            return dif

        self.output['status'] = "Getting file sizes" \
                                " (get_file_sizes)"

        _consistency = True
        _holes = True
        _sizes = True
        _ignore_first = 1
        _neighbrs = 2
        _tresh = 0.3
        if self.settings:
            def _value(key):
                item = self.settings.get(key)
                return item.get('value') if isinstance(item, dict) else None

            # unchecked / 0 are real values: test for None, not for truth
            if _value('check_sequence_size_consistency') is not None:
                _consistency = bool(_value('check_sequence_size_consistency'))
            if _value('check_sequence_holes') is not None:
                _holes = bool(_value('check_sequence_holes'))
            if _value('prefs_size_scan') is not None:
                _sizes = bool(_value('prefs_size_scan'))
            if _value('prefs_size_ignore_first') is not None:
                _ignore_first = max(0, int(_value('prefs_size_ignore_first')))
            if _value('prefs_size_neighborhood') is not None:
                _neighbrs = max(0, int(_value('prefs_size_neighborhood')))
            if _value('prefs_size_threshold'):
                _tresh = float(int(_value('prefs_size_threshold')))*0.01

        # end this if sizes should not be worked on
        if not _sizes:
            return

        if self.merged_list is not None and len(self.merged_list) > 0:
            for one_item in self.merged_list:
                one_item['size_bytes'] = 0
                one_item['size_human'] = '0'
                one_item['size_warning'] = ''

                # file sequence
                if one_item['category'] == 'sequence':
                    one_pth = one_item['path_prs']
                    start = one_item['start_number']
                    end = one_item['end_number']
                    pad = one_item['padding']
                    clean = one_item['clean_name']
                    ext = '.' + one_item['extension']

                    # calculate sequence size
                    my_size = 0
                    sizes = []
                    frames = []     # frame number of every size
                    zero_size = []
                    for one_frame in range(start, end+1):
                        one_file = one_pth + '/' + clean + str(one_frame).zfill(pad) + ext
                        try:
                            stat_info = os.stat(one_file)
                            one_size = stat_info.st_size
                            # size in bytes
                            my_size = my_size + one_size
                            if one_size == 0:
                                zero_size.append(one_frame)
                            sizes.append(one_size)
                            frames.append(one_frame)
                        except OSError:
                            pass

                    if sizes is not None and len(sizes) > 0:

                        one_item['size_bytes'] = my_size
                        one_item['size_human'] = helpers.humanize_file_size(
                            my_size)

                        # warn if files are missing
                        empty = len(zero_size)
                        if empty > 0:
                            warn = one_item.get('size_warning', '')
                            new_warn = "{} files have zero size: {}".format(
                                str(len(zero_size)),
                                zero_size
                            )
                            if warn == '':
                                one_item['size_warning'] = new_warn
                            else:
                                one_item['size_warning'] += ", " + new_warn

                        missing = len(one_item.get('missing_numbers') or [])
                        if _holes and missing > 0:
                            warn = one_item.get('size_warning', '')
                            new_warn = "{} missing files: {}".format(
                                str(missing),
                                one_item['missing_numbers']
                            )
                            if warn == "":
                                one_item['size_warning'] = new_warn
                            else:
                                one_item[
                                    'size_warning'] += ", " + new_warn

                        # analyze sizes
                        if _consistency:
                            #pprint.pprint(sizes)
                            # trim out frames to be ignored
                            # this is done for slates, they are often small
                            try:
                                sizes = sizes[_ignore_first:]
                                frames = frames[_ignore_first:]

                                # add the last item neighbor times
                                _s = sizes
                                if _neighbrs > 0:
                                    _st = [sizes[0] for i in range(_neighbrs)]
                                    _end = [sizes[-1] for i in range(_neighbrs)]
                                    _s = _st + sizes + _end

                                #pprint.pprint(_s)

                                inconsistent = []
                                itms = 2 * _neighbrs + 1

                                for cnt in range(_neighbrs, len(_s)-_neighbrs):
                                    _frame = frames[cnt - _neighbrs]
                                    _w = _s[(cnt - _neighbrs):(cnt + _neighbrs)+1]
                                    all_neighbrs = sum([i for i in _w if isinstance(i, int)])
                                    average = float(all_neighbrs / itms)
                                    _diff = abs(1 - float(float(_s[cnt]) / average))
                                    _diff_percent = int(round(_diff*100, 0))
                                    #print("{} {}: {} ave: {} diff: {}".format(cnt, _frame, _w, average, _diff_percent))
                                    if _diff > _tresh:
                                        inconsistent.append(_frame)
                                if len(inconsistent) > 0:
                                    warn = one_item.get('size_warning', '')
                                    new_warn = "{} file sizes greatly differ: {}"\
                                        .format(str(len(inconsistent)),
                                                str(inconsistent))
                                    if warn == '':
                                        one_item['size_warning'] = new_warn
                                    else:
                                        one_item['size_warning'] += ', ' + new_warn
                            except (IndexError, ZeroDivisionError):
                                # very short sequences (nothing left after Ignore First)
                                # or all frames zero size: no consistency check
                                pass
                else:
                    # video (multiframe container)
                    try:
                        stat_info = os.stat(one_item['path'])
                        # size in bytes
                        my_size = stat_info.st_size
                        one_item['size_bytes'] = my_size
                        one_item['size_human'] = helpers.humanize_file_size(my_size)
                        if my_size == 0:
                            one_item['size_warning'] = 'file has zero size'
                    except OSError:
                        pass

    @staticmethod
    def get_file_extension_groups():

        multi_frame_ext = ['mov', 'avi', 'mpg', 'mpeg', 'mp2', 'mpv', 'mp4', 'm4v', 'gov', 'qt', 'r3d', 'mxf']
        image_ext = ['dpx', 'cin', 'jpg', 'jpeg', 'tif', 'tiff', 'rgb', 'sgi', 'tga', 'png', 'exr', 'dng']
        meta_ext = ['ale', 'xml']
        audio_ext = ['aac', 'wav', 'aif', 'aiff', 'mp3', 'ac3', 'bwf', 'flac', 'm4a', 'ogg', 'wma', 'm2a']
        gfx_ext = ['psd', 'ai', 'pdf', 'eps']
        office_ext = ['pptx', 'doc', 'docx', 'xls', 'xlsx', 'csv']
        other_ext = ['aae', 'indd', 'ppro', 'c', 'cc', 'cube', '3dl']
        groups = dict(multiframe=multi_frame_ext, sequence=image_ext, metadata=meta_ext, audio=audio_ext,
                      graphics=gfx_ext, office=office_ext, other=other_ext)
        return groups

    def walk_dirs(self, in_path):
        """
        Returns all files in a directory as a list of paths

        if full path to filename is provided as in_path, it will only return
        It works recursive if recursive=True

        It will return empty list if path doesn't exist, suppressing exceptions
        """

        self.output['status'] = "Walking directories."
        if not in_path or not os.path.exists(in_path.rstrip('/\\') or in_path):
            # a path that doesn't exist (yet, e.g. while typing it) must not
            # scan its parent folder tree
            return []
        if os.path.isfile(in_path):
            # a file (e.g. the vendor csv dropped on Package Folder, or -i
            # pointing at it) stands for its folder: scan the folder
            my_dir = os.path.dirname(in_path)
        else:
            my_dir = in_path
        return_list = []
        for dir_path, dir_names, file_names in os.walk(my_dir):
            for one_file in file_names:
                return_list.append(os.path.join(dir_path, one_file))
        return return_list

    def multirames_from_file_list(self, file_list):

        self.output['status'] = "Finding multiframes in files." \
                                " (multirames_from_file_list)"
        temp_result = {}
        output_list = []

        file_extension_groups = self.get_file_extension_groups()
        mf_ext = file_extension_groups['multiframe']

        # build a dictionary of the sequences as {keyname: frames, fullpathofone(maybe last)file}
        # eg c:\mydir\beauty01.tif ... beauty99.tif  will convert to
        # { c:\mydir\beautytif : [1,2,...,98,99], c:\mydir\beauty.99.tif }
        # every value in key - value pair is list of three items :
        #   list of numbers, fullpath, list of missing numbers, list of subranges

        # [{'end_number': -1,
        #  'master_end_number': -1,
        #  'master_start_number': -1,
        #  'metadata': {},
        #  'missing_numbers': [],
        #  'path': 'F:/VW/VW30conform.mov',
        #  'pattern': 'VW30conform.mov',
        #  'start_number': -1,
        #  'sub_ranges': [{'end': -1, 'start': -1}],
        #  'trim_in': 0,
        #  'trim_out': 0}]

        if len(file_list) > 0:

            # add all multiframes to temp_result, find r3d split files
            for one_file in file_list:
                prs = parse_file_name.parse(one_file)
                fileext = str.lower(str(prs["extension"]))

                if fileext in mf_ext:
                    # only red raw files, they may produce "sequence"
                    if fileext == 'r3d':
                        mykey = prs["path"] + '/' + prs["clean_name"] + '.' + prs["extension"]
                        try:
                            temp_result[mykey][0].append(prs["number"])
                        except KeyError:
                            # we have a new file sequence, so create a new key:value pair
                            temp_result[mykey] = [[prs["number"]], prs["full_path"], [], []]
                    else:
                        mykey = prs["full_path"]
                        temp_result[mykey] = [[-1], prs["full_path"], [], []]

            for onekey in temp_result:
                frames = temp_result[onekey][0]
                frames.sort()

                if len(frames) > 0:
                    startFrame = frames[0]
                    endFrame = frames[-1]
                else:
                    startFrame = -1
                    endFrame = -1
                subRanges = []
                subRanges.append({'start': startFrame, 'end': endFrame})

                prs = parse_file_name.parse(temp_result[onekey][1])
                # add printf and hash pattern for convenience
                patt = prs["name"] + '.' + prs["extension"]

                if endFrame == -1:
                    _category = 'video'
                else:
                    # split video like long r3d
                    _category = 'video'

                onedict = {'path': temp_result[onekey][1], 'missing_numbers': [], 'sub_ranges': subRanges,
                           'printf_pattern': patt, 'hash_pattern': patt,
                           'master_start_number': startFrame, 'master_end_number': endFrame,
                           'start_number': startFrame, 'end_number': endFrame,
                           'trim_in': 0, 'trim_out': 0,
                           'category': _category
                           }
                if startFrame == -1 or endFrame == -1:
                    _range = ''
                    _range_slate = ''
                    _sequence = prs['name']
                    _sequence_slate = prs['name']
                    _sequence_nuke = prs['name']
                    _sequence_slate_nuke = prs['name']
                else:
                    _range = str(onedict['start_number']).zfill(prs['padding'])\
                             + '-' + str(onedict['end_number']).zfill(
                        prs['padding'])
                    _range_slate = str(onedict['start_number'] + 1).zfill(
                        prs['padding']) + '-' + str(onedict['end_number']).zfill(
                        prs['padding'])
                    _sequence = prs['name'] + _range
                    _sequence_slate = prs['name'] + _range_slate
                    _sequence_nuke = prs['name'] + '[' + _range + ']'
                    _sequence_slate_nuke = prs['name']\
                                           + '[' + _range_slate + ']'
                onedict.update({
                    'sequence':_sequence,
                    'sequence_slate': _sequence_slate,
                    'sequence_nuke':_sequence_nuke,
                    'sequence_slate_nuke': _sequence_slate_nuke
                })

                prs['path_prs'] = prs.pop('path')  # path in one_dict shadows path from parse
                onedict.update(prs)

                numbered_parts = {}
                for one_dir in range(-9, 0):
                    try:
                        numbered_parts['part' + str(-1 * one_dir)] = \
                        prs['parts'][one_dir]
                    except Exception:
                        numbered_parts['part' + str(-1 * one_dir)] = ''
                onedict.update(numbered_parts)

                output_list.append(onedict)

        return sorted(output_list, key=itemgetter('path'))

    def other_files_from_file_list(self, file_list):

        self.output['status'] = "Finding other file types in files." \
                                " (other_files_from_file_list)"
        temp_result = {}
        output_list = []
        ext_grp = self.get_file_extension_groups()
        mf_ext = ext_grp['audio'] + ext_grp['graphics'] + ext_grp['office'] + ext_grp['other']
        regular_ext = ext_grp['sequence'] + ext_grp['multiframe'] + ext_grp['metadata']

        if len(file_list) > 0:
            # add all multiframes to temp_result, find r3d split files
            for one_file in file_list:
                prs = parse_file_name.parse(one_file)
                fileext = str.lower(str(prs["extension"]))

                if fileext in mf_ext:
                    mykey = prs["full_path"]
                    temp_result[mykey] = [[-1], prs["full_path"], [], []]
                elif fileext in regular_ext:
                    pass
                else:
                    # also add UNKNOWN extensions
                    mykey = prs["full_path"]
                    temp_result[mykey] = [[-1], prs["full_path"], [], []]

            for onekey in temp_result:
                frames = temp_result[onekey][0]
                frames.sort()

                if len(frames) > 0:
                    startFrame = frames[0]
                    endFrame = frames[-1]
                else:
                    startFrame = -1
                    endFrame = -1
                subRanges = []
                subRanges.append({'start': startFrame, 'end': endFrame})

                prs = parse_file_name.parse(temp_result[onekey][1])
                patt = prs["name"] + '.' + prs["extension"]

                # .WAV is audio like .wav
                ext_low = str(prs["extension"]).lower()
                _cat = 'unknown'
                for _group in ('audio', 'graphics', 'office', 'other', 'sequence',
                               'multiframe', 'metadata'):
                    if ext_low in ext_grp[_group]:
                        _cat = _group
                        break

                onedict = {'path': temp_result[onekey][1], 'missing_numbers': [], 'sub_ranges': subRanges,
                            'printf_pattern': patt,
                            'master_start_number': startFrame, 'master_end_number': endFrame,
                            'start_number': startFrame, 'end_number': endFrame,
                            'trim_in': 0, 'trim_out': 0,
                            'category': _cat
                           }

                _range = ''
                _range_slate = ''
                _sequence = prs['name']
                _sequence_slate = prs['name']
                _sequence_nuke = prs['name']
                _sequence_slate_nuke = prs['name']
                onedict.update({
                    'sequence':_sequence,
                    'sequence_slate': _sequence_slate,
                    'sequence_nuke':_sequence_nuke,
                    'sequence_slate_nuke': _sequence_slate_nuke
                })

                prs['path_prs'] = prs.pop('path') # path in one_dict shadows path from parse
                onedict.update(prs)

                numbered_parts = {}
                for one_dir in range(-9, 0):
                    try:
                        numbered_parts['part' + str(-1 * one_dir)] = \
                            prs['parts'][one_dir]
                    except Exception:
                        numbered_parts['part' + str(-1 * one_dir)] = ''
                onedict.update(numbered_parts)

                output_list.append(onedict)

        return sorted(output_list, key=itemgetter('path'))

    def seq_list_from_file_list(self, file_list, mode='to_subsequences'):
        """
        Creates list of file sequences from list of files
        List of files can be recursive, ie there can be files from more then one directory

        File sequence can be:
            path/file001.ext - path/file009.ext
            path/file001.ext - numbered file, but only one file
            path/file.ext - only one file, not numbered

        If file sequence has missing frames, there are several ways to represent them with valid subranges in mind.
            If mode = holes_allowed
                output is one data struct per sequence with holes or not
            If mode = to_subsequences
                output as many sequences from one (master, with holes) sequnce as needed for all valid subranges
            If mode = to_first_hole
                output is one data struct per sequence with holes, end_number is last valid frame before first hole
            If mode = skip_seq_with_holes
                do not include sequences with holes in output


        Output data structure is list of dictionaries, one dictionary:
            path - full path to first frame of sequence (or subrange in sequence)
            missing_numbers - list of numbers missing in the sequence if sequence has missing frames
            subranges - list of dictionaries with start and end number for each subrange.
            pattern - name part of full path with printf notation
            start_number - first number in seq
            end_number - last number in seq
            trim_in - for sequence made from subranges, this indicates how many frames to remove from original seq with hole(s) start to get first frame of subrange
            trim_out - for sequence made from subranges, this indicates how many frames to remove from original seq with hole(s) end to get last frame of subrange

            >>>import pprint
            >>>
            >>>test_list=['F:/VW/scanTest/R1/0094288.dpx',
                         'F:/VW/scanTest/R1/0094289.dpx',
                         'F:/VW/scanTest/R1/0094287.dpx',
                         'F:/VW/scanTest/R1/blb/nemaCislo.dpx',
                         'F:/VW/scanTest/R1/blb/maJenNulu0.dpx',
                         'F:/VW/scanTest/R2/0180572.dpx',
                         'F:/VW/scanTest/R2/0180573.dpx',
                         'F:/VW/scanTest/R2/0180574.dpx',
                         'F:/VW/scanTest/R2/0180577.dpx',
                         'F:/VW/scanTest/R2/0180578.dpx',
                         'F:/VW/scanTest/R2/0180579.dpx',
                         'F:/VW/scanTest/R3/2048x1156/0279388.dpx',
                         'F:/VW/scanTest/R3/2048x1156/0279382.dpx',
                         'F:/VW/scanTest/R3/2048x1156/0279383.dpx',
                         'F:/VW/scanTest/R3/2048x1156/0279384.dpx',
                         'F:/VW/scanTest/R3/2048x1156/0279380.dpx',
                         'F:/VW/scanTest/R3/2048x1156/test0301338.dpx',
                         'F:/VW/scanTest/0094287.dpx',
                         'F:/VW/scanTest/0094288.dpx']
            >>>pprint.pprint(self.seq_list_from_file_list(test_list, sequence_can_have_holes= True, sequence_to_first_hole=True))
            >>>[{ 'end_number': 279380,
                  'missing_numbers': [279381, 279385, 279386, 279387],
                  'path': 'F:/VW/scanTest/R3/2048x1156/0279380.dpx',
                  'pattern': '%07d.dpx',
                  'start_number': 279380,
                  'subranges': [{'end': 279380, 'start': 279380},
                                {'end': 279384, 'start': 279382},
                                {'end': 279388, 'start': 279388}],
                  'trim_in': 0,
                  'trim_out': 8},
                 {'end_number': 180574,
                  'missing_numbers': [180575, 180576],
                  'path': 'F:/VW/scanTest/R2/0180572.dpx',
                  'pattern': '%07d.dpx',
                  'start_number': 180572,
                  'subranges': [{'end': 180574, 'start': 180572},
                                {'end': 180579, 'start': 180577}],
                  'trim_in': 0,
                  'trim_out': 5},
                 {'end_number': 94288,
                  'missing_numbers': [],
                  'path': 'F:/VW/scanTest/0094287.dpx',
                  'pattern': '%07d.dpx',
                  'start_number': 94287,
                  'subranges': [{'end': 94288, 'start': 94287}],
                  'trim_in': 0,
                  'trim_out': 0},
                 {'end_number': 94289,
                  'missing_numbers': [],
                  'path': 'F:/VW/scanTest/R1/0094287.dpx',
                  'pattern': '%07d.dpx',
                  'start_number': 94287,
                  'subranges': [{'end': 94289, 'start': 94287}],
                  'trim_in': 0,
                  'trim_out': 0},
                 {'end_number': -1,
                  'missing_numbers': [],
                  'path': 'F:/VW/scanTest/R1/blb/nemaCislo.dpx',
                  'pattern': 'nemaCislo.dpx',
                  'start_number': -1,
                  'subranges': [{'end': -1, 'start': -1}],
                  'trim_in': 0,
                  'trim_out': 0},
                 {'end_number': 0,
                  'missing_numbers': [],
                  'path': 'F:/VW/scanTest/R1/blb/maJenNulu0.dpx',
                  'pattern': 'maJenNulu%1d.dpx',
                  'start_number': 0,
                  'subranges': [{'end': 0, 'start': 0}],
                  'trim_in': 0,
                  'trim_out': 0},
                 {'end_number': 301338,
                  'missing_numbers': [],
                  'path': 'F:/VW/scanTest/R3/2048x1156/test0301338.dpx',
                  'pattern': 'test%07d.dpx',
                  'start_number': 301338,
                  'subranges': [{'end': 301338, 'start': 301338}],
                  'trim_in': 0,
                  'trim_out': 0}]
        """

        def fix_seq(one_rec, parsed):
            """
            adds sequence specific keys, and detects stills
            """

            if one_rec['end_number'] == -1:
                one_rec['category'] = 'still'
            elif one_rec['end_number'] == one_rec['start_number']:
                one_rec['category'] = 'still'

            else:
                # file name sequence
                _range = str(one_rec['start_number']).zfill(parsed['padding']) \
                         + '-' + str(one_rec['end_number']).zfill(parsed['padding'])
                _range_slate = str(one_rec['start_number'] + 1).zfill(parsed['padding']) \
                               + '-' + str(one_rec['end_number']).zfill(parsed['padding'])
                _sequence = parsed['clean_name'] + _range
                _sequence_slate = parsed['clean_name'] + _range_slate
                _sequence_nuke = parsed['clean_name'] + '[' + _range + ']'
                _sequence_slate_nuke = parsed['clean_name'] + '[' + _range_slate + ']'
                _more = {"range": _range,
                         "range_slate": _range_slate,
                         "sequence": _sequence,
                         "sequence_slate": _sequence_slate,
                         "sequence_nuke": _sequence_nuke,
                         "sequence_slate_nuke": _sequence_slate_nuke,
                         }
                one_rec.update(_more)

            # fill sequence for still as well, for convenience
            if one_rec['category'] == 'still':
                _more = {
                    "sequence": parsed['name'],
                    "sequence_slate": parsed['name'],
                    "sequence_nuke": parsed['name'],
                    "sequence_slate_nuke": parsed['name'],
                }
                one_rec.update(_more)

            return one_rec

        self.output['status'] = "Finding sequences in files. (seg_list_from_file_list)"
        temp_result = {}
        output_list = []

        file_extension_groups = self.get_file_extension_groups()
        sq_ext = file_extension_groups['sequence']

        # build a dictionary of the sequences as {keyname: frames, fullpathofone(maybe last)file}
        # eg c:\mydir\beauty01.tif ... beauty99.tif  will convert to
        # { c:\mydir\beautytif : [1,2,...,98,99], c:\mydir\beauty.99.tif }
        # every value in key - value pair is list of three items : list of numbers,
        # fullpath, list of missing numbers, list of subranges

        if len(file_list) > 0:
            for one_file in file_list:
                prs = parse_file_name.parse(one_file)
                img_ext = str.lower(str(prs["extension"]))

                # only image sequences
                if img_ext in sq_ext:
                    mykey = prs["path"] + '/' + prs["clean_name"] + '.' + prs["extension"]
                    try:
                        temp_result[mykey][0].append(prs["number"])
                    except KeyError:
                        # we have a new file sequence, so create a new key:value pair
                        temp_result[mykey] = [[prs["number"]], prs["full_path"], [], []]
                else:
                    pass

            # find start and end frames, plus missing frames
            for one_key in temp_result:
                frames = temp_result[one_key][0]
                frames.sort()

                if len(frames) > 0:
                    # find gaps in sequence
                    start_frame = frames[0]
                    end_frame = frames[-1]
                    ideal_range = set(range(start_frame, end_frame + 1))
                    real_frames = set([int(x) for x in frames])
                    # sets can't be sorted, so cast to a list here
                    missing_frames = list(ideal_range - real_frames)
                    missing_frames.sort()

                    # add list of missing frames to temp_results
                    temp_result[one_key][2] = missing_frames

                    # fix fullpath to be first frame of seq
                    prs = parse_file_name.parse(temp_result[one_key][1])
                    _pad = parse_file_name.pad_frame(start_frame, prs['padding'])
                    temp_result[one_key][1] = prs['path'] + '/' + prs['clean_name'] + _pad + '.' + prs['extension']

                    # get sub_ranges
                    sub_ranges = []
                    for gap in missing_frames:
                        if start_frame != gap:
                            sub_ranges.append({'start': start_frame, 'end': gap - 1})
                        start_frame = gap + 1

                    sub_ranges.append({'start': start_frame, 'end': end_frame})
                    temp_result[one_key][3] = sub_ranges

                    patt, hash_patt = parse_file_name.printf_pattern(temp_result[one_key][1])
                    prs = parse_file_name.parse(temp_result[one_key][1])

                    # now we have all data gathered, let's format it nicely for output
                    one_record = {'path': temp_result[one_key][1], 'missing_numbers': temp_result[one_key][2],
                                    'sub_ranges': temp_result[one_key][3], 'printf_pattern': patt, 'hash_pattern': hash_patt,
                                    'master_start_number': frames[0], 'master_end_number': frames[-1],
                                    'category': 'sequence'}
                    prs['path_prs'] = prs.pop('path')  # path in one_dict shadows path from parse
                    one_record.update(prs)
                    numbered_parts = {}
                    for one_dir in range(-9, 0):
                        try:
                            numbered_parts['part' + str(-1 * one_dir)] = prs['parts'][one_dir]
                        except Exception:
                            numbered_parts['part' + str(-1 * one_dir)] = ''
                    one_record.update(numbered_parts)

                    if mode == 'to_first_hole':
                        # seq can have holes, but only first sub is valid
                        one_record['start_number'] = frames[0]
                        one_record['end_number'] = sub_ranges[0]['end']
                        one_record['trim_in'] = 0
                        one_record['trim_out'] = frames[-1] - sub_ranges[0]['end']
                        output_list.append(fix_seq(one_record, prs))
                    elif mode == 'holes_allowed':
                        # seq can have holes
                        one_record['start_number'] = frames[0]
                        one_record['end_number'] = frames[-1]
                        one_record['trim_in'] = 0
                        one_record['trim_out'] = 0
                        output_list.append(fix_seq(one_record, prs))
                    elif mode == 'to_subsequences':
                        # seq for every subseq
                        for one_subrange in sub_ranges:
                            sub_range_first_frame = prs['path_prs'] + '/' + prs['clean_name'] + parse_file_name.pad_frame(
                                one_subrange['start'], prs['padding']) + '.' + prs['extension']
                            # a copy per sub range: the same dict appended N
                            # times made every sub sequence the last one
                            sub_record = dict(one_record)
                            sub_record['path'] = sub_range_first_frame
                            sub_record['start_number'] = one_subrange['start']
                            sub_record['end_number'] = one_subrange['end']
                            sub_record['trim_in'] = one_subrange['start'] - frames[0]
                            sub_record['trim_out'] = frames[-1] - one_subrange['end']
                            output_list.append(fix_seq(sub_record, prs))
                    elif mode == 'skip_seq_with_holes':
                        if len(temp_result[one_key][2]) > 0:
                            pass
                        else:
                            one_record['start_number'] = frames[0]
                            one_record['end_number'] = frames[-1]
                            one_record['trim_in'] = 0
                            one_record['trim_out'] = 0
                            output_list.append(fix_seq(one_record, prs))

        # return output_list sorted by path
        return sorted(output_list, key=itemgetter('path'))

    def filter_items_add_counters(self):
        """
        For every one of three "exports", you can filter out files to not be included
        There is exclude if path contains string and
        Include only if path contains a string

        """

        sub_exclude_list = ""
        sub_include_list = ""
        log_exclude_list = ""
        log_include_list = ""
        txt_exclude_list = ""
        txt_include_list = ""
        # file age defaults (a preset without the age settings)
        _age_enabled = False
        _age_number = 0.0
        _age_unit = 'days'
        _age_type = 'modified'
        age_exclude = []
        age_include = []
        counter_start = 1
        counter_step = 1
        counter_zeroes = 3
        if self.settings:
            sub_exclude_list = self._get_str('sub_exclude').split()
            sub_include_list = self._get_str('sub_include').split()
            log_exclude_list = self._get_str('log_exclude').split()
            log_include_list = self._get_str('log_include').split()
            txt_exclude_list = self._get_str('txt_exclude').split()
            txt_include_list = self._get_str('txt_include').split()

            # 0 is a valid counter start (it used to be ignored)
            counter_start = self._get_int('prefs_counter_start', counter_start)
            counter_step = self._get_int('prefs_counter_step', counter_step)
            counter_zeroes = self._get_int('prefs_counter_zeroes', counter_zeroes)

            # age
            _age_enabled = bool(self._get('age_enabled', _age_enabled))
            try:
                _age_number = float(self._get('age_number', _age_number))
            except (TypeError, ValueError):
                _age_number = 0.0
            _age_unit = self._get_str('age_unit', _age_unit) or _age_unit
            _age_type = self._get_str('age_type', _age_type) or _age_type
            age_exclude = self._get_str('age_exclude').split()
            age_include = self._get_str('age_include').split()

        # totals are 0 for an empty package (they used to be unbound)
        cnt_sub = cnt_log = cnt_txt = counter_start
        total_sub = total_log = total_txt = 0
        files_sub = files_log = files_txt = 0
        total_size_sub = total_size_log = total_size_txt = 0

        if self.merged_list and len(self.merged_list) > 0:
            for one_item in self.merged_list:
                one_item.update({"hide_sub": False})
                one_item.update({"hide_log": False})
                one_item.update({"hide_txt": False})

                # include ONLY
                if sub_include_list:
                    sub_found = False
                    for one_included in sub_include_list:
                        if one_included in one_item['path']:
                            sub_found = True
                            break
                    if not sub_found:
                        one_item['hide_sub'] = True
                if log_include_list:
                    log_found = False
                    for one_included in log_include_list:
                        if one_included in one_item['path']:
                            log_found = True
                            break
                    if not log_found:
                        one_item['hide_log'] = True
                if txt_include_list:
                    txt_found = False
                    for one_included in txt_include_list:
                        if one_included in one_item['path']:
                            txt_found = True
                            break
                    if not txt_found:
                        one_item['hide_txt'] = True

                # exclude
                for one_excluded in sub_exclude_list:
                    if one_excluded in one_item['path']:
                        one_item['hide_sub'] = True
                for one_excluded in log_exclude_list:
                    if one_excluded in one_item['path']:
                        one_item['hide_log'] = True
                for one_excluded in txt_exclude_list:
                    if one_excluded in one_item['path']:
                        one_item['hide_txt'] = True

                # hide by AGE, for submission Only
                if _age_enabled and not one_item['hide_sub']:
                    age_key = 'age_' + _age_unit + '_' + _age_type
                    item_age = one_item.get(age_key) or 0
                    hide_item = False
                    if item_age > _age_number:
                        _full_path = one_item.get('full_path', one_item.get('path', ''))
                        # Age Include: only these files are hidden by age
                        hide_item = (not age_include) or any(
                            one in _full_path for one in age_include)
                        # Age Exclude: never hidden by age, even if included
                        if any(one in _full_path for one in age_exclude):
                            hide_item = False
                        if hide_item:
                            one_item['hide_sub'] = True

                # Vendor tab: files not in the vendor csv (vendor_csv_add)
                one_item['vendor_ignore_sub'] = bool(one_item['hide_sub']) or \
                    bool(one_item.get('vendor_skip'))

                # add counter to the items that are not hidden
                try:
                    _frames = int(float(one_item.get('meta_duration_frames') or 0))
                except (TypeError, ValueError):
                    _frames = 0
                if not one_item['vendor_ignore_sub']:
                    one_item.update({"cnt_sub": str(cnt_sub).zfill(counter_zeroes)})
                    cnt_sub += counter_step
                    total_sub += 1
                    if one_item['category'] == 'sequence':
                        files_sub += _frames
                    else:
                        files_sub += 1
                    _bytes = one_item.get('size_bytes') or 0
                    total_size_sub += _bytes

                if not one_item['hide_log']:
                    one_item.update({"cnt_log": str(cnt_log).zfill(counter_zeroes)})
                    cnt_log += counter_step
                    total_log += 1
                    if one_item['category'] == 'sequence':
                        files_log += _frames
                    else:
                        files_log += 1
                    _bytes = one_item.get('size_bytes') or 0
                    total_size_log += _bytes

                if not one_item['hide_txt']:
                    one_item.update({"cnt_txt": str(cnt_txt).zfill(counter_zeroes)})
                    cnt_txt += counter_step
                    total_txt += 1
                    if one_item['category'] == 'sequence':
                        files_txt += _frames
                    else:
                        files_txt += 1
                    _bytes = one_item.get('size_bytes') or 0
                    total_size_txt += _bytes

        totals = {
            'total_sub': total_sub,
            'total_log': total_log,
            'total_txt': total_txt,
            'files_sub': files_sub,
            'files_log': files_log,
            'files_txt': files_txt,
            'total_size_sub': total_size_sub,
            'total_size_log': total_size_log,
            'total_size_txt': total_size_txt,
            'total_size_sub_human': helpers.humanize_file_size(
            total_size_sub),
            'total_size_log_human': helpers.humanize_file_size(
            total_size_log),
            'total_size_txt_human': helpers.humanize_file_size(
            total_size_txt)
        }
        self.static_keywords.update(totals)

    def prepare_regex(self):
        """
        Read regexes from gui
        Compiles regexes
        :return:
        dir of dirs
        """

        self.regexes = {}
        if self.settings:
            def _val(k):
                # presets saved before the extra rows existed don't have them
                return (self.settings.get(k) or {}).get("value") or ""

            indexes = [str(x).zfill(2) for x in range(1, PARSE_ROWS + 1)]
            for one in indexes:
                key = _val("parse_name_" + one)
                pat = _val("parse_pattern_" + one)
                fltr = _val("parse_filter_" + one)
                pat_compiled = None
                pat_valid = False
                if pat:
                    try:
                        pat_compiled = re.compile(pat)
                        pat_valid = True
                    except re.error as e:
                        # debug only: patterns are invalid while being typed
                        self.log.debug(f"Parsing row {one}: invalid pattern '{pat}': {e}")
                rep = _val("parse_repl_" + one)
                src = _val("parse_source_" + one)

                # only add regex if it is valid and not empty
                if key and pat and src and pat_valid:
                    one_regex = {one: {"key": key,
                                       "pattern": pat,
                                       "valid": pat_valid,
                                       "compiled": pat_compiled,
                                       "repl": rep,
                                       "source": src,
                                       "filter": fltr
                                       }}
                    self.regexes.update(one_regex)

    def fill_regexes(self):
        """
        For every item in merged list
        it generates the regex keywords
        :return:
        """

        class Default(dict):
            def __missing__(self, key):
                return '{' + key + '}'

        if self.merged_list and len(self.merged_list) > 0:
            for one_item in self.merged_list:
                # values the parse rows replaced: put them back first, so a row
                # that no longer applies (Filter, removed row) leaves no old result
                originals = one_item.setdefault('_parse_orig', {})
                for key, (had, value) in originals.items():
                    if had:
                        one_item[key] = value
                    else:
                        one_item.pop(key, None)
                # Parsing tab Preview: result of each row that ran for this
                # item, by row number ('01'...); filtered out rows aren't in it
                previews = {}
                one_item['_parse_preview'] = previews
                for k, one_regex in self.regexes.items():
                    do_filter = False
                    if one_regex['filter'] != '':
                        if not (one_regex['filter'] in one_item['path']):
                            do_filter = True
                    if not do_filter:
                        # expand keywords in source; an unknown token gives ''
                        try:
                            expanded = one_regex["source"].format(**one_item)
                        except KeyError:
                            expanded = None
                        except (ValueError, IndexError, AttributeError):
                            # stray braces: expand the known tokens only
                            expanded = expand_tokens(one_regex["source"], one_item)
                            if unresolved_tokens(expanded):
                                expanded = None
                        if expanded and expanded != '':
                            # expand static keywords
                            expanded = format_keep(expanded, self.static_keywords)
                            if one_regex["repl"] and one_regex["repl"] != "":
                                # it is a replace
                                if one_regex["repl"].startswith("lambda "):
                                    #LAMBDA!
                                    try:
                                        _eval = eval(str(one_regex["repl"]))
                                    except Exception as e:
                                        self.log.debug(f"Parsing row {k}: invalid lambda: {e}")
                                        _eval = one_regex["repl"]
                                    try:
                                        result = re.sub(one_regex["compiled"], _eval, expanded)
                                    except Exception as e:
                                        self.log.debug(f"Parsing row {k}: replace failed: {e}")
                                        result = ""
                                else:
                                    try:
                                        result = re.sub(one_regex["compiled"], one_regex["repl"], expanded)
                                    except (re.error, IndexError) as e:
                                        self.log.debug(f"Parsing row {k}: replace failed: {e}")
                                        result = ""
                            else:
                                m = one_regex["compiled"].search(expanded)
                                if m:
                                    # if user made a group, assign the group, otherwise use whole found string
                                    result = m.group(1) if one_regex["compiled"].groups else m.group(0)
                                    if result is None:
                                        # optional group that took no part in the match
                                        result = ""
                                else:
                                    # shot name exists but doesn't match the regex, so set shot name to empty string
                                    result = ""
                        else:
                            result = ""
                        key = one_regex["key"]
                        if key not in originals:
                            originals[key] = (key in one_item, one_item.get(key))
                        one_item.update({key: result})
                        previews[k] = result

    def prepare_package_name(self):

        class Default(dict):
            def __missing__(self, key):
                return '{' + key + '}'

        def str_to_bool(my_str):
            if my_str == "True":
                _b = True
            elif my_str == "False":
                _b = False
            else:
                _b = bool(my_str)
            return _b

        date_keys = {
            'y': str(int(time.strftime("%Y"))),
            'yy': str(int(time.strftime("%Y")))[2:],
            'm': str(int(time.strftime("%m"))),
            'mm': str(int(time.strftime("%m"))).zfill(2),
            'd': str(int(time.strftime("%d"))),
            'dd': str(int(time.strftime("%d"))).zfill(2),
            'package_version': '',
        }

        self.output['status'] = "Making package name." \
                                " (prepare_package_name)"

        _from_template = False
        if self.settings['name_from_template']['value'] is not None:
            _from_template = bool(self.settings['name_from_template']['value'])

        def _setting(key, default):
            item = self.settings.get(key)
            if isinstance(item, dict) and item.get('value') is not None:
                return item['value']
            return default

        def _compile(pattern, what):
            """regex from the gui; date tokens like {yy} are expanded first"""
            if not pattern:
                return None
            try:
                return re.compile(expand_tokens(pattern, date_keys))
            except re.error as e:
                self.log.warning(f"Package name: invalid {what} {pattern!r}: {e}")
                return None

        def _first_group(compiled, text):
            """group 1 of the match, or the whole match when there is no group"""
            if compiled is None:
                return ''
            m = compiled.search(text)
            if not m:
                return ''
            return m.group(1) if compiled.groups else m.group(0)

        _template = _setting('name_template', '') or ''
        _date_compiled = _compile(_setting('name_date_regex', ''), 'Date Regex')
        _version_compiled = _compile(_setting('name_version_regex', ''), 'Version Regex')
        _pkg_folder = _setting('package_folder', '') or ''
        _per_date = bool(_setting('name_version_per_date', False))
        try:
            _ver_zeroes = int(_setting('name_version_zeroes', 0) or 0)
        except (TypeError, ValueError):
            _ver_zeroes = 0
        _ver_letters = bool(_setting('name_version_use_letters', False))
        _ver_upper = bool(_setting('name_version_letters_uppercase', True))

        # get current date by applying regex to expanded template
        _temp_expanded = format_keep(_template, date_keys)
        if unresolved_tokens(_temp_expanded):
            self.log.warning(
                f"Package name template {_template!r}: only {{y}} {{yy}} {{m}} {{mm}} {{d}} "
                f"{{dd}} and {{package_version}} can be used, "
                f"unknown: {', '.join(unresolved_tokens(_temp_expanded))}")
        current_date = _first_group(_date_compiled, _temp_expanded)
        if _per_date and _from_template and not current_date:
            self.log.warning(
                "Package name: Date Regex finds no date in the template "
                f"{_temp_expanded!r}, so Per Date can't tell the dates apart")

        one_up = ''
        name_from_folder = ''
        # make sure path exists, it is a directory and has no trailing slash
        if _pkg_folder and os.path.exists(_pkg_folder):
            if _pkg_folder is None:
                _pkg_folder = ''
            else:
                # to detect if _pkg_folder is full path
                # or just path to directory with no end slash
                _pkg_folder = _pkg_folder.replace('\\', '/')
                if os.path.isdir(_pkg_folder) and (_pkg_folder[-1] == '/'):
                    # remove trailing slash
                    _pkg_folder = _pkg_folder[:-1]
                _spl = _pkg_folder.split('/')
                one_up = '/'.join(_spl[:-1])
                name_from_folder = _spl[-1]

        if not _from_template:
            # take submission name from folder name
            date_keys.update({
                'package_version': '',
                'package_date': '',
                'package_name_from_folder': name_from_folder,
                'package_name': name_from_folder,
                'package_name_root': one_up
            })
        else:
            # list all dirs, parse date and version
            dir_list = []
            try:
                siblings = os.listdir(one_up) if one_up else []
            except OSError as e:
                self.log.warning(f"Package name: can't list {one_up}: {e}")
                siblings = []
            for filename in siblings:
                if os.path.isdir(os.path.join(one_up, filename)):
                    if filename != name_from_folder:
                        dir_list.append({
                            'folder': filename,
                            'date': _first_group(_date_compiled, filename),
                            'version': _first_group(_version_compiled, filename)
                        })

            def _version_key(one_dir):
                """numbers compare by value (9 < 10), letters alphabetically"""
                v = one_dir['version']
                if v.isdigit():
                    return (0, int(v), '')
                return (1, 0, v.upper())

            if _per_date:
                # each date has separate version chain
                candidates = [d for d in dir_list
                              if d['date'] == current_date and d['version']]
            else:
                candidates = [d for d in dir_list if d['version']]
            if _ver_letters:
                candidates = [d for d in candidates
                              if len(d['version']) == 1 and d['version'].isalpha()]
            else:
                candidates = [d for d in candidates if d['version'].isdigit()]
            last_dir = max(candidates, key=_version_key) if candidates else None
            last_version = last_dir['version'] if last_dir else None

            if _ver_letters:
                if last_version is None:
                    next_version = 'A'
                elif last_version.upper() == 'Z':
                    next_version = 'A'
                    self.log.warning("Package name: version Z is used, next letter "
                                     "version wraps around to A")
                else:
                    next_version = chr(ord(last_version.upper()) + 1)
                if not _ver_upper:
                    next_version = next_version.lower()
            else:
                last_number = int(last_version) if last_version else 0
                next_version = str(last_number + 1).zfill(_ver_zeroes)

            # add what we know
            if _per_date:
                date_keys.update({
                    'package_version': next_version,
                    'package_date': current_date,
                    'package_name_from_folder': name_from_folder,
                    'package_name_root': one_up
                })
            else:
                date_keys.update({
                    'package_version': next_version,
                    'package_date': '',
                    'package_name_from_folder': name_from_folder,
                    'package_name_root': one_up
                })

            # use source folder as name
            _pkg_new_name = name_from_folder
            # expand template to make package name
            if _template:
                _pkg_new_name = format_keep(_template, date_keys)

            date_keys.update({
                'package_name': _pkg_new_name,
            })

        # make public
        self.static_keywords = {**date_keys, **self.static_keywords}
        # add to outputs
        self.output.update(date_keys)

    def prepare_columns(self, gui_columns, editable=None):
        """
        For Spreadsheet Table, parse columns

        Gets columns definition as a string like:
        Thumbnail={thumb_path}, Thumbnail={created_thumb_path},
        Shot={shot_name}, CheckShot={check_shot_name}, Notes=*{note}, ...
        Returns two lists: column_titles and column_expressions
        Title=*value: the column can be edited in the gui table; the * is not
        part of the expression. editable (a list) gets one bool per column.
        """

        column_titles = []
        column_expressions = []
        # one column per line works like comma separated (the result of
        # replace() used to be thrown away)
        gui_columns = str(gui_columns or '').replace("\r", "").replace("\n", ",")

        # title up to the first '=', spaces around both parts removed
        NM_RE = re.compile(r"^\s*(?P<column_title>[^=]*?)\s*=\s*(?P<column_expression>.*?)\s*$")
        split_list = gui_columns.split(",")
        column_count = 0
        columns = []

        for one_column in split_list:
            m = NM_RE.search(one_column)
            if m:
                title = m.group("column_title")
                expression = m.group("column_expression")
                is_editable = expression.startswith('*')
                if is_editable:
                    expression = expression[1:].lstrip()
                if editable is not None:
                    editable.append(is_editable)
                one_itm = {
                    'column_number': column_count,
                    'title': title,
                    'expression': expression
                }
                columns.append(one_itm)
                column_titles.append(title)
                column_expressions.append(expression)
                column_count += 1

        return column_titles, column_expressions

    def prepare_all_columns(self):
        _sub = ""
        _log = ""
        _txt = ""
        if self.settings:
            if self.settings['sub_columns']['value']:
                _sub = self.settings['sub_columns']['value']
            if self.settings['log_columns']['value']:
                _log = self.settings['log_columns']['value']
            if self.settings['txt_columns']['value']:
                _txt = self.settings['txt_columns']['value']

        self.column_editable_sub = []
        self.column_editable_log = []
        self.column_titles_sub, self.column_expressions_sub =\
            self.prepare_columns(_sub, self.column_editable_sub)
        self.column_titles_log, self.column_expressions_log =\
            self.prepare_columns(_log, self.column_editable_log)
        self.column_titles_txt, self.column_expressions_txt =\
            self.prepare_columns(_txt)


    def display_file_table(self):
        """
        table data to ui
        """
        if self.ui is None or QtWidgets is None:
            # command line mode: no tables
            return
        table = self.table_files
        table_ui = self.ui.file_table
        titles = self.columns_files

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
                one_item = line[-1]
                if type(one_item) is str:
                    one_item = None
                for column_number, one_column in enumerate(titles):
                    table_ui.setItem(row,
                                     column_number,
                                     QtWidgets.QTableWidgetItem(str(line[column_number]))
                                     )

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
            table_ui.setSortingEnabled(True)

    def prepare_file_table(self):
        if self.merged_list and len(self.merged_list) > 0:
            for one_item in self.merged_list:
                has_meta =  one_item.get("got_meta", False)
                self.table_files.append(
                    [
                        one_item['sequence_nuke'] + '.' + one_item['extension'],
                        one_item['size_human'],
                        one_item['category'],
                        str(one_item['missing_numbers']),
                        str(one_item['path_prs']),
                        ""
                    ]
                )

    def prepare_tables(self):

        class Default(dict):
            def __missing__(self, key):
                return '{' + key + '}'

        self.table_sub = []
        self.table_log = []
        self.table_txt = ""
        self.table_side = []
        self.table_rename = []
        self.columns_side = ['match', 'destination', 'source']
        body_txt = ""
        txt_sep = " "
        # defaults for settings missing from older presets (NameError before)
        do_txt_titles = False
        txt_header = ""
        txt_footer = ""
        side_sub_only = False
        side_log_only = False

        for one_item in self.merged_list or []:
            # RENAMES
            _r = one_item.get('rename')
            _s = one_item.get('rename_source')
            if _r and _s:
                self.table_rename.append([_s, _r])

        if self.settings:
            if self._get('text_sep_tab', False):
                txt_sep = "\t"
            do_txt_titles = bool(self._get('text_add_titles', False))
            txt_header = self._get_str('text_header')
            txt_footer = self._get_str('text_footer')

            side_sub_only = bool(self._get('side_sub_only', False))
            side_log_only = bool(self._get('side_log_only', False))

        else:
            return

        # Grouping tab: group tokens, errors and warnings before the rows are
        # built, so {group_...} tokens and {error} include them
        groups = self.group_items()
        if self.merged_list and len(self.merged_list) > 0:

            for one_item in self.merged_list:
                one_item.update(self.static_keywords)
                # build one row, if not hidden

                if not one_item['hide_sub']:

                    if one_item['vendor_ignore_sub']:
                        continue

                    one_row_sub = []
                    for one_expression in self.column_expressions_sub:
                        try:
                            #formatted = one_expression.format(**one_item)
                            formatted = format_keep(one_expression, one_item)
                            one_row_sub.append(formatted)
                        except KeyError:
                            # can't parse expression, put it in original form
                            #one_row_sub.append(str(one_expression))
                            one_row_sub.append("")
                    #  add item to the end of the row, so we can later
                    #  on easily reference all the data for the row
                    one_row_sub.append(one_item)

                    # add to table
                    self.table_sub.append(one_row_sub)
                    one_item['_row'] = one_row_sub

                if not one_item['hide_log']:
                    one_row_log = []
                    for one_expression in self.column_expressions_log:
                        try:
                            #formatted = one_expression.format(**one_item)
                            formatted = format_keep(one_expression, one_item)
                            one_row_log.append(formatted)
                        except KeyError:
                            # can't parse expression, put it in original form
                            #one_row_log.append(str(one_expression))
                            one_row_log.append("")
                    #  add item to the end of the row, so we can later
                    #  on easily reference all the data for the row
                    one_row_log.append(one_item)
                    # add to table
                    self.table_log.append(one_row_log)

                if not one_item['hide_txt']:
                    one_row_txt = []
                    for one_expression in self.column_expressions_txt:
                        try:
                            #formatted = one_expression.format(**one_item)
                            formatted = format_keep(one_expression, one_item)
                            one_row_txt.append(formatted)
                        except KeyError:
                            # can't parse expression, put it in original form
                            #one_row_txt.append(str(one_expression))
                            one_row_txt.append("")
                    whole_row = str(txt_sep.join(one_row_txt)) + "\n"
                    body_txt += whole_row

                sides = one_item.get('sidecars', None)
                if sides:
                    if side_sub_only:
                        do_side = not one_item.get('hide_sub') and \
                            not one_item.get('vendor_ignore_sub')
                    elif side_log_only:
                        do_side = not one_item.get('hide_log')
                    else:
                        do_side = True
                    if do_side:
                        for one_side in sides:
                            one_row_side = [
                                one_side['result'],
                                one_side['dest'],
                                one_side['file']
                            ]
                            self.table_side.append(one_row_side)

            # Grouping tab: inherit columns, keep groups together, collapse
            self.table_sub = self.group_rows(self.table_sub, self.column_titles_sub, groups, 'sub')
            self.table_log = self.group_rows(self.table_log, self.column_titles_log, groups, 'log')
            # cells edited in the gui (columns Title=*value)
            self.apply_cell_edits('sub')
            self.apply_cell_edits('log')

        try:
            #_header = txt_header.format(**self.static_keywords)
            _header = format_keep(txt_header, self.static_keywords)
        except KeyError:
            _header = txt_header
        if do_txt_titles:
            _titles = '\n' + str(txt_sep.join(self.column_titles_txt)) + '\n'
        else:
            _titles = ""
        try:
            #_footer = txt_footer.format(**self.static_keywords)
            _footer = format_keep(txt_footer, self.static_keywords)
        except KeyError:
            _footer = txt_footer
        self.table_txt = _header + '\n' + _titles + body_txt + '\n' + _footer

    # ------------------------------------------------- editable table cells
    def _edit_tables(self, mode):
        """(table, titles, editable flags) of 'sub' or 'log'"""
        if mode == 'sub':
            return self.table_sub, self.column_titles_sub, getattr(self, 'column_editable_sub', None)
        if mode == 'log':
            return self.table_log, self.column_titles_log, getattr(self, 'column_editable_log', None)
        return None, None, None

    @staticmethod
    def row_edit_key(row):
        """
        What a table row is, over table rebuilds: the file path, for a
        collapsed group row the group. None: the row can't keep edits.
        """
        it = row[-1] if row and isinstance(row[-1], dict) else None
        if not it:
            return None
        if it.get('_group_members'):
            group = it.get('group_key') or it.get('_group_number')
            return f"group:{group}" if group else None
        key = it.get('path') or it.get('sequence_nuke')
        return str(key) if key else None

    def is_cell_editable(self, mode, column):
        _, _, editable = self._edit_tables(mode)
        return bool(editable) and 0 <= column < len(editable) and editable[column]

    def set_cell_edit(self, mode, row_index, column, value):
        """
        A cell edited in the gui: the table row gets the value (so the tables,
        the exports and the Ayon publish csv use it) and it is kept for the
        next table rebuild. :return: True when stored
        """
        table, titles, _ = self._edit_tables(mode)
        if not table or not titles or not self.is_cell_editable(mode, column):
            return False
        if not 0 <= row_index < len(table) or column >= len(titles):
            return False
        row = table[row_index]
        key = self.row_edit_key(row)
        if key is None or column >= len(row) - 1:
            return False
        row[column] = value
        if getattr(self, 'cell_edits', None) is None:
            self.cell_edits = {'sub': {}, 'log': {}}
        self.cell_edits.setdefault(mode, {})[(key, titles[column])] = value
        return True

    def apply_cell_edits(self, mode):
        """put the kept cell edits into the rebuilt table (editable columns only)"""
        edits = (getattr(self, 'cell_edits', None) or {}).get(mode)
        table, titles, editable = self._edit_tables(mode)
        if not edits or not table or not titles:
            return
        columns = [(c, t) for c, t in enumerate(titles) if self.is_cell_editable(mode, c)]
        if not columns:
            return
        for row in table:
            key = self.row_edit_key(row)
            if key is None:
                continue
            for c, title in columns:
                value = edits.get((key, title))
                if value is not None and c < len(row) - 1:
                    row[c] = value

    # ------------------------------------------------------------ Grouping tab
    def group_config(self):
        """Grouping tab settings (grouping.config), defaults for missing keys"""
        def get(key, default):
            one = (self.settings or {}).get(key)
            if not isinstance(one, dict) or one.get('value') is None:
                return default
            return one['value']
        return grouping.config(get)

    def group_items(self):
        """
        Group the files (Grouping tab): group tokens, missing representation
        errors and warnings on every file. Runs on every refresh.
        :return: list of groups (grouping.assign)
        """
        cfg = self.group_config()
        try:
            self.groups = grouping.assign(self.merged_list or [], cfg)
        except Exception as e:      # grouping must never stop the tables
            self.log.error(f"Grouping failed: {e!r}")
            self.groups = []
        if self.groups:
            missing = [g for g in self.groups if g['missing']]
            msg = f"Grouping: {len(self.groups)} group(s)"
            if missing:
                msg += f", {len(missing)} with missing representations"
            self.log.debug(msg)
        return self.groups

    def group_rows(self, table, titles, groups, mode):
        """
        Grouping tab on a built table (mode 'sub' or 'log'): Inherit Columns
        (Submission only), keep the rows of a group together, Collapse.
        """
        cfg = self.group_config()
        if not cfg['group_on'] or not groups or not table:
            return table
        try:
            if mode == 'sub':
                filled = grouping.inherit(table, titles, groups)
                if filled:
                    self.log.debug(f"Grouping: {filled} Submission cell(s) inherited")
            if cfg['group_together']:
                table = grouping.keep_together(table)
            if cfg['group_collapse_' + mode]:
                table = grouping.collapse(table, cfg['group_collapse_sep'])
        except Exception as e:
            self.log.error(f"Grouping of the {mode} table failed: {e!r}")
        return table

    def submission_rows_for_export(self):
        """
        Submission rows to export: without the groups that miss a required
        representation when "Do not export items in group with missing
        Representations" is on
        """
        table = self.table_sub
        cfg = self.group_config()
        if cfg['group_on'] and cfg['group_no_export_missing']:
            kept = grouping.exportable(table)
            if len(kept) != len(table or []):
                self.log.warning(
                    f"Grouping: {len(table) - len(kept)} Submission row(s) of groups with missing "
                    "representations are not exported")
            table = kept
        return table

    def prepare_export_file_names(self):

        self.export_file_names = {}
        if self.settings and self.static_keywords:
            one_above = str(self.static_keywords.get('package_name_root', '')).replace('\\', '/') + '/'
            export_root = one_above + str(self.static_keywords.get('package_name_from_folder', '')) + '/'

            s_pth_above = bool(self._get('export_sub_above', False))
            s_pth_custom = bool(self._get('export_sub_custom', False))
            s_custom = self._get_str('export_sub_custom_path')
            s_suffix = self._get_str('export_sub_custom_suffix')
            s_do_excel = bool(self._get('export_sub_excel', False))
            s_do_csv = bool(self._get('export_sub_csv', False))
            s_export_root = export_root
            if s_pth_custom:
                s_export_root = s_custom.replace('\\', '/') + '/'
            elif s_pth_above:
                s_export_root = one_above

            s_nme = self._get_str('export_sub_name')
            s_do_split = bool(self._get('export_sub_split_on', False))
            s_split = self._get_str('export_sub_split')
            s_do_skip = bool(self._get('export_sub_skip_on', False))
            s_skip = self._get_str('export_sub_skip')
            s_num = self._get_int('export_sub_splitnum', 3)
            if s_nme != "":
                s_export_root += s_nme + s_suffix
            else:
                s_export_root += self.static_keywords['package_name'] + s_suffix

            # Drive Log
            d_pth_above = bool(self._get('export_log_above', False))
            d_pth_custom = bool(self._get('export_log_custom', False))
            d_custom = self._get_str('export_log_custom_path')
            d_suffix = self._get_str('export_log_custom_suffix')
            d_do_excel = bool(self._get('export_log_excel', False))
            d_do_csv = bool(self._get('export_log_csv', False))
            d_export_root = export_root
            if d_pth_custom:
                d_export_root = d_custom.replace('\\', '/') + '/'
            elif d_pth_above:
                d_export_root = one_above

            d_nme = self._get_str('export_log_name')
            d_do_split = bool(self._get('export_log_split_on', False))
            d_split = self._get_str('export_log_split')
            d_do_skip = bool(self._get('export_log_skip_on', False))
            d_skip = self._get_str('export_log_skip')
            d_num = self._get_int('export_log_splitnum', 3)
            # if exporting both sub and log, and using just package name (name is empty),
            # add suffix to avoid overwriting
            if d_suffix == "" and d_nme == "" and (s_do_excel or s_do_csv):
                d_suffix = '_log'
            if d_nme != "":
                d_export_root += d_nme + d_suffix
            else:
                d_export_root += self.static_keywords['package_name'] + d_suffix

            # Text
            t_pth_above = bool(self._get('text_above', False))
            t_pth_custom = bool(self._get('text_custom', False))
            t_custom = self._get_str('text_custom_path')
            t_do_txt = bool(self._get('text_txt', False))
            t_export_root = export_root
            if t_pth_custom:
                t_export_root = t_custom.replace('\\', '/') + '/'
            elif t_pth_above:
                t_export_root = one_above
            t_export_name = t_export_root + self.static_keywords['package_name'] + '.txt'

            exported_files = {
                'sub': {
                    'export_root': s_export_root,
                    'do_excel': s_do_excel,
                    'do_csv': s_do_csv,
                    'nme': s_nme,
                    'do_split': s_do_split,
                    'split': s_split,
                    'do_skip': s_do_skip,
                    'skip': s_skip,
                    'num': s_num
                },
                'log': {
                    'export_root': d_export_root,
                    'do_excel': d_do_excel,
                    'do_csv': d_do_csv,
                    'nme': d_nme,
                    'do_split': d_do_split,
                    'split': d_split,
                    'do_skip': d_do_skip,
                    'skip': d_skip,
                    'num': d_num
                },
                't_do_txt': t_do_txt,
                't_export_name': t_export_name
            }
            if s_do_csv:
                exported_files['submission_csv'] = s_export_root + '.csv'
            if s_do_excel:
                exported_files['submission_excel'] = s_export_root + '.xlsx'
            if d_do_csv:
                exported_files['drivelog_csv'] = d_export_root + '.csv'
            if d_do_excel:
                exported_files['drivelog_excel'] = d_export_root + '.xlsx'
            if t_do_txt:
                exported_files['text'] = t_export_name

            self.export_file_names = exported_files

    def publish_ayon(self, mode="local"):
        if self.settings and self.static_keywords:
            self.prepare_export_file_names()
        else:
            self.log.error("Ayon publish: no data, load a package first.")
            return

        # Ayon Publish
        csv_pth = self.export_file_names.get('submission_csv')
        ayon_project = self.settings['ayon_project']['value'] or ""
        ayon_folder = self.settings['dead_ayon_folder']['value'] or ""
        ayon_task = self.settings['dead_ayon_task']['value'] or ""
        if ayon_project == "" or ayon_folder == "" or ayon_task == "":
            self.log.error("Ayon publish: Ayon project, folder and task must be set (Ayon / Deadline tab).")
            return

        if csv_pth is None:
            self.log.error("Ayon publish: submission csv file name is not set, check the Exports tab.")
            return
        if not (self.export_file_names.get('sub') or {}).get('do_csv'):
            self.log.error("Ayon publish: turn on Exports > Submission > CSV, "
                           "the Ayon ingest reads the submission csv.")
            return

        # export the sub csv spreadsheet(s) now
        # the exports is a dict where keys are file names (excluding extension), and values are list
        exports = self.export_spreadsheet('sub', self.submission_rows_for_export(), self.column_titles_sub, None, dry_run=False)
        if not exports:
            self.log.error("Ayon publish: submission spreadsheet is empty, nothing to publish.")
            return
        csv_file_paths =  [s + '.csv' for s in list(exports.keys())]
        self.log.info(f"Publishing {len(csv_file_paths)} csv file(s) to Ayon ({mode})")

        credentials.ensure_ayon(self.paths)
        credentials.ensure_ftrack(self.paths, ask=False)
        a = AyonPublish(self.settings, self.paths)
        if a.are_paths_ok(mode=mode):
            for one_csv_file_path in csv_file_paths:
                a.build_ayon_csv_command(one_csv_file_path, ayon_project, ayon_folder, ayon_task)
                if mode == "local":
                    ret = a.publish_local()
                    self.log.info(f"Publish result for {one_csv_file_path}: return code {ret}")
                elif mode == "farm":
                    ret = a.publish_deadline()
                    self.log.info(f"Deadline submission for {one_csv_file_path}: return code {ret}")
        else:
            self.log.error(f"Ayon publish ({mode}) cancelled, required tools are missing (see errors above).")

    def export_all(self, column_width_sub=None, column_width_log=None):

        # Replace tab: Replace with Go. Runs first, before the package folder
        # can be renamed at the end of Go.
        if self._setting_on('replace_withgo'):
            self.replace_execute()

        if self.settings and bool(self.settings['side_copywithgo']['value']):
            self.sidecar_files_copy()

        if self.settings and bool(self.settings['thumbs_make_on_go']['value']):
            self.prepare_converts()
            self.run_converts()

        if self.settings and self.static_keywords:
            self.prepare_export_file_names()

            # submission
            self.export_spreadsheet('sub', self.submission_rows_for_export(), self.column_titles_sub, column_width_sub)
            # drive log
            self.export_spreadsheet('log', self.table_log, self.column_titles_log, column_width_log)

            # text
            if self.table_txt is not None and self.export_file_names['t_do_txt']:
                try:
                    with open(self.export_file_names['t_export_name'], 'w', encoding='utf-8') as f:
                        f.write(self.table_txt)
                    self.log.info(f"Text exported: {self.export_file_names['t_export_name']}")
                except (OSError, UnicodeError) as e:
                    self.log.error(f"Error exporting text file {self.export_file_names['t_export_name']}: {e}")

        # Ayon tab: Export with Go
        if self._setting_on('ayon_export_go'):
            self.ayon_export()

        # Ayon tab: Record Package with Go
        if self._setting_on('ayon_record_go'):
            self.ayon_record_packages()

        # Ayon Publish tab: Send Submission CSV to Ayon on Go (local publish),
        # before the package folder is renamed
        if self._setting_on('dead_go_ayon'):
            self.publish_ayon(mode="local")

        # rename if autorename is ON
        if self.settings and\
                bool(self.settings['name_rename_auto']['value']) and\
                bool(self.settings['name_from_template']['value']):
            self.rename_folder()

    def manual_rename(self):
        if self.settings and\
                bool(self.settings['name_from_template']['value']):
            self.rename_folder()

    def rename_folder(self):

        if self.static_keywords is None:
            return None
        try:
            pth = self.static_keywords['package_name_root'] + '/'
            src = self.static_keywords['package_name_from_folder']
            dst = self.static_keywords['package_name']
            if src == dst:
                self.log.debug(f"Package folder already named {dst}")
                return None
            os.rename(pth + src, pth + dst)
            self.log.info(f"Package folder renamed: {src} -> {dst}")
        except Exception as e:
            self.log.error(f"Renaming package folder failed: {e}")

    def export_spreadsheet(self, mode, table, titles, column_widths=None, dry_run=False):
        """
        Expects self.export_file_names dictionary with following keys:
        """

        def write_csv(file_name, table, titles):
            self.log.info(f"Writing {mode} csv: {file_name}.csv ({len(table)} rows)")
            try:
                with open(file_name + '.csv', 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(titles)
                    for row, line in enumerate(table):
                        writer.writerow(line[:len(titles)])
            except (OSError, csv.Error) as e:
                # e.g. the file is open in Excel: the other exports still run
                self.log.error(f"Writing {file_name}.csv failed: {e}")

        def write_excel(file_name, table, titles):
            _excel = 0.15
            # Excel
            if do_excel:
                self.log.info(f"Writing {mode} excel: {file_name}.xlsx ({len(table)} rows)")
                try:
                    # values are text: '=...' must not become a formula
                    workbook = xlsxwriter.Workbook(file_name + '.xlsx', {'strings_to_formulas': False})
                    worksheet = workbook.add_worksheet()
                    for column_number, one_column in enumerate(titles):
                        if column_widths and column_number < len(column_widths):
                            worksheet.set_column(
                                column_number,
                                column_number,
                                column_widths[column_number] * _excel
                            )
                        else:
                            worksheet.set_column(column_number, column_number)
                        worksheet.write(0, column_number, one_column)
                    # Grouping tab: row colors (errors and warnings win over group colors)
                    formats = {}
                    for row, line in enumerate(table):
                        fmt = None
                        if color_rows and line and isinstance(line[-1], dict):
                            color = grouping.excel_color(line[-1])
                            if color:
                                if color not in formats:
                                    formats[color] = workbook.add_format({'bg_color': color})
                                fmt = formats[color]
                        for column_number, one_column in enumerate(titles):
                            value = line[column_number] if column_number < len(line) else ''
                            if isinstance(value, dict):
                                value = ''
                            worksheet.write(row + 1, column_number, value, fmt)
                    workbook.close()
                except Exception as e:      # xlsxwriter raises its own errors, e.g. file open in Excel
                    self.log.error(f"Writing {file_name}.xlsx failed: {e}")

        spec = self.export_file_names.get(mode) or {}
        if not (spec.get('do_excel') or spec.get('do_csv')):
            # neither Excel nor CSV is on for this spreadsheet
            self.log.debug(f"Export {mode}: Excel and CSV are off, nothing to write")
            return
        if titles is None or len(titles) == 0:
            self.log.error("Spreadsheet column names empty. Nothing exported.")
            return
        if table is None or len(table) == 0:
            self.log.error("Spreadsheet for export is empty. Nothing exported.")
            return

        # mode is sub or log
        if self.export_file_names.get(mode) is None:
            pass

        # remove skips from table
        skip_column = self.export_file_names.get(mode)['skip']
        if self.export_file_names.get(mode)['do_skip'] and self.export_file_names.get(mode)['skip'] in titles:
            skip_index = titles.index(skip_column)
            skipped_table = []
            for row in table:
                if row[skip_index] is None or row[skip_index] == "":
                    skipped_table.append(row)
                else:
                    # there is some text in the column of this row - this row will be skipped
                    pass
            if len(skipped_table) == 0:
                self.log.warning(f"All {len(table)} rows were skipped, nothing to write to {mode} file!")
                return
            table = skipped_table

        # split to more than one table if needed
        split_column = self.export_file_names.get(mode)['split']
        if self.export_file_names.get(mode)['do_split'] and self.export_file_names.get(mode)['split'] in titles:
            split_tables = {}
            split_index = titles.index(split_column)
            for row in table:
                v = row[split_index]
                if v in split_tables.keys():
                    split_tables[v].append(row)
                else:
                    split_tables[v] = [row]
            subtable_count = len(split_tables.keys())
            self.log.info(f"{mode} Export will be split to {subtable_count} tables.")
        else:
            # split to just one
            split_tables = {'all': table}

        _gcfg = self.group_config()
        color_rows = _gcfg['group_on'] and _gcfg['group_colors_excel']
        do_excel = self.export_file_names.get(mode)['do_excel']
        do_csv = self.export_file_names.get(mode)['do_csv']

        # make split tables keys the file names, except extension
        file_tables = {}
        cnt = 1
        export_root = self.export_file_names.get(mode)['export_root']
        for tab_key, tab in split_tables.items():
            if len(split_tables.keys()) == 1 or not self.export_file_names.get(mode)['do_split']:
                # do not add a split number at the end of file name
                file_name = export_root
            else:
                file_name = export_root + str(cnt).zfill(self.export_file_names.get(mode)['num'])
            file_tables[file_name] = tab
            cnt += 1
            if do_excel and not dry_run:
                write_excel(file_name, tab, titles)
            if do_csv and not dry_run:
                write_csv(file_name, tab, titles)

        return file_tables

    def sidecar_files_copy(self):

        self.output['status'] = "Copying sidecar files."

        if self.table_side is not None and len(self.table_side) > 0:
            copied = 0
            for one_item in self.table_side:
                _src = one_item[2]
                _dst = one_item[1]
                if not (_src and _dst):
                    continue
                if os.path.normcase(os.path.abspath(_src)) == os.path.normcase(os.path.abspath(_dst)):
                    self.log.warning(f"Sidecar copy skipped, source and destination are the same: {_src}")
                    continue
                try:
                    _dir = os.path.dirname(_dst)
                    if _dir:
                        os.makedirs(_dir, exist_ok=True)
                    if os.path.exists(_dst):
                        self.log.warning(f"Sidecar copy overwrites {_dst}")
                    self.log.info(f"Sidecar copy {_src} -> {_dst}")
                    shutil.copy(_src, _dst)
                    copied += 1
                except OSError as e:
                    self.log.error(f"Sidecar copy {_src} -> {_dst} failed: {e}")
            self.log.info(f"Sidecar files copied: {copied} of {len(self.table_side)}")

    def sidecar_files_find(self):

        class Default(dict):
            def __missing__(self, key):
                return '{' + key + '}'

        self.output['status'] = "Finding sidecar files."
        if not self.settings:
            return

        # get all files that can be sidecar files
        sidecars = []
        side_exclude_list = []
        file_list = []
        if self.settings['side_exclude']['value']:
            side_exclude_list = self.settings['side_exclude']['value'].split()
        side_include_list = []
        if self.settings['side_include']['value']:
            side_include_list = self.settings['side_include']['value'].split()
        if self.settings['side_folder']['value'] is not None:
            side_folder = self.settings['side_folder']['value']
            if side_folder != '':
                side_folder = side_folder.replace('\\', '/')
                if side_folder[-1] != '/':
                    side_folder += '/'
                file_list = self.walk_dirs(side_folder)

            # filter out exclude and include
            for one in file_list:
                one_sidecar = one.replace('\\', '/')
                include_keep = False
                if side_include_list:
                    for one_included in side_include_list:
                        if one_included in one_sidecar:
                            include_keep = True
                            break
                else:
                    include_keep = True
                exclude_keep = True
                if side_exclude_list:
                    for one_excluded in side_exclude_list:
                        if one_excluded in one_sidecar:
                            exclude_keep = False
                            break
                if include_keep and exclude_keep:
                    sidecars.append(one_sidecar)
        self.sidecars = sidecars

    def sidecar_files_filter(self):

        class Default(dict):
            def __missing__(self, key):
                return '{' + key + '}'

        self.output['status'] = "Filtering sidecar files."
        if not self.settings:
            return

        # clear the sidecar matches of the last refresh, also when there are
        # no sidecar files any more
        for item in self.merged_list or []:
            if 'sidecars' in item:
                item['sidecars'] = []

        if not self.sidecars:
            return

        # Get regexes from UI
        side_regexes = {}
        indexes = [str(x) for x in range(1, 7)]
        for one in indexes:
            if 'side_pattern_' + one not in self.settings:
                continue
            name_pat = 'side_pattern_' + one
            pat = self.settings[name_pat]['value']
            name_rep = 'side_repl_' + one
            rep = self.settings[name_rep]['value']
            name_match = "side_match_" + one
            match = self.settings[name_match]['value']
            name_dest = 'side_dest_' + one
            dest = self.settings[name_dest]['value']
            name_filter = 'side_filter_' + one
            my_filter = self.settings[name_filter]['value']
            pat_valid = True
            try:
                pat_compiled = re.compile(pat)
            except re.error:
                pat_compiled = None
                pat_valid = False
            # only add regex if it is valid and not empty
            if match and pat and dest and pat_valid:
                one_regex = {one: {
                    'pattern': pat,
                    'valid': pat_valid,
                    'compiled': pat_compiled,
                    'repl': rep,
                    'match': match,
                    'destination': dest,
                    'filter': my_filter
                }}
                side_regexes.update(one_regex)

        if side_regexes is None:
            return

        if self.merged_list is None:
            return

        if len(self.merged_list) == 0:
            return

        for one_item in self.sidecars:
            one_path, _, one_file = one_item.rpartition('/')
            if not one_file:
                continue
            one_file_noext, dot, one_file_ext = one_file.rpartition('.')
            if not dot:
                # no extension
                one_file_noext, one_file_ext = one_file, ''

            for k, one_regex in side_regexes.items():
                # Filter: only sidecar files with this text in the file name
                if one_regex['filter'] and one_regex['filter'] not in one_file:
                    continue
                result = None
                if one_regex['repl'] and one_regex['repl'] != '':
                    # it is a replace
                    try:
                        if one_regex['repl'].startswith("lambda "):
                            # LAMBDA!
                            result = re.sub(one_regex['compiled'],
                                            eval(str(one_regex['repl'])),
                                            one_file)
                        else:
                            result = re.sub(one_regex['compiled'],
                                            one_regex['repl'], one_file)
                    except Exception as e:
                        self.log.warning(f"Sidecar row {k}: Repl {one_regex['repl']!r} "
                                         f"failed on {one_file}: {e}")
                        result = None
                else:
                    m = one_regex['compiled'].search(one_file)
                    if m:
                        # if user made a group, assign the group,
                        # otherwise use whole found string
                        result = m.group(1) if one_regex['compiled'].groups else m.group(0)
                    else:
                        # shot name exists but doesn't match the regex,
                        # so set shot name to empty string
                        result = None

                sidecar_keywords = {
                    'sidecar_path': one_path,
                    'sidecar_file': one_file,
                    'sidecar_file_noext': one_file_noext,
                    'sidecar_ext': one_file_ext,
                    'sidecar_result': str(result)}
                if result:
                    # now we have the match or repl, see if it matches
                    # to some package item
                    for item in self.merged_list:
                        expanded = format_keep(one_regex['match'], item)
                        expanded = format_keep(expanded, self.static_keywords)
                        if expanded != result:
                            continue
                        # sidecar file matches the package file
                        dest = str(one_regex['destination'])
                        dest = format_keep(dest, sidecar_keywords)
                        dest = format_keep(dest, self.static_keywords)
                        dest = format_keep(dest, item)
                        dest = dest.replace('\\', '/')
                        one_side = {
                            'result': result,
                            'file': one_item,
                            'dest': dest
                        }
                        item.setdefault('sidecars', []).append(one_side)

    def rename_prepare(self):
        """

        """

        self.renames = []
        if self.settings:
            _root = str(self.settings['package_folder']['value'])
            # read checks from gui, save to self.checks
            indexes = [str(x).zfill(2) for x in range(1, 9)]
            for one in indexes:
                _filter = self._get_str("rename_filter_" + one)
                src = self._get_int("rename_source_" + one, 0)
                pat = self._get_str("rename_pattern_" + one)
                repl = self._get_str("rename_repl_" + one)
                if pat != '' and repl != '':
                    one_ren = {
                        "filter": _filter,
                        "src": src,
                        "pattern": pat,
                        "repl": repl,
                    }
                    self.renames.append(one_ren)

    def rename_preprocess(self):

        class Default(dict):
            def __missing__(self, key):
                return '{' + key + '}'

        if self.renames is None:
            return
        if self.merged_list is None:
            return

        for item in self.merged_list:

            # what to rename
            if item['category'] == 'sequence':
                _src = item['path_prs'] + '/' + item['clean_name']
            else:
                _src = item['path_prs'] + '/' + item['name']
            _target = _src
            item['rename'] = ''
            item.pop('rename_source', None)

            for one_rename in self.renames:
                # tokens only: regex counts like \d{3} stay as they are
                _f = expand_tokens(one_rename['filter'], self.static_keywords, item)
                _p = expand_tokens(one_rename['pattern'], self.static_keywords, item)
                if not _p or unresolved_tokens(_p):
                    continue
                try:
                    _p_comp = re.compile(_p)
                except re.error:
                    continue

                _r = expand_tokens(one_rename['repl'], self.static_keywords, item)
                if not _r or unresolved_tokens(_r):
                    continue

                # filter out first
                _if_eval = False
                if _f != '':
                    try:
                        _if_eval = bool(eval(_f))
                    except Exception:
                        pass
                else:
                    # no filtering, so true for all
                    _if_eval = True
                if not _if_eval:
                    continue

                # find what to rename
                one_src = _target
                one_before = ''
                one_after = ''
                if one_rename['src'] > 0:
                    # want to rename just one folder or filename
                    _s = _target.split('/')
                    if len(_s) < one_rename['src']:
                        continue
                    one_before = '/'.join(_s[: -1 * (one_rename['src'])])
                    one_src = _s[-1 * (one_rename['src'])] or ''
                    one_after = ''
                    if one_rename['src']-1 > 0:
                        one_after = '/'.join(_s[-1 * (one_rename['src']-1):])
                    if one_after != '':
                        one_after = '/' + one_after
                    if one_before != '':
                        one_before = one_before + '/'

                # do regex replace
                result = None
                if _r.startswith("lambda "):
                    # LAMBDA!
                    try:
                        _eval = eval(str(_r))
                    except Exception:
                        _eval = _r
                    try:
                        result = re.sub(_p_comp, _eval, one_src)
                    except Exception:
                        result = None
                else:
                    try:
                        result = re.sub(_p_comp, _r, one_src)
                    except Exception:
                        result = None
                if not result:
                    continue

                # put back together
                _target = one_before + result + one_after
            if _target != _src:
                item['rename'] = _target
                item['rename_source'] = _src

    def rename_execute(self):
        """
        Will rename the merged items that have rename and rename_source
        If item category is a sequence, it will assemble the full filename
        with sequence counter and extension

        the rename has the clean filename with optional sequence separator, but
        no sequence number, and no extension

        Therefore, extension can't be renamed
        :return:
        """

        def one_rename(pairs):

            if pairs is None:
                return
            if len(pairs) == 0:
                return

            _dst_dir = os.path.dirname(pairs[0][1])
            try:
                if _dst_dir:
                    os.makedirs(_dst_dir, exist_ok=True)
            except OSError as e:
                self.log.error(f"Rename: can't create folder {_dst_dir}: {e}")
                return

            done = 0
            for one_file in pairs:
                try:
                    if not os.path.exists(one_file[0]):
                        # skip rename if source doesn't exist
                        self.log.debug(f"Rename skipped, source missing: {one_file[0]}")
                        continue
                    if os.path.exists(one_file[1]):
                        # skip rename if destination exist
                        self.log.warning(f"Rename skipped, destination exists: {one_file[1]}")
                        continue
                    os.replace(one_file[0], one_file[1])
                    done += 1
                    self.log.debug(f"Renamed {one_file[0]} -> {one_file[1]}")
                except OSError as e:
                    self.log.error(f"Failed to rename {one_file[0]} -> {one_file[1]}: {e}")
            if done:
                self.log.info(f"Renamed {done} file(s): {pairs[0][0]} -> {pairs[0][1]}"
                              + (" ..." if len(pairs) > 1 else ""))

        for item in self.merged_list or []:
            _r = item.get('rename')
            _s = item.get('rename_source')
            _c = item.get('category')
            _ext = item.get('extension')
            if (not _r) or (not _s) or (_c is None) or (_ext is None):
                continue

            # what to rename
            if _c != 'sequence':
                one_rename([[_s + '.' + _ext, _r + '.' + _ext]])
            else:
                _seq = []
                _pad = item.get('padding')
                _sub = item.get('sub_ranges')
                if (not _pad) or (not _sub):
                    continue
                for one in _sub:
                    for cnt in range(one['start'], one['end'] + 1):
                        counter = str(cnt).zfill(_pad) + '.' + _ext
                        _seq.append([
                            _s + counter,
                            _r + counter,
                        ])
                one_rename(_seq)

    def ayon_collect_gui(self):

        def split_itms(itm):
            """
            Gui task types and assignees are separated by commas
            """
            out = []
            if itm is None:
                return out
            if len(itm) == 0:
                return out
            _s = itm.split(',')
            for one in _s:
                one = one.strip()
                if one == '':
                    continue
                out.append(one.lower())
            return out

        self.ayon_gui = {
            'do_shotlist': bool(self.settings['ayon_do_shotlist']['value']) or False,
            'do_csv': bool(
                self.settings['ayon_export_csv']['value']) or False,
            'do_excel': bool(
                self.settings['ayon_export_excel']['value']) or False,
            'do_thumbs': bool(
                self.settings['ayon_thumbnails']['value']) or False,
            'project': self.settings['ayon_project']['value'] or "",
            'prefix': self.settings['ayon_prefix']['value'] or "",
            'out_folder': self.settings['ayon_output_folder']['value'] or "",
            'filter_assets': bool(
                self.settings['ayon_filter_assets']['value']) or False,
            'filter_shots': bool(
                self.settings['ayon_filter_shots']['value']) or False,
            'filter_tasks': bool(
                self.settings['ayon_filter_tasks']['value']) or False,
            'filter_other': bool(
                self.settings['ayon_filter_other']['value']) or False,
            'filter_matched': bool(
                self.settings['ayon_filter_matched']['value']) or False,
            'filter_tasktype': bool(
                self.settings['ayon_filter_tasktype_chbx']['value']) or False,
            'filter_tasktypes': split_itms(self.settings['ayon_filter_tasktypes'][
                                    'value'] or ""),
            'filter_taskname': bool((self.settings.get('ayon_filter_taskname_chbx') or {}).get('value')),
            'filter_tasknames': split_itms((self.settings.get('ayon_filter_tasknames') or {}).get('value') or ""),
            'filter_assignee': bool(
                self.settings['ayon_filter_assignee_chbx']['value']) or False,
            'filter_assignees': split_itms(self.settings['ayon_filter_assignees'][
                                    'value'] or ""),
            # added later, missing in older presets
            'do_versions': bool((self.settings.get('ayon_versions_chbx') or {}).get('value')),
            'do_versions_csv': bool((self.settings.get('ayon_export_versions_csv') or {}).get('value')),
            'version_match': bool((self.settings.get('ayon_version_match_chbx') or {}).get('value')),
            'version_match_pkg': (self.settings.get('ayon_version_match_pkg') or {}).get('value') or '',
            'version_match_data': (self.settings.get('ayon_version_match_data') or {}).get('value') or '',
            'product_filters': parse_product_filters(
                (self.settings.get('ayon_product_filters') or {}).get('value') or ""),
        }
        # turn off multi filter if no filter provided
        if self.ayon_gui['filter_tasktypes'] is None or len(self.ayon_gui['filter_tasktypes']) == 0:
            self.ayon_gui['filter_tasktype'] = False
        if self.ayon_gui['filter_assignees'] is None or len(self.ayon_gui['filter_assignees']) == 0:
            self.ayon_gui['filter_assignee'] = False
        if not self.ayon_gui['filter_tasknames']:
            self.ayon_gui['filter_taskname'] = False


    def ayon_data_read(self, force=False):
        """
        Read the shot list (and versions, if enabled) from Ayon
        :param force: read even when the Ayon "Enable" checkbox is off (Scan button)
        """
        self.ayon_collect_gui()

        if self.ayon_gui['project'] == "":
            if force:
                self.log.warning("Ayon scan: set the Ayon project first")
            self.ayon_data = []
            return self.ayon_data
        if not self.ayon_gui['do_shotlist'] and not force:
            self.ayon_data = []
            return self.ayon_data

        # a working Ayon login: renewed when expired, the gui asks to sign in
        credentials.ensure_ayon(self.paths)
        self.my_ayon = AyonShotlist(
            self.ayon_gui,
            self.ui,
            self.paths
        )
        self.ayon_data = self.my_ayon.get_shotlist() or []
        if self.my_ayon.error:
            self.log.error(f"Ayon: {self.my_ayon.error}")
        else:
            self.log.info(f"Ayon: {len(self.ayon_data)} row(s) read from project {self.ayon_gui['project']}")
            # gui: AYON Lists auto-read uses this connection
            hook = getattr(Sequencer, 'on_ayon_connected', None)
            if hook is not None and self.ui is not None:
                try:
                    hook(getattr(self.my_ayon, 'ayon', None), self.ayon_gui['project'])
                except Exception as e:
                    self.log.warning(f"AYON Lists auto-read failed: {e}")
        return self.ayon_data

    def ayon_scan(self):
        """
        Scan button: read the Ayon list now, match it to the files (if any)
        and show it
        """
        self.ayon_data_read(force=True)
        if self.my_ayon is None or self.my_ayon.error:
            return
        self.ayon_data_filter()
        if self.merged_list:
            self.ayon_data_assign()
            self.ayon_versions_update()
            self.ayon_versions_assign()
            self.display_ayon_table()
            self.display_ayon_versions_table()

    def ayon_versions_update(self):
        """
        Matched Versions: with Pull versions on and files matched to Ayon
        folders, read every version of the products of those folders
        (cached in AyonShotlist, Ayon is asked only when the matches change)
        """
        rows = []
        if self.my_ayon is not None and not self.my_ayon.error and self.ayon_gui \
                and self.ayon_gui.get('do_versions') and self.merged_list:
            matched = {r.get('_folder_id') for r in self.ayon_data or [] if r.get('_matched')}
            if matched:
                rows = self.my_ayon.get_matched_versions(matched)
        self.ayon_matched_versions = rows

    # Matched Versions columns that show the preferred (green) / file
    # matched (teal) mark; the others keep the folder shade
    AYON_MARKED_COLUMNS = ('Folder Name', 'Folder Type', 'Product', 'Product Type',
                           'Version', 'Version Name')

    # prefix + this + column, e.g. {ayon_Matched Version}
    MATCHED_VERSION_KEY = "Matched "

    @staticmethod
    def _version_number(value):
        """version as int, "v007" -> 7, not a number -> 0"""
        digits = re.sub(r'\D', '', str(value or ''))
        return int(digits) if digits else 0

    @staticmethod
    def _same_value(a, b):
        """equal text, or equal numbers ("007" == "7", "v007" == "v7" is not)"""
        a, b = str(a).strip(), str(b).strip()
        if a == b:
            return True
        return a.isdigit() and b.isdigit() and int(a) == int(b)

    def ayon_versions_assign(self):
        """
        Match version: for every file matched to an Ayon folder, find the row
        of Matched Versions (same folder) where the package key equals the
        list key, e.g. {version} == {Version}. Its columns are added to the
        file as {<prefix>Matched <column>}, e.g. {ayon_Matched Version Status}.
        """
        class Default(dict):
            def __missing__(self, key):
                return '{' + key + '}'

        def expand(template, values):
            try:
                return format_keep(template, values)
            except (ValueError, IndexError, AttributeError):
                return template

        prefix = (self.ayon_gui or {}).get('prefix', '')
        key_start = prefix + self.MATCHED_VERSION_KEY
        for item in self.merged_list or []:
            for k in [k for k in item if str(k).startswith(key_start)]:
                del item[k]
            for k in ('_ayon_version_id', '_ayon_repre_id', '_ayon_repre_name'):
                item.pop(k, None)
        for row in self.ayon_matched_versions or []:
            row["Matched Files"] = ''
            row["Version Exists"] = "False"

        gui = self.ayon_gui or {}
        if not gui.get('version_match') or not self.ayon_matched_versions or not self.merged_list:
            return
        pkg_tpl, data_tpl = gui.get('version_match_pkg', ''), gui.get('version_match_data', '')
        if not pkg_tpl or not data_tpl:
            self.log.warning("Match version is on, but its package or list key is empty")
            return

        rows_by_folder = {}
        for row in self.ayon_matched_versions:
            rows_by_folder.setdefault(row.get('_folder_id'), []).append(row)

        files_matched = 0
        files_in_folders = 0
        example = None
        repres_paired = 0
        repre_example = None
        for item in self.merged_list:
            folder_ids = item.get('_ayon_folder_ids') or set()
            candidates = [r for f in folder_ids for r in rows_by_folder.get(f, [])]
            if not candidates:
                continue
            files_in_folders += 1
            pkg = expand(pkg_tpl, item)
            hits = [r for r in candidates if self._same_value(pkg, expand(data_tpl, {**item, **r}))]
            if not hits:
                if example is None:
                    example = (item.get('name', ''), pkg,
                               sorted({expand(data_tpl, {**item, **r}) for r in candidates})[:6])
                # the file's version is not in Ayon yet: still tell the
                # checks so, and what the highest existing version is
                # (of the preferred product, or of all listed products)
                preferred = next((r for r in candidates if r.get('Preferred')), None)
                same_product = [r for r in candidates
                                if preferred is None or r.get('Product') == preferred.get('Product')]
                item[key_start + "Version Exists"] = "False"
                item[key_start + "Max Existing Version"] = str(
                    max((self._version_number(r.get('Version')) for r in same_product), default=0))
                continue
            for r in hits:
                r["Matched Files"] = str(self._version_number(r["Matched Files"]) + 1)
                r["Version Exists"] = "True"
            # several products can have the same version number: prefer the
            # preferred one, then the first by sort order
            hit = next((r for r in hits if r.get('Preferred')), hits[0])
            for k, v in hit.items():
                if not str(k).startswith('_') and k != "Matched Files":
                    item[key_start + k] = v
            files_matched += 1
            item['_ayon_version_id'] = hit.get('_version_id')
            # which representation of the version this file is
            repre, how = ayon_packages.pair_representation(
                item.get('extension', ''), item.get('size_bytes'), hit.get('_repres') or [],
                self._ayon_allowed_repres(hit.get('Product', '')))
            item[key_start + "Representation"] = repre['name'] if repre else ''
            item[key_start + "Representation By"] = how if repre else ''
            if repre:
                item['_ayon_repre_id'] = repre['id']
                item['_ayon_repre_name'] = repre['name']
                repres_paired += 1
            elif repre_example is None:
                repre_example = (item.get('name', ''), how)

        if files_in_folders and files_matched < files_in_folders:
            msg = (f"Match version: {files_matched} of {files_in_folders} file item(s) matched a version")
            if example:
                msg += (f"; e.g. '{example[0]}': package {pkg_tpl!r} -> {example[1]!r}, "
                        f"list {data_tpl!r} gives {example[2]}")
            level = logging.WARNING
        else:
            msg = f"Match version: {files_matched} of {files_in_folders} file item(s) matched a version"
            level = logging.INFO
        if msg != getattr(self, '_last_version_match_msg', None):
            self._last_version_match_msg = msg
            self.log.log(level, msg)

        if files_matched:
            msg = f"Match representation: {repres_paired} of {files_matched} file item(s) paired"
            if repre_example:
                msg += f"; e.g. '{repre_example[0]}': {repre_example[1]}"
            if msg != getattr(self, '_last_repre_match_msg', None):
                self._last_repre_match_msg = msg
                self.log.log(logging.WARNING if repres_paired < files_matched else logging.INFO, msg)

    def _ayon_allowed_repres(self, product):
        """
        Representation names a file of this product may be paired with: the
        representations of the product filters that match the product. Empty
        list when any representation is allowed (a filter without one, such
        as :renderCompMain: or :renderCompMain).
        """
        from ayon_shotlist import _match
        patterns = []
        for flt in (self.ayon_gui or {}).get('product_filters') or []:
            if not _match(flt['product'], product):
                continue
            if not flt['repre']:
                return []
            patterns.append(flt['repre'])
        return patterns

    def ayon_record_packages(self, dry_run=False):
        """
        Record the package in Ayon: on every version with files in the package,
        the package name and the representations in it; on every paired
        representation, the package name. Uses the files of the Submission
        (not the ones left out by filters or the vendor csv) that Match version
        paired with a version.
        """
        if not self.merged_list:
            self.log.error("Record package: no package loaded.")
            return None
        if self.my_ayon is None or self.my_ayon.error:
            self.log.error("Record package: the Ayon list is not available, "
                           "enable Ayon and set the project, then Scan.")
            return None
        if not (self.ayon_gui or {}).get('version_match'):
            self.log.error("Record package: turn on Pull versions and Match version, "
                           "files are recorded with the version they matched.")
            return None
        package = str((self.output or {}).get('package_name') or
                      (self.static_keywords or {}).get('package_name') or '').strip()
        if not package or unresolved_tokens(package):
            self.log.error(f"Record package: no package name ({package!r}), check the Package tab.")
            return None

        in_package = [i for i in self.merged_list
                      if not i.get('vendor_ignore_sub', i.get('hide_sub'))]
        with_version = [i for i in in_package if i.get('_ayon_version_id')]
        without_repre = [i for i in with_version if not i.get('_ayon_repre_id')]
        if not with_version:
            self.log.error(f"Record package {package}: none of the {len(in_package)} submission "
                           f"file item(s) matched an Ayon version, nothing recorded.")
            return None
        if len(with_version) < len(in_package):
            self.log.warning(f"Record package {package}: {len(in_package) - len(with_version)} of "
                             f"{len(in_package)} submission file item(s) have no Ayon version, not recorded")
        for item in without_repre[:10]:
            self.log.warning(f"Record package {package}: '{item.get('name', '')}' has no representation "
                             f"(version recorded without it)")
        if len(without_repre) > 10:
            self.log.warning(f"Record package {package}: ... {len(without_repre) - 10} more without representation")

        records = ayon_packages.collect_package_records(with_version)
        result = self.my_ayon.record_packages(records, package, dry_run=dry_run)
        for error in result['errors']:
            self.log.error(f"Record package {package}: {error}")
        self.log.info(
            f"Record package {package}{' (dry run)' if dry_run else ''}: "
            f"{result['versions']} version(s) and {result['repres']} representation(s) updated, "
            f"{result['versions_same']} version(s) and {result['repres_same']} representation(s) "
            f"already had it")
        return result

    def _setting_on(self, key):
        settings = getattr(self, 'settings', None)
        return bool((settings.get(key) or {}).get('value')) if settings else False

    def _get(self, key, default=None):
        """
        value of a setting, default when the setting or its value is missing.
        Unchecked boxes and 0 are real values (tested with 'is None', not truth).
        """
        settings = getattr(self, 'settings', None) or {}
        item = settings.get(key)
        if not isinstance(item, dict) or item.get('value') is None:
            return default
        return item['value']

    def _get_int(self, key, default):
        try:
            return int(float(self._get(key, default)))
        except (TypeError, ValueError):
            return default

    def _get_str(self, key, default=''):
        value = self._get(key, default)
        return default if value is None else str(value)

    def ayon_visible_list(self):
        """
        Shot list rows as shown and exported: list filters, and Matched Only
        """
        matched_only = self._setting_on('ayon_filter_matched')
        return [r for r in self.ayon_data or []
                if not r.get('_hide') and (not matched_only or r.get('_matched'))]

    def ayon_visible_versions(self):
        """
        Matched Versions rows as shown and exported: only folders still shown
        in the shot list (list filters apply), and with "Show matched only"
        only the versions a file matched (teal)
        """
        visible_folders = {r.get('_folder_id') for r in self.ayon_visible_list()}
        rows = [r for r in self.ayon_matched_versions or [] if r.get('_folder_id') in visible_folders]
        if self._setting_on('ayon_versions_matched_only'):
            rows = [r for r in rows if r.get('Matched Files')]
        return rows

    def display_ayon_versions_table(self):
        if self.ui is None or QtWidgets is None:
            # command line mode: no tables
            return
        table_ui = getattr(self.ui, 'ayon_versions_table', None)
        if table_ui is None:
            return
        rows = self.ayon_visible_versions()
        from ayon_shotlist import MATCHED_VERSION_COLUMNS
        titles = list(MATCHED_VERSION_COLUMNS)
        table_ui.setSortingEnabled(False)
        table_ui.clear()
        table_ui.setColumnCount(len(titles))
        table_ui.setHorizontalHeaderLabels(titles)
        table_ui.setRowCount(len(rows))
        # rows of the same folder share a shade, alternating per folder
        band_colors = ('#4d4d4d', '#3a3a3a')
        band = 0
        last_folder = None
        for row, line in enumerate(rows):
            preferred = bool(line.get('Preferred'))
            file_matched = bool(line.get('Matched Files'))
            folder = line.get('Folder Path')
            if last_folder is not None and folder != last_folder:
                band = 1 - band
            last_folder = folder
            for col, title in enumerate(titles):
                value = str(line.get(title) or '')
                shown = ' '.join(value.split()) if '\n' in value else value
                itm = QtWidgets.QTableWidgetItem(shown)
                if title in self.AYON_CAPPED_COLUMNS or shown != value:
                    itm.setToolTip(value)
                # file matched (Match version): teal, preferred: green
                color = band_colors[band]
                if title in self.AYON_MARKED_COLUMNS:
                    color = '#1f6f78' if file_matched else ('darkgreen' if preferred else color)
                itm.setBackground(QtGui.QColor(color))
                table_ui.setItem(row, col, itm)
        self.fit_ayon_columns(table_ui, titles)
        self.single_line_rows(table_ui)
        table_ui.setSortingEnabled(True)
        # sub tab title shows the count
        tabs = getattr(self.ui, 'ayon_tables_tab', None)
        if tabs is not None:
            idx = tabs.indexOf(getattr(self.ui, 'ayon_versions_page', None))
            if idx >= 0:
                total = len(self.ayon_matched_versions or [])
                if not total:
                    text = "Matched Versions"
                elif len(rows) == total:
                    text = f"Matched Versions ({total})"
                else:
                    text = f"Matched Versions ({len(rows)} of {total})"
                tabs.setTabText(idx, text)

    def ayon_data_filter(self):
        if self.my_ayon is None or getattr(self.my_ayon, 'error', None):
            self.log.warning("Ayon shot list is not available (shotlist disabled, no project, or connection failed).")
            return
        self.ayon_collect_gui()
        self.my_ayon.ayon_gui = self.ayon_gui
        self.my_ayon.filter_shotlist()
        self.ayon_data = self.my_ayon.data
        self.display_ayon_table()
        # list filters also limit Matched Versions
        self.display_ayon_versions_table()

    def ayon_export(self):
        """
        Export Shot List button / headless action a: write what the tables
        show. Ayon is only read when nothing is loaded yet (then like Scan,
        including matching to the files); re-reading used to drop the
        matches, which emptied the tables and the csv with Matched Only on.
        """
        if self.my_ayon is None or self.my_ayon.error or not self.ayon_data:
            self.ayon_scan()
        else:
            self.ayon_data_filter()
        self.ayon_data_write()

    def ayon_data_write(self):
        if self.my_ayon is not None and not getattr(self.my_ayon, 'error', None):
            self.ayon_collect_gui()
            self.my_ayon.update_output(self.ayon_gui)
            # export what is shown
            self.my_ayon.write_csv(self.ayon_visible_list())
            if self.ayon_gui and self.ayon_gui.get('do_versions_csv'):
                self.my_ayon.write_versions_csv(self.ayon_visible_versions())

    def ayon_data_assign(self):
        class Default(dict):
            def __missing__(self, key):
                return '{' + key + '}'

        if self.ayon_data is None or len(self.ayon_data) == 0:
            return
        # matches from an earlier assign are stale (files or rules changed)
        for one_data_line in self.ayon_data:
            one_data_line.pop("_matched", None)
        for item in self.merged_list or []:
            item.pop("_ayon_folder_ids", None)
        if self.merged_list is None or len(self.merged_list) == 0:
            return
        if self.settings is None:
            return
        if self.ayon_gui is None:
            return

        # get filters from gui, exit if filters empty
        filters = []
        if bool(self.settings['ayon_package1_chbx']['value']):
            filters.append({
                'pkg' : self.settings['ayon_package1']['value'],
                'data': self.settings['ayon_list1']['value']
            })
        if bool(self.settings['ayon_package2_chbx']['value']):
            filters.append({
                'pkg': self.settings['ayon_package2']['value'],
                'data': self.settings['ayon_list2']['value']
            })
        if bool(self.settings['ayon_package3_chbx']['value']):
            filters.append({
                'pkg': self.settings['ayon_package3']['value'],
                'data': self.settings['ayon_list3']['value']
            })

        if filters is None or len(filters) == 0:
            return

        def expand(template, first, second):
            try:
                out = format_keep(template, first)
                return format_keep(out, second)
            except (ValueError, IndexError, AttributeError):
                return template

        def compare(item, one_data_line):
            """:return: list of (package value, list value, equal) per rule"""
            out = []
            for one_filter in filters:
                pkg = expand(one_filter['pkg'] or '', item, one_data_line)
                data = expand(one_filter['data'] or '', one_data_line, item)
                out.append((str(pkg), str(data), str(pkg) == str(data)))
            return out

        matched_items = 0
        best = None  # closest miss, for the log: (rules equal, item, row, compare result)
        for item in self.merged_list:
            item_matched = False
            for one_data_line in self.ayon_data:
                result = compare(item, one_data_line)
                equal = sum(1 for r in result if r[2])

                # skip item if not matching
                if equal != len(filters):
                    if best is None or equal > best[0]:
                        best = (equal, item, one_data_line, result)
                    continue

                # merge data lines (not the internal _ columns)
                prefixed_line = {}
                for k, v in one_data_line.items():
                    if str(k).startswith('_'):
                        continue
                    prefixed_line[f"{self.ayon_gui['prefix']}{k}"] = v
                item.update(prefixed_line)
                one_data_line["_matched"] = True
                item.setdefault("_ayon_folder_ids", set()).add(one_data_line.get("_folder_id"))
                item_matched = True
            if item_matched:
                matched_items += 1

        self._log_ayon_matching(matched_items, len(self.merged_list), filters, best)

    def _log_ayon_matching(self, matched, total, filters, best):
        """
        Summary of the Ayon matching. When nothing matched, show what the
        rules compared for the closest row, so a wrong rule is easy to spot.
        Logged only when the result changes (refreshes run on every edit).
        """
        if matched:
            msg = f"Ayon matching: {matched} of {total} file item(s) matched Ayon rows"
            level = logging.INFO
        else:
            lines = [f"Ayon matching: none of {total} file item(s) matched an Ayon row "
                     f"(all enabled rules must be equal)."]
            if best is not None:
                _, item, row, result = best
                name = item.get('name') or item.get('full_path') or ''
                where = row.get('Folder Path', '') + (f" / {row.get('Task Name')}" if row.get('Task Name') else '')
                lines.append(f"  closest: file '{name}' vs Ayon '{where}'")
                for n_rule, (one_filter, (pkg, data, equal)) in enumerate(zip(filters, result), 1):
                    lines.append(f"  rule {n_rule}: package {one_filter['pkg']!r} -> {pkg!r}  "
                                 f"{'==' if equal else '!='}  list {one_filter['data']!r} -> {data!r}")
            msg = "\n".join(lines)
            level = logging.WARNING
        if msg != getattr(self, '_last_ayon_match_msg', None):
            self._last_ayon_match_msg = msg
            self.log.log(level, msg)

    def display_ayon_table(self):
        """
        table data to ui
        """
        if self.ui is None or QtWidgets is None:
            # command line mode: no tables
            return
        if self.ayon_data is None or len(self.ayon_data) == 0:
            return

        show_matched_only = bool(self.settings['ayon_filter_matched']['value']) or False

        table = self.ayon_data
        table_ui = self.ui.ayon_table
        # internal columns (_hide, _folder_id, _matched) are not shown
        titles = [t for t in table[0].keys() if not str(t).startswith('_')]

        # display table
        table_ui.clear()
        table_ui.setColumnCount(0)
        table_ui.setRowCount(0)
        if table and titles:
            table_ui.setSortingEnabled(False)
            table_ui.setColumnCount(len(titles))
            table_ui.setHorizontalHeaderLabels(titles)
            table_ui.setRowCount(len(table))

            row = -1
            # only the rows that pass the list filters / Matched Only
            for line in self.ayon_visible_list():
                # skip displaying filtered out lines
                if line.get('_hide', False):
                    continue
                if bool(line.get('_matched', False)):
                    color = 'green'
                else:
                    color = 'white'
                if color != 'green' and show_matched_only:
                    # skip showing this
                    continue
                row += 1
                for column_number, one_column in enumerate(titles):
                    value = line.get(one_column)
                    if value is None:
                        value = ''
                    value = str(value)
                    # one line per row: multi line values (comments) are joined
                    shown = ' '.join(value.split()) if '\n' in value else value
                    table_ui.setItem(row,
                                     column_number,
                                     QtWidgets.QTableWidgetItem(shown)
                                     )
                    # colorize
                    itm = table_ui.item(row, column_number)
                    if itm and (one_column in self.AYON_CAPPED_COLUMNS or shown != value):
                        # shortened text: full text in the tooltip
                        itm.setToolTip(value)
                    if itm:
                        if color == 'green':
                            itm.setBackground(QtGui.QColor('darkgreen'))
                        else:
                            # white
                            itm.setBackground(QtGui.QColor("#4d4d4d"))

            table_ui.setRowCount(row+1)
            self.fit_ayon_columns(table_ui, titles)
            self.single_line_rows(table_ui)
            table_ui.setSortingEnabled(True)

    # columns that don't get their full text width, see fit_ayon_columns
    AYON_CAPPED_COLUMNS = ('Repre Path',)
    AYON_CAPPED_MIN = 120

    @staticmethod
    def capped_width(widths, index, minimum=120):
        """
        Width for a capped column: like the wider of its neighbours, at least
        minimum, never wider than its own content
        :param widths: content widths of all columns
        """
        neighbours = [widths[i] for i in (index - 1, index + 1) if 0 <= i < len(widths)]
        target = max(neighbours + [minimum])
        return min(widths[index], target)

    def fit_ayon_columns(self, table_ui, titles):
        """
        Every column as wide as its widest text (all rows, not only the
        visible ones, and the header), except the capped columns
        """
        header = table_ui.horizontalHeader()
        # -1: measure all rows. The default only looks at the visible rows,
        # so columns came out too narrow when the tab was not shown.
        header.setResizeContentsPrecision(-1)
        table_ui.resizeColumnsToContents()
        widths = [table_ui.columnWidth(i) for i in range(len(titles))]
        for i, title in enumerate(titles):
            if title in self.AYON_CAPPED_COLUMNS:
                table_ui.setColumnWidth(i, self.capped_width(widths, i, self.AYON_CAPPED_MIN))
        # long paths keep their start and file name visible
        table_ui.setTextElideMode(QtCore.Qt.ElideMiddle)

    @staticmethod
    def single_line_rows(table_ui):
        """
        Every row exactly one text line high: no word wrap (long Repre Path
        values made rows several lines tall), fixed row height
        """
        table_ui.setWordWrap(False)
        vh = table_ui.verticalHeader()
        line = table_ui.fontMetrics().height()
        vh.setMinimumSectionSize(1)
        vh.setDefaultSectionSize(line + 6)
        vh.setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

    def _get_latest_valid_csv_file(self, file_path, get_latest=False):
        """
        Checks if path is a folder. If it is a file, converts it to its parent folder.
        Gets all .csv files in that folder, sorts them and checks if they can be parsed as CSV.

        :param file_path: Path to file or folder
        :param get_latest: If True, returns the latest CSV file in the folder. If False, returns the csv file provided in file_path.
        :return: Path to valid csv file, or None
        """

        def validate_csv(csv_file):
            is_valid = False
            try:
                with open(csv_file, "r", encoding='utf-8-sig', newline='') as f:
                    reader = csv.reader(f)
                    # Read the first row to validate
                    next(reader, None)
                    is_valid = True
            except Exception:
                pass
            return is_valid

        valid_csv_files = []
        csv_files = []

        # get list of csv files
        file_path = str(file_path or '')
        if not file_path:
            return None
        if not get_latest and os.path.isfile(file_path):
            csv_files = [file_path]
        else:
            if os.path.isfile(file_path):
                folder_path = os.path.dirname(file_path)
            else:
                folder_path = file_path
            if folder_path and os.path.isdir(folder_path):
                csv_files = [
                    os.path.join(folder_path, f) for f in
                    os.listdir(folder_path)
                    if f.lower().endswith(".csv")
                ]

        if csv_files is None or len(csv_files) == 0:
            return None

        for csv_file in csv_files:
            if validate_csv(csv_file):
                valid_csv_files.append(csv_file)

        if valid_csv_files is None or len(valid_csv_files) == 0:
            return None

        latest = sorted(valid_csv_files)[-1]
        latest = latest.replace("\\", "/")
        return latest

    def _csv_to_list_of_dicts(self, csv_path, prefix=''):
        """
        Reads a CSV file and returns a list of dictionaries.

        :param csv_path: Path to the CSV file.
        :param prefix: Prefix to be added to the keys of the dictionaries.
        :return: List of dictionaries representing the data in the file.
        """

        result = []
        try:
            with open(csv_path, mode='r', newline='',
                      encoding='utf-8-sig') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    prefixed_row = {f"{prefix}{key}": value for key, value
                                    in row.items()}
                    # for pairing indication
                    prefixed_row["_matched"] = False
                    result.append(prefixed_row)
        except Exception as e:
            self.log.error(f"Failed to read CSV file: {e}")
        return result


    def csv_replace_data_read(self):

        # Remember the file name for reporting later.
        self.static_keywords['csv_replace_file'] = ""
        if self.settings is None or self.settings.get('replace_enable') is None:
            return

        if not bool(self.settings['replace_enable']['value']):
            return

        valid_csv = self._get_latest_valid_csv_file(self.settings['replace_csv_path']['value'], True)
        if valid_csv is None or valid_csv == '':
            return

        csv_data = self._csv_to_list_of_dicts(valid_csv, '')
        if csv_data is None or len(csv_data) == 0:
            return

        valid_columns = ['Extension', 'Pattern', 'Search', 'Replace']
        columns = list(csv_data[0].keys())
        missing_columns = set(valid_columns) - set(columns)
        if missing_columns:
            self.log.error(f"File {valid_csv} is missing required columns: {missing_columns}")
            return

        # put the name of the csv data file to static keywords, so it can be part of the output
        self.static_keywords['csv_replace_file'] = valid_csv.replace("\\", "/").split("/")[-1]

        self.replace_data = csv_data

    def csv_replace_prepare(self):

        self.replace_prep = None
        if self.replace_data is None or len(self.replace_data) == 0:
            return
        if self.merged_list is None or len(self.merged_list) == 0:
            return
        if self.settings is None:
            return

        # build dict of lists of dicts: file: [{search:'', replace:''}]
        # A rule applies to a file when:
        #  - Extension (without dot, any case) equals the file extension
        #  - Pattern is empty, or the file name contains it (literal text,
        #    case-sensitive, no regex or wildcards)
        # Search and Replace are literal text too. Rules with an empty Search
        # are skipped.
        to_replace = {}
        for item in self.merged_list:
            ext = item.get('extension')
            if ext is None:
                continue
            file_path = item.get('full_path')
            if not file_path:
                continue
            file_name = str(file_path).replace('\\', '/').split('/')[-1]
            for one_rule in self.replace_data:
                if str(one_rule.get('Extension') or '').lower().lstrip('.') != str(ext).lower():
                    continue
                pattern = str(one_rule.get('Pattern') or '')
                if pattern and pattern not in file_name:
                    continue
                search = str(one_rule.get('Search') or '')
                if search == '':
                    continue
                # every matching rule (append() returns None: only the
                # first rule used to survive)
                to_replace.setdefault(file_path, []).append(
                    {'search': search, 'replace': str(one_rule.get('Replace') or '')})
        self.replace_prep = to_replace

    def replace_execute(self):
        """
        Replace button / Replace with Go / headless action 'e'.
        Applies the Search and Replace CSV rules to the package text files,
        in place, with no backup: the package is expected to be a copy already.

        The CSV is read again and the rules are matched to the current file
        list, so edits to the CSV and renamed files are picked up.
        Rules are applied in CSV order, each to the result of the previous one.

        Running it twice applies the rules twice. That is harmless when the
        Replace text doesn't contain the Search text (D:/projects/ ->
        /mnt/projects/), but a rule like 'a' -> 'ab' grows on every run.
        This is an accepted risk, nothing tracks what was already replaced.

        Files are decoded as UTF-8 (latin-1 as a lossless fallback) and
        written back with the same encoding and the original line endings.
        :return: dict {file path: number of replacements}, files that failed
                 are left out
        """
        result = {}
        if not self._setting_on('replace_enable'):
            self.log.warning("Search and Replace: Enable is off on the Replace tab, nothing replaced.")
            return result
        self.replace_data = []
        self.csv_replace_data_read()
        if not self.replace_data:
            self.log.warning("Search and Replace: no valid CSV with rules, nothing replaced.")
            return result
        self.csv_replace_prepare()
        if not self.replace_prep:
            self.log.info("Search and Replace: no package file matches the rules.")
            return result

        for file_path, rules in self.replace_prep.items():
            try:
                with open(file_path, 'rb') as f:
                    raw = f.read()
            except OSError as e:
                self.log.error(f"Search and Replace: can't read {file_path}: {e}")
                continue
            encoding = 'utf-8'
            try:
                text = raw.decode(encoding)
            except UnicodeDecodeError:
                encoding = 'latin-1'
                text = raw.decode(encoding)

            count = 0
            for rule in rules:
                hits = text.count(rule['search'])
                if hits:
                    text = text.replace(rule['search'], rule['replace'])
                    count += hits

            if count:
                try:
                    with open(file_path, 'wb') as f:
                        f.write(text.encode(encoding))
                except (OSError, UnicodeError) as e:
                    self.log.error(f"Search and Replace: can't write {file_path}: {e}")
                    continue
            result[file_path] = count
            self.log.info(f"Search and Replace: {count} replacement(s) in {file_path}")

        total = sum(result.values())
        self.log.info(f"Search and Replace: {total} replacement(s) in {len(result)} file(s).")
        if not self.headless and self.ui is not None:
            self.display_replace_table()
        return result


    def display_replace_table(self):
        """
        table data to ui
        """
        if self.ui is None or QtWidgets is None:
            # command line mode: no tables
            return
        if self.replace_prep is None or self.replace_prep == {}:
            return

        titles = ['File', 'Number of Searches', 'Rules']
        table = []
        for file_path, rules in self.replace_prep.items():
            if rules is None or len(rules) == 0:
                continue
            rules_str = ""
            for rule in rules:
                rules_str += f"{rule['search']} => {rule['replace']};"
            one_line = {
                'File': file_path.replace('\\', '/').split('/')[-1],
                'Number of Searches': str(len(rules)),
                'Rules': rules_str
            }
            table.append(one_line)
        table_ui = self.ui.replace_table


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
                    if line[one_column] is None:
                        line[one_column] = ''
                    table_ui.setItem(row,
                                     column_number,
                                     QtWidgets.QTableWidgetItem(
                                         line[one_column])
                                     )

            table_ui.resizeColumnsToContents()
            table_ui.resizeRowsToContents()
            table_ui.setSortingEnabled(True)

    def csv_data_read(self):
        """
        Retrieves and processes CSV data based on settings configured in the instance. The function identifies
        valid CSV files either from a specified directory or directly from the provided file path. It validates
        the structure of any discovered CSV file and loads its contents into dictionaries. The processed data, in
        the form of a list of dictionaries, is stored in the instance property for further use.

        :return: None
        """
        self.static_keywords['csv_data_file'] = ""

        if self.settings is None:
            return

        do_csv_data = bool(self.settings['data_enable']['value'])
        if not do_csv_data:
            return

        valid_csv = self._get_latest_valid_csv_file(self.settings['data_csv_path']['value'], bool(self.settings['data_csv_latest']['value']))
        if valid_csv is None or valid_csv == '':
            return

        csv_data = []
        csv_data = self._csv_to_list_of_dicts(valid_csv, self.settings['name_date_prefix']['value'])
        if csv_data is None or len(csv_data) == 0:
            return

        # put the name of the csv data file to static keywords, so it can be part of the output
        self.static_keywords['csv_data_file'] = valid_csv.replace("\\", "/").split("/")[-1]

        self.csv_data = csv_data

    def csv_data_assign(self):

        # remove what the last assign merged into the files: the csv, the
        # prefix or the rules may have changed since
        for item in self.merged_list or []:
            for key in item.pop('_data_keys', []):
                item.pop(key, None)
        for one_data_line in self.csv_data or []:
            one_data_line.pop("_matched", None)

        if self.csv_data is None or len(self.csv_data) == 0:
            return
        if self.merged_list is None or len(self.merged_list) == 0:
            return
        if self.settings is None:
            return

        # get filters from gui, exit if filters empty
        filters = []
        if bool(self.settings['data_package1_chbx']['value']):
            filters.append({
                'pkg' : self.settings['data_package1']['value'],
                'data': self.settings['data_data1']['value']
            })
        if bool(self.settings['data_package2_chbx']['value']):
            filters.append({
                'pkg': self.settings['data_package2']['value'],
                'data': self.settings['data_data2']['value']
            })
        if bool(self.settings['data_package3_chbx']['value']):
            filters.append({
                'pkg': self.settings['data_package3']['value'],
                'data': self.settings['data_data3']['value']
            })

        if filters is None or len(filters) == 0:
            return

        for item in self.merged_list:
            for one_data_line in self.csv_data:
                matched_filters = 0
                for one_filter in filters:
                    pkg = format_keep(one_filter['pkg'], item)
                    pkg = format_keep(pkg, one_data_line)
                    data = format_keep(one_filter['data'], one_data_line)
                    data = format_keep(data, item)
                    if pkg is None or data is None:
                        continue
                    if str(pkg) == str(data):
                        matched_filters += 1

                # skip item if not matching
                if matched_filters != len(filters):
                    continue
                # flag data line as matched
                one_data_line["_matched"] = True

                # merge data to matched item, remember the keys for the next assign
                merged = [k for k in one_data_line if k != "_matched"]
                item.update({k: one_data_line[k] for k in merged})
                item['_data_keys'] = sorted(set(item.get('_data_keys', [])) | set(merged))
                continue

    def data_rows_to_show(self):
        """Data tab rows for the table: only matched rows when Show Matched Only is on"""
        rows = self.csv_data or []
        if self._get('data_filter_matched', True):
            rows = [r for r in rows if r.get('_matched')]
        return rows

    def display_data_table(self):
        """
        table data to ui
        """
        if self.ui is None or QtWidgets is None:
            # command line mode: no tables
            return
        if self.csv_data is None or len(self.csv_data) == 0:
            # Data off or the csv is gone: don't keep showing the old rows
            if self.ui is not None and not self.headless:
                self.ui.data_table.clear()
                self.ui.data_table.setColumnCount(0)
                self.ui.data_table.setRowCount(0)
            return

        table = self.csv_data
        table_ui = self.ui.data_table
        # every key of every row, in order; _matched is the row color, not a
        # column (rows that matched nothing have no _matched key: KeyError)
        titles = []
        for line in table:
            for key in line:
                if key != '_matched' and key not in titles:
                    titles.append(key)

        # Show Matched Only (on by default): only the rows paired with a file
        table = self.data_rows_to_show()

        # display table
        table_ui.clear()
        table_ui.setColumnCount(0)
        table_ui.setRowCount(0)
        if titles:
            table_ui.setSortingEnabled(False)
            table_ui.setColumnCount(len(titles))
            table_ui.setHorizontalHeaderLabels(titles)
            table_ui.setRowCount(len(table))

            for row, line in enumerate(table):
                for column_number, one_column in enumerate(titles):
                    value = line.get(one_column)
                    table_ui.setItem(row,
                                     column_number,
                                     QtWidgets.QTableWidgetItem(
                                         '' if value is None else str(value))
                                     )

                    # colorize
                    itm = table_ui.item(row, column_number)
                    color = 'white'
                    if line.get('_matched'):
                        color = 'green'
                    if itm:
                        if color == 'green':
                            itm.setBackground(QtGui.QColor('darkgreen'))
                        else:
                            # white
                            itm.setBackground(QtGui.QColor("#4d4d4d"))

            table_ui.resizeColumnsToContents()
            table_ui.resizeRowsToContents()
            table_ui.setSortingEnabled(True)

    # ------------------------------------------------------------------ ftrack
    # Columns of the table on the ftrack tab, one row per file
    FTRACK_TABLE_COLUMNS = ['File', 'Ext', 'Shot', 'Task', 'Version', 'Status',
                            'Shot Found', 'Task Found', 'Notes', 'Note', 'Range']

    @staticmethod
    def _fq(value):
        """value quoted for an ftrack query expression"""
        return '"' + str(value).replace('\\', '\\\\').replace('"', '\\"') + '"'

    @staticmethod
    def _ftrack_file_name(item):
        full = item.get('full_path') or ''
        if full:
            return os.path.basename(str(full))
        ext = item.get('extension', '')
        return str(item.get('name', '')) + ('.' + str(ext) if ext else '')

    def _ftrack_setting(self, key, default=None):
        one = (self.settings or {}).get(key)
        if one is None or one.get('value') is None:
            return default
        return one['value']

    def ftrack_query(self):
        """
        Everything the ftrack tab does for the loaded files: connect, query
        notes (Query Notes) and shot / task attributes (Query OpenPype
        Attributes). Logs an INFO summary and DEBUG details per file, both only
        when they changed (this runs on every edit of the ftrack tab).
        """
        self.ftrack_clean_notes()
        if self.ftrack is None:
            self.ftrack = {}
        self.ftrack['status'] = ''
        self._ftrack_cache = {}
        self._ftrack_details = []
        for item in self.merged_list or []:
            item['_ftrack_status'] = ''
            item['_ftrack_shot'] = ''
            item['_ftrack_task'] = ''
            item['_ftrack_version'] = ''

        if not self.settings:
            return
        do_ftrack = bool(self._ftrack_setting('ftrack_use', False))
        if not do_ftrack:
            self.ftrack['session'] = None
            self.ftrack['status'] = "Ftrack is off: check 'Use Ftrack' on the ftrack tab"
            self._ftrack_log_summary(self.ftrack['status'], level=logging.DEBUG)
            return

        t0 = time.time()
        self.get_ftrack_session()
        if self.ftrack.get('session') is None:
            self.ftrack['status'] = "No ftrack connection (see the warnings above)"
            self._ftrack_log_summary(self.ftrack['status'], level=logging.WARNING)
            return

        do_notes = bool(self._ftrack_setting('ftrack_do_notes', False))
        do_op = bool(self._ftrack_setting('ftrack_do_op', False))

        problems = []
        if not self.ftrack.get('project'):
            problems.append("Project is empty")
        elif self.ftrack.get('project_id') is None:
            problems.append(f"project '{self.ftrack['project']}' not found among active ftrack projects")
        if not self.ftrack.get('shot'):
            problems.append("Shot is empty")
        if not self.ftrack.get('task'):
            problems.append("Task is empty")
        if problems:
            self.ftrack['status'] = "Ftrack query skipped, set on the ftrack tab: " + ", ".join(problems)
            self._ftrack_log_summary(self.ftrack['status'], level=logging.WARNING)
            return
        if not do_notes and not do_op:
            self.ftrack['status'] = ("Ftrack connected, but nothing to query: check 'Query Notes' "
                                     "and / or 'Query OpenPype Attributes' on the ftrack tab")
            self._ftrack_log_summary(self.ftrack['status'], level=logging.INFO)
            return

        if do_notes:
            self.get_ftrack_notes()
        if do_op:
            self.ftrack_op_attrs()

        items = self.merged_list or []
        statuses = {}
        for item in items:
            st = item.get('_ftrack_status') or 'not queried'
            # "ok, 3 notes" -> "ok"
            st = st.split(',')[0]
            statuses[st] = statuses.get(st, 0) + 1
        with_notes = sum(1 for i in items if i.get('ftrack_notes'))
        shots_found = sum(1 for i in items if i.get('ftrack_shot_exists') == "1")
        tasks_found = sum(1 for i in items if i.get('ftrack_task_exists') == "1")
        parts = [f"project '{self.ftrack['project']}'", f"{len(items)} file(s)"]
        if do_notes:
            parts.append(f"{with_notes} with notes")
        if do_op:
            parts.append(f"{shots_found} shot(s) and {tasks_found} task(s) found")
        parts.append("status: " + ", ".join(f"{k} {v}" for k, v in sorted(statuses.items())))
        self.ftrack['status'] = "Ftrack: " + "; ".join(parts)
        level = logging.INFO
        if items and do_notes and with_notes == 0:
            level = logging.WARNING
            self.ftrack['status'] += (". No notes found: check the Shot / Task / Version templates, "
                                      "Extensions and Note Label (details in the log at DEBUG level)")
        self._ftrack_log_summary(self.ftrack['status'], level=level,
                                 details=self._ftrack_details,
                                 seconds=time.time() - t0)

    def _ftrack_log_summary(self, message, level=logging.INFO, details=None, seconds=None):
        """log the summary and the per file details, only when they changed"""
        details = list(details or [])
        signature = (message, tuple(details))
        if getattr(self, '_last_ftrack_log', None) == signature:
            return
        self._last_ftrack_log = signature
        self.log.log(level, message + (f" ({seconds:.1f}s)" if seconds is not None else ""))
        for line in details:
            self.log.debug("Ftrack: " + line)

    def ftrack_clean_notes(self):
        for item in self.merged_list or []:
            item['ftrack_notes'] = []
            item['ftrack_note'] = ''

    def ftrack_clean_note(self):
        for item in self.merged_list or []:
            item['ftrack_note'] = ''

    def ftrack_get_hierarchical_attribute( self,
            session,
            entity,
            attribute_name
    ):
        '''Return hierarchical attribute *attribute_name* or default.'''
        entities = []
        if isinstance(entity, session.types['Project']):
            entities = [entity]
        else:
            if isinstance(entity, session.types['AssetVersion']):
                asset_version = session.query(
                    'select asset.parent.ancestors.id, asset.parent.project ' +
                    'from AssetVersion where id is "{}"'.format(entity['id'])
                ).one()
                parent = asset_version['asset']['parent']
                if isinstance(parent, session.types['Project']):
                    entities = (
                            [asset_version] +
                            [parent]
                    )
                else:
                    entities = (
                            [asset_version] +
                            [parent] +
                            list(reversed(parent['ancestors'])) +
                            [parent['project']]
                    )
            else:
                typed_context = session.query(
                    'select ancestors.id, project ' +
                    'from TypedContext where id is "{}"'.format(entity['id'])
                ).one()
                entities = (
                        [typed_context] +
                        list(reversed(typed_context['ancestors'])) +
                        [typed_context['project']]
                )

        entity_ids = [item['id'] for item in entities]

        [values, default_value] = session.call([{
            'action': 'query',
            'expression': (
                'select value, entity_id from CustomAttributeValue '
                'where entity_id in ({0}) and configuration.key is "{1}"'
                .format(
                    ', '.join(
                        ['"{0}"'.format(entity_id) for entity_id in entity_ids]
                    ),
                    attribute_name
                )
            )
        }, {
            'action': 'query',
            'expression': (
                'select default from CustomAttributeConfiguration '
                'where key is "{0}"'.format(
                    attribute_name
                )
            )
        }])

        attribute_value = default_value['data'][0]['default']
        if values['data']:
            attribute_value = sorted(
                values['data'],
                key=lambda value: entity_ids.index(value['entity_id'])
            )[0]['value']

        return attribute_value

    def get_ftrack_session(self):
        """
        Reads ftrack install prefs and gui settings
        Tries to connect to Ftrack
        Tries to query project id from project name and
        label object from label name

        :return:
        self.ftrack dict with all ftrack info gathered
        """

        if self.settings:
            def _val(*keys, default=''):
                # first key that exists; missing keys don't crash
                for k in keys:
                    one = self.settings.get(k)
                    if one is not None and one.get('value') is not None:
                        return one['value']
                return default

            self.ftrack['do_ftrack'] = bool(_val('ftrack_use', default=False))
            # the Extensions field is "ftrack_include_2" in the ui file;
            # "ftrack_include" is its old name, still in older presets
            self.ftrack['include'] = str(_val('ftrack_include_2', 'ftrack_include'))
            self.ftrack['project'] = str(_val('ftrack_project')).strip()
            self.ftrack['shot'] = str(_val('ftrack_shot')).strip()
            self.ftrack['task'] = str(_val('ftrack_task')).strip()
            self.ftrack['do_label'] = bool(_val('ftrack_label_use', default=False))
            self.ftrack['label'] = str(_val('ftrack_label')).strip()
            self.ftrack['do_version'] = bool(_val('ftrack_version_use', default=False))
            self.ftrack['version'] = str(_val('ftrack_version')).strip()
            self.ftrack['note_pattern'] = str(_val('ftrack_note_pattern'))
            self.ftrack['note_repl'] = str(_val('ftrack_note_repl'))

            # extensions separated by spaces or commas, with or without dot
            self.ftrack['include'] = [e.strip().lstrip('.').lower()
                                      for e in self.ftrack['include'].replace(',', ' ').split()
                                      if e.strip()]

            self.ftrack['session'] = None
            self.ftrack['project_id'] = None
            self.ftrack['label_obj'] = None
            if self.ftrack['do_ftrack']:
                # no credentials: the gui asks the user to sign in (once)
                credentials.ensure_ftrack(self.paths)
                self.ftrack['url'] = self.paths.get('FTRACK_SERVER', '')
                self.ftrack['key'] = self.paths.get('FTRACK_API_KEY', '')
                self.ftrack['user'] = self.paths.get('FTRACK_API_USER', '')
                # never raises: missing settings / failed connection are logged
                # and the session stays None (ftrack is then skipped)
                self.ftrack['session'] = open_session(
                    self.ftrack['url'], self.ftrack['user'], self.ftrack['key'])
                self.ftrack['project_id'] = find_project_id(
                    self.ftrack['session'], self.ftrack['project'])

                settings_msg = (
                    f"Ftrack settings: server {self.ftrack['url'] or '(not set)'}, "
                    f"user {self.ftrack['user'] or '(not set)'}, "
                    f"connected {self.ftrack['session'] is not None}, "
                    f"project '{self.ftrack['project']}' "
                    f"{'found' if self.ftrack['project_id'] else 'NOT found'}, "
                    f"shot '{self.ftrack['shot']}', task '{self.ftrack['task']}', "
                    f"version {repr(self.ftrack['version']) if self.ftrack['do_version'] else 'off'}, "
                    f"label {repr(self.ftrack['label']) if self.ftrack['do_label'] else 'off'}, "
                    f"extensions {','.join(self.ftrack['include']) or 'all'}")
                if getattr(self, '_last_ftrack_settings_msg', None) != settings_msg:
                    self._last_ftrack_settings_msg = settings_msg
                    self.log.debug(settings_msg)

                if self.ftrack['session'] is not None and self.ftrack['do_label']:
                    if self.ftrack['label'] == '':
                        self.log.debug("Ftrack: Note Label is checked but empty, notes are not filtered by label")
                    else:
                        try:
                            self.ftrack['label_obj'] = self.ftrack['session']\
                                .query('NoteLabel where name is {}'.format(
                                    self._fq(self.ftrack['label']))).first()
                        except Exception as e:
                            self.log.warning(f"Ftrack note label '{self.ftrack['label']}' query failed: {e}")
                        if self.ftrack['label_obj'] is None:
                            msg = f"Ftrack note label '{self.ftrack['label']}' not found, no notes will match"
                            if getattr(self, '_last_ftrack_label_msg', None) != msg:
                                self._last_ftrack_label_msg = msg
                                self.log.warning(msg)

    def get_ftrack_notes(self):
        """
        For every merged list item it tries to get Ftrack note
        :return:
        item['ftrack_notes']
        """
        if not self.settings or not self.ftrack or self.merged_list is None:
            return
        if not bool(self._ftrack_setting('ftrack_do_notes', False)):
            return

        include = self.ftrack.get('include') or []
        for item in self.merged_list:
            if include:
                e = str(item.get('extension', '')).lower().lstrip('.')
                if e not in include:
                    item['_ftrack_status'] = 'skipped (extension)'
                    self._ftrack_details.append(
                        f"{self._ftrack_file_name(item)}: skipped, extension '{e}' "
                        f"is not in Extensions ({', '.join(include)})")
                    continue
            self.assign_ftrack_notes(item)

    def _ftrack_resolve(self, item):
        """shot, task and version names of the item from the ftrack tab templates"""
        current_shot = format_keep(self.ftrack.get('shot', ''), item)
        current_task = format_keep(self.ftrack.get('task', ''), item)
        current_version = format_keep(self.ftrack.get('version', ''), item)
        item['_ftrack_shot'] = current_shot
        item['_ftrack_task'] = current_task
        item['_ftrack_version'] = current_version if self.ftrack.get('do_version') else ''
        return current_shot, current_task, current_version

    def _ftrack_cached(self, key, query):
        """
        first() of the query, cached for one refresh: files of one shot / task
        share the result. Returns (entity or None, error text or None)
        """
        cache = getattr(self, '_ftrack_cache', None)
        if cache is None:
            cache = self._ftrack_cache = {}
        if key in cache:
            return cache[key]
        try:
            result = (self.ftrack['session'].query(query).first(), None)
        except Exception as e:
            result = (None, str(e))
            self.log.warning(f"Ftrack query failed: {query}: {e}")
        cache[key] = result
        return result

    def _ftrack_find_task(self, shot, task):
        query = 'Task where name is {} and parent.name is {} and project.full_name is {}'.format(
            self._fq(task), self._fq(shot), self._fq(self.ftrack['project']))
        return self._ftrack_cached(('task', shot, task), query)

    def _ftrack_find_shot(self, shot):
        query = 'Shot where name is {} and project.full_name is {}'.format(
            self._fq(shot), self._fq(self.ftrack['project']))
        return self._ftrack_cached(('shot', shot), query)

    @staticmethod
    def _note_label_ids(note):
        """ids of the labels of an ftrack note"""
        ids = set()
        try:
            links = note['note_label_links'] or []
        except Exception:
            links = []
        for link in links:
            lid = None
            try:
                lid = link['label_id']
            except Exception:
                try:
                    lid = link['label']['id']
                except Exception:
                    lid = None
            if lid is not None:
                ids.add(lid)
        return ids

    def _ftrack_note_ok(self, note):
        """True when the note passes the Note Label filter"""
        if not self.ftrack.get('do_label') or not self.ftrack.get('label'):
            return True
        label_obj = self.ftrack.get('label_obj')
        if label_obj is None:
            return False
        return label_obj['id'] in self._note_label_ids(note)

    @staticmethod
    def _note_text(note):
        content = str(note['content'])
        try:
            content = unidecode(content)
        except Exception:
            pass
        return content

    def assign_ftrack_notes(self, item):
        """
        for item in merged_list, query all ftrack notes
        that fit project, shot, task, optional label, optional version
        :param item:
        :return:
        add to item['ftrack_notes'] all notes on task or version
        """
        if not self.settings or not bool(self._ftrack_setting('ftrack_do_notes', False)):
            return
        if not self.ftrack or self.ftrack.get('session') is None:
            return
        name = self._ftrack_file_name(item)
        details = getattr(self, '_ftrack_details', None)
        if details is None:
            details = self._ftrack_details = []

        def _status(status, detail):
            item['_ftrack_status'] = status
            details.append(f"{name}: {detail}")

        item['ftrack_notes'] = []
        current_shot, current_task, current_version = self._ftrack_resolve(item)

        version_gui = 0
        if self.ftrack.get('do_version'):
            try:
                version_gui = int(current_version)
            except (TypeError, ValueError):
                _status('version not a number',
                        f"Version '{self.ftrack.get('version')}' gives '{current_version}', not a number")
                return

        if current_shot == '' or current_task == '' or self.ftrack.get('project', '') == '':
            _status('empty shot / task', f"shot '{current_shot}' or task '{current_task}' is empty")
            return
        if '{' in current_shot or '{' in current_task:
            _status('template not resolved',
                    f"shot '{current_shot}', task '{current_task}': the {{keys}} left are not "
                    f"parsed for this file (see the Parsing tab)")
            return

        f_task, error = self._ftrack_find_task(current_shot, current_task)
        if error:
            _status('query error', f"task query failed: {error}")
            return
        if f_task is None:
            _status('task not found',
                    f"task '{current_task}' on shot '{current_shot}' not found in project "
                    f"'{self.ftrack['project']}'")
            return

        all_notes = []
        seen = 0
        if self.ftrack.get('do_version'):
            key = ('versions', f_task['id'])
            cache = self._ftrack_cache
            if key not in cache:
                try:
                    cache[key] = (self.ftrack['session'].query(
                        'select asset.name, version from AssetVersion '
                        'where task_id is "{}" and asset.name is_not '
                        'none order by version desc'.format(f_task['id'])).all(), None)
                except Exception as e:
                    self.log.warning(f"Ftrack version query failed for task '{current_task}' "
                                     f"on shot '{current_shot}': {e}")
                    cache[key] = (None, str(e))
            assets, error = cache[key]
            if assets is None:
                _status('query error', f"version query failed: {error}")
                return
            existing = []
            matched = 0
            for one_asset in assets:
                try:
                    version_asset = int(one_asset['version'])
                except Exception:
                    version_asset = 0
                existing.append(version_asset)
                if version_gui == version_asset:
                    matched += 1
                    for one_note in one_asset['notes']:
                        seen += 1
                        if self._ftrack_note_ok(one_note):
                            all_notes.append(self._note_text(one_note))
            if not matched:
                _status('version not found',
                        f"task found, but no version {version_gui} on it "
                        f"(versions: {', '.join(str(v) for v in sorted(set(existing))) or 'none'})")
                return
        else:
            for one_note in f_task['notes']:
                seen += 1
                if self._ftrack_note_ok(one_note):
                    all_notes.append(self._note_text(one_note))

        item['ftrack_notes'] = all_notes
        where = f"version {version_gui}" if self.ftrack.get('do_version') else "task"
        label = ''
        if self.ftrack.get('do_label') and self.ftrack.get('label'):
            label = f", {seen - len(all_notes)} without label '{self.ftrack['label']}'"
            if self.ftrack.get('label_obj') is None:
                label = f", label '{self.ftrack['label']}' does not exist in ftrack"
        if all_notes:
            _status(f"ok, {len(all_notes)} notes",
                    f"shot '{current_shot}', task '{current_task}': {len(all_notes)} note(s) on {where}"
                    f" ({seen} in total{label})")
        else:
            _status('no notes',
                    f"shot '{current_shot}', task '{current_task}': no matching notes on {where}"
                    f" ({seen} in total{label})")

    def ftrack_op_attrs(self):
        """
        Query OpenPype Attributes: shot / task exist, frame range and handles
        of the shot (hierarchical attributes)
        """
        if not self.settings or not bool(self._ftrack_setting('ftrack_do_op', False)):
            return
        if not self.ftrack or self.ftrack.get('session') is None:
            self.log.debug("Ftrack query skipped: no ftrack session")
            return
        if self.merged_list is None:
            self.log.debug("Ftrack query skipped: no files")
            return
        if not self.ftrack.get('project') or not self.ftrack.get('shot') or not self.ftrack.get('task') \
                or self.ftrack.get('project_id') is None:
            # ftrack_query explains what is missing
            return
        details = getattr(self, '_ftrack_details', None)
        if details is None:
            details = self._ftrack_details = []

        empty = ['ftrack_op_frame_start', 'ftrack_op_handle_start', 'ftrack_op_start',
                 'ftrack_op_start_slate', 'ftrack_op_frame_end', 'ftrack_op_handle_end',
                 'ftrack_op_end', 'ftrack_op_range', 'ftrack_op_range_slate',
                 'ftrack_op_length', 'ftrack_op_length_slate']
        attr_cache = {}
        for item in self.merged_list:
            name = self._ftrack_file_name(item)
            for k in empty:
                item[k] = ""
            item['ftrack_task_exists'] = "0"
            item['ftrack_shot_exists'] = "0"

            current_shot, current_task, _ = self._ftrack_resolve(item)
            if '{' in current_shot or '{' in current_task or not current_shot:
                if not item.get('_ftrack_status'):
                    item['_ftrack_status'] = 'template not resolved'
                details.append(f"{name}: attributes skipped, shot '{current_shot}' / "
                               f"task '{current_task}' not resolved")
                continue

            f_shot, _ = self._ftrack_find_shot(current_shot)
            f_task = None
            if current_task:
                f_task, _ = self._ftrack_find_task(current_shot, current_task)
            if f_task:
                item['ftrack_task_exists'] = "1"
            if not f_shot:
                if not item.get('_ftrack_status'):
                    item['_ftrack_status'] = 'shot not found'
                details.append(f"{name}: shot '{current_shot}' not found in project '{self.ftrack['project']}'")
                continue
            item['ftrack_shot_exists'] = "1"

            if f_shot['id'] not in attr_cache:
                values = {}
                # first name is the one used until now, then the OpenPype / Ayon spelling
                for attr, keys in (("frameStart", ("framestart", "frameStart")),
                                   ("frameEnd", ("frameend", "frameEnd")),
                                   ("handleStart", ("handleStart", "handlestart")),
                                   ("handleEnd", ("handleEnd", "handleend"))):
                    values[attr] = None
                    errors = []
                    for one_key in keys:
                        try:
                            v = self.ftrack_get_hierarchical_attribute(self.ftrack['session'], f_shot, one_key)
                            values[attr] = int(float(v))
                            break
                        except Exception as e:
                            errors.append(f"{one_key}: {e or type(e).__name__}")
                    if values[attr] is None:
                        details.append(f"shot '{current_shot}': attribute {attr} not readable ({'; '.join(errors)})")
                attr_cache[f_shot['id']] = values
            values = attr_cache[f_shot['id']]
            _fs, _fe = values["frameStart"], values["frameEnd"]
            _hs, _he = values["handleStart"] or 0, values["handleEnd"] or 0
            if _fs is None or _fe is None:
                if not item.get('_ftrack_status'):
                    item['_ftrack_status'] = 'no frame range'
                details.append(f"{name}: shot '{current_shot}' found, no frameStart / frameEnd")
                continue
            item['ftrack_op_frame_start'] = str(_fs)
            item['ftrack_op_handle_start'] = str(_hs)
            item['ftrack_op_start'] = str(_fs - _hs)
            item['ftrack_op_start_slate'] = str(_fs - _hs - 1)
            item['ftrack_op_frame_end'] = str(_fe)
            item['ftrack_op_handle_end'] = str(_he)
            item['ftrack_op_end'] = str(_fe + _he)
            # _slate tokens include one slate frame before the first frame,
            # like ftrack_op_start_slate (range / length had it the other way)
            _start, _end = _fs - _hs, _fe + _he
            item['ftrack_op_range'] = "{}-{}".format(_start, _end)
            item['ftrack_op_range_slate'] = "{}-{}".format(_start - 1, _end)
            item['ftrack_op_length'] = str(_end - _start + 1)
            item['ftrack_op_length_slate'] = str(_end - _start + 2)
            if not item.get('_ftrack_status'):
                item['_ftrack_status'] = 'ok'
            details.append(f"{name}: shot '{current_shot}' {_fs}-{_fe}, handles {_hs}/{_he}, "
                           f"task '{current_task}' {'found' if f_task else 'NOT found'}")

    def select_ftrack_note(self):
        """
        from item['ftrack_notes'] queried from ftrack by assign_ftrack_notes
        filter the first note that fits note regex and optionally repl
        :return:
        """
        if self.ftrack is None:
            self.ftrack = {}
        self.ftrack_clean_note()
        self.ftrack['note_pattern'] = str(self._ftrack_setting('ftrack_note_pattern', ''))
        self.ftrack['note_repl'] = str(self._ftrack_setting('ftrack_note_repl', ''))
        with_notes = 0
        selected = 0
        for item in self.merged_list or []:
            all_notes = item.get('ftrack_notes', [])
            if not all_notes:
                continue
            with_notes += 1
            current_note = expand_tokens(self.ftrack.get('note_pattern', ''), item)
            notes = []
            for one in all_notes:
                v = self.note_regex(one, current_note, self.ftrack['note_repl'])
                if v is not None:
                    notes.append(v)
            out_note = ";---;".join(notes) if notes else ''
            if out_note:
                selected += 1
            item['ftrack_note'] = out_note

        if with_notes:
            msg = (f"Ftrack notes: {selected} of {with_notes} file(s) with notes match the Note pattern "
                   f"'{self.ftrack['note_pattern']}'")
            if getattr(self, '_last_ftrack_select_msg', None) != msg:
                self._last_ftrack_select_msg = msg
                if selected == 0:
                    self.log.warning(msg + ", check the Note pattern (it is a regex, {keys} are filled per file)")
                else:
                    self.log.info(msg)

    def ftrack_table_rows(self):
        """rows of the ftrack tab table, one per file"""
        rows = []
        for item in self.merged_list or []:
            notes = item.get('ftrack_notes') or []
            rows.append({
                'File': self._ftrack_file_name(item),
                'Ext': str(item.get('extension', '')),
                'Shot': item.get('_ftrack_shot', ''),
                'Task': item.get('_ftrack_task', ''),
                'Version': item.get('_ftrack_version', ''),
                'Status': item.get('_ftrack_status', '') or 'not queried',
                'Shot Found': {"1": "yes", "0": "no"}.get(item.get('ftrack_shot_exists'), ''),
                'Task Found': {"1": "yes", "0": "no"}.get(item.get('ftrack_task_exists'), ''),
                'Notes': str(len(notes)) if notes else '',
                'Note': item.get('ftrack_note', ''),
                'Range': item.get('ftrack_op_range', ''),
            })
        return rows

    def display_ftrack_table(self):
        """fill the table on the ftrack tab"""
        if self.headless or self.ui is None or not hasattr(self.ui, 'ftrack_table'):
            return
        table_ui = self.ui.ftrack_table
        table_ui.setSortingEnabled(False)
        table_ui.clear()
        table_ui.setColumnCount(0)
        table_ui.setRowCount(0)
        rows = self.ftrack_table_rows()
        status = (self.ftrack or {}).get('status', '')
        titles = list(self.FTRACK_TABLE_COLUMNS)
        if status and (not rows or all(r['Status'] == 'not queried' for r in rows)):
            # nothing queried: say why instead of an empty table
            titles = ['Info']
            rows = [{'Info': status}]
        if not rows:
            return
        table_ui.setColumnCount(len(titles))
        table_ui.setHorizontalHeaderLabels(titles)
        table_ui.setRowCount(len(rows))
        for r, row in enumerate(rows):
            ok = str(row.get('Status', '')).startswith('ok')
            for c, title in enumerate(titles):
                value = str(row.get(title, '') or '')
                itm = QtWidgets.QTableWidgetItem(value.replace('\n', ' '))
                itm.setToolTip(value)
                if ok:
                    itm.setBackground(QtGui.QColor('darkgreen'))
                table_ui.setItem(r, c, itm)
        table_ui.resizeColumnsToContents()
        # long notes: keep the Note column readable
        if 'Note' in titles:
            col = titles.index('Note')
            if table_ui.columnWidth(col) > 400:
                table_ui.setColumnWidth(col, 400)
        table_ui.setSortingEnabled(True)

    def ftrack_export(self, path=None):
        """
        Export button on the ftrack tab / headless action x: write the ftrack
        shot list. path: a .csv file or a folder, default the package folder
        """
        path = path or str(self._ftrack_setting('ftrack_path', '') or '').strip()
        if not path:
            if not self.in_path:
                self.log.warning("Ftrack export: set the export path on the ftrack tab")
                return None
            path = self.in_path if os.path.isdir(self.in_path) else os.path.dirname(self.in_path)
        if not path.lower().endswith('.csv'):
            path = os.path.join(path, "ftrack_shotlist.csv")
        f = FtrackHelper(self.settings, self.paths)
        if not f.is_session_ok():
            self.log.warning("Ftrack session is not available (check Use Ftrack, the project "
                             "and install.json), shot list not exported.")
            return None
        self.log.info(f"Ftrack export: reading project '{f.ftrack.get('project')}'...")
        f.get_ftrack_info()
        f.ftrack_info_to_csv(path)
        return path

    def note_regex(self, content, note_pattern, note_repl):
        try:
            compiled = re.compile(note_pattern, re.MULTILINE)
        except Exception:
            return None
        result = None
        if note_repl and note_repl != "":
            # it is a replace
            if note_repl.startswith("lambda "):
                try:
                    _eval = eval(str(note_repl))
                except Exception:
                    _eval = note_repl
                try:
                    result = re.sub(compiled, _eval, content)
                except Exception:
                    result = None
            else:
                try:
                    result = compiled.match(content).expand(note_repl)
                except Exception:
                    result = None
        else:
            m = compiled.search(content)
            result = content if m else None
        return result

    def run_checks(self):

        class Default(dict):
            def __missing__(self, key):
                return '{' + key + '}'

        self.checks_init()
        if self.checks is None:
            return
        self._check_errors_logged = set()

        for item in self.merged_list or []:
            item['warning'] = ''
            item['error'] = ''

        for item in self.merged_list or []:
            for one_check in self.checks:
                # filter out first
                _if_eval = False
                if one_check['filter'] != '':
                    try:
                        _if = format_keep(one_check['filter'], item)
                        _if_eval = bool(eval(_if))
                    except Exception as e:
                        self._log_check_error(one_check, 'If', e)
                else:
                    # no filtering, so true for all
                    _if_eval = True

                if _if_eval:
                    # not filtered out
                    _check_eval = False
                    try:
                        _check = format_keep(one_check['check'], item)
                        _check_eval = bool(eval(_check))
                    except Exception as e:
                        self._log_check_error(one_check, 'Check', e)
                    if _check_eval:
                        # it is warning or error
                        m = format_keep(one_check['message'], item)
                        if one_check['is_error']:
                            e = item.get('error', '')
                            if e == '':
                                item['error'] = m
                            else:
                                item['error'] = f"{item['error']}; {m}"
                        else:
                            w = item.get('warning', '')
                            if w == '':
                                item['warning'] = m
                            else:
                                item['warning'] = f"{item['warning']}; {m}"
            sw = item.get('size_warning', '')
            if sw and sw != '':
                if item['warning'] and item['warning'] != '':
                    item['warning'] = item['warning'] + '; ' + sw
                else:
                    item['warning'] = sw
            # the check messages without the Grouping tab ones (grouping.assign
            # adds those on top on every refresh)
            item['check_error'] = item['error']
            item['check_warning'] = item['warning']

    def _log_check_error(self, one_check, field, error):
        """a check expression that fails: logged once per refresh, not per file"""
        seen = self.__dict__.setdefault('_check_errors_logged', set())
        key = (field, one_check.get(field.lower() if field == 'Check' else 'filter'), type(error).__name__)
        if key in seen:
            return
        seen.add(key)
        self.log.debug(f"Checks: {field} expression {key[1]!r} failed: {error!r}")

    def prepare_converts(self):
        """
        Execute command lines for every media file
        :return: add vendor_Thumbs to media files
        """

        class Default(dict):
            def __missing__(self, key):
                return '{' + key + '}'

        self.converts = []
        _root = ''
        if self.settings:
            # read all the settings from ui
            _root = self._get_str('package_folder')
            indexes = [str(x).zfill(2) for x in range(1, 9)]
            for one in indexes:
                if_filter = self._get_str("thumbs_if_" + one)
                exe = self._get_str("thumbs_exe_" + one)
                args = self._get_str("thumbs_args_" + one)
                fn = self._get_str("thumbs_name_" + one)
                if args != '' and fn != '':
                    one_conv = {
                        "filter": if_filter,
                        "exe": exe,
                        "args": args,
                        "fn": fn,
                        "cmd": ""
                    }
                    self.converts.append(one_conv)

        if self.converts is None:
            return

        _exes = {
                'ffmpeg': self.paths.get('ffmpeg', ''),
                'ffprobe': self.paths.get('ffprobe', ''),
                'oiio': self.paths.get('oiiotool', ''),
                'ocio': self.paths.get('ocio', ''),
                'vfx-transcode': self.paths.get('vfx-transcode', ''),
        }

        for item in self.merged_list or []:
            # commands by convert number (01 = first row with Arguments and File
            # Name), rebuilt on every refresh: a stale list paired commands with
            # the wrong output paths
            commands = {}
            for convert_number, one_conv in enumerate(self.converts, start=1):
                convert_count_string = str(convert_number).zfill(2)
                item[f"convert_path{convert_count_string}"] = None
                item[f"convert_path_relative{convert_count_string}"] = None
                # filter out first
                _if_eval = True
                if one_conv['filter'] != '':
                    try:
                        _if = format_keep(one_conv['filter'], item)
                        _if_eval = bool(eval(_if))
                    except Exception:
                        _if_eval = False
                if not _if_eval:
                    continue
                _e = format_keep(one_conv['exe'], self.static_keywords)
                _e = format_keep(_e, _exes)
                _a = format_keep(one_conv['args'], self.static_keywords)
                _a = format_keep(_a, item)
                _a = format_keep(_a, _exes)
                _cmd = "{} {}".format(_e, _a).strip()
                _fn = format_keep(one_conv['fn'], self.static_keywords)
                _fn = format_keep(_fn, item)
                # static keywords or item can include "unfilled tokens": skip
                # file outputs with unknown tokens
                if unresolved_tokens(_fn):
                    continue
                _fnr = _fn
                if _root and _fn.startswith(_root):
                    _fnr = _fn[len(_root)+1:]
                item[f"convert_path{convert_count_string}"] = _fn
                item[f"convert_path_relative{convert_count_string}"] = _fnr
                commands[convert_count_string] = _cmd
            item["convert_cmd"] = commands

    def run_converts(self):
        """
        Execute command lines for every media file
        :return: add vendor_Thumbs to media files
        """
        _skip_existing = bool(self._get('thumbs_skip_existing', True))
        for item in self.merged_list or []:
            commands = item.get("convert_cmd")
            if not isinstance(commands, dict) or not commands:
                continue
            # there can be more than one convert for one item
            for number, one_command in sorted(commands.items()):
                if not one_command:
                    # skip empty commands
                    continue

                _pth = item.get(f"convert_path{number}") or ""
                if _pth == "":
                    # skip empty paths
                    continue

                item_label = str(item.get('part2', '')) + '/' + str(item.get('part1', ''))

                _run = True
                if _skip_existing and os.path.exists(_pth):
                    _run = False

                if _pth and one_command and _run:
                    self.log.debug(
                        "Running Convert of item {}:\n{}".format(item_label, one_command))
                    try:
                        os.makedirs(os.path.dirname(os.path.abspath(_pth)), exist_ok=True)
                        # shell=True on purpose: Convert rows are command lines
                        process = subprocess.Popen(one_command, shell=True,
                                                   stdout=subprocess.PIPE,
                                                   stderr=subprocess.PIPE,
                                                   bufsize=-1,
                                                   **helpers.no_window())
                        out, err = process.communicate()
                    except OSError as e:
                        # one failing convert doesn't stop the others
                        self.log.error(f"Convert of item {item_label} could not run: {e}")
                        continue
                    # was inverted: 0 logged as failure
                    if process.returncode == 0:
                        self.log.debug(
                            "Convert of item {} OK".format(
                                item_label))
                    else:
                        _err = (err or b'').decode('utf-8', errors='replace').strip()
                        self.log.warning(
                            "Convert of item {} failed (return code {}): {}".format(
                                item_label, process.returncode, _err[-500:]))

                    # if command didn't produce desired output, clear convert path to indicate so
                    if not os.path.exists(_pth):
                        item[f"convert_path{number}"] = ''
                        item[f"convert_path_relative{number}"] = ''

    def checks_init(self):
        self.checks = []
        if self.settings:
            # read checks from gui, save to self.checks
            indexes = [str(x).zfill(2) for x in range(1, 22)]
            for one in indexes:
                if_filter = self._get_str("check_if_" + one)
                check = self._get_str("check_check_" + one)
                is_error = bool(self._get("check_error_" + one, False))
                message = self._get_str("check_message_" + one)
                if message == '':
                    if is_error:
                        message = "Error check {}".format(one)
                    else:
                        message = "Warning check {}".format(one)
                if check != '':
                    # only add if check is not empty
                    one_check = {
                        "filter": if_filter,
                        "check": check,
                        "is_error": is_error,
                        "message": message,
                       }
                    self.checks.append(one_check)

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()

    x = Sequencer(in_path=r"C:/projects/OP_2D_testing/resources")
    #pprint.pprint(x.merged_list)

    # finalSeqList = []
    # y = seqLS(x)
