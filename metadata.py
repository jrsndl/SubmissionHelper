# -*- coding: utf-8 -*-
import os
import pprint
import sys
import re
import subprocess
import struct
import json
import logging

import xml.etree.ElementTree

from PyTimeCode import PyTimeCode
import helpers
import inspect
import logging

from nukery.parser import NukeScriptParser

# for meta from exr header
import parse_metadata


class MetaData(object):

    def __init__(self, item, gui, pths):

        self.log = logging.getLogger("MetaData")
        self.settings = gui
        self.paths = pths

        self.gui_fps = '24'
        if self.settings['prefs_frame_rate_txt']['value'] is not None:
            self.gui_fps = self.settings['prefs_frame_rate_txt']['value']

        self.gui_force_fps = False
        if self.settings['prefs_frame_rate_use_meta']['value'] is not None:
            self.gui_force_fps = \
                not bool(self.settings['prefs_frame_rate_use_meta']['value'])

        self.default_tc = '01:00:00:00'
        if self.settings['prefs_tc_default']['value'] is not None:
            self.default_tc = str(self.settings['prefs_tc_default']['value'])

        # get file path
        # get file path
        self.item = item

        self.meta = {'file': item['path'], 'error': '', 'width': 0, 'height': 0,
                     'fps_str': '', 'fps': 0.0, 'fps_a': 0, 'fps_b': 0, 'fps_raw': '',
                     'duration_frames': 0, 'duration_secs': 0.0,
                     'bitrate_video': 0, 'aspect': 0.0, 'aspect_x': 0, 'aspect_y': 0,
                     'codec_name_video': '', 'codec_long_name_video': '', 'codec_profile_video': '',
                     'time_stamp_video': '', 'fields': 0,
                     'time_code': '', 'reel': '',
                     'sample_rate_audio': 0, 'channels_audio': 0, 'bits_per_sample_audio': 0,
                     'duration_audio': 0.0, 'bitrate_audio': 0, 'codec_name_audio': '',
                     'codec_long_name_audio': '', 'time_stamp_audio': '',
                     'video_present': 0, 'audio_present': 0, 'data_present': 0,
                     'is_log': False}

        self.meta_exr = {}
        self.meta_nk = {}

        self.platform, self.platform_extension = self.__get_platform()
        self.ffmpeg_path = self.paths['ffmpeg']
        self.ffprobe_path = self.paths['ffprobe']
        self.oiiotool_path = self.paths['oiiotool']
        self.meta_data = {}

    def meta_get(self):
        self.__read_from_drive()
        self.meta_data = self.metadata_to_keywords()
        return self

    def metadata_to_keywords(self):
        meta_data = {
            'meta_file': self.meta.get('file'),
            'meta_error': self.meta.get('error'),
            'meta_width': str(self.meta.get('width')),
            'meta_height': str(self.meta.get('height')),
            'meta_fps': self.meta.get('fps_str'),
            'meta_fps_a': str(self.meta.get('fps_a')),
            'meta_fps_b': str(self.meta.get('fps_b')),
            'meta_fps_raw': self.meta.get('fps_raw', '0/0'),
            'meta_duration_frames': str(self.meta.get('duration_frames')),
            'meta_duration_frames_slate': str(self.meta.get('duration_frames_slate', '')),
            'meta_duration_secs': str(self.meta.get('duration_secs')),
            'meta_bitrate_video': str(self.meta.get('bitrate_video')),
            'meta_aspect': str(self.meta.get('aspect')),
            'meta_aspect_x': str(self.meta.get('aspect_x')),
            'meta_aspect_y': str(self.meta.get('aspect_y')),
            'meta_codec_name_video': self.meta.get('codec_name_video'),
            'meta_codec_long_name_video': self.meta.get('codec_long_name_video'),
            'meta_time_stamp_video': self.meta.get('time_stamp_video'),
            'meta_codec_profile_video': self.meta.get('codec_profile_video'),
            'meta_fields': str(self.meta.get('fields')),
            'meta_time_code': self.meta.get('time_code'),
            'time_code_from_metadata': self.meta.get('time_code_from_metadata'),
            'time_code_from_seq': self.meta.get('time_code_from_seq'),
            'meta_reel': self.meta.get('reel'),
            'meta_sample_rate_audio': str(self.meta.get('sample_rate_audio')),
            'meta_channels_audio': str(self.meta.get('channels_audio')),
            'meta_bits_per_sample_audio': str(self.meta.get('bits_per_sample_audio')),
            'meta_duration_audio': str(self.meta.get('duration_audio')),
            'meta_bitrate_audio': str(self.meta.get('bitrate_audio')),
            'meta_codec_name_audio': self.meta.get('codec_name_audio'),
            'meta_codec_long_name_audio': self.meta.get('codec_long_name_audio'),
            'meta_time_stamp_audio': self.meta.get('time_stamp_audio'),
            'meta_video_present': str(self.meta.get('video_present')),
            'meta_audio_present': str(self.meta.get('audio_present')),
            'meta_data_present': str(self.meta.get('data_present')),
            'meta_is_log': str(self.meta.get('is_log')),
            'meta_frame_start_from_tc': str(self.meta.get('frame_start_from_tc', '')),
            'meta_frame_start_from_tc_slate': str(self.meta.get('frame_start_from_tc_slate', '')),
            'meta_frame_end_from_tc': str(self.meta.get('frame_end_from_tc', '')),
            'meta_frame_end_from_tc_slate': str(self.meta.get('frame_end_from_tc_slate', '')),
            'meta_thumbnail_time': self.meta.get('thumbnail_time', "0"),
            'meta_thumbnail_frame': self.meta.get('thumbnail_frame', "0")
        }

        # add exr header
        try:
            meta_data = {**meta_data, **self.meta_exr}
        except:
            print("Reading EXR metadata failed")

        # add nuke and maya metadata
        try:
            meta_data.update(self.meta_nk)
            meta_data.update(self.meta_maya)
        except:
            pass

        return meta_data

    @staticmethod
    def __get_platform():

        platform = 'win'
        platform_exe_extension = '.exe'
        if sys.platform.startswith('darvin'):
            platform = 'mac'
            platform_exe_extension = ''
        if str(os.name).startswith('posix'):
            platform = 'nix'
            platform_exe_extension = ''
        return platform, platform_exe_extension

    def __get_ffmpeg_path(self):

        """
        script_path = os.path.dirname(
            os.path.abspath(inspect.stack()[-1][1])).replace("\\", "/")
        """
        if getattr(sys, 'frozen', False):
            script_path = os.path.dirname(sys.executable).replace("\\", "/")
        else:
            script_path = os.path.dirname(__file__).replace("\\", "/")


        #TODO remove before packaging
        #script_path = 'D:/_code/SubmissionHelper'
        probe = script_path + '/ffmpeg/ffprobe' + self.platform_extension
        if not os.path.exists(probe):
            probe = None
        mpg = script_path + '/ffmpeg/ffmpeg' + self.platform_extension
        if not os.path.exists(mpg):
            mpg = None
        return mpg, probe

    def __read_from_drive(self):
        """
        self. meta dictionary with metadata defaults is initialized
        external apps are called (if allowed by prefs) to update metadata
        """

        fn = self.meta['file']
        my_extension = str.lower(str(self.item['extension']))
        ff_categories = ['still', 'sequence', 'video', 'audio', 'multiframe']

        if self.ffprobe_path is None:
            self.log.warning('Ffprobe not found')
        else:
            try:
                self.meta.update(self.probe_ffprobe())
            except:
                print("Reading ffprobe metadata failed.")

            if self.meta['error'] != '':
                if self.item['category'] in ff_categories:
                    self.log.warning("Problem getting metadata by ffprobe: {} for file {}"
                                     .format(self.meta['error'], fn))
                self.meta['error'] = ''

        # DPX:
        if my_extension == 'dpx':
            self.meta.update(self.read_metadata_from_dpx())

        # Nuke
        if my_extension == 'nk':
            self.meta_nk = self.read_metadata_from_nuke()

        if my_extension == 'ma':
            self.meta_maya = self.read_metadata_from_maya()

        # EXR
        if my_extension == 'exr':
            try:
                self.meta_exr = self.read_metadata_from_exr()

                # overwrite key meta_ from EXR values
                self.meta['time_code'] = self.meta_exr.get(
                    'metaExr_time_code', self.meta['time_code'])

                self.meta['fps'] = str(self.meta_exr.get(
                    'metaExr_fps', self.meta['fps']))
                self.meta['fps_a'] = str(self.meta_exr.get(
                    'metaExr_fps_a', self.meta['fps_a']))
                self.meta['fps_b'] = str(self.meta_exr.get(
                    'metaExr_fps_b', self.meta['fps_b']))
                self.meta['fps_raw'] = self.meta_exr.get(
                    'metaExr_fps_raw', self.meta['fps_raw'])

                self.meta['codec_name_video'] = self.meta_exr.get(
                    'metaExr_compression', self.meta['codec_name_video'])
                self.meta['codec_long_name_video'] = self.meta_exr.get(
                    'metaExr_compression',
                    self.meta['codec_long_name_video'])

                self.meta['aspect'] = str(self.meta_exr.get(
                    'metaExr_pixelAspectRatio', self.meta['aspect']))
            except:
                print("Reading EXR metadata failed")


        # Other TCs
        self.meta['time_code_from_metadata'] =\
            self.get_source_tc_start(method='meta')

        try:
            self.meta['time_code_from_seq'] =\
                self.get_source_tc_start(method='filename')
        except:
            pass
        self.meta['time_code'] = self.meta['time_code_from_metadata']

        # get fps from gui if meta not available or if forced
        self.__fix_fps()

        # create duration for sequences
        self.__fix_duration()

        self._frame_range_from_tc()

        # mark object as read from drive, so we do not need to
        # use external programs to read metadata all the time
        MetaData.meta_read_from_file = True

    def __fix_duration(self):
        """
        create duration for sequences from images and fps
        :return:
        """

        if self.meta['file'] and self.meta['file'] != '':
            category = self.item['category']
            if category == 'sequence':
                self.meta['duration_frames'] = self.item['end_number'] - self.item['start_number'] + 1
                self.meta['duration_frames_slate'] = self.meta['duration_frames'] - 1
                self.meta['duration_secs'] = helpers.frames_to_seconds(frames=self.meta['duration_frames'],
                                                                     fps=self.meta['fps_str'])
                self.meta['thumbnail_frame'] = int(self.meta['duration_frames'] / 2) + self.item['start_number']
                self.meta['thumbnail_time'] = helpers.frames_to_seconds(frames=int(self.meta['duration_frames'] / 2),
                                                                     fps=self.meta['fps_str'])
            elif category == 'still':
                self.meta['duration_frames'] = 1
                self.meta['duration_frames_slate'] = 1
                self.meta['duration_secs'] = 0.0
                self.meta['thumbnail_frame'] = 0
                self.meta['thumbnail_time'] = 0
            elif category == 'video':
                #self.meta['thumbnail_time'] = (float(self.meta['duration_secs']) / 2.0)
                #self.meta['thumbnail_frame'] = helpers.seconds_to_frames(seconds=float(self.meta['duration_secs']) / 2.0, fps=self.meta['fps_str'])
                self.meta['thumbnail_frame'] = int(self.meta['duration_frames'] / 2) + self.item['start_number']
                self.meta['thumbnail_time'] = helpers.frames_to_seconds(frames=int(self.meta['duration_frames'] / 2), fps=self.meta['fps_str'])


    def _frame_range_from_tc(self):
        if self.meta['file'] and self.meta['file'] != '':
            if self.item['category'] == 'video':

                if self.meta['fps_b'] > 0 and self.meta['time_code']:
                    start_tc_frames = helpers.tc_to_frames(self.meta['time_code'], self.meta['fps_a'], self.meta['fps_b'])
                else:
                    start_tc_frames = 0

                self.meta['frame_start_from_tc'] = str(start_tc_frames)
                self.meta['frame_start_from_tc_slate'] = str(start_tc_frames+1)
                if self.meta['duration_frames']:
                    _dur = int(self.meta['duration_frames'])
                    self.meta['frame_end_from_tc'] = str(start_tc_frames + _dur - 1)
                    self.meta['frame_end_from_tc_slate'] = str(start_tc_frames + _dur - 2)

            elif self.item['category'] == 'sequence':
                self.meta['frame_start_from_tc'] = self.item['start_number']
                self.meta['frame_start_from_tc_slate'] = self.item['start_number'] + 1
                self.meta['frame_end_from_tc'] = self.item['end_number']
                self.meta['frame_end_from_tc_slate'] = self.item['end_number']


    def __fix_fps(self):
        """
        get fps from gui if meta not available or if forced
        """
        if self.meta['file'] and self.meta['file'] != '':

            # reset fps for sequences and stills if ext is not exr or dpx (the only formats that can hold fps)
            my_ext = str.lower(str(self.item['extension']))
            cat = self.item['category']
            if cat in ['sequence', 'still']:
                if my_ext in ['dpx', 'exr']:
                    pass
                else:
                    self.meta['fps_str'] = ''

            # if fps was not read from metadata
            if self.gui_force_fps and self.meta['fps_str'] == '':
                # get fps from gui if meta not available
                self.meta['fps_str'] = self.gui_fps
            elif self.gui_force_fps:
                # get fps from gui ALWAYS
                self.meta['fps_str'] = self.gui_fps

    @property
    def reel(self):
        return self.get_reel_name()

    @property
    def tc(self):
        return self.get_source_tc_start()

    def get(self):
        return self.meta

    def get_length_in_frames(self):
        """
        Method for getting length in frames
        For image sequences, end-start+1
        For multiframe files, get seconds from meta, fps from meta (or default) and calc
        For sound files, get seconds from meta, fps from meta (or default) and calc
        """
        pass

    def get_source_tc_start(self, method='meta'):
        """
        Use metadata and gui settings
        """

        default_tc = '01:00:00:00'
        f_tc = default_tc
        if method == 'meta':
            f_tc = self.meta['time_code']
        elif method == 'filename':
            if self.item['category'] in ['sequence']:
                # get frame number
                num = int(self.item['number'])
                f_tc = helpers.frames_to_tc(num, self.meta['fps_a'], self.meta['fps_b'])

        if f_tc is None:
            f_tc = default_tc
        return f_tc

    def get_reel_name(self):
        """
        Use metadata and gui settings
        """

        # start from nothing
        reel_start = ''

        # FROM META
        method = 'method'
        if method == 'meta':
            reel_start = self.meta['reel']

    def probe_ffprobe(self):

        filename = str(self.meta['file'])  # no unicode
        outdata = {'file': filename, 'error': '',
                   'width': 0, 'height': 0, 'fps_str': '', 'fps_a': 0, 'fps_b': 0, 'duration_frames': 0,
                   'duration_secs': 0.0, 'bitrate_video': 0, 'aspect': 0.0, 'aspect_x': 0, 'aspect_y': 0,
                   'codec_name_video': '', 'codec_long_name_video': '', 'time_stamp_video': '', 'fields': 0,
                   'time_code': '', 'reel': '',
                   'sample_rate_audio': 0, 'channels_audio': 0, 'bits_per_sample_audio': 0,
                   'duration_audio': 0.0, 'bitrate_audio': 0, 'codec_name_audio': '', 'codec_long_name_audio': '',
                   'time_stamp_audio': '',
                   'video_present': 0, 'audio_present': 0, 'data_present': 0,
                   'is_log': False,
                   }

        args = [self.ffprobe_path, '-show_streams', '-print_format', 'xml', '-i', filename]
        process = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        out, err = process.communicate()

        if process.returncode != 0:
            outdata['error'] = "Probing file " + str(filename) + "  failed with error " + str(err)
        else:
            try:
                tree = xml.etree.ElementTree.fromstring(out)
                StreamFind = tree.find("streams")
                StreamList = StreamFind.findall("stream")
                for onestr in StreamList:
                    streamType = onestr.attrib['codec_type']

                    if streamType == 'video':
                        outdata['video_present'] = 1
                        try:
                            outdata['width'] = int(onestr.attrib.get('width'))
                        except:
                            pass

                        try:
                            outdata['height'] = int(onestr.attrib.get('height'))
                        except:
                            pass

                        try:
                            rawfps = str(onestr.attrib['r_frame_rate'])  # "24/1"
                            outdata['fps_raw'] = rawfps
                            outdata['fps'] = float(eval(rawfps))
                            outdata['fps_str'] = helpers.get_fps_for_PyTimeCode(outdata['fps'])
                            outdata['fps_a'] = int(rawfps.split('/')[0])
                            outdata['fps_b'] = int(rawfps.split('/')[1])
                        except:
                            pass

                        try:
                            outdata['duration_frames'] = int(onestr.attrib['nb_frames'])
                            outdata['duration_frames_slate'] = int(
                                onestr.attrib['nb_frames']) - 1
                        except:
                            if onestr.attrib.get('duration_ts') is not None:
                                outdata['duration_frames'] = int(onestr.attrib['duration_ts'])
                                outdata['duration_frames_slate'] = int(onestr.attrib['duration_ts']) - 1

                        try:
                            outdata['duration_secs'] = float(onestr.attrib['duration'])  # "38.333333" seconds
                        except:
                            pass

                        try:
                            outdata['bitrate_video'] = int(onestr.attrib['bit_rate'])  # "71376397"
                        except:
                            pass

                        try:
                            rawsar = str(onestr.attrib['sample_aspect_ratio']).replace(':', '/')  # "1:1"
                            outdata['aspect_x'] = int(rawsar.split('/')[0])
                            outdata['aspect_y'] = int(rawsar.split('/')[1])
                            outdata['aspect'] = float(outdata['aspect_x']) / float(outdata['aspect_y'])
                        except:
                            pass

                        try:
                            outdata['codec_name_video'] = str(onestr.attrib['codec_name'])
                        except:
                            pass

                        try:
                            outdata['codec_long_name_video'] = str(onestr.attrib['codec_long_name'])
                        except:
                            pass

                        try:
                            outdata['codec_profile_video'] = str(onestr.attrib['profile'])
                        except:
                            pass

                        try:
                            TagFind = onestr.findall("tag")
                            for onetag in TagFind:
                                if onetag.attrib['key'] == 'creation_time':
                                    outdata['time_stamp_video'] = onetag.attrib['value']  # "2012-04-25 15:45:12"
                        except:
                            pass

                    if streamType == 'data':
                        outdata['data_present'] = 1
                    try:
                        TagFind = onestr.findall("tag")
                        for onetag in TagFind:
                            if onetag.attrib['key'] == 'timecode':
                                outdata['time_code'] = onetag.attrib['value']
                    except:
                        pass

                    if streamType == 'audio':
                        outdata['audio_present'] = 1

                        try:
                            outdata['sample_rate_audio'] = int(onestr.attrib['sample_rate'])  # "48000"
                        except:
                            pass

                        try:
                            outdata['channels_audio'] = int(onestr.attrib['channels'])  # '2'
                        except:
                            pass

                        try:
                            outdata['bits_per_sample_audio'] = int(onestr.attrib['bits_per_sample'])  # "16"
                        except:
                            pass

                        try:
                            outdata['duration_audio'] = float(onestr.attrib['duration'])
                        except:
                            pass

                        try:
                            outdata['bitrate_audio'] = int(onestr.attrib['bitrate'])  # "1536000"
                        except:
                            pass

                        try:
                            outdata['codec_name_audio'] = str(onestr.attrib['codec_name'])
                        except:
                            pass

                        try:
                            outdata['codec_long_name_audio'] = str(onestr.attrib['codec_long_name'])
                        except:
                            pass
                        try:
                            TagFind = onestr.findall("tag")
                            for onetag in TagFind:
                                if onetag.attrib['key'] == 'creation_time':
                                    outdata['time_stamp_audio'] = onetag.attrib['value']  # "2012-04-25 15:45:12"
                        except:
                            pass
            except:
                outdata['error'] = "Probing file " + filename + " failed. Error parsing Xml output."

        return outdata

    def probeFileFfmbc(self, filename, ffmbcpath='ffmbc'):

        ppth = ffmbcpath.replace('\"', '')
        filename = filename.replace('\"', '')
        filename = str(filename)  # no unicode

        outdata = {'file': filename, 'error': '',
                   'reel': '', 'time_code': '',
                   'fps': 0.0, 'fps_a': 0, 'fps_b': 0,
                   'duration_secs': '',
                   'is_log': False, }

        args = [ppth, '-i', filename]
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # outputs error with file description including metadata        
        out, err = process.communicate()

        try:
            if "timecode: " in err:
                outdata['time_code'] = err.split("timecode: ")[1].split('\r')[0]
        except:
            outdata['error'] += 'Failed to parse time_code from file ' + filename + ' by ffmbc'

        try:
            if "reel_name(eng): " in err:
                outdata['reel'] = err.split("reel_name(eng): ")[1].split('\r')[0]
        except:
            outdata['error'] += 'Failed to parse reel from file ' + filename + ' by ffmbc'

        try:
            if "com.apple.proapps.reel: " in err:
                outdata['reel'] = err.split("com.apple.proapps.reel: ")[1].split('\r')[0]
                aa = err.split("com.apple.proapps.reel: ")[1]
                bb = aa.split('\r')[0]

        except:
            outdata['error'] += 'Failed to parse reel from file ' + filename + ' by ffmbc'

        try:
            if " fps" in err:
                outdata['fps'] = float(err.split(" fps")[0].split(' ')[-1])
                a, b = helpers.get_fps_ratio(outdata['fps'])
                outdata['fps_a'] = a
                outdata['fps_b'] = b
        except:
            outdata['error'] += 'Failed to parse fps from file ' + filename + ' by ffmbc'

        try:
            if "Duration: " in err:
                outdata['duration_secs'] = err.split("Duration: ")[1].split(",")[0]
        except:
            outdata['error'] += 'Failed to parse duration_secs from file ' + filename + ' by ffmbc'

        try:
            if "com.arri.camera.ColorGammaSxS: LOG-C" in err:
                outdata['is_log'] = True
        except:
            outdata['error'] += 'Failed to parse is_log from file ' + filename + ' by ffmbc'

        return outdata

    def read_metadata_from_maya(self):
        """
        search text file for two regular expressions
        :return:
        return list of dictionaries containing ref ref_rn and path named groups
        """

        regrex1 = r"(?s)^file -rdi([^\"]*)\"(?P<ref>[^\"]*)\"([^\"]*)\"(?P<ref_rn>[^\"]*)\"([^\"]*)\"([^\"]*)\"([^\"]*)\"(?P<path>[^\"]*)\".*;$"
        regrex2 = r"(?s)^file -r -ns \"(?P<ref>[^\"]*)\"([^\"]*)\"(?P<ref_rn>[^\"]*)\"([^\"]*)\"([^\"]*)\"([^\"]*)\"(?P<path>[^\"]*)\";$"

        pth = self.meta['file']

        result = []
        try:
            with open(pth, 'r') as f:
                content = f.read()

            # Search for both regex patterns
            matches1 = re.finditer(regrex1, content, re.MULTILINE)
            matches2 = re.finditer(regrex2, content, re.MULTILINE)

            # Process matches from first regex
            for match in matches1:
                result.append({
                    'ref': match.group('ref'),
                    'ref_rn': match.group('ref_rn'),
                    'path': match.group('path'),
                    'type': 'rdi'
                })

            # Process matches from second regex 
            for match in matches2:
                result.append({
                    'ref': match.group('ref'),
                    'ref_rn': match.group('ref_rn'),
                    'path': match.group('path'),
                    'type': 'r'
                })

        except Exception as e:
            self.log.warning(f"Failed to read Maya metadata from {pth}: {str(e)}")

        refs = [match.get('ref') for match in result]
        metadict = {
            'meta_maya_allrefs':  ' '.join(refs)
        }
        return metadict

    def read_metadata_from_nuke(self):
        """
        Use Nukery to read metadata from file.

        :return:
        """
        pth = self.meta['file']
        metadict = {
            "file": pth,
            "error": '',
            "meta_nk_handleStart": '',
            "meta_nk_handleEnd": '',
            "meta_nk_folderPath": '',
            "meta_nk_task": '',
            "meta_nk_first_frame": '',
            "meta_nk_last_frame": '',
            "meta_nk_fps": '',
            "meta_nk_ocio_path": '',
            "meta_nk_width": '',
            "meta_nk_height": '',
            "meta_nk_pixel_aspect": '',
            "meta_nk_format_name": ''
        }

        if pth is None:
            metadict["error"] = f"File {pth} is not set."
            return metadict

        try:
            prs = list(NukeScriptParser.from_file(pth))
        except Exception as e:
            metadict["error"] = f"Problem parsing file:{pth} error {e}"
            return metadict

        for one in prs:
            node_class = one.get('class')
            node_knobs = one.get('knobs')
            if node_class == 'Group':
                for knob_name, knob_value in node_knobs.items():
                    if knob_name == 'renderCompMain':
                        render_json = node_knobs['publish_instance']

            elif node_class == 'Root':
                root_json = node_knobs.get('publish_instance')
                if root_json is not None and len(root_json) > 9:
                    j = str(root_json)[8:-1].replace("\\", "")
                    root_json_dict = json.loads(j)
                    if root_json_dict is not None:
                        metadict['meta_nk_handleStart'] = root_json_dict.get("handleStart")
                        metadict['meta_nk_handleEnd'] = root_json_dict.get("handleEnd")
                        metadict['meta_nk_folderPath'] = root_json_dict.get("folderPath")
                        metadict['meta_nk_task'] = root_json_dict.get("task")
                metadict['meta_nk_first_frame'] = node_knobs.get('first_frame')
                metadict['meta_nk_last_frame'] = node_knobs.get('last_frame')
                metadict['meta_nk_fps'] = node_knobs.get('fps')
                metadict['meta_nk_ocio_path'] = node_knobs.get('customOCIOConfigPath')

                root_format = node_knobs.get('format')
                if root_format is not None and len(root_format) > 2:
                    sep = root_format[1:-1].split(' ')
                    if len(sep) == 8:
                        metadict['meta_nk_width'] = sep[0]
                        metadict['meta_nk_height'] = sep[1]
                        metadict['meta_nk_pixel_aspect'] = sep[6]
                        metadict['meta_nk_format_name'] = sep[7]
        return metadict

    def read_metadata_from_dpx(self):

        """ Read some metadata from dpx header."""

        fn = self.meta['file']

        metadict = {"file": fn, "error": '',
                    'creator': '', 'project_name': '',
                    'width': 0, 'height': 0,
                    'aspect_x': 1, 'aspect_y': 1,
                    'fps_str': '', 'fps': 0.0, 'fps_a': 0, 'fps_b': 0,
                    'reel': '', 'time_code': '',
                    'is_log': False,
                    }

        try:
            fh = open(fn, "rb")
            byte_array = fh.read(2048)  # reads first 2 kB from file
            fh.close()

            # get magic signature at the begining of file
            m1, m2, m3, m4 = struct.unpack("cccc", byte_array[0:4])
            magic = m1 + m2 + m3 + m4

            endian = ''
            if magic == "SDPX":
                # big endian
                endian = '>'
            elif magic == "XPDS":
                # little endian
                endian = '<'

            if endian != '':

                # creator
                creator = byte_array[160:160 + byte_array[160:261].find('\x00')]
                metadict['creator'] = creator

                # project name
                projectname = byte_array[260:260 + byte_array[260:461].find('\x00')]
                metadict['project_name'] = projectname

                # x y in pixels
                rx, ry = struct.unpack(endian + "II", byte_array[772:780])  # resolution x y
                metadict['width'] = rx
                metadict['height'] = ry

                # reel id
                inputdevice = byte_array[1556:1556 + byte_array[1556:1589].find('\x00')]  # reel
                metadict['reel'] = inputdevice

                # transfer characteristic
                trch, = struct.unpack(endian + "B", byte_array[801:802])  # 0 user, 1 print dens, 2 linear
                if trch == 1:
                    metadict['is_log'] = True
                else:
                    metadict['is_log'] = False

                # TC
                if magic == "SDPX":
                    t1, t2, t3, t4 = struct.unpack("BBBB", byte_array[1920:1924])  # tc
                else:
                    t4, t3, t2, t1 = struct.unpack("BBBB", byte_array[1920:1924])  # tc
                timecode = "%(hh)02x:%(mm)02x:%(ss)02x:%(ff)02x" % {'hh': t1, 'mm': t2, 'ss': t3, 'ff': t4, }
                if timecode == 'ff:ff:ff:ff':
                    timecode = '00:00:00:00'
                metadict["time_code"] = timecode

                # pixel aspect ratio
                ax, ay = struct.unpack(endian + "II", byte_array[1628:1636])
                # can be undefined (FFFFFFFF), so reset to "default" 1:1
                if ax > 4294967294:
                    ax = 1
                if ay > 4294967294:
                    ay = 1

                metadict['aspect_x'] = ax
                metadict['aspect_y'] = ay

                # fps
                fpsf, = struct.unpack(endian + "f", byte_array[1724:1728])  # float number!!!
                a, b = helpers.get_fps_ratio(fpsf)
                metadict['fps_a'] = a
                metadict['fps_b'] = b
                metadict['fps'] = float(metadict['fps_a']) / float(metadict['fps_b'])
                metadict['fps_str'] = helpers.get_fps_for_PyTimeCode(fpsf)
            else:
                metadict["error"] = "File " + str(fn) + " is not DPX file."

        except:
            metadict["error"] = "Can't open file " + str(fn)

        return metadict

    def read_metadata_from_exr_header(self):
        """ Read some metadata from exr header."""
        """
            from include/OpenEXR/ImfTimeCode.h:

              bits    packing for      packing for        packing for
                        24-frame       60-field         50-field
                        film          television        television
             0 -  3    frame units      frame units        frame units
             4 -  5    frame tens      frame tens        frame tens
             6        unused, set to 0  drop frame flag   unused, set to 0
             7        unused, set to 0  color frame flag  color frame flag
             8 - 11    seconds units      seconds units        seconds units
            12 - 14    seconds tens      seconds tens        seconds tens
            15        phase flag      field/phase flag  bgf0
            16 - 19    minutes units      minutes units        minutes units
            20 - 22    minutes tens      minutes tens        minutes tens
            23        bgf0          bgf0            bgf2
            24 - 27    hours units      hours units        hours units
            28 - 29    hours tens      hours tens        hours tens
            30        bgf1          bgf1            bgf1
            31        bgf2          bgf2            field/phase flag
        """

        def calc_res(data_window):
            if data_window is not None:
                w = int(data_window.get('xMax', 0)) - int(data_window.get('xMin', 0)) + 1
                h = int(data_window.get('yMax', 0)) - int(data_window.get('yMin', 0)) + 1
                return w, h
            return 0, 0

        exr_metadata = {}
        exr_fpstc = {}
        exr_metadata = parse_metadata.read_exr_header(self.meta['file'])

        try:
            # get resolutions from coordinates
            data_width, data_height = calc_res(exr_metadata.get('dataWindow'))
            if data_width > 0 and data_height > 0:
                exr_metadata['dataWindow_width'] = data_width
                exr_metadata['dataWindow_height'] = data_height
            display_width, display_height = calc_res(exr_metadata.get('displayWindow'))
            if display_width > 0 and display_height > 0:
                exr_metadata['displayWindow_width'] = display_width
                exr_metadata['displayWindow_height'] = display_height

            # this updates tc and framerate from ffprobe
            # to be taken from EX instead
            fps_a = int(exr_metadata['framesPerSecond']['first_num'])
            fps_b = int(exr_metadata['framesPerSecond']['second_num'])
            exr_metadata['fps_a'] = fps_a
            exr_metadata['fps_b'] = fps_b
            exr_metadata['fps_raw'] = '{}/{}'.format(
                str(exr_metadata['fps_a']),
                str(exr_metadata['fps_b']))  # "24/1"
            exr_metadata['fps'] = float(fps_a) / float(fps_b)
            exr_metadata['fps_str'] = helpers.get_fps_for_PyTimeCode(
                exr_metadata['fps'])

            tc = int(exr_metadata['timeCode']['timeAndFlags'])
            _f = str((tc >> 4) & 3) + str(tc & 15)
            _s = str((tc >> 12) & 7) + str((tc >> 8) & 15)
            _m = str((tc >> 20) & 7) + str((tc >> 16) & 15)
            _h = str((tc >> 28) & 3) + str((tc >> 24) & 15)
            _drop = ';' if bool((tc >> 6) & 1) else ':'
            exr_metadata['time_code'] = "{}:{}:{}{}{}".format(_h, _m, _s, _drop, _f)
        except Exception:
            pass
        return exr_metadata

    def exr_get_first_subimage_meta(self, oiio_meta):

        first_meta = {}
        if not oiio_meta:
            return first_meta
        if len(oiio_meta) == 0:
            return first_meta

        picked_meta = ['width', 'height', 'full_width', 'full_height', 'format', 'nchannels',]
        first_meta = oiio_meta[0].get('attribs')
        for one in picked_meta:
            if oiio_meta[0].get(one):
                first_meta[one] = oiio_meta[0].get(one)
        return first_meta

    def read_metadata_from_exr_oiio(self):

        if self.oiiotool_path is not None and os.path.exists(self.oiiotool_path):
            oiio_meta = self.get_oiio_info_for_input(self.meta['file'], oiio_path=self.oiiotool_path, subimages=True)
            first_meta = self.exr_get_first_subimage_meta(oiio_meta)
            chans = self.oiio_chanels_prep(oiio_meta)
            return {**first_meta, **chans}
        else:
            return {}

    def read_metadata_from_exr(self):
        header = self.read_metadata_from_exr_header()
        oiio = self.read_metadata_from_exr_oiio()
        exr_metadata_merged = {**header, **oiio}

        # add exr prefix to meta
        exr_renamed = {}
        for k, v in exr_metadata_merged.items():
            exr_renamed[f"metaExr_{str(k)}"] = v

        return exr_renamed

    def oiio_chanels_prep(self, oiio_meta):
        """
        make list of layers and list of layers and channels
        channels['layers_list'] == ['rgba', 'box1', 'circle1']
        channels['layers_extra_list'] == ['box1', 'circle1']
        channels['layers_channels_list'] == ['rgba.r', 'rgba.g', 'rgba.b', 'rgba.a', 'box1.matte', 'circle1.matte']
        channels['layers_channels_extra_list'] == ['box1.matte', 'circle1.matte']
        """

        # oiio_meta is list of dicts
        # list has more than one item for multipart exrs
        channels = {
            'layers_list': [],
            'layers_extra_list': [],
            'layers_channels_list': [],
            'layers_channels_extra_list': [],
            'layers_count': 0,
            'layers_extra_count': 0,
            'layers_channels_count': 0,
            'layers_channels_extra_count': 0,
            'layers': '',
            'layers_extra': '',
            'layers_channels': '',
            'layers_channels_extra': '',
            'layers_extra_summary': ''
        }

        if not oiio_meta:
            return channels
        subimages = len(oiio_meta)
        if subimages == 0:
            return channels

        default_name_1 = 'r'
        default_name_3 = 'rgb'
        default_name_4 = 'rgba'

        cnt = 0
        for one in oiio_meta:
            channel_names = one.get('channelnames', [])
            channel_number = one.get('nchannels', 3)
            if channel_number == 4:
                default_name = default_name_4
            elif channel_number == 1:
                default_name = default_name_1
            else:
                default_name = default_name_3

            # get subimage name
            subimage_name = None
            subimage_attribs = one.get('attribs')
            if subimage_attribs is not None:
                subimage_name_whole = subimage_attribs.get('name')
                if subimage_name_whole:
                    subimage_name = subimage_name_whole.split('.')[0]
            else:
                if cnt == 0:
                    # not multipart
                    subimage_name = default_name

            if (channel_names is not None) and (subimage_name is not None):
                if cnt == 0:
                    channels['layers_list'].append(subimage_name)
                else:
                    channels['layers_list'].append(subimage_name)
                    channels['layers_extra_list'].append(subimage_name)

                for one_chan in channel_names:
                    if one_chan is None:
                        continue
                    if cnt == 0:
                        # do not add first subimage to extra list
                        channels['layers_channels_list'].append(
                            subimage_name + '.' + one_chan.lower())
                    else:
                        channels['layers_channels_list'].append(
                            subimage_name + '.' + one_chan)
                        channels['layers_channels_extra_list'].append(
                            subimage_name + '.' + one_chan)
            cnt += 1
        # join lists and store counts
        summary = ""
        if len(channels['layers_channels_extra_list']) > 0:
            summary = f"{len(channels['layers_channels_extra_list'])} : {' '.join(channels['layers_channels_extra_list'])}"
        channels = {
            'layers_count': len(channels['layers_list']),
            'layers_extra_count': len(channels['layers_extra_list']),
            'layers_channels_count': len(channels['layers_channels_list']),
            'layers_channels_extra_count': len(channels['layers_channels_extra_list']),
            'layers': ' '.join(channels['layers_list']),
            'layers_extra': ' '.join(channels['layers_extra_list']),
            'layers_channels': ' '.join(channels['layers_channels_list']),
            'layers_channels_extra': ' '.join(channels['layers_channels_extra_list']),
            'layers_extra_summary' : summary
        }

        return channels

    class RationalToInt:
        """Rational value stored as division of 2 integers using string."""

        def __init__(self, string_value):
            parts = string_value.split("/")
            top = float(parts[0])
            bottom = 1.0
            if len(parts) != 1:
                bottom = float(parts[1])

            self._value = float(top) / float(bottom)
            self._string_value = string_value

        @property
        def value(self):
            return self._value

        @property
        def string_value(self):
            return self._string_value

        def __format__(self, *args, **kwargs):
            return self._string_value.__format__(*args, **kwargs)

        def __float__(self):
            return self._value

        def __str__(self):
            return self._string_value

        def __repr__(self):
            return "<{}> {}".format(self.__class__.__name__,
                                    self._string_value)

    def convert_value_by_type_name(self, value_type, value):
        """Convert value to proper type based on type name.

        In some cases value types have custom python class.
        """

        # Regex to parse array attributes
        ARRAY_TYPE_REGEX = re.compile(r"^(int|float|string)\[\d+\]$")

        # Simple types
        if value_type == "string":
            return value

        if value_type == "int":
            return int(value)

        if value_type in ("float", "double"):
            return float(value)

        # Vectors will probably have more types
        if value_type in ("vec2f", "float2", "float2d"):
            return [float(item) for item in value.split(",")]

        # Matrix should be always have square size of element 3x3, 4x4
        # - are returned as list of lists
        if value_type in ("matrix", "matrixd"):
            output = []
            current_index = -1
            parts = value.split(",")
            parts_len = len(parts)
            if parts_len == 1:
                divisor = 1
            elif parts_len == 4:
                divisor = 2
            elif parts_len == 9:
                divisor = 3
            elif parts_len == 16:
                divisor = 4
            else:
                for part in parts:
                    output.append(float(part))
                return output

            for idx, item in enumerate(parts):
                list_index = idx % divisor
                if list_index > current_index:
                    current_index = list_index
                    output.append([])
                output[list_index].append(float(item))
            return output

        if value_type == "rational2i":
            return self.RationalToInt(value)

        if value_type in ("vector", "vectord"):
            parts = [part.strip() for part in value.split(",")]
            output = []
            for part in parts:
                if part == "-nan":
                    output.append(None)
                    continue
                try:
                    part = float(part)
                except ValueError:
                    pass
                output.append(part)
            return output

        if value_type == "timecode":
            return value

        # Array of other types is converted to list
        re_result = ARRAY_TYPE_REGEX.findall(value_type)
        if re_result:
            array_type = re_result[0]
            output = []
            for item in value.split(","):
                output.append(
                    self.convert_value_by_type_name(array_type, item)
                )
            return output

        return value

    def parse_oiio_xml_output(self, xml_string):
        """Parse xml output from OIIO info command."""

        STRING_TAGS = {
            "format"
        }
        INT_TAGS = {
            "x", "y", "z",
            "width", "height", "depth",
            "full_x", "full_y", "full_z",
            "full_width", "full_height", "full_depth",
            "tile_width", "tile_height", "tile_depth",
            "nchannels",
            "alpha_channel",
            "z_channel",
            "deep",
            "subimages",
        }
        XML_CHAR_REF_REGEX_HEX = re.compile(r"&#x?[0-9a-fA-F]+;")

        PREFERRED_CHANNELS = [
            ['R', 'G', 'B', 'A'],
            ['r', 'g', 'b', 'a'],
            ['R', 'G', 'B'],
            ['r', 'g', 'b'],
            ['beauty.R', 'beauty.G', 'beauty.B', 'beauty.A'],
            ['beauty.R', 'beauty.G', 'beauty.B']
        ]
        output = {}
        if not xml_string:
            return output

        # Fix values with ampresand (lazy fix)
        # - oiiotool exports invalid xml which ElementTree can't handle
        #   e.g. "&#01;"
        # WARNING: this will affect even valid character entities. If you need
        #   those values correctly, this must take care of valid character ranges.
        #   See https://github.com/pypeclub/OpenPype/pull/2729
        matches = XML_CHAR_REF_REGEX_HEX.findall(xml_string)
        for match in matches:
            new_value = match.replace("&", "&amp;")
            xml_string = xml_string.replace(match, new_value)

        tree = xml.etree.ElementTree.fromstring(xml_string)
        attribs = {}
        output["attribs"] = attribs
        for child in tree:
            tag_name = child.tag
            if tag_name == "attrib":
                attrib_def = child.attrib
                value = self.convert_value_by_type_name(
                    attrib_def["type"], child.text
                )

                attribs[attrib_def["name"]] = value
                continue

            # Channels are stored as tex on each child
            if tag_name == "channelnames":
                value = []
                for channel in child:
                    value.append(channel.text)

            # Convert known integer type tags to int
            elif tag_name in INT_TAGS:
                value = int(child.text)

            # Keep value of known string tags
            elif tag_name in STRING_TAGS:
                value = child.text

            # Keep value as text for unknown tags
            # - feel free to add more tags
            else:
                value = child.text

            output[child.tag] = value

        return output

    def get_oiio_info_for_input(self, my_file, oiio_path, subimages=True):
        """Call oiiotool to get information about input and return stdout.

        Stdout should contain xml format string.
        """

        def run_subprocess(*args, **kwargs):

            kwargs["stdout"] = subprocess.PIPE
            kwargs["stderr"] = subprocess.PIPE
            kwargs["stdin"] = subprocess.PIPE
            proc = subprocess.Popen(*args, **kwargs)
            full_output = ""
            _stdout, _stderr = proc.communicate()
            if _stdout:
                _stdout = _stdout.decode("utf-8", errors="backslashreplace")
                full_output += _stdout
            if _stderr:
                _stderr = _stderr.decode("utf-8", errors="backslashreplace")
                if full_output:
                    full_output += "\n"
                full_output += _stderr
            if proc.returncode != 0:
                exc_msg = "Executing arguments was not successful: \"{}\"".format(
                    args)
                if _stdout:
                    exc_msg += "\n\nOutput:\n{}".format(_stdout)
                if _stderr:
                    exc_msg += "Error:\n{}".format(_stderr)
            return full_output

        args = [
            oiio_path,
            "--info",
            "-v"
        ]
        if subimages:
            args.append("-a")

        args.extend(["-i:infoformat=xml", my_file])

        output = run_subprocess(args)
        output = output.replace("\r\n", "\n")

        xml_started = False
        subimages_lines = []
        lines = []
        for line in output.split("\n"):
            if not xml_started:
                if not line.startswith("<"):
                    continue
                xml_started = True

            if xml_started:
                lines.append(line)
                if line == "</ImageSpec>":
                    subimages_lines.append(lines)
                    lines = []

        if not xml_started:
            raise ValueError(
                "Failed to read input file \"{}\".\nOutput:\n{}".format(
                    my_file, output
                )
            )

        output = []
        for subimage_lines in subimages_lines:
            xml_text = "\n".join(subimage_lines)
            output.append(self.parse_oiio_xml_output(xml_text))

        if subimages:
            return output
        return output[0]

if __name__ == "__main__":
    pass
