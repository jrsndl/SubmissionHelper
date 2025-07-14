import ftrack_api

class FtrackHelper(object):

    def __init__(self, gui, pths):
        self.settings = gui
        self.paths = pths
        self.ftrack_list = None


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

            if self.ftrack['include'] is not None:
                self.ftrack['include'] = self.ftrack['include'].split()
            else:
                self.ftrack['include'] = []

            self.ftrack['session'] = None
            self.ftrack['project_id'] = None
            self.ftrack['label_obj'] = None
            if self.ftrack['do_ftrack']:
                self.ftrack['url'] = self.paths.get('FTRACK_SERVER', '')
                self.ftrack['key'] = self.paths.get('FTRACK_API_KEY', '')
                self.ftrack['user'] = self.paths.get('FTRACK_API_USER', '')
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
                        self.ftrack['label_obj'] = self.ftrack['session'] \
                            .query('NoteLabel where name is "{}"'.format(
                            self.ftrack['label'])).first()
                    except:
                        pass