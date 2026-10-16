import csv
import fnmatch
import json
import logging
import os

import ayon_api

import ayon_packages

LIST_CSV_NAME = "ayon-list.csv"
VERSIONS_CSV_NAME = "ayon-list-versions.csv"

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
    # version attrib
    "Version Frame Start",
    "Version Frame End",
    "Version Handle Start",
    "Version Handle End",
    "Version FPS",
    "Version Width",
    "Version Height",
    "Version Pixel Aspect",
    # version data
    "Version Step",
    "Version Host",
    "Version Colorspace",
]

# version attrib -> column
VERSION_ATTRIBS = {
    "frameStart": "Version Frame Start",
    "frameEnd": "Version Frame End",
    "handleStart": "Version Handle Start",
    "handleEnd": "Version Handle End",
    "fps": "Version FPS",
    "resolutionWidth": "Version Width",
    "resolutionHeight": "Version Height",
    "pixelAspect": "Version Pixel Aspect",
}
# version data -> column
VERSION_DATA = {
    "step": "Version Step",
    "host_name": "Version Host",
    "colorspace": "Version Colorspace",
}


# columns of the "Matched Versions" list: every version of every product of
# the Ayon folders matched to package files
MATCHED_VERSION_COLUMNS = [
    "Folder Path",
    "Folder Name",
    "Folder Type",
    "Product",
    "Product Type",
    "Version",
    # "True" when a package file has this version (Match version)
    "Version Exists",
    # highest existing version of the same product in the folder
    "Max Existing Version",
    "Version Name",
    "Preferred",
    "Version Status",
    "Version Author",
    "Version Date",
    "Version Comment",
    "Version Task",
    "Representations",
] + list(VERSION_ATTRIBS.values()) + list(VERSION_DATA.values()) + [
    # number of package files whose version matched this row (Match version)
    "Matched Files",
]


def _as_dict(value):
    """entity 'data' may come as a dict or as a json string"""
    if isinstance(value, dict):
        return value
    if isinstance(value, str) and value.strip():
        try:
            data = json.loads(value)
            return data if isinstance(data, dict) else {}
        except ValueError:
            return {}
    return {}


def _cell(value):
    if value is None:
        return ''
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


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


def version_detail_columns(ver, repre=None):
    """version attrib / data columns, colorspace falls back to the representation"""
    attrib = ver.get('attrib') or {}
    info = {}
    for key, column in VERSION_ATTRIBS.items():
        info[column] = _cell(attrib.get(key))
    data = _as_dict(ver.get('data'))
    for key, column in VERSION_DATA.items():
        info[column] = _cell(data.get(key))
    if not info["Version Colorspace"] and repre:
        cs = _as_dict(repre.get('data')).get('colorspaceData') or {}
        info["Version Colorspace"] = _cell(cs.get('colorspace') if isinstance(cs, dict) else '')
    return info


def version_matches_filters(prod, ver, ver_repres, task_names, filters):
    """
    True when the version fits any product filter: product name, task the
    version was published from (if given), representation (if given)
    """
    task_name = task_names.get(ver.get('taskId'), '')
    for flt in filters:
        if not _match(flt['product'], prod.get('name')):
            continue
        if not _match(flt['task'], task_name):
            continue
        if flt['repre'] and not any(_match(flt['repre'], r.get('name')) for r in ver_repres):
            continue
        return True
    return False


def matched_version_rows(folders, products, versions, repres, task_names, preferred, filters=None):
    """
    Rows for the Matched Versions list: every version of the configured
    products (product filters) of the matched folders
    :param folders: dict folder id -> {'Folder Path', 'Folder Name', 'Folder Type'}
    :param products: product dicts (id, name, folderId, productType)
    :param versions: version dicts (id, version, productId, taskId, author, status,
                     createdAt, attrib, data)
    :param repres: representation dicts (id, name, versionId, data, files, context)
    :param task_names: task id -> name
    :param preferred: folder id -> version id picked by the product filters
    :param filters: product filters, versions not fitting any are left out;
                    None keeps every version
    :return: rows sorted by folder path, then version number (then product)
    """
    product_by_id = {p['id']: p for p in products}
    repres_by_version = {}
    for r in repres:
        repres_by_version.setdefault(r.get('versionId'), []).append(r)
    rows = []
    for ver in versions:
        prod = product_by_id.get(ver.get('productId'))
        if prod is None:
            continue
        folder_id = prod.get('folderId')
        folder = folders.get(folder_id, {})
        ver_repres = repres_by_version.get(ver.get('id'), [])
        if filters is not None and not version_matches_filters(prod, ver, ver_repres, task_names, filters):
            continue
        number = int(ver.get('version') or 0)
        attrib = ver.get('attrib') or {}
        row = {
            "Folder Path": folder.get("Folder Path", ''),
            "Folder Name": folder.get("Folder Name", ''),
            "Folder Type": folder.get("Folder Type", ''),
            "Product": prod.get('name', ''),
            "Product Type": prod.get('productType', ''),
            "Version": str(number),
            "Version Name": f"v{number:03d}",
            "Preferred": "yes" if preferred.get(folder_id) and preferred.get(folder_id) == ver.get('id') else "",
            "Version Status": ver.get('status') or '',
            "Version Author": ver.get('author') or '',
            "Version Date": str(ver.get('createdAt') or ''),
            "Version Comment": attrib.get('comment') or '',
            "Version Task": task_names.get(ver.get('taskId'), ''),
            "Representations": " ".join(sorted(r.get('name', '') for r in ver_repres)),
            "_folder_id": folder_id,
            "_version_id": ver.get('id'),
            # for pairing package files with a representation
            "_repres": [ayon_packages.repre_summary(r) for r in ver_repres],
        }
        row.update(version_detail_columns(ver, ver_repres[0] if ver_repres else None))
        rows.append(row)
    # highest version per folder + product
    max_version = {}
    for r in rows:
        key = (r["_folder_id"], r["Product"])
        max_version[key] = max(max_version.get(key, 0), int(r["Version"] or 0))
    for r in rows:
        r["Max Existing Version"] = str(max_version[(r["_folder_id"], r["Product"])])
        r["Version Exists"] = "False"
    rows.sort(key=lambda r: (r["Folder Path"], int(r["Version"] or 0), r["Product"].lower()))
    return rows


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
            "_version_id": ver.get('id'),
        }
        # newer publishes keep the colorspace on the representation
        result[folder_id].update(version_detail_columns(ver, repre))
    return result

class AyonShotlist(object):
    def __init__(self, ayon_gui, settings, paths):
        self.error = None
        self.log = logging.getLogger("AyonShotlist")
        # set before connecting: with a failed connection callers still read
        # these (AttributeError before)
        self.data = []
        self.task_names = {}
        self.product_filters = ayon_gui.get('product_filters') or []
        self._matched_cache_key = None
        self._matched_cache_rows = []
        # ayon_api reads the server and key from the environment
        os.environ["AYON_SERVER_URL"] = paths.get('AYON_SERVER_URL', '') or ''
        os.environ["AYON_API_KEY"] = paths.get('AYON_API_KEY', '') or ''

        self.error = None
        try:
            self.log.info("Connecting to Ayon")
            # the token may have been renewed since the last connection
            ayon_api.change_token(paths['AYON_SERVER_URL'], paths['AYON_API_KEY'])
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
        self.output_csv_path = f"{self.output_folder}/{LIST_CSV_NAME}"
        self.output_versions_csv_path = f"{self.output_folder}/{VERSIONS_CSV_NAME}"
        self.do_output_versions_csv = bool(ayon_gui.get('do_versions_csv'))
        self.do_output_excel = ayon_gui['do_excel']
        self.output_excel_path = f"{self.output_folder}/ayon-list.xlsx"
        self.do_output = True
        self.do_versions = bool(ayon_gui.get('do_versions'))
        self.product_filters = ayon_gui.get('product_filters') or []
        self.prep_paths()

        # task id -> task name, filled by get_full_shotlist
        self._thumb_stats = {'ok': 0, 'failed': 0}

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

        if self.do_thumbs and not self.output_folder:
            # thumbnails go to <output>/_thumbsDownload, would land in the drive root
            self.log.warning("Ayon thumbnails are on, but the output folder is empty: no thumbnails")
            self.do_thumbs = False
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

            folder_type_full = str(one.get('Folder Type') or '')
            is_task = "task" in folder_type_full.lower()
            folder_type = folder_type_full.lower().split('/')[0]

            hide = True
            asset_or_shot = False

            if self.ayon_gui['filter_tasks']:
                if is_task:
                    hide = False
                    # only check task types / names if tasks are allowed
                    if self.ayon_gui['filter_tasktype']:
                        if str(one.get("Task Type") or '').lower() in self.ayon_gui['filter_tasktypes']:
                            hide = False
                        else:
                            hide = True
                    if self.ayon_gui.get('filter_taskname') and not any(
                            _match(p, one["Task Name"]) for p in self.ayon_gui.get('filter_tasknames', [])):
                        hide = True
                else:
                    # it is not a task
                    if self.ayon_gui['filter_assets'] and "asset" in folder_type_full.lower():
                        hide = False
                        asset_or_shot = True
                    if self.ayon_gui['filter_shots'] and "shot" in folder_type_full.lower():
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
                # narrows only (it used to show rows hidden by the other
                # filters again); any of the row's assignees may match
                assignees = str(one.get("Task Assignees") or '').lower().split()
                if not any(a in self.ayon_gui['filter_assignees'] for a in assignees):
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
                            "createdAt", "data", "attrib.comment"}
                    | {f"attrib.{k}" for k in VERSION_ATTRIBS}) or {}
            version_ids = {v['id'] for v in last_versions.values() if v}
            repres = []
            if version_ids:
                kwargs = {'version_ids': version_ids}
                if repre_names:
                    kwargs['representation_names'] = repre_names
                repres = list(self._query('get_representations', self.project,
                                          fields={"id", "name", "versionId", "attrib.path", "data"}, **kwargs))
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

    THUMB_EXTENSIONS = {'image/jpeg': '.jpg', 'image/jpg': '.jpg', 'image/png': '.png',
                        'image/webp': '.webp', 'image/gif': '.gif'}

    def _download_thumbnail(self, entity_type, entity_id, thumbnail_id, file_base):
        """
        Download the thumbnail of a folder / task.

        Uses get_thumbnail(entity type, id), which works for every user;
        get_thumbnail_by_id is only allowed for admins and managers, for other
        users it returned empty content, so no thumbnail was ever written.
        :param file_base: path without extension, the extension comes from
                          the image type (Ayon thumbnails are often jpg)
        :return: written file path, or None
        """
        stats = self._thumb_stats
        thumbnail = None
        try:
            thumbnail = self.ayon.get_thumbnail(self.project, entity_type, entity_id)
        except Exception as e:
            self.log.debug(f"get_thumbnail {entity_type} {entity_id} failed: {e}")
        if thumbnail is None or not getattr(thumbnail, 'is_valid', bool(getattr(thumbnail, 'content', None))):
            # fall back for admins / older servers
            try:
                thumbnail = self.ayon.get_thumbnail_by_id(self.project, thumbnail_id)
            except Exception as e:
                self.log.debug(f"get_thumbnail_by_id {thumbnail_id} failed: {e}")
        content = getattr(thumbnail, 'content', None) if thumbnail is not None else None
        if not content:
            stats['failed'] += 1
            self.log.debug(f"No thumbnail content for {entity_type} {entity_id}")
            return None
        content_type = (getattr(thumbnail, 'content_type', None) or '').split(';')[0].strip().lower()
        file_path = file_base + self.THUMB_EXTENSIONS.get(content_type, '.png')
        try:
            with open(file_path, "wb") as stream:
                stream.write(content)
        except OSError as e:
            stats['failed'] += 1
            self.log.warning(f"Writing thumbnail {file_path} failed: {e}")
            return None
        stats['ok'] += 1
        return file_path

    def _log_thumbnail_stats(self):
        ok, failed = self._thumb_stats['ok'], self._thumb_stats['failed']
        if not ok and not failed:
            return
        msg = f"Ayon thumbnails: {ok} downloaded to {self.thumbs_dir}"
        if failed:
            msg += (f", {failed} not available (no permission or no thumbnail on the server, "
                    f"set log level DEBUG for details)")
        self.log.log(logging.WARNING if failed and not ok else logging.INFO, msg)

    def _links_by_folder(self, folder_ids):
        """
        folder id -> names of the folders linked in. One query for the whole
        project when the installed ayon_api has get_folders_links, otherwise
        one query per folder (as before).
        """
        links = {}
        folder_ids = list(folder_ids)
        batch = getattr(self.ayon, 'get_folders_links', None)
        if batch is not None:
            try:
                links = dict(batch(self.project, folder_ids=folder_ids, link_direction="in") or {})
            except Exception as e:
                self.log.debug(f"Ayon get_folders_links failed ({e}), reading links per folder")
                links = {}
                batch = None
        if batch is None:
            for folder_id in folder_ids:
                try:
                    links[folder_id] = list(self.ayon.get_folder_links(
                        self.project, folder_id, link_direction="in") or [])
                except Exception as e:
                    self.log.warning(f"Reading Ayon links of folder {folder_id} failed: {e}")
                    links[folder_id] = []

        linked_ids = {link["entityId"] for one in links.values() for link in one or []
                      if link.get("entityType") == "folder"}
        names = {}
        if linked_ids:
            try:
                for f in self.ayon.get_folders(self.project, folder_ids=linked_ids, fields={"id", "name"}):
                    names[f["id"]] = f["name"]
            except Exception as e:
                self.log.warning(f"Reading names of linked Ayon folders failed: {e}")
        out = {}
        for folder_id, one in links.items():
            out[folder_id] = [names[link["entityId"]] for link in one or []
                              if link.get("entityType") == "folder" and link.get("entityId") in names]
        return out

    def _tasks_by_folder(self, folder_ids):
        """folder id -> task entities, one query for all folders with tasks"""
        tasks = {}
        if not folder_ids:
            return tasks
        for task_info in self.ayon.get_tasks(self.project, folder_ids=set(folder_ids),
                                             fields={"name", "id", "type", "label", "assignees",
                                                     "status", "attrib", "thumbnailId", "folderId"}):
            tasks.setdefault(task_info.get("folderId"), []).append(task_info)
        return tasks

    def get_full_shotlist(self):

        try:
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
            # keyed by path: folder names are only unique per parent
            asset_entities = {f["path"]: f for f in asset_entities}
            # links and tasks of all folders at once, not two queries per folder
            links = self._links_by_folder(f["id"] for f in asset_entities.values())
            tasks = self._tasks_by_folder(
                [f["id"] for f in asset_entities.values() if f.get("hasTasks")])
        except Exception as e:
            error = f"Error getting folders from Ayon: {e}"
            self.log.error(error)
            self.error = error
            return

        # get folders + tasks and their attribs
        data = []
        for _path, asset in asset_entities.items():
            asset_name = asset["name"]
            link_names = links.get(asset["id"], [])

            thumb_name_folder = asset["path"].replace("/", "-").strip("-")
            thumbnail_path = None
            if asset.get("thumbnailId") is not None and self.do_thumbs:
                thumbnail_path = self._download_thumbnail(
                    "folder", asset["id"], asset["thumbnailId"], f"{self.thumbs_dir}/{thumb_name_folder}")

            base = {
                "Thumbnail": thumbnail_path,
                "Folder Type": asset.get("type") or "",
                "Folder Name": asset_name,
                "Folder Path": asset["path"],
                "Folder Label": asset.get("label") or "",
                "Folder Status": asset.get("status", ""),
                "Links": " ".join(link_names),
                "_folder_id": asset["id"],
            }
            attrs = self.attribs_to_columns(asset.get("attrib"))
            shot_clean = {**base, **attrs}
            shot_only = {**shot_clean, **self.task_empty}
            data.append(shot_only)

            for task_info in tasks.get(asset["id"], []):
                task_name = task_info["name"]
                self.task_names[task_info["id"]] = task_name
                thumb_name_task = thumb_name_folder + "-task-" + task_name
                thumbnail_path = None
                if task_info.get("thumbnailId") is not None and self.do_thumbs:
                    thumbnail_path = self._download_thumbnail(
                        "task", task_info["id"], task_info["thumbnailId"],
                        f"{self.thumbs_dir}/{thumb_name_task}")
                tsk = {
                    "Task Type": task_info.get("type") or "",
                    "Task Name": task_info["name"],
                    "Task Label": task_info.get("label") or "",
                    "Task Status": task_info.get("status") or "",
                    "Task Assignees": " ".join(task_info.get("assignees") or [])
                }
                shot_task = {**shot_clean, **tsk}
                shot_task["Thumbnail"] = thumbnail_path or shot_clean["Thumbnail"]
                shot_task["Folder Type"] = f'{shot_task["Folder Type"]}/Task'
                shot_task_attr = {**shot_task, **self.attribs_to_columns(task_info.get("attrib"))}
                data.append(shot_task_attr)
        self.data = sorted(data, key=lambda d: d['Folder Path'])
        self._log_thumbnail_stats()

    def update_output(self, ayon_gui):
        """
        Take the current output settings (folder, csv checkboxes), they may
        have changed since the list was read
        """
        self.ayon_gui = ayon_gui
        self.output_folder = (ayon_gui.get('out_folder') or '').replace("\\", "/")
        self.thumbs_dir = f"{self.output_folder}/_thumbsDownload"
        self.do_output_csv = ayon_gui.get('do_csv')
        self.do_output_versions_csv = bool(ayon_gui.get('do_versions_csv'))
        self.output_csv_path = f"{self.output_folder}/{LIST_CSV_NAME}"
        self.output_versions_csv_path = f"{self.output_folder}/{VERSIONS_CSV_NAME}"
        self.output_excel_path = f"{self.output_folder}/ayon-list.xlsx"
        self.do_output_excel = bool(ayon_gui.get('do_excel'))
        self.do_output = True
        do_thumbs = self.do_thumbs
        self.do_thumbs = False      # thumbnails were downloaded with the read
        self.prep_paths()
        self.do_thumbs = do_thumbs

    def write_csv(self, rows=None):
        """
        :param rows: rows to write (what the table shows), default: rows not
                     hidden by the list filters
        """
        if not self.data:
            self.log.warning("Ayon shot list is empty, nothing written")
            return
        if not self.do_output:
            return
        if rows is None:
            rows = [r for r in self.data if not r.get('_hide')]
        do_csv = bool(self.do_output_csv)
        do_excel = bool(getattr(self, 'do_output_excel', False))
        # with neither checkbox on, the csv is written (Export Shot List always
        # wrote it before the checkboxes worked)
        if do_csv or not do_excel:
            self._write_rows(self.output_csv_path, self.columns, rows, "Ayon shot list")
        if do_excel:
            self._write_rows_excel(self.output_excel_path, self.columns, rows, "Ayon shot list")

    def write_versions_csv(self, rows):
        """Matched Versions list to ayon-list-versions.csv, next to ayon-list.csv"""
        if not self.do_output:
            return
        if not rows:
            self.log.warning("Matched Versions list is empty, nothing written "
                             "(needs Pull versions and files matched to Ayon folders)")
            return
        self._write_rows(self.output_versions_csv_path, MATCHED_VERSION_COLUMNS, rows, "Matched Versions")

    def _write_rows_excel(self, path, columns, rows, what):
        """rows to an .xlsx file, same columns as the csv"""
        try:
            import xlsxwriter
        except ImportError:
            self.log.error(f"Writing {what} {path} failed: xlsxwriter is not installed")
            return
        columns = [c for c in columns if not c.startswith('_')]
        try:
            # values are text: don't turn '=...' or urls into formulas / links
            workbook = xlsxwriter.Workbook(path, {'strings_to_formulas': False,
                                                  'strings_to_urls': False})
            sheet = workbook.add_worksheet()
            bold = workbook.add_format({'bold': True})
            for col, title in enumerate(columns):
                sheet.write_string(0, col, str(title), bold)
            for row_number, row in enumerate(rows, start=1):
                for col, title in enumerate(columns):
                    value = row.get(title, '')
                    sheet.write_string(row_number, col, '' if value is None else str(value))
            sheet.freeze_panes(1, 0)
            workbook.close()
            self.log.info(f"{what} written to {path} ({len(rows)} rows)")
        except Exception as e:      # xlsxwriter raises its own errors, e.g. file open in Excel
            self.log.error(f"Writing {what} {path} failed: {e}")

    def _write_rows(self, path, columns, rows, what):
        try:
            # utf-8-sig so Excel reads non-ascii names correctly
            with open(path, 'w', newline='', encoding='utf-8-sig') as output_file:
                dict_writer = csv.DictWriter(output_file, [c for c in columns if not c.startswith('_')],
                                             extrasaction='ignore')
                dict_writer.writeheader()
                dict_writer.writerows(rows)
            self.log.info(f"{what} written to {path} ({len(rows)} rows)")
        except OSError as e:
            self.log.error(f"Writing {what} {path} failed: {e}")

    def get_matched_versions(self, folder_ids):
        """
        Every version of every product of the given folders (the ones matched
        to package files). Cached: refreshes run on every edit, Ayon is only
        asked again when the matched folders or the product filters change.
        :return: rows with MATCHED_VERSION_COLUMNS
        """
        folder_ids = frozenset(f for f in folder_ids if f)
        key = (folder_ids, tuple(f['text'] for f in self.product_filters))
        if key == self._matched_cache_key:
            return self._matched_cache_rows
        rows = []
        if folder_ids and self.error is None and not self.product_filters:
            self.log.warning("Matched Versions: no product filters set, nothing to list")
        elif folder_ids and self.error is None:
            try:
                kwargs = {'folder_ids': set(folder_ids)}
                # only the configured products; exact names narrow the query
                if not any(_has_wildcard(f['product']) for f in self.product_filters):
                    kwargs['product_names'] = sorted({f['product'] for f in self.product_filters})
                products = list(self._query('get_products', self.project,
                                            fields={"id", "name", "folderId", "productType"},
                                            **kwargs))
                products = [p for p in products
                            if any(_match(f['product'], p.get('name')) for f in self.product_filters)]
                product_ids = {p['id'] for p in products}
                versions = []
                if product_ids:
                    versions = list(self._query(
                        'get_versions', self.project,
                        fields={"id", "version", "productId", "taskId", "author", "status",
                                "createdAt", "data", "attrib.comment"}
                        | {f"attrib.{k}" for k in VERSION_ATTRIBS},
                        product_ids=product_ids, hero=False))
                version_ids = {v['id'] for v in versions}
                repres = []
                if version_ids:
                    # files (name, size) and context pair package files
                    # with a representation (extension, then size)
                    repres = list(self._query('get_representations', self.project,
                                              fields={"id", "name", "versionId", "data",
                                                      "context", "files"},
                                              version_ids=version_ids))
            except Exception as e:
                self.log.error(f"Reading matched versions from Ayon failed: {e}")
                self.log.debug("Ayon matched versions traceback", exc_info=True)
                return self._matched_cache_rows
            folders = {}
            preferred = {}
            for r in self.data:
                fid = r.get('_folder_id')
                if fid in folder_ids and fid not in folders and not r.get('Task Name'):
                    folders[fid] = {k: r.get(k, '') for k in ("Folder Path", "Folder Name", "Folder Type")}
                if fid in folder_ids and r.get('_version_id'):
                    preferred[fid] = r['_version_id']
            rows = matched_version_rows(folders, products, versions, repres, self.task_names, preferred,
                                        self.product_filters)
            self.log.info(f"Matched Versions: {len(rows)} version(s) of {len(product_ids)} product(s) "
                          f"in {len(folder_ids)} matched folder(s)")
        self._matched_cache_key = key
        self._matched_cache_rows = rows
        return rows

    def record_packages(self, records, package, dry_run=False):
        """
        Write to the version / representation data which package includes
        them (see ayon_packages).
        :param records: from ayon_packages.collect_package_records
        :return: result dict of ayon_packages.write_package_records
        """
        if self.error is not None:
            return {'versions': 0, 'repres': 0, 'versions_same': 0, 'repres_same': 0,
                    'errors': [self.error]}
        from datetime import datetime
        user = os.environ.get('AYON_USERNAME') or ''
        if not user:
            try:
                user = (self.ayon.get_user() or {}).get('name') or ''
            except Exception:
                user = ''
        info = {'date': datetime.now().astimezone().isoformat(timespec='seconds')}
        if user:
            info['user'] = user
        return ayon_packages.write_package_records(
            self.ayon, self.project, records, package, info, log=self.log, dry_run=dry_run)
