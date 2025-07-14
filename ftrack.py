import pprint
import csv
import ftrack_api

class FtrackHelper(object):

    def __init__(self, gui, pths):
        self.settings = gui
        self.paths = pths
        self.ftrack = {}
        self.get_ftrack_session()

    def get_ftrack_info(self):
        """
        Get ftrack info for current project
        Gathers assets and shots with all links and selected other attributes
        :return:
        """

        def traverse(itms, itm_type="Shot"):
            def get_all_link_names(links, mode="from"):
                l = []
                if links is not None:
                    for link in links:
                        l.append(link.get(mode, {}).get('name'))
                return l

            attribs = ["id", "name", "incoming_links", "outgoing_links", "description", "ancestors", "descendants", "parent_id"]
            my_itms = []
            for shot in itms:
                one = {}
                for a in attribs:
                    one[a] = shot.get(a)

                """
                t = shot.get("thumbnail_url")
                if t is not None:
                    one['thumbnail_url'] = t.get("url")
                """

                # shot or asset?
                one['type'] = itm_type

                # make path
                anc = shot.get("ancestors")
                if anc is not None:
                    p = []
                    for a in anc:
                        p.append(a['name'])
                    p = sorted(p)
                    one['path'] = "/" + "/".join(p) + "/" + one['name']

                # desc name:desc type, another name: another type
                dsc = shot.get("descendants")
                if dsc is not None:
                    try:
                        p = []
                        for a in dsc:
                            p.append(f"{a.get('name', 'unknown')}:{a.get('type', {}).get('name', 'unknown')}")
                        p = sorted(p)
                        one['desc'] = ", ".join(p)
                    except Exception as e:
                        pass

                # get in links
                lnk = sorted(get_all_link_names(shot.get("incoming_links"), "from"))
                one['links_in'] = ", ".join(lnk)
                lnk = sorted(get_all_link_names(shot.get("outgoing_links"), "to"))
                one['links_out'] = ", ".join(lnk)

                my_itms.append(one)
            return my_itms

        try:
            #shots = self.ftrack['session'].query('select id, name, thumbnail_url, incoming_links, outgoing_links, ancestors, descendants, parent_id from Shot where project.id is "{0}"'.format(self.ftrack['project_id'])).all()
            shots = self.ftrack['session'].query(
                'select id, name, incoming_links, outgoing_links, ancestors, descendants, parent_id from Shot where project.id is "{0}"'.format(
                    self.ftrack['project_id'])
            ).all()
            s = traverse(shots, "Shot")
        except:
            s = []

        try:
            assets = self.ftrack['session'].query(
                'select id, name, incoming_links, outgoing_links, ancestors, descendants, parent_id from AssetBuild where project.id is "{0}"'.format(
                    self.ftrack['project_id'])
            ).all()
            a = traverse(assets, "Asset Build")
        except:
            a = []

        self.ftrack['info'] = a + s

    def ftrack_info_to_csv(self, csv_path):

        if self.ftrack.get('info') is None:
            return
        if len(self.ftrack['info']) == 0:
            return

        self.columns = [
            "Thumbnail",
            "Folder Name",
            "Folder Path",
            "Folder Type",
            "Tasks",
            "Links In",
            "Links Out",
        ]

        ftrack_table = []
        for one in self.ftrack['info']:
            line = {
                "Thumbnail": one.get('thumbnail_url', ''),
                "Folder Name": one.get('name', ''),
                "Folder Path": one.get('path', ''),
                "Folder Type": one.get('type', ''),
                "Tasks": one.get('desc', ''),
                "Links In": one.get('links_in', ''),
                "Links Out": one.get('links_out', '')
            }
            ftrack_table.append(line)
        if len(ftrack_table) == 0:
            return

        ftrack_table_sorted = sorted(ftrack_table, key=lambda d: d['Folder Path'])

        pprint.pprint(ftrack_table_sorted)

        with open(csv_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=ftrack_table_sorted[0].keys())
            writer.writeheader()
            for row in ftrack_table_sorted:
                writer.writerow(row)

    def _get_ftrack_assets_simple(self):
        assets = self.ftrack['session'].query(
            'AssetBuild where project.id is "{0}"'.format(self.ftrack['project_id'])
        ).all()
        for asset in assets:
            print(asset['name'])
        self.ftrack['assets'] = assets

    def _get_ftrack_shots_simple(self):
        shots = self.ftrack['session'].query(
            'Shot where project.id is "{0}"'.format(self.ftrack['project_id'])
        ).all()
        for shot in shots:
            print(shot['name'])
        self.ftrack['shots'] = shots

    def _get_ftrack_shot_links_simple(self):
        shots = self.ftrack['shots']
        for shot in shots:
            print(f"--- Shot: {shot['name']}")
            for link in shot['incoming_links']:
                from_link = link.get('from')
                if from_link is not None:
                    print(f"--- Incoming: {from_link['name']}")

    def _get_ftrack_asset_links_simple(self):
        assets = self.ftrack['assets']
        for asset in assets:
            print(f"--- Asset: {asset['name']}")
            for link in asset['outgoing_links']:
                from_link = link.get('to')
                if from_link is not None:
                    print(f"--- Outgoing: {from_link['name']}")

    def is_session_ok(self):
        if self.ftrack is None:
            return False
        if self.ftrack.get('session') is None:
            return False
        if self.ftrack.get('project_id') is None:
            return False
        return True

    def get_ftrack_session(self):
        """
        Reads ftrack project name
        Tries to connect to Ftrack
        Tries to query project id from project name and
        label object from label name

        :return:
        self.ftrack dict with ftrack session and project id
        """

        if self.settings:
            self.ftrack['do_ftrack'] = bool(
                self.settings['ftrack_use']['value'])
            self.ftrack['project'] = str(
                self.settings['ftrack_project']['value'])

            self.ftrack['session'] = None
            self.ftrack['project_id'] = None
            self.ftrack['all_projects'] = None
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
                        self.ftrack['all_projects'] = self.ftrack['session'].query(
                            'Project where status is "Active"').all()
                        for p in self.ftrack['all_projects']:
                            if p["full_name"] == self.ftrack['project']:
                                self.ftrack['project_id'] = p["id"]
                    except ftrack_api.exception.NoResultFoundError:
                        print('FTRACK failed')
                        pass