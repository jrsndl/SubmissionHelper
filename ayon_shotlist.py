import csv
import fnmatch
import logging
import os

import ayon_api

# columns added by "Pull versions"
VERSION_COLUMNS = [
    "Product",
    "Product Type",
    "Version",
    "Version Name",
    "Version Status",
    "Version Author",
    "Version Date",
    "Version Comment",
    "Version Task",
    "Representation",
    "Repre Path",
    "Version Filter",
]


def parse_product_filters(text):
    """
    Parse product filters "task:product:representation", separated by commas,
    semicolons or new lines. The task is optional:
        comp:renderCompMain:exr  -> task comp, product renderCompMain, repre exr
        :platePl01:exr           -> any task
        platePl01:exr            -> same as above
        :platePl01               -> any task, any representation
        renderComp*:exr          -> wildcards (* ? [..]) in any part, case insensitive
    An empty representation means any representation.
    :return: list of dicts {'task', 'product', 'repre', 'text'}, in the given order
    """
    out = []
    if not text:
        return out
    for one in text.replace(';', ',').replace('\n', ',').split(','):
        one = one.strip()
        if not one:
            continue
        parts = [x.strip() for x in one.split(':')]
        if len(parts) == 1:
            task, product, repre = '', parts[0], ''
        elif len(parts) == 2:
            if parts[0] == '':
                # ":product" - task skipped, any representation
                task, product, repre = '', parts[1], ''
            else:
                # "product:repre"
                task, (product, repre) = '', parts
        else:
            task, product, repre = parts[0], parts[1], ':'.join(parts[2:])
        if not product:
            continue
        out.append({'task': task, 'product': product, 'repre': repre, 'text': one})
    return out


def _match(pattern, value):
    """empty pattern matches anything, wildcards allowed, case insensitive"""
    if not pattern:
        return True
    return fnmatch.fnmatchcase(str(value or '').lower(), pattern.lower())


def _has_wildcard(pattern):
    return any(c in pattern for c in '*?[')


def pick_versions(folder_ids, products, last_versions, repres, task_names, filters):
    """
    For every folder pick the version of the preferred product.

    Filters are tried in order, the first filter that has a match wins. Within
    a filter, the highest version number of the matching products wins.

    :param folder_ids: iterable of folder ids
    :param products: list of product dicts (id, name, folderId, productType)
    :param last_versions: dict product id -> last version dict
                          (id, version, taskId, author, status, createdAt, attrib)
    :param repres: list of representation dicts (id, name, versionId, attrib)
    :param task_names: dict task id -> task name
    :param filters: from parse_product_filters
    :return: dict folder id -> dict with VERSION_COLUMNS values
    """
    products_by_folder = {}
    for p in products:
        products_by_folder.setdefault(p.get('folderId'), []).append(p)
    repres_by_version = {}
    for r in repres:
        repres_by_version.setdefault(r.get('versionId'), []).append(r)

    result = {}
    for folder_id in folder_ids:
        found = None
        for flt in filters:
            best = None
            for prod in products_by_folder.get(folder_id, []):
                if not _match(flt['product'], prod.get('name')):
                    continue
                ver = last_versions.get(prod.get('id'))
                if not ver:
                    continue
                task_name = task_names.get(ver.get('taskId'), '')
                if not _match(flt['task'], task_name):
                    continue
                ver_repres = [r for r in repres_by_version.get(ver.get('id'), [])
                              if _match(flt['repre'], r.get('name'))]
                if flt['repre'] and not ver_repres:
                    continue
                key = (int(ver.get('version') or 0), str(ver.get('createdAt') or ''))
                if best is None or key > best[0]:
                    best = (key, prod, ver, task_name, ver_repres[0] if ver_repres else None)
            if best is not None:
                found = (flt, best)
                break
        if found is None:
            continue
        flt, (_, prod, ver, task_name, repre) = found
        attrib = ver.get('attrib') or {}
        repre_attrib = (repre or {}).get('attrib') or {}
        repre_path = repre_attrib.get('path') or ''
        if not repre_path and repre and repre.get('files'):
            repre_path = (repre['files'][0] or {}).get('path', '')
        number = int(ver.get('version') or 0)
        result[folder_id] = {
            "Product": prod.get('name', ''),
            "Product Type": prod.get('productType', ''),
            "Version": str(number),
            "Version Name": f"v{number:03d}",
            "Version Status": ver.get('status') or '',
            "Version Author": ver.get('author') or '',
            "Version Date": str(ver.get('createdAt') or ''),
            "Version Comment": attrib.get('comment') or '',
            "Version Task": task_name,
            "Representation": (repre or {}).get('name', ''),
            "Repre Path": repre_path,
            "Version Filter": flt['text'],
        }
    return result

class AyonShotlist(object):
    def __init__(self, ayon_gui, settings, paths):
        self.error = None
        self.log = logging.getLogger("AyonShotlist")
        os.environ["AYON_SERVER_URL"] = paths['AYON_SERVER_URL']
        os.environ["AYON_API_KEY"] = paths['AYON_API_KEY']

        self.error = None
        try:
            self.log.info("Connecting to Ayon")
            self.ayon = ayon_api.get_server_api_connection()
            self.log.info("Connected to Ayon")
        except Exception as e:
            error = f"Error connecting to Ayon: {e}"
            self.log.warning(error)
            self.error = error
            return

        self.data = []
        self.project = ayon_gui['project']
        self.projects = None
        self.settings = settings
        self.ayon_gui = ayon_gui

        self.prefix = ayon_gui['prefix']
        self.do_thumbs = ayon_gui['do_thumbs']
        self.output_folder = ayon_gui['out_folder'].replace("\\", "/")
        self.thumbs_dir = f"{self.output_folder}/_thumbsDownload"
        self.show_matched_only = ayon_gui['filter_matched']

        # where to put thumbnails and shotlist
        self.output_folder = ayon_gui['out_folder']
        self.do_output_csv = ayon_gui['do_csv']
        self.output_csv_path = f"{self.output_folder}/list.csv"
        self.do_output_excel = ayon_gui['do_excel']
        self.output_excel_path = f"{self.output_folder}/list.xls"
        self.do_output = True
        self.do_versions = bool(ayon_gui.get('do_versions'))
        self.product_filters = ayon_gui.get('product_filters') or []
        self.prep_paths()

        self.data = []
        # task id -> task name, filled by get_full_shotlist
        self.task_names = {}

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
            "Start Date",
            "End Date",
            "Folder Label",
            "Folder Status",
            "Task Label",
            "Task Status",
            "Links",
            "_hide"
        ]
        if self.do_versions:
            self.columns[-1:-1] = VERSION_COLUMNS
        self.version_columns_empty = {c: '' for c in VERSION_COLUMNS}

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
            if self.output_folder != "":
                os.makedirs(self.output_folder, exist_ok=True)
            else:
                self.log.warning("Ayon Shotlist output folder is empty")
                self.do_output = False
        except OSError as e:
            self.log.error(f"Error creating Ayon Shotlist output folder {self.output_folder} : {e}")
            self.do_output = False

    @staticmethod
    def attribs_to_columns(a):
        a = a or {}

        def num(key):
            try:
                return int(float(a.get(key) or 0))
            except (TypeError, ValueError):
                return 0

        def text(key):
            v = a.get(key)
            return '' if v is None else str(v)

        # range with handles: first frame - head .. last frame + tail
        fin = num("frameStart") - num("handleStart")
        fout = num("frameEnd") + num("handleEnd")
        d = {
            "Range": f"{fin}-{fout}",
            "Length": str(fout - fin + 1),
            "In": text("frameStart"),
            "Out": text("frameEnd"),
            "Head": text("handleStart"),
            "Tail": text("handleEnd"),
            "Width": text("resolutionWidth"),
            "Height": text("resolutionHeight"),
            "Pixel Aspect": text("pixelAspect"),
            "Clip In": text("clipIn"),
            "Clip Out": text("clipOut"),
            "Start Date": AyonShotlist.date_only(a.get("startDate")),
            "End Date": AyonShotlist.date_only(a.get("endDate")),
        }
        return d

    @staticmethod
    def date_only(value):
        """
        Ayon dates are ISO date-times ("2026-10-01T00:00:00+00:00"),
        return just the date "2026-10-01", or "" when not set
        """
        if not value:
            return ''
        value = str(value)
        if len(value) >= 10 and value[4] == '-' and value[7] == '-':
            return value[:10]
        return value

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
            if self.error is None and self.do_versions:
                self.add_versions()
            self.filter_shotlist()
        return self.data

    def _query(self, method, *args, fields=None, **kwargs):
        """
        Call an ayon_api query, retry without the field list if the server or
        the installed ayon_api version doesn't know some of the fields.
        """
        fn = getattr(self.ayon, method)
        try:
            return fn(*args, fields=fields, **kwargs)
        except Exception as e:
            if fields is None:
                raise
            self.log.debug(f"Ayon {method} with fields {sorted(fields)} failed ({e}), retrying with all fields")
            return fn(*args, **kwargs)

    def add_versions(self):
        """
        Add version info of the preferred product (Product filters) to every
        folder row and its task rows. Three queries for the whole project.
        """
        filters = self.product_filters
        for row in self.data:
            row.update(self.version_columns_empty)
        if not filters:
            self.log.warning("Pull versions is on, but no product filters are set")
            return
        folder_ids = {row['_folder_id'] for row in self.data if row.get('_folder_id')}
        if not folder_ids:
            return

        product_names = None
        if not any(_has_wildcard(f['product']) for f in filters):
            product_names = sorted({f['product'] for f in filters})
        repre_names = None
        if all(f['repre'] and not _has_wildcard(f['repre']) for f in filters):
            repre_names = sorted({f['repre'] for f in filters})

        try:
            kwargs = {'folder_ids': folder_ids}
            if product_names:
                kwargs['product_names'] = product_names
            products = list(self._query('get_products', self.project,
                                        fields={"id", "name", "folderId", "productType"}, **kwargs))
            product_ids = {p['id'] for p in products}
            last_versions = {}
            if product_ids:
                last_versions = self._query(
                    'get_last_versions', self.project, product_ids,
                    fields={"id", "version", "productId", "taskId", "author", "status",
                            "createdAt", "attrib.comment"}) or {}
            version_ids = {v['id'] for v in last_versions.values() if v}
            repres = []
            if version_ids:
                kwargs = {'version_ids': version_ids}
                if repre_names:
                    kwargs['representation_names'] = repre_names
                repres = list(self._query('get_representations', self.project,
                                          fields={"id", "name", "versionId", "attrib.path"}, **kwargs))
        except Exception as e:
            self.log.error(f"Reading versions from Ayon failed: {e}")
            self.log.debug("Ayon versions traceback", exc_info=True)
            return

        picked = pick_versions(folder_ids, products, last_versions, repres, self.task_names, filters)
        for row in self.data:
            info = picked.get(row.get('_folder_id'))
            if info:
                row.update(info)
        self.log.info(f"Ayon versions: {len(picked)} of {len(folder_ids)} folder(s) have a matching product "
                      f"({len(products)} product(s), {len(repres)} representation(s) read)")

    def _download_thumbnail(self, thumbnail_id, file_path):
        """
        :return: file_path, or None when the thumbnail is missing / invalid
        """
        try:
            thumbnail = self.ayon.get_thumbnail_by_id(self.project, thumbnail_id)
        except Exception as e:
            self.log.warning(f"Downloading thumbnail {thumbnail_id} failed: {e}")
            return None
        content = getattr(thumbnail, 'content', None)
        if not content or (hasattr(thumbnail, 'is_valid') and not thumbnail.is_valid):
            return None
        with open(file_path, "wb") as stream:
            stream.write(content)
        return file_path if os.path.isfile(file_path) else None

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
            # keyed by path: folder names are only unique per parent
            asset_entities = {f["path"]: f for f in asset_entities}
        except Exception as e:
            error = f"Error getting assets from Ayon: {e}"
            self.log.error(error)
            self.error = error
            return


        # get folders + tasks and their attribs
        data = []
        for _path, asset in asset_entities.items():
            asset_name = asset["name"]
            link_list = get_links(asset["id"])
            if link_list is not None and len(link_list) > 0:
                #print(f"{asset_name} Link List:")
                #pprint.pprint(link_list)
                pass

            thumb_name_folder = asset["path"].replace("/", "-").strip("-")
            thumbnail_path = None
            if asset["thumbnailId"] is not None and self.do_thumbs:
                thumbnail_path = self._download_thumbnail(
                    asset["thumbnailId"], f"{self.thumbs_dir}/{thumb_name_folder}.png")

            base = {
                "Thumbnail": thumbnail_path,
                "Folder Type": asset["type"],
                "Folder Name": asset_name,
                "Folder Path": asset["path"],
                "Folder Label": asset["label"],
                "Folder Status": asset.get("status", ""),
                "Links": " ".join([link["name"] for link in link_list]),
                "_folder_id": asset["id"],
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
                for task_info in task_entities:
                    task_name = task_info["name"]
                    self.task_names[task_info["id"]] = task_name
                    thumb_name_task = thumb_name_folder + "-task-" + task_name
                    thumbnail_path = None
                    if task_info["thumbnailId"] is not None and self.do_thumbs:
                        thumbnail_path = self._download_thumbnail(
                            task_info["thumbnailId"], f"{self.thumbs_dir}/{thumb_name_task}.png")
                    tsk = {
                        "Task Type": task_info["type"],
                        "Task Name": task_info["name"],
                        "Task Label": task_info["label"],
                        "Task Status": task_info["status"],
                        "Task Assignees": " ".join(task_info["assignees"])
                    }
                    shot_task = {**shot_clean, **tsk}
                    shot_task["Thumbnail"] = thumbnail_path or shot_clean["Thumbnail"]
                    shot_task["Folder Type"] = f'{shot_task["Folder Type"]}/Task'
                    shot_task_attr = {**shot_task, **self.attribs_to_columns(task_info["attrib"])}
                    data.append(shot_task_attr)
        self.data = sorted(data, key=lambda d: d['Folder Path'])

    def write_csv(self):
        if not self.data:
            self.log.warning("Ayon shot list is empty, nothing written")
            return
        if not self.do_output:
            return
        rows = [r for r in self.data if not r.get('_hide')]
        try:
            # utf-8-sig so Excel reads non-ascii names correctly
            with open(self.output_csv_path, 'w', newline='', encoding='utf-8-sig') as output_file:
                dict_writer = csv.DictWriter(output_file, [c for c in self.columns if not c.startswith('_')],
                                             extrasaction='ignore')
                dict_writer.writeheader()
                dict_writer.writerows(rows)
            self.log.info(f"Ayon shot list written to {self.output_csv_path} ({len(rows)} rows)")
        except OSError as e:
            self.log.error(f"Writing Ayon shot list {self.output_csv_path} failed: {e}")


