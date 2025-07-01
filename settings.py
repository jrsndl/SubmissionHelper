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

        self.install_settings = None
        self.read_install()

        # start by reading last settings
        self.find_all()
        self.read(name)

        # merge install settings to settings
        #self.settings = {**self.settings, **self.install_settings}

    def read_install(self):

        pth = self._get_script_path() + '/install.json'
        try:
            with open(pth, 'r') as json_data:
                self.install_settings = json.load(json_data)

            # replace relative path in ffprobe path
            if self.install_settings is not None:
                if self.install_settings['ffprobe_path']:
                    if self.install_settings['ffprobe_path'].startswith('./'):
                        _p = self._get_script_path() + self.install_settings[
                                                           'ffprobe_path'][1:]
                if self.install_settings['ffmpeg_path']:
                    if self.install_settings['ffmpeg_path'].startswith('./'):
                        _p = self._get_script_path() + self.install_settings[
                                                           'ffmpeg_path'][1:]
                        self.install_settings['ffprobe_path'] = _p
                if self.install_settings['oiio_path']:
                    if self.install_settings['oiio_path'].startswith('./'):
                        _p = self._get_script_path() + self.install_settings[
                                                           'oiio_path'][1:]
                        self.install_settings['oiio_path'] = _p

                if self.install_settings['ayon_path']:
                    if self.install_settings['ayon_path'].startswith('./'):
                        _p = self._get_script_path() + self.install_settings[
                                                           'ayon_path'][1:]
                        self.install_settings['ayon_path'] = _p

        except Exception:
            # no prefs found
            self.log.error("-> Error opening install prefs file {}".format(
                str(pth)))

    def read(self, name):
        """
        Reads settings from HDD
        :param name: the file name of the settings on hdd, no ext, no path
        it is either full path, or just name with no extension and no path
        :return: sets self.settings
        """

        self.log.debug('-> settings_read')
        is_full_path = False
        if os.path.exists(name):
            is_full_path = True
            prefs_path = name.replace('\\', '/')
        else:
            name_json = name + '.json'
            _gsp = self.get_settings_path()
            prefs_path = None
            if _gsp:
                prefs_path = os.path.join(_gsp, name_json).replace('\\', '/')
            if not prefs_path:
                prefs_path = os.path.join(
                    self._get_script_path(), name_json).replace('\\', '/')

            if not os.path.exists(prefs_path):
                self.log.warning("{} settings file not found, trying default."
                                 .format(str(name_json)))
                prefs_path = self._get_script_path() + '/default.json'

        if os.path.exists(prefs_path):
            self.log.debug("Reading settings from {}".format(prefs_path))
            try:
                with open(prefs_path, 'r') as json_data:
                    self.settings = json.load(json_data)
                self.current_settings_name = name
            except Exception:
                # no prefs found
                self.log.error("-> Error opening prefs file {}. Trying Default.".format(
                    str(prefs_path)))
                try:
                    prefs_path = self._get_script_path() + '/default.json'
                    with open(prefs_path, 'r') as json_data:
                        self.settings = json.load(json_data)
                    self.current_settings_name = 'default'
                except Exception:
                    self.log.error(
                        "-> Error opening default prefs file {}.".format(
                            str(prefs_path)))
        else:
            self.log.error("-> error opening prefs file {}"
                           .format(str(prefs_path)))

    def write(self, name):
        """
        Writes self.settings to hdd as json
        """

        self.log.debug('-> gui_write_preferences')
        name_json = name + '.json'

        _gsp = self.get_settings_path()
        if _gsp:
            prefs_path = os.path.join(_gsp, name_json).replace('\\', '/')

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

        # local prefs path
        all_files = self._find_in_dir(self.get_user_settings_path())
        _gsp = self.get_global_settings_path()
        if _gsp:
            # replace by global prefs path
            all_files = self._find_in_dir(_gsp)
            self.log.debug('-> reading prefs from global prefs folder')
        # always add app root path
        all_files += self._find_in_dir(self._get_script_path())
        all_files.sort()
        self.preset_names = []
        for one_file in all_files:
            self.preset_names.append(
                os.path.splitext(os.path.basename(one_file))[0])
        self.preset_names.sort()

    def _get_script_path(self):

        if getattr(sys, 'frozen', False):
            pth = os.path.dirname(sys.executable).replace("\\", "/")
        else:
            pth = os.path.dirname(__file__).replace("\\", "/")

        self.log.debug('-> App Location: {}'.format(pth))
        return pth
        """
        return os.path.dirname(
            os.path.abspath(inspect.stack()[-1][1])).replace("\\", "/")
        """

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

    def get_global_settings_path(self):
        _p = None
        if self.install_settings is not None:
            if bool(self.install_settings['global_prefs_enabled']):
                if self.install_settings['global_prefs_path']:
                    if os.path.exists(
                            self.install_settings['global_prefs_path']):
                                _p = self.install_settings['global_prefs_path']
                                _p + _p.replace('\\', '/')
        return _p

    def get_settings_path(self):
        self.get_global_settings_path()
        if self.get_global_settings_path():
            return self.get_global_settings_path()
        else:
            return self.get_user_settings_path()


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
                if one_file != 'install.json':
                    files.append(_dir + '/' + one_file)
        return files
