# -*- coding: utf-8 -*-
import os
import pprint
import sys
import subprocess
import struct
import logging

from xml.etree import ElementTree as et
from PyTimeCode import PyTimeCode
import helpers
import inspect
import logging


class MetaData(object):

    def __init__(self, item, gui, gui_force_fps=False, gui_fps='24'):

        self.log = logging.getLogger("mylog")
        self.settings = gui

        self.gui_fps = '24'
        if self.settings['prefs_frame_rate']['value'] is not None:
            self.gui_fps = self.settings['prefs_frame_rate']['value']

        self.gui_force_fps = False
        if self.settings['prefs_frame_rate_use_meta']['value'] is not None:
            self.gui_force_fps = \
                not self.settings['prefs_frame_rate_use_meta']['value']

        self.default_tc = '01:00:00:00'
        if self.settings['prefs_tc_default']['value'] is not None:
            self.default_tc = str(self.settings['prefs_tc_default']['value'])

        # get file path
        self.item = item

        self.meta = {'file': item['path'], 'error': '', 'width': 0, 'height': 0,
                     'fps_str': '', 'fps': 0.0, 'fps_a': 0, 'fps_b': 0, 'duration_frames': 0, 'duration_secs': 0.0,
                     'bitrate_video': 0, 'aspect': 0.0, 'aspect_x': 0, 'aspect_y': 0,
                     'codec_name_video': '', 'codec_long_name_video': '', 'time_stamp_video': '', 'fields': 0,
                     'time_code': '', 'reel': '',
                     'sample_rate_audio': 0, 'channels_audio': 0, 'bits_per_sample_audio': 0,
                     'duration_audio': 0.0, 'bitrate_audio': 0, 'codec_name_audio': '',
                     'codec_long_name_audio': '', 'time_stamp_audio': '',
                     'video_present': 0, 'audio_present': 0, 'data_present': 0,
                     'is_log': False}

        self.platform, self.platform_extension = self.__get_platform()
        self.ffmpeg_path, self.ffprobe_path = self.__get_ffmpeg_path()
        self.__read_from_drive()
        self.meta_data = self.metadata_to_keywords()

    def metadata_to_keywords(self):

        meta_data = {
            'meta_file': self.meta['file'],
            'meta_error': self.meta['error'],
            'meta_width': str(self.meta['width']),
            'meta_height': str(self.meta['height']),
            'meta_fps': self.meta['fps_str'],
            'meta_fps_a': str(self.meta['fps_a']),
            'meta_fps_b': str(self.meta['fps_b']),
            'meta_fps_raw': self.meta['fps_raw'],
            'meta_duration_frames': str(self.meta['duration_frames']),
            'meta_duration_frames_slate': str(self.meta['duration_frames_slate']),
            'meta_duration_secs': str(self.meta['duration_secs']),
            'meta_bitrate_video': str(self.meta['bitrate_video']),
            'meta_aspect': str(self.meta['aspect']),
            'meta_aspect_x': str(self.meta['aspect_x']),
            'meta_aspect_y': str(self.meta['aspect_y']),
            'meta_codec_name_video': self.meta['codec_name_video'],
            'meta_codec_long_name_video': self.meta['codec_long_name_video'],
            'meta_time_stamp_video': self.meta['time_stamp_video'],
            'meta_fields': str(self.meta['fields']),
            'meta_time_code': self.meta['time_code'],
            'time_code_from_metadata': self.meta['time_code_from_metadata'],
            'time_code_from_seq': self.meta['time_code_from_seq'],
            'meta_reel': self.meta['reel'],
            'meta_sample_rate_audio': str(self.meta['sample_rate_audio']),
            'meta_channels_audio': str(self.meta['channels_audio']),
            'meta_bits_per_sample_audio': str(self.meta['bits_per_sample_audio']),
            'meta_duration_audio': str(self.meta['duration_audio']),
            'meta_bitrate_audio': str(self.meta['bitrate_audio']),
            'meta_codec_name_audio': self.meta['codec_name_audio'],
            'meta_codec_long_name_audio': self.meta['codec_long_name_audio'],
            'meta_time_stamp_audio': self.meta['time_stamp_audio'],
            'meta_video_present': str(self.meta['video_present']),
            'meta_audio_present': str(self.meta['audio_present']),
            'meta_data_present': str(self.meta['data_present']),
            'meta_is_log': str(self.meta['is_log']),
            'meta_frame_start_from_tc': str(self.meta['frame_start_from_tc']),
            'meta_frame_start_from_tc_slate': str(self.meta['frame_start_from_tc_slate']),
            'meta_frame_end_from_tc': str(self.meta['frame_end_from_tc']),
            'meta_frame_end_from_tc_slate': str(self.meta['frame_end_from_tc_slate']),
        }

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

        script_path = os.path.dirname(os.path.abspath(inspect.stack()[-1][1])).replace("\\", "/")
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
            self.meta.update(self.probe_ffprobe())
            #pprint.pprint(self.meta)

            if self.meta['error'] != '':
                if self.item['category'] in ff_categories:
                    self.log.warning("Problem getting metadata by ffprobe: {} for file {}"
                                     .format(self.meta['error'], fn))
                self.meta['error'] = ''

        # DPX:
        if my_extension == 'dpx':
            self.meta.update(self.read_metadata_from_dpx())

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
                                                                     fps=float(self.meta['fps_str']))

    def _frame_range_from_tc(self):
        if self.meta['file'] and self.meta['file'] != '':
            if self.item['category'] == 'video':

                if self.meta['fps_b'] > 0:
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
            elif not self.gui_force_fps:
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
                tree =et.fromstring(out)
                StreamFind = tree.find("streams")
                StreamList = StreamFind.findall("stream")
                for onestr in StreamList:
                    streamType = onestr.attrib['codec_type']

                    if streamType == 'video':
                        outdata['video_present'] = 1
                        try:
                            outdata['width'] = int(onestr.attrib['width'])
                        except:
                            pass

                        try:
                            outdata['height'] = int(onestr.attrib['height'])
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
                            pass

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


if __name__ == "__main__":
    pass










