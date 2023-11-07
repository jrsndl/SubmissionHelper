import os
import re
import sys
import shutil
from operator import itemgetter
import pprint
import time
import logging

import xlsxwriter
import csv
import json

import parse_file_name
from metadata import MetaData
import helpers

import ftrack_api
import arrow
import inspect
import subprocess

class Sequencer(object):
    def __init__(self, in_path, sequence_mode='to_subsequences', gui=None, more_settings=None):

        self.log = logging.getLogger("mylog")
        self.sequence_mode = sequence_mode
        self.merged_list = None
        self.settings = gui
        self.regexes = None
        self.static_keywords = None
        self.column_titles_sub = None
        self.column_expressions_sub = None
        self.column_titles_log = None
        self.column_expressions_log = None
        self.column_titles_txt = None
        self.column_expressions_txt = None
        self.table_sub = []
        self.table_log = []
        self.table_side = []
        self.columns_side = []
        self.table_txt = ""

        self.output = {}

        self.vendor_csv = []
        self.vendor_csv_transformed = []
        self.vendor_csv_prefs_spreadsheet = {}
        self.vendor_csv_prefs_repres = {}

        self.in_path = in_path
        self._prepare_in_path()
        self.more_settings = more_settings

        if os.path.exists(self.in_path):
            self.read_files()
            self.transform_data()

        #pprint.pprint(self.merged_list)
        # logging.debug('-> Sequencer Init')

    def _prepare_in_path(self):

        if self.in_path is None:
            self.in_path = ''
        # to detect if in_path is full path
        # or just path to directory with no end slash
        if os.path.isdir(self.in_path) \
                and not (self.in_path[-1] == os.sep or
                         self.in_path[-1] == os.altsep):
            # add end slash
            self.in_path += os.sep
        self.in_path.replace("\\", "/")

    def read_files(self):
        """
        Do all the slow stuff like finding files
        and reading metadata
        :return:
        """
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

        # get file sizes for merged list
        self.get_file_sizes()

        # sidecar files
        self.sidecar_files_find()

        # metadata
        self.get_metadata()

        # vendor ingest
        #self.vendor_csv_read()

    def transform_data(self):
        """
        Transform file info and prepare data for export
        :return:
        """

        # this sets static keywords like date and package name
        self.prepare_package_name()

        # make paths relative
        self.get_relative_paths(parse_file_name.parse(self.in_path))

        # also adds totals to static keywords
        self.filter_items_add_counters()

        # read from settings and compile
        self.prepare_regex()

        # for every found item prepare regex items
        self.fill_regexes()

        self.ftrack = {}
        self.ftrack_query()
        self.select_ftrack_note()
        self.ftrack_op_attrs()

        # sidecar files filter
        self.sidecar_files_filter()

        # vendor ingest
        self.vendor_csv_all()

        # prepare conversions
        self.prepare_converts()

        # parse table headers
        self.prepare_all_columns()

        # fill tables for export and display
        self.prepare_tables()

        self.select_ftrack_note()

        #self.checks = []
        self.run_checks()

    def get_metadata(self):

        self.output['status'] = "Getting meta data" \
                                " (get_metadata)"

        if self.merged_list and len(self.merged_list) > 0:
            for one_item in self.merged_list:
                if one_item['category'] in\
                        ['still', 'video', 'sequence', 'audio']:
                    one_item.update(
                        MetaData(one_item, self.settings).meta_data)

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
                with open(pth) as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        vendor_csv.append(dict(row))
            except IOError:
                self.log.error('Error opening vendor csv file ' + pth)
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

        try:
            vendor_csv_prefs_spreadsheet = json.loads(prefs_spread)
        except Exception:
            self.log.error('Error opening Vendor spreadsheet Json')
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

        try:
            vendor_csv_prefs_repre = json.loads(prefs_repre)
        except Exception:
            self.log.error('Error opening Vendor representation Json')
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

            for one_row in self.vendor_csv:

                row_keys = one_row.keys()
                trans_row = {}
                row_errors = []
                for k, v in self.vendor_csv_prefs_spreadsheet.items():
                    if k in row_keys:
                        # prefs column present in csv

                        if bool(re.match(v['validate'], one_row[k])):
                            # store valid value to renamed column
                            if one_row[k]:
                                # store if not empty
                                trans_row[v['column']] = one_row[k]
                            else:
                                # set to default if empty
                                trans_row[v['column']] = v['default']
                        else:
                            row_errors.append(
                                "Row {} has invalid column {} = {}".format(
                                    self.vendor_csv.index(one_row)+2, k, one_row[k]))
                    else:
                        # prefs column NOT present in csv
                        if bool(v['required']):
                            row_errors.append(
                                "Row {} has missing column {}".format(
                                    self.vendor_csv.index(one_row)+2, k))
                        else:
                            # not required, let's fill with default
                            trans_row[v['column']] = v['default']

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
                fc = csv.DictWriter(output_file,
                                    fieldnames=self.vendor_csv_transformed[
                                        0].keys(), )
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
                _skip_what = str(self.settings['vendor_csv_skip_what']['value']).split(" ")
            if self.settings['vendor_csv_skip']['value'] is not None:
                _skip = bool(self.settings['vendor_csv_skip']['value'])
                if (not _skip_what) or (not _skip_by):
                    _skip = False

            if self.merged_list is not None and len(
                    self.merged_list) > 0 and self.vendor_csv_transformed:

                for one_item in self.merged_list:
                    #package_key = p_key.format(**one_item)
                    package_key = p_key.format_map(Default(one_item))
                    for one_row in self.vendor_csv_transformed:
                        vendor_key = v_key.format_map(Default(one_row))
                        #vendor_key = v_key.format(**one_row)
                        if vendor_key == package_key:
                            # vendor csv row identification matches
                            # the package scan row identification
                            for k, v in one_row.items():
                                # add key from csv to the item
                                one_item[k] = v
                            one_row['merged_item'] = one_item

                # now ignore unassigned items
                if _ignore:
                    all_vendor_keys = self.vendor_csv_transformed[0].keys()
                    one_vendor_key = list(all_vendor_keys)[0]
                    for one_item in self.merged_list:
                        if one_item['hide_sub']:
                            one_item['vendor_ignore_sub'] = True
                        _tst = one_item.get(one_vendor_key, None)
                        if not _tst:
                            one_item['vendor_ignore_sub'] = True
                        else:
                            one_item['vendor_ignore_sub'] = False

                        if _skip:
                            try:
                                _skip_by = _skip_by.format(**one_item)
                                if _skip_by in _skip_what:
                                    one_item['vendor_ignore_sub'] = True
                            except Exception:
                                pass


                else:
                    for one_item in self.merged_list:
                        one_item['vendor_ignore_sub'] = False


    def vendor_csv_repre_checks(self):

        class Default(dict):
            def __missing__(self, key):
                return '{' + key + '}'

        if self.vendor_csv_transformed and self.vendor_csv_prefs_repre:
            # find line merges
            merge_key = self.vendor_csv_prefs_repre['merge_repres_by']
            merge_groups = {}
            for one_row in self.vendor_csv_transformed:

                # add merge key to the transformed csv
                # also keep track of grouped rows in merge_groups
                current = int(self.vendor_csv_transformed.index(one_row))
                print('current {}'.format(current))
                try:
                    one_row['vendor_Merge_by'] = merge_key.format(**one_row)
                    print('merge by {}'.format(one_row['vendor_Merge_by']))
                except Exception:
                    print('Vendor CSV failed to expand, line {}'.format(current+2))
                    continue

                if one_row['vendor_Merge_by']:
                    if one_row['vendor_Merge_by'] in merge_groups:
                        merge_groups[one_row['vendor_Merge_by']].append(current)
                        pprint.pprint(merge_groups)
                    else:
                        _empty = []
                        _empty.append(current)
                        merge_groups[one_row['vendor_Merge_by']] = _empty
                        pprint.pprint(merge_groups)

                    current_repre_name = one_row['vendor_Output']
                    current_line = self.vendor_csv_transformed.index(one_row)+2

                    if not any(d['name'] == current_repre_name for d in self.vendor_csv_prefs_repre['repres']):
                        # repre does not exist in repre json, skip
                        one_row['vendor_row_errors'].append("Output Type {} not found in preferences for line {}".format(current_repre_name, current_line))
                    else:
                        for one_repre in self.vendor_csv_prefs_repre['repres']:
                            if one_repre['name'] == current_repre_name:
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
                                            "File extension {} doesn't match the representation extensions {}".format(
                                                current_extension, ', '.join(
                                                    one_repre['extensions'])))
                                except Exception:
                                    pass

            all_tasks = self.vendor_csv_prefs_repre['task_intent_repres'].keys()
            for one_merge_key, merge_list in merge_groups.items():
                task = self.vendor_csv_transformed[merge_list[0]][
                    'vendor_Task']
                _always = []
                _optional = []
                intent = self.vendor_csv_transformed[merge_list[0]][
                    'vendor_Intent']
                _repres = []
                if task in all_tasks:
                    for one_task_set in self.vendor_csv_prefs_repre['task_intent_repres'][task]:
                        if intent in one_task_set['intents']:
                            _always = one_task_set['always']
                            _optional = one_task_set['optional']
                            # now check if all repres fit:
                            for one_index in merge_list:
                                _type = self.vendor_csv_transformed[one_index]['vendor_Output']
                                _repres.append(_type)
                                self.vendor_csv_transformed[one_index]['vendor_One_task_set'] = one_task_set
                                if not(_type in _always or _type in _optional):
                                    self.vendor_csv_transformed[one_index][
                                        'vendor_row_errors'].append("Output type {}, is not found in Json (task_intent_repres section).".format(_type))

                            duplicates = [number for number in _repres if _repres.count(number) > 1]
                            unique_duplicates = list(set(duplicates))
                            if len(unique_duplicates) > 0:
                                for one_index in merge_list:
                                    self.vendor_csv_transformed[one_index][
                                        'vendor_row_errors'].append(
                                        "Output type {} is present more than once in merged group {}".format(
                                            _type, self.vendor_csv_transformed[one_index]['vendor_Merge_by']))
                            break
                    if not _always:
                        # assuming all grouped have to match some intent
                        for one_index in merge_list:
                            self.vendor_csv_transformed[one_index]['vendor_row_errors'].append("For task {}, Intent {} was not found in Json (task_intent_repres section).".format(task, intent))
                else:
                    # assuming all grouped have the same task
                    for one_index in merge_list:
                        self.vendor_csv_transformed[one_index]['vendor_row_errors'].append("Task {} was not found in Json task_intent_repres section: {}.".format(task, all_tasks))


            try:
                for mrg_key in merge_groups.keys():


                    # make dicts where each length / tc / range serves as key,
                    # with value being a list of indexes for self.vendor_csv_transformed
                    # _ranges_no_slate = {'1001-1010': [1, 2, 3], '1001-1001': [4]}

                    _lengths = {}
                    _ranges_no_slate = {}
                    _tcs_no_slate = {}
                    for one_index in merge_groups[mrg_key]:
                        ln = self.vendor_csv_transformed[one_index]['vendor_frame_range']['length']

                        fs = int(self.vendor_csv_transformed[one_index]['vendor_frame_range']['frame_start'])
                        fe = int(self.vendor_csv_transformed[one_index]['vendor_frame_range']['frame_end'])
                        tc = str(self.vendor_csv_transformed[one_index]['vendor_frame_range']['timecode'])
                        fps = str(self.vendor_csv_transformed[one_index]['vendor_frame_range']['frame_rate'])
                        slate = bool(self.vendor_csv_transformed[one_index]['vendor_frame_range']['slate_present'])
                        if tc and fps:
                            tc_to_num = helpers.tc_to_frames(tc, fps, '1')
                            tc_to_num += 1
                            tc_no_slate = helpers.frames_to_tc(tc_to_num, int(fps), 1)
                            if slate:

                                tc = tc_no_slate
                        if slate:
                            fs += 1
                        frame_range = '{}-{}'.format(fs, fe)

                        if ln in _lengths.keys():
                            _lengths[ln].append(one_index)
                        else:
                            _lengths[ln] = [one_index]

                        if frame_range in _ranges_no_slate.keys():
                            _ranges_no_slate[frame_range].append(one_index)
                        else:
                            _ranges_no_slate[frame_range] = [one_index]

                        if tc in _tcs_no_slate.keys():
                            _tcs_no_slate[tc].append(one_index)
                        else:
                            _tcs_no_slate[tc] = [one_index]


                # add errors to all rows in merged group if one or more output is required but have error(s)
                for mrg_key in merge_groups.keys():
                    _failed_required_outputs = []
                    indexes = merge_groups[mrg_key]
                    for one_index in indexes:
                        if self.vendor_csv_transformed[one_index]['vendor_row_errors']:
                            if self.vendor_csv_transformed[one_index]['vendor_Output'] in self.vendor_csv_transformed[one_index]['vendor_One_task_set']['always']:
                                _failed_required_outputs.append(self.vendor_csv_transformed[one_index]['vendor_Output'])

                    if len(_failed_required_outputs) > 0:
                        _err = "Required outputs: {} ;have error(s)".format(", ".join(_failed_required_outputs))
                        for one_index in merge_groups[mrg_key]:
                            self.vendor_csv_transformed[one_index]['vendor_row_errors'].append(_err)

                # convert errors to string
                for one_row in self.vendor_csv_transformed:
                    _e = ', '.join(one_row['vendor_row_errors'])
                    one_row['vendor_row_errors'] = _e
            except Exception:
                pass

    def get_relative_paths(self, parsed_in_path):

        self.output['status'] = "Getting relative paths" \
                                " (get_relative_paths)"

        root_dir = parsed_in_path['path']
        root_dir_length = len(root_dir)
        if self.merged_list and len(self.merged_list) > 0:
            for one_item in self.merged_list:
                one_item['relative_path'] = one_item['path'][root_dir_length:]

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
            if self.settings['check_sequence_size_consistency']['value']:
                _consistency = bool(self.settings['check_sequence_size_consistency']['value'])
            if self.settings['check_sequence_holes']['value']:
                _holes = bool(self.settings['check_sequence_holes']['value'])
            if self.settings['prefs_size_scan']['value']:
                _sizes = bool(self.settings['prefs_size_scan']['value'])
            if self.settings['prefs_size_ignore_first']['value']:
                _ignore_first = int(self.settings['prefs_size_ignore_first']['value'])
            if self.settings['prefs_size_neighborhood']['value']:
                _neighbrs = int(self.settings['prefs_size_neighborhood']['value'])
            if self.settings['prefs_size_threshold']['value']:
                _tresh = float(int(self.settings['prefs_size_threshold']['value']))*0.01

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
                        except:
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

                        missing = len(one_item['missing_numbers'])
                        if missing > 0:
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
                                start = start + _ignore_first

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
                                    _frame = start + _ignore_first + cnt - _neighbrs - 1
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
                            except:
                                # TODO fix for very short sequences (ln=2, ifnofe frst 1 = fail)
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
                    except:
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
        my_dir = os.path.dirname(in_path)
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
                patt = prs["name"] + '.' + prs["extension"]

                if endFrame == -1:
                    _category = 'video'
                else:
                    # split video like long r3d
                    _category = 'video'

                onedict = {'path': temp_result[onekey][1], 'missing_numbers': [], 'sub_ranges': subRanges,
                           'printf_pattern': patt,
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
                    except:
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

                if prs["extension"] in ext_grp['audio']:
                    _cat = 'audio'
                elif prs["extension"] in ext_grp['graphics']:
                    _cat = 'graphics'
                elif prs["extension"] in ext_grp['office']:
                    _cat = 'office'
                elif prs["extension"] in ext_grp['other']:
                    _cat = 'other'
                elif prs["extension"] in ext_grp['sequence']:
                    _cat = 'sequence'
                elif prs["extension"] in ext_grp['multiframe']:
                    _cat = 'multiframe'
                elif prs["extension"] in ext_grp['metadata']:
                    _cat = 'metadata'
                else:
                    _cat = 'unknown'

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
                    except:
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

                    patt = parse_file_name.printf_pattern(temp_result[one_key][1])
                    prs = parse_file_name.parse(temp_result[one_key][1])

                    # now we have all data gathered, let's format it nicely for output
                    one_record = {'path': temp_result[one_key][1], 'missing_numbers': temp_result[one_key][2],
                                    'sub_ranges': temp_result[one_key][3], 'printf_pattern': patt,
                                    'master_start_number': frames[0], 'master_end_number': frames[-1],
                                    'category': 'sequence'}
                    prs['path_prs'] = prs.pop('path')  # path in one_dict shadows path from parse
                    one_record.update(prs)
                    numbered_parts = {}
                    for one_dir in range(-9, 0):
                        try:
                            numbered_parts['part' + str(-1 * one_dir)] = prs['parts'][one_dir]
                        except:
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
                            one_record['path'] = sub_range_first_frame # may not be needed
                            one_record['start_number'] = one_subrange['start']
                            one_record['end_number'] = one_subrange['end']
                            one_record['trim_in'] = one_subrange['start'] - frames[0]
                            one_record['trim_out'] = frames[-1] - one_subrange['end']
                            output_list.append(fix_seq(one_record, prs))
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
        counter_start = 1
        counter_step = 1
        counter_zeroes = 3
        try:
            if self.settings:
                if self.settings['sub_exclude']['value']:
                    sub_exclude_list = self.settings['sub_exclude']['value'].split()
                if self.settings['sub_include']['value']:
                    sub_include_list = self.settings['sub_include']['value'].split()
                if self.settings['log_exclude']['value']:
                    log_exclude_list = self.settings['log_exclude']['value'].split()
                if self.settings['log_include']['value']:
                    log_include_list = self.settings['log_include']['value'].split()
                if self.settings['txt_exclude']['value']:
                    txt_exclude_list = self.settings['txt_exclude']['value'].split()
                if self.settings['txt_include']['value']:
                    txt_include_list = self.settings['txt_include']['value'].split()

                if self.settings['prefs_counter_start']['value']:
                    counter_start = int(self.settings['prefs_counter_start']['value'])
                if self.settings['prefs_counter_step']['value']:
                    counter_step = int(self.settings['prefs_counter_step']['value'])
                if self.settings['prefs_counter_zeroes']['value']:
                    counter_zeroes = int(self.settings['prefs_counter_zeroes']['value'])
        except:
            pass

        if self.merged_list and len(self.merged_list) > 0:
            cnt_sub = counter_start
            cnt_log = counter_start
            cnt_txt = counter_start
            total_sub = 0
            total_log = 0
            total_txt = 0
            files_sub = 0
            files_log = 0
            files_txt = 0
            total_size_sub = 0
            total_size_log = 0
            total_size_txt = 0


            for one_item in self.merged_list:
                one_item.update({"hide_sub": False})
                one_item.update({"hide_log": False})
                one_item.update({"hide_txt": False})
                one_item.update({"hide_sub": False})
                one_item.update({"hide_log": False})
                one_item.update({"hide_txt": False})
                one_item.update({"vendor_ignore_sub": False})

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

                # add counter to the items that are not hidden
                _frames = int(one_item.get('meta_duration_frames', 0))
                if not one_item['hide_sub']:
                    one_item.update({"cnt_sub": str(cnt_sub).zfill(counter_zeroes)})
                    cnt_sub += counter_step
                    total_sub += 1
                    if one_item['category'] == 'sequence':
                        files_sub += _frames
                    else:
                        files_sub += 1
                    _bytes = one_item.get('size_bytes', 0)
                    total_size_sub += _bytes

                if not one_item['hide_log']:
                    one_item.update({"cnt_log": str(cnt_log).zfill(counter_zeroes)})
                    cnt_log += counter_step
                    total_log += 1
                    if one_item['category'] == 'sequence':
                        files_log += _frames
                    else:
                        files_log += 1
                    _bytes = one_item.get('size_bytes', 0)
                    total_size_log += _bytes

                if not one_item['hide_txt']:
                    one_item.update({"cnt_txt": str(cnt_txt).zfill(counter_zeroes)})
                    cnt_txt += counter_step
                    total_txt += 1
                    if one_item['category'] == 'sequence':
                        files_txt += _frames
                    else:
                        files_txt += 1
                    _bytes = one_item.get('size_bytes', 0)
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
            indexes = [str(x).zfill(2) for x in range(1, 33)]
            for one in indexes:
                name_key = "parse_name_" + one
                key = self.settings[name_key]["value"]
                name_pat = "parse_pattern_" + one
                pat = self.settings[name_pat]["value"]
                name_filter = "parse_filter_" + one
                fltr = self.settings[name_filter]["value"]
                try:
                    pat_compiled = re.compile(pat)
                    pat_valid = True
                except re.error:
                    pat_compiled = None
                    pat_valid = False
                name_rep = "parse_repl_" + one
                rep = self.settings[name_rep]["value"]
                name_src = "parse_source_" + one
                src = self.settings[name_src]["value"]

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
                for k, one_regex in self.regexes.items():
                    do_filter = False
                    if one_regex['filter'] != '':
                        if not (one_regex['filter'] in one_item['path']):
                            do_filter = True
                    if not do_filter:
                        # expand keywords in source
                        try:
                            expanded = one_regex["source"].format(**one_item)
                            #
                        except KeyError:
                            expanded = None
                        if expanded and expanded != '':
                            # expand static keywords
                            try:
                                expanded = expanded.format(**self.static_keywords)
                                #expanded = expanded.format_map(Default(self.static_keywords))
                            except KeyError:
                                pass
                            if one_regex["repl"] and one_regex["repl"] != "":
                                # it is a replace
                                if one_regex["repl"].startswith("lambda "):
                                    #LAMBDA!
                                    try:
                                        _eval = eval(str(one_regex["repl"]))
                                    except:
                                        _eval = one_regex["repl"]
                                    try:
                                        result = re.sub(one_regex["compiled"], _eval, expanded)
                                    except:
                                        result = ""
                                else:
                                    try:
                                        result = re.sub(one_regex["compiled"], one_regex["repl"], expanded)
                                    except:
                                        result = ""
                            else:
                                m = one_regex["compiled"].search(expanded)
                                if m:
                                    # if user made a group, assign the group, otherwise use whole found string
                                    try:
                                        capture = m.group(1)
                                        result = capture
                                    except:
                                        capture = None
                                        #result = m.group(0)
                                        result = ""
                                else:
                                    # shot name exists but doesn't match the regex, so set shot name to empty string
                                    result = ""
                        else:
                            result = ""
                        one_item.update({one_regex["key"]: result})

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

        if self.settings['name_template']['value'] is not None:
            _template = self.settings['name_template']['value']
        if self.settings['name_date_regex']['value'] is not None:
            _date_regex = self.settings['name_date_regex']['value']
            _date_compiled = re.compile(_date_regex)
        if self.settings['name_version_regex']['value'] is not None:
            _version_regex = self.settings[
                                     'name_version_regex']['value']
            _version_compiled = re.compile(_version_regex)
        if self.settings['package_folder']['value'] is not None:
            _pkg_folder = self.settings['package_folder']['value']
        if self.settings['name_version_per_date']['value'] is not None:
            _per_date = bool(self.settings[
                                 'name_version_per_date']['value'])
        if self.settings['name_version_zeroes']['value'] is not None:
            _ver_zeroes = self.settings[
                                  'name_version_zeroes']['value']
        if self.settings['name_version_use_letters']['value'] is not None:
            _ver_letters = bool(self.settings[
                'name_version_use_letters']['value'])
        if self.settings['name_version_letters_uppercase']['value'] is not None:
            _ver_upper = bool(self.settings[
                'name_version_letters_uppercase']['value'])

        # get current date by applying regex to expanded template
        try:
            _temp_expanded = _template.format(**date_keys)
            #_temp_expanded = _template.format_map(Default(date_keys))
        except KeyError:
            self.log.error("Package name template failed")

        if _date_compiled:

            d = _date_compiled.search(_temp_expanded)
            if d:
                try:
                    current_date = d.group(1)
                except :
                    self.log.error("Package date failed")

        # make sure path exists, it is a directory and has no trailing slash
        if os.path.exists(_pkg_folder):
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
            for filename in os.listdir(one_up):
                if os.path.isdir(os.path.join(one_up, filename)):
                    if filename != name_from_folder:
                        d = _date_compiled.search(filename)
                        dd = ''
                        if d:
                            try:
                                dd = d.group(1)
                            except:
                                dd = ''
                        v = _version_compiled.search(filename)
                        vv = ''
                        if v:
                            try:
                                vv = v.group(1)
                            except:
                                vv = ''
                        dir_list.append({
                            'folder': filename,
                            'date': dd,
                            'version': vv
                        })

            if _per_date:
                # each date has separate version chain
                _today_subs = []
                for one_dir in dir_list:
                    if one_dir['date'] == current_date:
                        if one_dir['version'] and one_dir['version'] != '':
                            _today_subs.append(one_dir)
                if _today_subs:
                    last_dir = sorted(_today_subs, key=lambda i: i['version'])[-1]
                else:
                    last_dir = None
            else:
                # sort by version, take highest
                try:
                    last_dir = sorted(dir_list, key=lambda i: i['version'])[-1]
                except:
                    last_dir = None
            if last_dir:
                last_version = last_dir['version']
            else:
                last_version = None

            if _ver_letters:
                if last_version is None:
                    last_version = 'Z'
                try:
                    _test = last_version.upper()
                except:
                    last_version = 'Z'
                next_version = chr(
                    (ord(last_version.upper()) + 1 - 65) % 26 + 65)
                if not _ver_upper:
                    next_version = next_version.lower()
            else:
                if last_version is None:
                    last_version = 0
                try:
                    _test = int(last_version)
                except ValueError:
                    last_version = 0
                # version is number
                next_version = str(int(last_version) + 1).zfill(_ver_zeroes)

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
            try:
                _pkg_new_name = _template.format(**date_keys)
                #_pkg_new_name = _template.format_map(Default(date_keys))
            except:
                pass

            date_keys.update({
                'package_name': _pkg_new_name,
            })

        # make public
        self.static_keywords = date_keys
        # add to outputs
        self.output.update(date_keys)

    def prepare_columns(self, gui_columns):
        """
        Gets columns definition as a string like:
        Thumbnail={thumb_path}, Thumbnail={created_thumb_path},
        Shot={shot_name}, CheckShot={check_shot_name}, ...
        Returns two lists: column_titles and column_expressions
        """

        column_titles = []
        column_expressions = []
        gui_columns.replace("\n", ",")

        NM_RE = re.compile(r"\s*(?P<column_title>.*)\s*=\s*(?P<column_expression>.*)\s*")
        split_list = gui_columns.split(",")
        column_count = 0
        columns = []

        for one_column in split_list:
            m = NM_RE.search(one_column)
            if m:
                title = m.group("column_title")
                expression = m.group("column_expression")
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

        self.column_titles_sub, self.column_expressions_sub =\
            self.prepare_columns(_sub)
        self.column_titles_log, self.column_expressions_log =\
            self.prepare_columns(_log)
        self.column_titles_txt, self.column_expressions_txt =\
            self.prepare_columns(_txt)

    def prepare_tables(self):

        class Default(dict):
            def __missing__(self, key):
                return '{' + key + '}'

        def row_merge(rows, collapse, separator, sort, order):
            columns = len(rows[0]) - 1

            # vertically merge rows
            merged = []
            for one in rows[0]:
                merged.append([])
            for idx, one_row in enumerate(rows):
                for idy, one_column in enumerate(one_row):
                    if isinstance(one_column, dict):
                        pass
                        # skip last item that contains whole data record dict
                    else:
                        merged[idy].append(one_column)

            merged_c = []
            for one in merged:
                if collapse:
                    kill_dupes = (list(set(one)))
                else:
                    kill_dupes = one
                # skip none
                kill_dupes = [x for x in kill_dupes if x is not None]
                # skip empty strings
                kill_dupes = [x for x in kill_dupes if x is not ""]
                merged_c.append(kill_dupes)

            merged_str = []
            for one in merged_c:
                merged_str.append(separator.join(map(str, one)))

            return merged_str

        self.table_sub = []
        self.table_log = []
        self.table_txt = ""
        self.table_side = []
        self.columns_side = ['match', 'destination', 'source']
        body_txt = ""
        txt_sep = " "

        if self.settings:
            if self.settings['text_sep_tab']['value'] is not None:
                if self.settings['text_sep_tab']['value']:
                    txt_sep = "\t"
            if self.settings['text_add_titles']['value'] is not None:
                do_txt_titles = bool(self.settings['text_add_titles']['value'])
            if self.settings['text_header']['value'] is not None:
                txt_header = self.settings['text_header']['value']
            if self.settings['text_footer']['value'] is not None:
                txt_footer = self.settings['text_footer']['value']

            side_sub_only = False
            if self.settings['side_sub_only']['value'] is not None:
                side_sub_only = bool(self.settings['side_sub_only']['value'])
            side_log_only = False
            if self.settings['side_log_only']['value'] is not None:
                side_log_only = bool(self.settings['side_log_only']['value'])

            if self.settings['prefs_merge_chbx']['value'] is not None:
                _merge_chbx = bool(self.settings['prefs_merge_chbx']['value'])
            if self.settings['prefs_merge_by']['value']:
                _merge_by = str(
                    self.settings['prefs_merge_by']['value']).strip('{}')
            if self.settings['prefs_merge_collapse']['value'] is not None:
                _merge_collapse = bool(
                    self.settings['prefs_merge_collapse']['value'])
            if self.settings['prefs_merge_sep']['value']:
                _merge_sep = str(self.settings['prefs_merge_sep']['value'])
            if self.settings['prefs_merge_sort']['value']:
                _merge_sort = str(self.settings['prefs_merge_sort']['value'])
            if self.settings['prefs_merge_order']['value']:
                _merge_order = str(self.settings['prefs_merge_order']['value'])
            if self.settings['prefs_merge_hide']['value'] is not None:
                _merge_hide = bool(self.settings['prefs_merge_hide']['value'])
        else:
            return

        sub_merges = {}
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
                            formatted = one_expression.format(**one_item)
                            #formatted = one_expression.format_map(Default(one_item))
                            one_row_sub.append(formatted)
                        except KeyError:
                            # can't parse expression, put it in original form
                            #one_row_sub.append(str(one_expression))
                            one_row_sub.append("")
                    #  add item to the end of the row, so we can later
                    #  on easily reference all the data for the row
                    one_row_sub.append(one_item)

                    if _merge_chbx:
                        key = one_item.get(_merge_by, None)
                        if not key:
                            # add None as last row item -> flag as non-merge-able
                            one_row_sub.append(None)
                        else:
                            # add key as last row item
                            one_row_sub.append(key)
                            cnt = sub_merges.get(key, None)
                            if cnt:
                                sub_merges[key] += 1
                            else:
                                sub_merges[key] = 1

                    # add to table
                    self.table_sub.append(one_row_sub)
                    one_item['_row'] = one_row_sub

                if not one_item['hide_log']:
                    one_row_log = []
                    for one_expression in self.column_expressions_log:
                        try:
                            formatted = one_expression.format(**one_item)
                            #formatted = one_expression.format_map(Default(one_item))
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
                            formatted = one_expression.format(**one_item)
                            #formatted = one_expression.format_map(Default(one_item))
                            one_row_txt.append(formatted)
                        except KeyError:
                            # can't parse expression, put it in original form
                            #one_row_txt.append(str(one_expression))
                            one_row_txt.append("")
                    whole_row = str(txt_sep.join(one_row_txt)) + "\n"
                    body_txt += whole_row

                sides = one_item.get('sidecars', None)
                if sides:
                    do_side = False
                    if side_sub_only and (not one_item['hide_sub']) and (not one_item['vendor_ignore_sub']):
                        do_side = True
                    elif side_log_only and not one_item['hide_log']:
                        do_side = True
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

            # merging
            if _merge_chbx:
                _rows_merged = []
                for one_merge_key, count in sub_merges.items():
                    if count > 1:
                        _all_merged = []
                        for one_row in self.table_sub:
                            merge_key = one_row[-1]
                            if merge_key and merge_key == one_merge_key:
                                _all_merged.append(one_row[:-1])
                                if not _merge_hide:
                                    one_row[-1] = None
                        if len(_all_merged) > 0:
                            # there is something to merge
                            merged_row = row_merge(rows=_all_merged,
                                                   collapse=_merge_collapse,
                                                   separator=_merge_sep,
                                                   sort=_merge_sort,
                                                   order=_merge_order)
                            _rows_merged.append(merged_row)
                for one_row in self.table_sub:
                    merge_key = one_row[-1]
                    if not merge_key:
                        _rows_merged.append(one_row[:-1])
                self.table_sub = _rows_merged

        try:
            _header = txt_header.format(**self.static_keywords)
            #_header = txt_header.format_map(Default(self.static_keywords))
        except KeyError:
            _header = txt_header
        if do_txt_titles:
            _titles = '\n' + str(txt_sep.join(self.column_titles_txt)) + '\n'
        else:
            _titles = ""
        try:
            _footer = txt_footer.format(**self.static_keywords)
            #_footer = txt_footer.format_map(Default(self.static_keywords))
        except KeyError:
            _footer = txt_footer
        self.table_txt = _header + '\n' + _titles + body_txt + '\n' + _footer

    def export_all(self, column_width_sub=None, column_width_log=None):

        if self.settings and bool(self.settings['side_copywithgo']['value']):
            self.sidecar_files_copy()

        if self.settings and bool(self.settings['thumbs_make_on_go']['value']):
            self.prepare_converts()
            self.run_converts()

        if self.settings and self.static_keywords:
            one_above = str(self.static_keywords['package_name_root']).replace('\\', '/') + '/'
            export_root = one_above + self.static_keywords['package_name_from_folder'] + '/'
            # Submission
            s_pth_above = bool(self.settings['export_sub_above']['value'])
            s_pth_custom = bool(self.settings['export_sub_custom']['value'])
            s_custom = str(self.settings['export_sub_custom_path']['value'])
            s_suffix = str(self.settings['export_sub_custom_suffix']['value'])
            s_do_excel = bool(self.settings['export_sub_excel']['value'])
            s_do_csv = bool(self.settings['export_sub_csv']['value'])
            s_export_root = export_root
            if s_pth_custom:
                s_export_root = s_custom.replace('\\', '/') + '/'
            elif s_pth_above:
                s_export_root = one_above
            s_export_root += self.static_keywords['package_name']
            if s_suffix:
                s_export_root += s_suffix

            self.export_spreadsheet(s_export_root, s_do_excel, s_do_csv,
                                    self.table_sub, self.column_titles_sub,
                                    column_width_sub)

            # Drive Log
            d_pth_above = bool(self.settings['export_log_above']['value'])
            d_pth_custom = bool(self.settings['export_log_custom']['value'])
            d_custom = str(self.settings['export_log_custom_path']['value'])
            d_suffix = str(self.settings['export_log_custom_suffix']['value'])
            d_do_excel = bool(self.settings['export_log_excel']['value'])
            d_do_csv = bool(self.settings['export_log_csv']['value'])
            d_export_root = export_root
            if d_pth_custom:
                d_export_root = d_custom.replace('\\', '/') + '/'
            elif d_pth_above:
                d_export_root = one_above
            d_export_root += self.static_keywords['package_name']
            if d_suffix:
                d_export_root += d_suffix
            else:
                d_export_root += '_log'

            self.export_spreadsheet(d_export_root, d_do_excel, d_do_csv,
                                    self.table_log, self.column_titles_log,
                                    column_width_log)

            # Text
            t_pth_above = bool(self.settings['text_above']['value'])
            t_pth_custom = bool(self.settings['text_custom']['value'])
            t_custom = str(self.settings['text_custom_path']['value'])
            t_do_txt = bool(self.settings['text_txt']['value'])
            t_export_root = export_root
            if t_pth_custom:
                t_export_root = t_custom.replace('\\', '/') + '/'
            elif t_pth_above:
                t_export_root = one_above
            t_export_root += self.static_keywords['package_name'] + '.txt'

            if self.table_txt is not None and t_do_txt:
                with open(t_export_root, 'w') as f:
                    f.write(self.table_txt)

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
            os.rename(pth + src, pth + dst)
        except:
            logging.error('Renaming {} {} -> {} failed'.format(pth, src, dst))

    def export_spreadsheet(self, export_root, do_excel, do_csv,
                           table, titles, column_widths=None):

        _excel = 0.15
        if table and titles:
            # Excel
            if do_excel:
                workbook = xlsxwriter.Workbook(export_root + '.xlsx')
                worksheet = workbook.add_worksheet()
                cnt = -1
                for column_number, one_column in enumerate(
                        titles):
                    cnt += 1
                    if column_widths:
                        worksheet.set_column(
                            column_number,
                            column_number,
                            column_widths[cnt] * _excel
                        )
                    else:
                        worksheet.set_column(column_number, column_number)
                    worksheet.write(0, column_number, one_column)
                for row, line in enumerate(table):
                    for column_number, one_column in enumerate(
                            titles):
                        worksheet.write(row + 1, column_number,
                                        line[column_number])
                workbook.close()
            # CSV
            if do_csv:
                with open(export_root + '.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(titles)
                    for row, line in enumerate(table):
                        writer.writerow(line[:len(titles)])

    def sidecar_files_copy(self):

        self.output['status'] = "Copying sidecar files."

        if self.table_side is not None and len(self.table_side) > 0:
            for one_item in self.table_side:
                _src = one_item[2]
                _dst = one_item[1]
                if _src and _dst:
                    if not os.path.exists(os.path.dirname(_dst)):
                        os.makedirs(os.path.dirname(_dst))
                    print("Sidecar file copy {} -> {}".format(_src, _dst))
                    shutil.copy(_src, _dst)

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

        do_sidecar = False
        if self.sidecars is not None:
            if len(self.sidecars) > 0:
                do_sidecar = True
        if not do_sidecar:
            return

        # clear the sidecar files
        for item in self.merged_list:
            sides = item.get('sidecars', None)
            if sides is not None:
                item['sides'] = []

        # Get regexes from UI
        side_regexes = {}
        indexes = [str(x) for x in range(1, 6)]
        for one in indexes:
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
            one_file = one_item
            _s = one_item.split('/')
            if not _s:
                break
            else:
                one_file = _s[-1]
                one_path = '/'.join(_s[:-1])

            if one_file:
                _e = one_item.split('.')
                if not _e:
                    break
                else:
                    one_file_noext = '.'.join(_e[:-1])
                    one_file_ext = _e[-1]

            for k, one_regex in side_regexes.items():
                result = None
                if one_regex['repl'] and one_regex['repl'] != '':
                    # it is a replace
                    if one_regex['repl'].startswith("lambda "):
                        # LAMBDA!
                        result = re.sub(one_regex['compiled'],
                                        eval(str(one_regex['repl'])),
                                        one_file)
                    else:
                        result = re.sub(one_regex['compiled'],
                                        one_regex['repl'], one_file)
                else:
                    m = one_regex['compiled'].search(one_file)
                    if m:
                        # if user made a group, assign the group,
                        # otherwise use whole found string
                        try:
                            result = m.group(1)
                        except:
                            result = None
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
                        expanded = None
                        try:
                            expanded = one_regex['match'].format_map(
                                Default(item))
                            expanded = expanded.format_map(
                                Default(self.static_keywords))
                            dest = None
                            dest = None
                            try:
                                dest = str(one_regex['destination'])
                                try:
                                    dest = dest.format_map(
                                        Default(sidecar_keywords))
                                except:
                                    pass
                                try:
                                    dest = dest.format_map(
                                        Default(self.static_keywords))
                                except:
                                    pass
                                try:
                                    dest = dest.format_map(Default(item))
                                except:
                                    pass
                                try:
                                    dest = dest.replace('\\', '/')
                                except:
                                    pass
                            except:
                                pass
                            if expanded is not None:
                                if expanded == result:
                                    # sidecar file matches the package file
                                    one_side = {
                                        'result': result,
                                        'file': one_item,
                                        'dest': dest
                                    }
                                    try:
                                        item['sidecars'].append(one_side)
                                    except:
                                        item['sidecars'] = [one_side]
                        except KeyError:
                            pass

    def ftrack_query(self):
        self.ftrack_clean_notes()
        do_ftrack = False
        if self.settings:
            if self.settings['ftrack_use']['value'] is not None:
                do_ftrack = bool(self.settings['ftrack_use']['value'])
        if do_ftrack:
            self.get_ftrack_session()
            if self.ftrack['session'] is not None:
                self.get_ftrack_notes()

    def ftrack_clean_notes(self):
        for item in self.merged_list:
            item['ftrack_notes'] = []
            item['ftrack_note'] = ''

    def ftrack_clean_note(self):
        for item in self.merged_list:
            item['ftrack_note'] = ''

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
            self.ftrack['do_ftrack'] = bool(
                self.settings['ftrack_use']['value'])
            self.ftrack['include'] = str(
                self.settings['ftrack_include']['value'])
            self.ftrack['project'] = str(
                self.settings['ftrack_project']['value'])
            self.ftrack['shot'] = str(
                self.settings['ftrack_shot']['value'])
            self.ftrack['task'] = str(
                self.settings['ftrack_task']['value'])
            self.ftrack['do_label'] = bool(
                self.settings['ftrack_label_use']['value'])
            self.ftrack['label'] = str(
                self.settings['ftrack_label']['value'])
            self.ftrack['do_version'] = bool(
                self.settings['ftrack_version_use']['value'])
            self.ftrack['version'] = str(
                self.settings['ftrack_version']['value'])
            self.ftrack['note_pattern'] = str(
                self.settings['ftrack_note_pattern']['value'])
            self.ftrack['note_repl'] = str(
                self.settings['ftrack_note_repl']['value'])

            if self.ftrack['include'] != None:
                self.ftrack['include'] = self.ftrack['include'].split()
            else:
                self.ftrack['include'] = []

            self.ftrack['session'] = None
            self.ftrack['project_id'] = None
            self.ftrack['label_obj'] = None
            if self.ftrack['do_ftrack']:
                self.ftrack['url'] = self.more_settings.get('server_url', '')
                self.ftrack['key'] = self.more_settings.get('api_key', '')
                self.ftrack['user'] = self.more_settings.get('api_user', '')
                self.ftrack['session'] = ftrack_api.Session(
                    server_url=self.ftrack['url'],
                    api_key=self.ftrack['key'],
                    api_user=self.ftrack['user']
                )

                if self.ftrack['session'] is not None:
                    try:
                        all_projects = self.ftrack['session'].query(
                            'Project where status is "Active"').all()
                        for p in all_projects:
                            if p["full_name"] == self.ftrack['project']:
                                self.ftrack['project_id'] = p["id"]
                    except ftrack_api.exception.NoResultFoundError:
                        print('FTRACK failed')
                        pass

                if self.ftrack['label'] != '' and self.ftrack['do_label']:
                    try:
                        self.ftrack['label_obj'] = self.ftrack['session']\
                            .query('NoteLabel where name is "{}"'.format(
                            self.ftrack['label'])).first()
                    except:
                        pass

    def get_ftrack_notes(self):
        """
        For every merged list item it tries to get Ftrack note
        :return:
        item['ftrack_notes']
        """

        if not self.settings:
            return

        _do_notes = False
        if self.settings['ftrack_do_notes']['value'] is not None:
            _do_notes = bool(self.settings['ftrack_do_notes']['value'])
        if not _do_notes:
            return

        if self.ftrack is None:
            print("Ftrack cancelled (1)")
            return
        if self.ftrack['project_id'] is None or self.ftrack['shot'] == '' or self.ftrack['task'] == '':
            print("Ftrack cancelled (2)")
            return
        if self.merged_list is None:
            print("Ftrack cancelled (3)")
            return

        do_filter = False
        if len(self.ftrack['include']) > 0:
            do_filter = True
        for item in self.merged_list:
            if do_filter:
                e = item.get('extension', '')
                if e in self.ftrack['include']:
                    self.assign_ftrack_notes(item)
            else:
                self.assign_ftrack_notes(item)

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

    def ftrack_op_attrs(self):
        """

        :return:
        add to item['ftrack_notes'] all notes on task or version
        """
        class Default(dict):
            def __missing__(self, key):
                return '{' + key + '}'

        if not self.settings:
            return
        _do_op = False
        if self.settings['ftrack_do_op']['value'] is not None:
            _do_op = bool(self.settings['ftrack_do_op']['value'])
        if not _do_op:
            return

        if self.ftrack is None:
            print("Ftrack cancelled (1)")
            return
        if self.ftrack['project_id'] is None or self.ftrack['shot'] == '' or self.ftrack['task'] == '':
            print("Ftrack cancelled (2)")
            return
        if self.merged_list is None:
            print("Ftrack cancelled (3)")
            return

        for item in self.merged_list:
            self.assign_ftrack_notes(item)

            current_shot = self.ftrack.get('shot', '').format_map(Default(item))
            current_task = self.ftrack.get('task', '').format_map(Default(item))

            f_shot = self.ftrack['session'].query(
                'Shot where name is {}'
                ' and project.full_name is {}'.format(
                    current_shot, self.ftrack['project'])).first()

            f_task = self.ftrack['session'].query(
                'Task where name is {} and parent.name is {}'
                ' and project.full_name is {}'.format(
                    current_task, current_shot, self.ftrack['project'])).first()

            item['ftrack_task_exists'] = "0"
            if f_task:
                item['ftrack_task_exists'] = "1"
            item['ftrack_shot_exists'] = "0"
            if f_shot:
                item['ftrack_shot_exists'] = "1"
                _fs = int(float(self.ftrack_get_hierarchical_attribute(self.ftrack['session'], f_shot, "framestart")))
                _fe = int(float(self.ftrack_get_hierarchical_attribute(self.ftrack['session'], f_shot, "frameend")))
                _hs = int(float(self.ftrack_get_hierarchical_attribute(self.ftrack['session'], f_shot, "handleStart")))
                _he = int(float(self.ftrack_get_hierarchical_attribute(self.ftrack['session'], f_shot, "handleEnd")))
                item['ftrack_op_frame_start'] = str(_fs)
                item['ftrack_op_handle_start'] = str(_hs)
                item['ftrack_op_start'] = str(_fs - _hs)
                item['ftrack_op_start_slate'] = str(_fs - _hs - 1)
                item['ftrack_op_frame_end'] = str(_fe)
                item['ftrack_op_handle_end'] = str(_he)
                item['ftrack_op_end'] = str(_fe + _he)
                item['ftrack_op_range'] = "{}-{}".format(_fs - _hs - 1, _fe + _he)
                item['ftrack_op_range_slate'] = "{}-{}".format(_fs - _hs, _fe + _he)
            else:
                item['ftrack_op_frame_start'] = ""
                item['ftrack_op_frame_end'] = ""
                item['ftrack_op_handle_start'] = ""
                item['ftrack_op_handle_end'] = ""
                item['ftrack_op_range'] = ""
                item['ftrack_op_range_slate'] = ""
                item['ftrack_op_start'] = ""
                item['ftrack_op_start_slate'] = ""
                item['ftrack_op_end'] = ""


    def assign_ftrack_notes(self, item):
        """
        for item in merged_list, query all ftrack notes
        that fit project, shot, task, optional label, optional version
        :param item:
        :return:
        add to item['ftrack_notes'] all notes on task or version
        """

        class Default(dict):
            def __missing__(self, key):
                return '{' + key + '}'

        all_notes = []
        current_shot = self.ftrack.get('shot', '').format_map(Default(item))
        current_task = self.ftrack.get('task', '').format_map(Default(item))
        current_version = self.ftrack.get('version', '').format_map(Default(item))

        version_gui = 0
        if self.ftrack['do_version']:
            try:
                version_gui = int(current_version)
            except:
                return ''

        if current_shot == '' or current_task == '' or self.ftrack['project'] == '':
            return ''

        # get task from Ftrack
        try:
            f_task = self.ftrack['session'].query(
                'Task where name is {} and parent.name is {}'
                ' and project.full_name is {}'.format(
                    current_task, current_shot, self.ftrack['project'])).first()
        except:
            return ''
        if f_task is None:
            return ''

        # get sorted versions on the task
        if self.ftrack['do_version']:
            try:
                assets = self.ftrack['session'].query(
                    'select asset.name, version from AssetVersion '
                    'where task_id is "{}" and asset.name is_not '
                    'none order by version desc'.format(
                        f_task['id'])).all()
            except:
                assets = None
            if assets is None:
                return ''
            for one_asset in assets:
                try:
                    version_asset = int(one_asset['version'])
                except:
                    version_asset = 0
                if version_gui == version_asset:
                    for one_note in one_asset['notes']:
                        content = str(one_note['content'])
                        _save = False
                        if self.ftrack['do_label']:
                            l = one_note['note_label_links']
                            if self.ftrack['label_obj']['id'] in l:
                                _save = True
                        else:
                            _save = True
                        if _save:
                            all_notes.append(content)
        else:
            for one_note in f_task['notes']:
                _save = False
                content = str(one_note['content'])
                if self.ftrack['do_label']:
                    l = one_note['note_label_links']
                    if self.ftrack['label_obj']['id'] in l:
                        _save = True
                else:
                    _save = True
                if _save:
                    all_notes.append(content)

        item['ftrack_notes'] = all_notes

    def select_ftrack_note(self):
        """
        from item['ftrack_notes'] queried from ftrack by assign_ftrack_notes
        filter the first note that fits note regex and optionally repl
        :return:
        """

        class Default(dict):
            def __missing__(self, key):
                return '{' + key + '}'

        self.ftrack_clean_note()
        self.ftrack['note_pattern'] = str(
            self.settings['ftrack_note_pattern']['value'])
        self.ftrack['note_repl'] = str(
            self.settings['ftrack_note_repl']['value'])
        for item in self.merged_list:
            all_notes = item.get('ftrack_notes', [])
            if all_notes == []:
                continue
            current_note = self.ftrack.get('note_pattern', '').format_map(
                Default(item))
            notes = []
            for one in all_notes:
                v = self.note_regex(one, current_note, self.ftrack['note_repl'])
                if v is not None:
                    notes.append(v)

            out_note = ''
            if notes is not None:
                if len(notes) > 0:
                    #out_note = notes[0]
                    out_note = "\n---\n".join(notes)
            item['ftrack_note'] = out_note


    def note_regex(self, content, note_pattern, note_repl):
        try:
            compiled = re.compile(note_pattern, re.MULTILINE)
        except:
            return None
        result = None
        if note_repl and note_repl != "":
            # it is a replace
            if note_repl.startswith("lambda "):
                try:
                    _eval = eval(str(note_repl))
                except:
                    _eval = note_repl
                try:
                    result = re.sub(compiled, _eval, content)
                except:
                    result = None
            else:
                try:
                    result = compiled.match(content).expand(note_repl)
                except:
                    result = None
        else:
            try:
                m = re.search(note_pattern, content)
            except:
                pass
            if m:
                try:
                    result = content
                except:
                    result = None
            else:
                result = None
        return result

    def run_checks(self):

        class Default(dict):
            def __missing__(self, key):
                return '{' + key + '}'

        self.checks_init()
        if self.checks is None:
            return

        for item in self.merged_list:
            item['warning'] = ''
            item['error'] = ''

        for item in self.merged_list:
            for one_check in self.checks:
                # filter out first
                _if_eval = False
                if one_check['filter'] != '':
                    try:
                        _if = one_check['filter'].format_map(Default(item))
                        _if_eval = bool(eval(_if))
                    except:
                        pass
                else:
                    # no filtering, so true for all
                    _if_eval = True

                if _if_eval:
                    # not filtered out
                    _check_eval = False
                    try:
                        _check = one_check['check'].format_map(Default(item))
                        _check_eval = bool(eval(_check))
                    except:
                        pass
                    if _check_eval:
                        # it is warning or error
                        m = one_check['message'].format_map(Default(item))
                        if one_check['is_error']:
                            try:
                                item['error'] = item['error'] + '\n' + m
                            except:
                                item['error'] = m
                        else:
                            if item['warning'] and item['warning'] != '':
                                item['warning'] = item['warning'] + '\n' + m
                            else:
                                item['warning'] = m
            sw = item.get('size_warning', '')
            if sw and sw != '':
                if item['warning'] and item['warning'] != '':
                    item['warning'] = item['warning'] + '\n' + sw
                else:
                    item['warning'] = sw

    def prepare_converts(self):
        """
        Execute command lines for every media file
        :return: add vendor_Thumbs to media files
        """

        class Default(dict):
            def __missing__(self, key):
                return '{' + key + '}'

        def _get_exes():
            if sys.platform.startswith('win'):
                exe_extension = '.exe'
            else:
                exe_extension = ''
            script_path = os.path.dirname(
                os.path.abspath(inspect.stack()[-1][1])).replace("\\", "/")
            probe = script_path + '/ffmpeg/ffprobe' + exe_extension
            if not os.path.exists(probe):
                probe = ''
            mpg = script_path + '/ffmpeg/ffmpeg' + exe_extension
            if not os.path.exists(mpg):
                mpg = ''
            oiio = script_path + '/oiio/win/oiiotool.exe'
            if not os.path.exists(oiio):
                oiio = ''
            ocio = script_path + '/ocio/config.ocio'
            if not os.path.exists(ocio):
                ocio = ''
            return {'ffmpeg': mpg, 'ffprobe': probe, 'oiio': oiio, 'ocio': ocio}

        self.converts = []
        if self.settings:

            _root = str(self.settings['package_folder']['value'])
            # read checks from gui, save to self.checks
            indexes = [str(x).zfill(2) for x in range(1, 9)]
            for one in indexes:
                if_filter = str(self.settings["thumbs_if_" + one]["value"])
                exe = str(self.settings["thumbs_exe_" + one]["value"])
                args = str(self.settings["thumbs_args_" + one]["value"])
                fn = str(self.settings["thumbs_name_" + one]["value"])
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

        _exes = _get_exes()
        for item in self.merged_list:
            for one_conv in self.converts:
                # filter out first
                _if_eval = False
                if one_conv['filter'] != '':
                    try:
                        _if = one_conv['filter'].format_map(Default(item))
                        _if_eval = bool(eval(_if))
                    except:
                        pass
                else:
                    # no filtering, so true for all
                    _if_eval = True

                if _if_eval:
                    # not filtered out
                    _check_eval = False
                    try:
                        _e = one_conv['exe'].format_map(Default(self.static_keywords))
                        _e = _e.format_map(Default(_exes))
                        _a = one_conv['args'].format_map(Default(self.static_keywords))
                        _a = _a.format_map(Default(item))
                        _a = _a.format_map(Default(_exes))
                        _cmd = "{} {}".format(_e, _a)
                        _fn = one_conv['fn'].format_map(Default(self.static_keywords))
                        _fn = _fn.format_map(Default(item))

                        _fnr = _fn
                        if _fn.startswith(_root):
                            _fnr = _fn[len(_root)+1:]
                        item['convert_path'] = _fn
                        item['convert_path_relative'] = _fnr
                        item['convert_cmd'] = _cmd

                    except:
                        pass

    def run_converts(self):
        """
        Execute command lines for every media file
        :return: add vendor_Thumbs to media files
        """

        for item in self.merged_list:
            _fn = item.get('convert_path')
            _cmd = item.get('convert_cmd')

            if _fn and _cmd:
                if not os.path.exists(_fn):
                    _d = os.path.dirname(os.path.abspath(_fn))
                    if not os.path.exists(_d):
                        os.makedirs(_d)

                    print("exe: {}".format(_cmd))
                    process = subprocess.Popen(_cmd, shell=True,
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE,
                                               bufsize=-1)
                    out, err = process.communicate()

                    if process.returncode != 0:
                        print("bad convert")
                    else:
                        print("good convert")

                if not os.path.exists(_fn):
                    item['convert_path'] = ''

    def checks_init(self):
        self.checks = []
        if self.settings:
            # read checks from gui, save to self.checks
            indexes = [str(x) for x in range(1, 10)]
            for one in indexes:
                if_filter = str(self.settings["check_if_" + one]["value"])
                check = str(self.settings["check_check_" + one]["value"])
                is_error = bool(self.settings["check_error_" + one]["value"])
                message = str(self.settings["check_message_" + one]["value"])
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
