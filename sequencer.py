import os
import re
from operator import itemgetter
import pprint
import time
import logging

import parse_file_name
from metadata import MetaData
import helpers


class Sequencer(object):
    def __init__(self, in_path, sequence_mode='to_subsequences', gui=None):

        self.log = logging.getLogger("mylog")
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
        self.table_txt = ""
        self.static_keywords = None

        self.output = {}

        if os.path.exists(in_path):
            if in_path is None:
                in_path = ''

            # to detect if in_path is full path
            # or just path to directory with no end slash
            if os.path.isdir(in_path)\
                    and not (in_path[-1] == os.sep or
                             in_path[-1] == os.altsep):
                # add end slash
                in_path += os.sep
            in_path.replace("\\", "/")

            in_path_parsed = parse_file_name.parse(in_path)
            self.in_path = in_path

            # get list of all files
            file_list = self.walk_dirs(self.in_path)

            # get list of dirs of sequences
            self.merged_list = []
            self.merged_list = self.seq_list_from_file_list(
                file_list, mode=sequence_mode)

            # get list of dirs of multi-frame files
            self.merged_list.extend(self.multirames_from_file_list(file_list))

            # other (audio, office, graphics, other)
            self.merged_list.extend(self.other_files_from_file_list(file_list))

            # get file sizes for merged list
            self.get_file_sizes()

            self.get_relative_paths(in_path_parsed)

            self.get_metadata()

            # this sets static keywords like date and package name
            self.prepare_package_name()

            # also adds totals to static keywords
            self.filter_items_add_counters()

            # read from settings and compile
            self.prepare_regex()

            # for every found item prepare regex items
            self.fill_regexes()

            # parse table headers
            self.prepare_all_columns()

            # fill tables for export and display
            self.prepare_tables()

            pprint.pprint(self.merged_list)

            # pprint.pprint(self.table_sub)
            #print("number of files: {}".format(len(file_list)))

            # logging.debug('-> Sequencer Init')

    def get_metadata(self):

        self.output['status'] = "Getting meta data" \
                                " (get_metadata)"

        if self.merged_list and len(self.merged_list) > 0:
            for one_item in self.merged_list:
                if one_item['category'] in\
                        ['still', 'video', 'sequence', 'audio']:
                    one_item.update(
                        MetaData(one_item, self.settings).meta_data)

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

        def get_big_devs(difs, treshold=0.3):
            dif = []
            low = 1.0 - treshold
            high = 1.0 + treshold
            for one in difs:
                if one < low or one > high:
                    dif.append(one)
            return dif

        self.output['status'] = "Getting file sizes" \
                                " (get_file_sizes)"

        if self.merged_list is not None and len(self.merged_list) > 0:
            for one_item in self.merged_list:
                one_item['size_bytes'] = 0
                one_item['size_human'] = '0'

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
                    for one_frame in range(start, end):
                        one_file = one_pth + '/' + clean + str(one_frame).zfill(pad) + ext
                        try:
                            stat_info = os.stat(one_file)
                            # size in bytes
                            my_size = my_size + stat_info.st_size
                            if my_size == 0:
                                one_item['size_warning'] = 'file has zero size'
                            sizes.append(stat_info.st_size)
                        except:
                            pass

                    if sizes is not None and len(sizes) > 0:
                        # warn if files are missing
                        missing = len(one_item['missing_numbers'])
                        if missing > 0:
                            if one_item['size_warning'] == "":
                                one_item['size_warning'] = str(missing) + " missing files"
                            else:
                                one_item['size_warning'] += ", " + str(missing) + " missing files"

                        # analyze sizes
                        size_median = median(sizes)
                        size_differences = median_difference(sizes, size_median)
                        # consider 30% difference as big
                        big_deviations = get_big_devs(size_differences, 0.3)
                        # warn if 5 or more files differ greatly in size
                        if len(big_deviations) > 4:
                            if one_item['size_warning'] == '':
                                one_item['size_warning'] = str(len(big_deviations)) + ' files greatly differs in size'
                            else:
                                one_item['size_warning'] += ', ' + str(len(big_deviations)) + ' files greatly differs in size'

                        one_item['size_bytes'] = my_size
                        one_item['size_human'] = helpers.humanize_file_size(my_size)
                else:
                    # video (multiframe container)
                    try:
                        statinfo = os.stat(one_item['path'])
                        # size in bytes
                        my_size = statinfo.st_size
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

            for one_item in self.merged_list:
                one_item.update({"hide_sub": False})
                one_item.update({"hide_log": False})
                one_item.update({"hide_txt": False})
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

                # add counter to the items that are not hidden
                if not one_item['hide_sub']:
                    one_item.update({"cnt_sub": str(cnt_sub).zfill(counter_zeroes)})
                    cnt_sub += counter_step
                    total_sub += 1
                    if one_item['category'] == 'sequence':
                        files_sub += int(one_item['meta_duration_frames'])
                    else:
                        files_sub += 1
                if not one_item['hide_log']:
                    one_item.update({"cnt_log": str(cnt_log).zfill(counter_zeroes)})
                    cnt_log += counter_step
                    total_log += 1
                    if one_item['category'] == 'sequence':
                        files_log += int(one_item['meta_duration_frames'])
                    else:
                        files_log += 1
                if not one_item['hide_txt']:
                    one_item.update({"cnt_txt": str(cnt_txt).zfill(counter_zeroes)})
                    cnt_txt += counter_step
                    total_txt += 1
                    if one_item['category'] == 'sequence':
                        files_txt += int(one_item['meta_duration_frames'])
                    else:
                        files_txt += 1

        totals = {
            'total_sub': total_sub,
            'total_log': total_log,
            'total_txt': total_txt,
            'files_sub': files_sub,
            'files_log': files_log,
            'files_txt': files_txt
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
            indexes = [str(x) for x in range(1, 9)]
            for one in indexes:
                name_key = "parse_name_" + one
                key = self.settings[name_key]["value"]
                name_pat = "parse_pattern_" + one
                pat = self.settings[name_pat]["value"]
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
                    one_regex = {key: {"pattern": pat,
                                       "valid": pat_valid,
                                       "compiled": pat_compiled,
                                       "repl": rep,
                                       "source": src
                                       }}
                    self.regexes.update(one_regex)

    def fill_regexes(self):
        """
        For every item in merged list
        it generates the regex keywords
        :return:
        """
        if self.merged_list and len(self.merged_list) > 0:
            for one_item in self.merged_list:
                for k, one_regex in self.regexes.items():
                    # expand keywords in source
                    try:
                        expanded = one_regex["source"].format(**one_item)
                    except KeyError:
                        expanded = None
                    if expanded and expanded != '':
                        # expand static keywords
                        try:
                            expanded = expanded.format(**self.static_keywords)
                        except KeyError:
                            pass
                        if one_regex["repl"] and one_regex["repl"] != "":
                            # it is a replace
                            if one_regex["repl"].startswith("lambda "):
                                #LAMBDA!
                                result = re.sub(one_regex["compiled"], eval(str(one_regex["repl"])), expanded)
                            else:
                                #result = re.sub(one_regex["compiled"], one_regex["repl"], expanded)
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
                    one_item.update({k: result})


    def prepare_package_name(self):

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
            _per_date = self.settings[
                                 'name_version_per_date']['value']
        if self.settings['name_version_zeroes']['value'] is not None:
            _ver_zeroes = self.settings[
                                  'name_version_zeroes']['value']
        if self.settings['name_version_use_letters']['value'] is not None:
            _ver_letters = self.settings[
                'name_version_use_letters']['value']
        if self.settings['name_version_letters_uppercase']['value'] is not None:
            _ver_upper = self.settings[
                'name_version_letters_uppercase']['value']

        # get current date by applying regex to expanded template
        try:
            _temp_expanded = _template.format(**date_keys)
        except KeyError:
            self.log.error("Package name template failed")

        d = _date_compiled.search(_temp_expanded)
        if d:
            try:
                current_date = d.group(1)
            except :
                self.log.error("Package date failed")

        # make sure path exists, it is a directory and has trailing slash
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
                one_up = _pkg_folder
                name_from_folder = _spl[-1]

        # list all dirs, parse date and version
        dir_list = []
        for filename in os.listdir(one_up):
            if os.path.isdir(os.path.join(one_up, filename)):
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
                    _today_subs.append(one_dir)
            if _today_subs:
                last_dir = sorted(_today_subs, key=lambda i: i['version'])[-1]
            else:
                last_dir = None
        else:
            # sort by version, take highest
            last_dir = sorted(dir_list, key=lambda i: i['version'])[-1]
        if last_dir:
            last_version = last_dir['version']
        else:
            last_version = 'Z'

        if _ver_letters:
            if _ver_upper:
                next_version = chr(
                    (ord(last_version.upper()) + 1 - 65) % 26 + 65)
            else:
                next_version = chr(
                    (ord(last_version.upper()) + 1 - 65) % 26 + 65).lower()
        else:
            # version is number
            next_version = str(int(last_version) + 1).zfill(_ver_zeroes)

        # add what we know
        date_keys.update({
            'package_version': next_version,
            'package_date': current_date,
            'package_name_from_folder': name_from_folder,
            'package_name_root': one_up
        })
        # expand template to make package name
        try:
            _pkg_new_name = _template.format(**date_keys)
        except:
            # use source folder as name
            _pkg_new_name = name_from_folder
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
        Thumbnail={thumb_path}, Thumbnail={created_thumb_path}, Shot={shot_name}, CheckShot={check_shot_name}, ...
        Returns two lists: column_titles and column_expressions
        """

        column_titles = []
        column_expressions = []
        gui_columns.replace("\n", ",")

        NM_RE = re.compile(r"\s*(?P<columntitle>.*)\s*=\s*(?P<columnexpression>.*)\s*")
        split_list = gui_columns.split(",")
        column_count = 0
        columns = []

        for one_column in split_list:
            m = NM_RE.search(one_column)
            if m:
                title = m.group("columntitle")
                expression = m.group("columnexpression")
                one_itm = {'column_number': column_count, 'title': title, 'expression': expression}
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

        self.column_titles_sub, self.column_expressions_sub = self.prepare_columns(_sub)
        self.column_titles_log, self.column_expressions_log = self.prepare_columns(_log)
        self.column_titles_txt, self.column_expressions_txt = self.prepare_columns(_txt)

    def prepare_tables(self):

        self.table_sub = []
        self.table_log = []
        self.table_txt = ""
        body_txt = ""
        txt_sep = " "

        if self.settings:
            if self.settings['text_sep_tab']['value'] is not None:
                if self.settings['text_sep_tab']['value']:
                    txt_sep = "\t"
            if self.settings['text_add_titles']['value'] is not None:
                txt_titles = bool(self.settings['text_add_titles']['value'])
            if self.settings['text_header']['value'] is not None:
                txt_header = self.settings['text_header']['value']
            if self.settings['text_footer']['value'] is not None:
                txt_footer = self.settings['text_footer']['value']

        if self.merged_list and len(self.merged_list) > 0:
            for one_item in self.merged_list:
                one_item.update(self.static_keywords)
                # build one row, if not hidden
                if not one_item['hide_sub']:
                    one_row_sub = []
                    for one_expression in self.column_expressions_sub:
                        try:
                            formatted = one_expression.format(**one_item)
                            one_row_sub.append(formatted)
                        except KeyError:
                            # can't parse expression, put it in original form
                            #one_row_sub.append(str(one_expression))
                            one_row_sub.append("")
                    #  add item to the end of the row, so we can later on easily reference all the data for the row
                    one_row_sub.append(one_item)
                    # add to table
                    self.table_sub.append(one_row_sub)

                if not one_item['hide_log']:
                    one_row_log = []
                    for one_expression in self.column_expressions_log:
                        try:
                            formatted = one_expression.format(**one_item)
                            one_row_log.append(formatted)
                        except KeyError:
                            # can't parse expression, put it in original form
                            #one_row_log.append(str(one_expression))
                            one_row_log.append("")
                    #  add item to the end of the row, so we can later on easily reference all the data for the row
                    one_row_log.append(one_item)
                    # add to table
                    self.table_log.append(one_row_log)

                if not one_item['hide_txt']:
                    one_row_txt = []
                    for one_expression in self.column_expressions_txt:
                        try:
                            formatted = one_expression.format(**one_item)
                            one_row_txt.append(formatted)
                        except KeyError:
                            # can't parse expression, put it in original form
                            #one_row_txt.append(str(one_expression))
                            one_row_txt.append("")
                    whole_row = str(txt_sep.join(one_row_txt)) + "\n"
                    body_txt += whole_row
        try:
            _header = txt_header.format(**self.static_keywords)
        except KeyError:
            _header = txt_header
        if txt_titles:
            _titles = '\n' + str(txt_sep.join(self.column_titles_txt)) + '\n'
        else:
            _titles = ""
        try:
            _footer = txt_footer.format(**self.static_keywords)
        except KeyError:
            _footer = txt_footer
        self.table_txt = _header + '\n' + _titles + body_txt + '\n' + _footer

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()

    x = Sequencer(in_path=r"C:/projects/OP_2D_testing/resources")
    #pprint.pprint(x.merged_list)

    # finalSeqList = []
    # y = seqLS(x)