import os
import pprint
import httpx
import ayon_api

import csv
import logging
import os

class AyonShotlist(object):
    def __init__(self, ayon_gui, settings, paths):
        self.error = None
        self.log = logging.getLogger("mylog")
        os.environ["AYON_SERVER_URL"] = paths['AYON_SERVER_URL']
        os.environ["AYON_API_KEY"] = paths['AYON_API_KEY']


        self.error = None
        try:
            self.ayon = ayon_api.get_server_api_connection()
        except Exception as e:
            error = f"Error connecting to Ayon: {e}"
            print(error)
            self.error = error
            return

        self.project = ayon_gui['project']
        self.projects = None
        self.settings = settings
        self.ayon_gui = ayon_gui

        self.prefix = ayon_gui['prefix']
        self.do_thumbs = ayon_gui['do_thumbs']
        self.output_folder = ayon_gui['out_folder'].replace("\\", "/")
        self.thumbs_dir = f"{self.output_folder}/_thumbsDownload"

        # where to put thumbnails and shotlist
        self.output_folder = ayon_gui['out_folder']
        self.do_output_csv = ayon_gui['do_csv']
        self.output_csv_path = f"{self.output_folder}/list.csv"
        self.do_output_excel = ayon_gui['do_excel']
        self.output_excel_path = f"{self.output_folder}/list.xls"
        self.do_output = True
        self.prep_paths()

        self.data = []

        self.columns = [
            "Thumbnail",
            "Folder Name",
            "Folder Path",
            "Folder Type",
            "Task Type",
            "Task Name",
            "Task Assignees",
            "Range",
            "Length",
            "In",
            "Out",
            "Head",
            "Tail",
            "Width",
            "Height",
            "Pixel Aspect",
            "Clip In",
            "Clip Out",
            "Folder Label",
            "Folder Status",
            "Task Label",
            "Task Status",
            "Links",
            "_hide"
        ]

        self.task_empty = {
            "Task Type": "",
            "Task Name": "",
            "Task Label": "",
            "Task Status": "",
            "Task Assignees": ""
        }

    def get_projects(self):
        if self.error is None:
            self.projects = self.ayon.get_projects()

    def project_exists(self):
        if self.error is None:
            if self.project in self.projects:
                return True
            else:
                return False

    def prep_paths(self):

        if self.do_thumbs:
            try:
                os.makedirs(self.thumbs_dir, exist_ok=True)
            except OSError as e:
                self.log.error(f"Error creating thumbs dir: {e}")
                self.do_thumbs = False
        try:
            os.makedirs(os.path.dirname(self.output_folder), exist_ok=True)
        except OSError as e:
            self.log.error(f"Error creating output dir: {e}")
            self.do_output = False

    @staticmethod
    def attribs_to_columns(a):
        fin = int(a["frameStart"]) - int(a["handleStart"])
        fout = int(a["frameEnd"]) - int(a["handleEnd"])
        d = {
            "Range": f"{fin}-{fout}",
            "Length": str(fout - fin + 1),
            "In": str(a["frameStart"]),
            "Out": str(a["frameEnd"]),
            "Head": str(a["handleStart"]),
            "Tail": str(a["handleEnd"]),
            "Width": str(a["resolutionWidth"]),
            "Height": str(a["resolutionHeight"]),
            "Pixel Aspect": str(a["pixelAspect"]),
            "Clip In": str(a["clipIn"]),
            "Clip Out": str(a["clipOut"]),
        }
        return d

    def set_filters(self, ayon_gui):
        self.ayon_gui = ayon_gui

    def filter_shotlist(self):
        if self.ayon_gui is None or len(self.ayon_gui) == 0:
            return

        for one in self.data:

            is_task = False
            if "task" in one['Folder Type'].lower():
                is_task = True
            folder_type = ''
            if len(one['Folder Type']) > 0:
                _s = one['Folder Type'].lower().split('/')
                folder_type = _s[0]

            hide = True
            asset_or_shot = False

            if self.ayon_gui['filter_tasks']:
                if is_task:
                    hide = False
                    # only check task types if tasks are allowed
                    if self.ayon_gui['filter_tasktype']:
                        if one["Task Type"].lower() in self.ayon_gui['filter_tasktypes']:
                            hide = False
                        else:
                            hide = True
                else:
                    # it is not a task
                    if self.ayon_gui['filter_assets'] and "asset" in one[
                        'Folder Type'].lower():
                        hide = False
                        asset_or_shot = True
                    if self.ayon_gui['filter_shots'] and "shot" in one[
                        'Folder Type'].lower():
                        hide = False
                        asset_or_shot = True
                    # if hide is true, it is not asset or shot, so it IS "other"
                    if self.ayon_gui['filter_other'] and not asset_or_shot:
                        hide = False
            else:
                if self.ayon_gui['filter_assets'] and "asset" in folder_type:
                    hide = False
                    asset_or_shot = True
                if self.ayon_gui['filter_shots'] and "shot" in folder_type:
                    hide = False
                    asset_or_shot = True
                # if hide is true, it is not asset or shot, so it IS "other"
                if self.ayon_gui['filter_other'] and not asset_or_shot:
                    hide = False

                # hide again rows that are tasks, if tasks are not wanted
                if is_task:
                    hide = True

            if self.ayon_gui['filter_assignee']:
                if one["Task Assignees"].lower() in self.ayon_gui['filter_assignees']:
                    hide = False
                else:
                    hide = True

            one["_hide"] = hide


    def get_shotlist(self):
        if self.error is None:
            self.get_full_shotlist()
            self.filter_shotlist()
            return self.data

    def get_full_shotlist(self):

        def get_links(folder_id):
            links = self.ayon.get_folder_links(
                self.project, folder_id, link_direction="in"
            )
            linked_folder_ids = {
                link["entityId"]
                for link in links
                if link["entityType"] == "folder"
            }
            if not linked_folder_ids:
                return []
            return list(self.ayon.get_folders(
                self.project, folder_ids=linked_folder_ids
            ))

        # get folders
        asset_entities = self.ayon.get_folders(self.project,
                                               fields={
                                                   "name",
                                                   "id",
                                                   "path",
                                                   "type",
                                                   "label",
                                                   "status",
                                                   "hasTasks",
                                                   "attrib",
                                                   "thumbnailId"})

        try:
            asset_entities = {f["name"]: f for f in asset_entities}
        except Exception as e:
            error = f"Error getting assets from Ayon: {e}"
            print(error)
            self.error = error
            return


        # get folders + tasks and their attribs
        data = []
        for asset_name, asset in asset_entities.items():
            link_list = get_links(asset["id"])
            if link_list is not None and len(link_list) > 0:
                #print(f"{asset_name} Link List:")
                #pprint.pprint(link_list)
                pass

            thumb_name_folder = asset["path"].replace("/", "-").strip("-")
            thumbnail_path = None
            if asset["thumbnailId"] is not None and self.do_thumbs:
                thumbnail = self.ayon.get_thumbnail_by_id(
                    self.project, asset["thumbnailId"])
                thumbnail_path = f"{self.thumbs_dir}/{thumb_name_folder}.png"
                with open(thumbnail_path, "wb") as stream:
                    stream.write(thumbnail.content)
                if not os.path.isfile(thumbnail_path):
                    thumbnail_path = None

            base = {
                "Thumbnail": thumbnail_path,
                "Folder Type": asset["type"],
                "Folder Name": asset_name,
                "Folder Path": asset["path"],
                "Folder Label": asset["label"],
                "Folder Status": asset["label"],
                "Links": " ".join(link_list)
            }
            attrs = self.attribs_to_columns(asset["attrib"])
            shot_clean = {**base, **attrs}
            shot_only = {**shot_clean, **self.task_empty}
            data.append(shot_only)

            if asset["hasTasks"]:
                task_entities = self.ayon.get_tasks(self.project, folder_ids={asset["id"]},
                                                   fields={"name",
                                                           "id",
                                                           "type",
                                                           "label",
                                                           "assignees",
                                                           "status",
                                                           "attrib",
                                                           'thumbnailId'})
                task_entities = {f["name"]: f for f in task_entities}
                for task_name, task_info in task_entities.items():
                    thumb_name_task = thumb_name_folder + "-task-" + task_name
                    thumbnail_path = None
                    if task_info["thumbnailId"] is not None and self.do_thumbs:
                        thumbnail = self.ayon.get_thumbnail_by_id(
                            self.project, task_info["thumbnailId"])
                        thumbnail_path = f"{self.thumbs_dir}/{thumb_name_task}.png"
                        with open(thumbnail_path, "wb") as stream:
                            stream.write(thumbnail.content)
                        if not os.path.isfile(thumbnail_path):
                            thumbnail_path = None
                    tsk = {
                        "Task Type": task_info["type"],
                        "Task Name": task_info["name"],
                        "Task Label": task_info["label"],
                        "Task Status": task_info["status"],
                        "Task Assignees": " ".join(task_info["assignees"])
                    }
                    shot_task = {**shot_clean, **tsk}
                    shot_task["Folder Type"] = f'{shot_task["Folder Type"]}/Task'
                    shot_task_attr = {**shot_task, **self.attribs_to_columns(task_info["attrib"])}
                    data.append(shot_task_attr)
        self.data = sorted(data, key=lambda d: d['Folder Path'])

    def write_csv(self):
        if self.data is not None and len(self.data) > 0:
            with open(self.output_csv_path, 'w', newline='') as output_file:
                dict_writer = csv.DictWriter(output_file, self.columns)
                dict_writer.writeheader()
                dict_writer.writerows(self.data)


if __name__ == "__main__":
    project = "HH"
    output_folder = "D:/_code/SubmissionHelper/output"
    do_thumbs = True
    gui = None
    ayon_server_url = "http://192.168.0.162:5000"

    # just a test api key to test ayon instance here,
    my_ayon = AyonShotlist(
        project,
        output_folder,
        do_thumbs,
        gui,
        ayon_server_url,
        ""
        )