import sys
import os
import json
import inspect
import logging

class Settings(object):
    def __init__(self, name, args):
        self.settings = None

        self.log = logging.getLogger("Settings")
        #self.log.setLevel(logging.DEBUG)

        self.app_name = "SubmissionHelper"
        self.preset_names = []
        self.current_settings_name = ""

        self.install_settings = None
        self.read_install()

        # start by reading last settings
        self.find_all()
        self.read(name)

        self.args = args

        # merge install settings to settings
        #self.settings = {**self.settings, **self.install_settings}

    def read_install(self):
        def fix_path(pth, do_exe=True):
            pth_value = self.install_settings.get(pth, None)
            if pth_value is not None and pth_value != "":
                if pth_value.startswith('./'):
                    pth_value = self._get_script_path() + pth_value[1:]
                    if sys.platform == "win32":
                        if do_exe:
                            if not pth_value.endswith('.exe'):
                                pth_value = f"{pth_value}.exe"
                    else:
                        if pth_value.endswith('.exe'):
                            # rstrip(".exe") strips characters, not the suffix
                            pth_value = pth_value[:-len('.exe')]
                self.install_settings[pth] = pth_value

        install_path = self._get_script_path() + '/install.json'
        if not os.path.exists(install_path):
            self.log.info("No install prefs file {}, using defaults".format(install_path))
            return
        try:
            self.install_settings = self._load_json(install_path)

            # replace relative path in ffprobe path
            if self.install_settings is not None:
                pths = ['ffprobe_path', 'ffmpeg_path', 'oiio_path', 'ayon_path', 'vfx-transcode_path']
                for pth in pths:
                    fix_path(pth, do_exe=True)
                pths_noexe = ['ocio_path']
                for pth in pths_noexe:
                    fix_path(pth, do_exe=False)
        except Exception:
            self.log.exception("-> Error opening install prefs file {}".format(install_path))

    def _load_json(self, pth):
        """
        Load json file, return dict or None on failure
        """
        try:
            try:
                with open(pth, 'r', encoding='utf-8-sig') as json_data:
                    data = json.load(json_data)
            except UnicodeDecodeError:
                # presets written by older versions used the system encoding
                with open(pth, 'r') as json_data:
                    data = json.load(json_data)
            if isinstance(data, dict):
                return data
            self.log.error("-> Prefs file {} does not contain a json object".format(pth))
        except Exception:
            self.log.exception("-> Error opening prefs file {}".format(pth))
        return None

    def read(self, name):
        """
        Reads settings from HDD
        :param name: the file name of the settings on hdd, no ext, no path
        it is either full path, or just name with no extension and no path
        :return: sets self.settings (always a dict, empty if nothing found)
        """

        self.log.debug('-> settings_read')
        candidates = []
        if os.path.isfile(name):
            candidates.append(name.replace('\\', '/'))
        else:
            name_json = name + '.json'
            # settings folder (global or user) first, then presets shipped with the app
            _gsp = self.get_settings_path()
            if _gsp:
                candidates.append(os.path.join(_gsp, name_json).replace('\\', '/'))
            candidates.append(os.path.join(self._get_script_path(), name_json).replace('\\', '/'))

        for prefs_path in candidates:
            if os.path.isfile(prefs_path):
                self.log.debug("Reading settings from {}".format(prefs_path))
                data = self._load_json(prefs_path)
                if data is not None:
                    self.settings = data
                    self.current_settings_name = name
                    return

        self.log.warning("{} settings file not found or invalid, trying default.".format(name))
        default_path = self._get_script_path() + '/default.json'
        data = self._load_json(default_path) if os.path.isfile(default_path) else None
        if data is None:
            self.log.warning("-> No usable default.json, starting with built-in gui defaults.")
            data = {}
        self.settings = data
        # don't keep the requested name, saving would overwrite that preset with defaults
        self.current_settings_name = 'default'

    def write(self, name):
        """
        Writes self.settings to hdd as json
        """

        self.log.debug('-> gui_write_preferences')
        name_json = name + '.json'

        prefs_path = os.path.join(self.get_settings_path(), name_json).replace('\\', '/')
        os.makedirs(os.path.dirname(prefs_path), exist_ok=True)

        with open(prefs_path, 'w', encoding='utf-8') as outfile:
            json.dump(
                self.settings,
                outfile,
                # ascii output reads correctly with any encoding, also in older versions
                ensure_ascii=True,
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

        #self.log.debug('-> App Location: {}'.format(pth))
        return pth
        """
        return os.path.dirname(
            os.path.abspath(inspect.stack()[-1][1])).replace("\\", "/")
        """

    def get_user_settings_path(self):
        if sys.platform.startswith('darwin'):
            # from AppKit import NSSearchPathForDirectoriesInDomains
            # appdata = NSSearchPathForDirectoriesInDomains(14, 1, True)[0]
            appdata = os.path.join(os.path.expanduser('~'), self.app_name)
        elif str(os.name).startswith('posix'):
            appdata = os.path.join(os.path.expanduser('~'), self.app_name)
        else:
            appdata = os.environ.get('APPDATA') or os.path.expanduser('~')
            appdata = os.path.join(appdata, self.app_name)
            appdata = appdata.replace('\\', '/')
        return appdata

    def get_global_settings_path(self):
        _p = None
        if self.install_settings is not None:
            enabled = self.install_settings.get('global_prefs_enabled', False)
            if isinstance(enabled, str):
                enabled = enabled.strip().lower() in ('1', 'true', 'yes', 'on')
            gpath = self.install_settings.get('global_prefs_path')
            if enabled and gpath and os.path.isdir(gpath):
                _p = gpath.replace('\\', '/')
        return _p

    def get_settings_path(self):
        _gsp = self.get_global_settings_path()
        if _gsp:
            return _gsp
        return self.get_user_settings_path()


    @staticmethod
    def _find_in_dir(dir_path):

        files = []
        # don't fall back to the parent folder, that would list every json
        # in the home / APPDATA folder as a preset
        if not dir_path or not os.path.isdir(dir_path):
            return files
        _dir = dir_path
        for one_file in os.listdir(_dir):
            if one_file.endswith(".json"):
                if one_file != 'install.json':
                    files.append(_dir + '/' + one_file)
        return files
