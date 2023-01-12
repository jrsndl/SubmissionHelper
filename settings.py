import sys
import os
import json
import inspect
import logging


class Settings(object):
    def __init__(self, name):
        self.settings = None

        self.log = logging.getLogger("mylog")
        self.log.setLevel(logging.DEBUG)

        self.app_name = "SubmissionHelper"
        self.preset_names = []
        self.current_settings_name = ""

        # start by reading last settings
        self.find_all()
        self.read(name)

    def read(self, name):
        """
        Reads settings from HDD
        :param name: the file name of the settings on hdd, no ext, no path
        :return: sets self.settings
        """

        self.log.debug('-> settings_read')
        name_json = name + '.json'

        # try both possible prefs locations
        prefs_path = os.path.join(
            self.get_user_settings_path(), name_json).replace('\\', '/')
        if not os.path.exists(prefs_path):
            prefs_path = os.path.join(
                self._get_script_path(), name_json).replace('\\', '/')
        if os.path.exists(prefs_path):
            self.log.debug("Reading settings from {}".format(prefs_path))
            try:
                with open(prefs_path, 'r') as json_data:
                    self.settings = json.load(json_data)
                self.current_settings_name = name
            except IOError:
                # no prefs found
                self.log.error("-> Error opening prefs file {}".format(
                    str(prefs_path)))
        else:
            if name_json != 'Default':
                self.log.warning("-> {} settings file not found"
                                 .format(str(name_json)))
                self.read('Default')
            else:
                self.log.error("-> error opening prefs file {}"
                               .format(str(prefs_path)))

    def write(self, name):
        """
        Writes self.settings to hdd as json
        """

        self.log.debug('-> gui_write_preferences')
        name_json = name + '.json'
        prefs_path = os.path.join(
            self.get_user_settings_path(), name_json).replace('\\', '/')
        if not os.path.exists(os.path.dirname(prefs_path)):
            os.makedirs(os.path.dirname(prefs_path))
        with open(prefs_path, 'w') as outfile:
            json.dump(
                self.settings,
                outfile,
                ensure_ascii=False,
                indent=1,
                sort_keys=True)
        self.current_settings_name = name
        self.find_all()

    def find_all(self):
        """
        find all saved settings in user path and app path
        return as all_prefs_paths and all_prefs_names
        :return:
        self.preset_names
        """
        all_files = self._find_in_dir(self._get_script_path())
        all_files += self._find_in_dir(self.get_user_settings_path())
        all_files.sort()
        self.preset_names = []
        for one_file in all_files:
            self.preset_names.append(
                os.path.splitext(os.path.basename(one_file))[0])
        self.preset_names.sort()

    @staticmethod
    def _get_script_path():
        return os.path.dirname(
            os.path.abspath(inspect.stack()[-1][1])).replace("\\", "/")

    def get_user_settings_path(self):
        if sys.platform.startswith('darvin'):
            # from AppKit import NSSearchPathForDirectoriesInDomains
            # appdata = NSSearchPathForDirectoriesInDomains(14, 1, True)[0]
            appdata = os.path.join(os.path.expanduser('~'), self.app_name)
        elif str(os.name).startswith('posix'):
            appdata = os.path.join(os.path.expanduser('~'), self.app_name)
        else:
            appdata = os.environ['APPDATA']
            appdata = os.path.join(appdata, self.app_name)
            appdata = appdata.replace('\\', '/')
        return appdata

    @staticmethod
    def _find_in_dir(dir_path):

        files = []
        if os.path.isdir(dir_path):
            _dir = dir_path
        else:
            _dir = os.path.dirname(dir_path)
        if not os.path.exists(_dir):
            return files
        for one_file in os.listdir(_dir):
            if one_file.endswith(".json"):
                files.append(_dir + '/' + one_file)
        return files
