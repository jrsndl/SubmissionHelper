import csv
import logging
import time

import ftrack_api

import credentials

log = logging.getLogger("Ftrack")

# (url, user, key) -> session; connecting takes seconds and refreshes run on
# every edit, so a working session is reused
_SESSIONS = {}
# (url, user, key) -> time of the last failed attempt
_FAILED = {}
RETRY_AFTER = 30.0
_last_message = None


def _log_once(level, msg):
    """same message is logged only once in a row (refreshes repeat it)"""
    global _last_message
    if msg != _last_message:
        _last_message = msg
        log.log(level, msg)


def open_session(url, user, key):
    """
    Connect to ftrack, or reuse the connection for the same server and user.
    Never raises: a missing setting or a failed connection is logged and
    None returned, the app then works without ftrack data.
    """
    missing = [name for name, value in (("server url", url), ("api user", user), ("api key", key))
               if not value]
    if missing:
        _log_once(logging.WARNING,
                  f"Ftrack is on, but the {', '.join(missing)} is not set: ftrack is skipped. "
                  f"Sign in on the Preferences tab (Accounts), or set "
                  f"FTRACK_SERVER / FTRACK_API_USER / FTRACK_API_KEY, or "
                  f"ftrack_server_url / ftrack_api_user / ftrack_api_key in install.json.")
        return None
    cache_key = (url, user, key)
    session = _SESSIONS.get(cache_key)
    if session is not None:
        return session
    failed_at = _FAILED.get(cache_key)
    if failed_at is not None and time.monotonic() - failed_at < RETRY_AFTER:
        return None
    try:
        # 15 s instead of 60: a server that is down must not freeze the gui for a minute
        session = ftrack_api.Session(server_url=url, api_key=key, api_user=user,
                                     auto_connect_event_hub=False, timeout=15)
    except Exception as e:
        _FAILED[cache_key] = time.monotonic()
        _log_once(logging.ERROR, f"Connecting to ftrack {url} as {user} failed: {e}")
        return None
    _FAILED.pop(cache_key, None)
    _SESSIONS[cache_key] = session
    _log_once(logging.INFO, f"Connected to ftrack {url} as {user}")
    return session


def find_project_id(session, project_name):
    """id of the active project with this full name, or None (logged)"""
    if session is None or not project_name:
        return None
    try:
        for p in session.query('Project where status is "Active"').all():
            if p["full_name"] == project_name:
                return p["id"]
    except Exception as e:
        _log_once(logging.ERROR, f"Ftrack project query failed: {e}")
        return None
    _log_once(logging.WARNING, f"Ftrack project '{project_name}' not found among active projects")
    return None


# ---------------------------------------------------------------------------
# Ftrack tab > Get Lists: version lists of a project and the versions in a list
# ---------------------------------------------------------------------------

LIST_COLUMNS = ("Version Link", "Version", "Version Status", "Version Description",
                "Asset Type", "Published By")
NO_FOLDER = "(no folder)"
# ids per "AssetVersion where id in (...)" query
_ID_CHUNK = 100


def _get(entity, *keys):
    """entity[k1][k2]... or None when anything on the way is missing"""
    value = entity
    for key in keys:
        if value is None:
            return None
        try:
            value = value[key]
        except Exception:
            return None
    return value


def _text(value):
    return '' if value is None else str(value)


def version_name(asset_name, number):
    """name of a version as shown in Get Lists, e.g. compMain_v003"""
    try:
        return f"{asset_name}_v{int(number):03d}"
    except (TypeError, ValueError):
        return f"{asset_name}_v{_text(number)}"


def version_link(version):
    """
    ftrack hierarchy path of the version's asset parent followed by the
    version name, e.g. proj/sq010/sh010/compMain_v003
    """
    names = []
    for one in _get(version, 'asset', 'parent', 'link') or []:
        name = _get(one, 'name')
        if name:
            names.append(str(name))
    names.append(version_name(_text(_get(version, 'asset', 'name')), _get(version, 'version')))
    return "/".join(names)


def version_row(version):
    """one row of the Get Lists table, keys LIST_COLUMNS"""
    first = _text(_get(version, 'user', 'first_name'))
    last = _text(_get(version, 'user', 'last_name'))
    user = f"{first} {last}".strip() or _text(_get(version, 'user', 'username'))
    number = _get(version, 'version')
    return {
        "Version Link": version_link(version),
        "Version": number if isinstance(number, int) else _text(number),
        "Version Status": _text(_get(version, 'status', 'name')),
        "Version Description": _text(_get(version, 'comment')),
        "Asset Type": _text(_get(version, 'asset', 'type', 'name')),
        "Published By": user,
    }


def query_version_lists(session, project_id):
    """
    Version lists of the project:
    [{'id', 'name', 'folder'}] sorted by folder (lists without one last), name.
    Never raises, errors are logged.
    """
    if session is None or not project_id:
        return []
    try:
        lists = session.query(
            'select id, name, category.name from AssetVersionList '
            'where project.id is "{0}"'.format(project_id)).all()
    except Exception as e:
        log.error(f"Reading ftrack lists failed: {e}")
        return []
    out = []
    for one in lists:
        out.append({'id': _get(one, 'id'),
                    'name': _text(_get(one, 'name')),
                    'folder': _text(_get(one, 'category', 'name')) or NO_FOLDER})
    out.sort(key=lambda d: (d['folder'] == NO_FOLDER, d['folder'].lower(), d['name'].lower()))
    return out


_VERSION_FIELDS = ('version, comment, status.name, asset.name, asset.type.name, '
                   'user.first_name, user.last_name, user.username')


def query_list_versions(session, list_id):
    """
    Rows (version_row) of the versions in an ftrack list, sorted by Version Link.
    Never raises, errors are logged.
    """
    if session is None or not list_id:
        return []
    try:
        ids = [_get(o, 'entity_id') for o in session.query(
            'select entity_id from ListObject where list_id is "{0}"'.format(list_id)).all()]
    except Exception as e:
        log.error(f"Reading ftrack list items failed: {e}")
        return []
    ids = [i for i in ids if i]
    rows = []
    for start in range(0, len(ids), _ID_CHUNK):
        id_list = ', '.join(f'"{i}"' for i in ids[start:start + _ID_CHUNK])
        versions = None
        # with the hierarchy in one go; without it (read per version) when the
        # server refuses the nested projection
        for fields in (_VERSION_FIELDS + ', asset.parent.link', _VERSION_FIELDS):
            try:
                versions = session.query(
                    'select {0} from AssetVersion where id in ({1})'.format(fields, id_list)).all()
                break
            except Exception as e:
                err = e
        if versions is None:
            log.error(f"Reading ftrack list versions failed: {err}")
            continue
        rows.extend(version_row(v) for v in versions)
    rows.sort(key=lambda r: r["Version Link"].lower())
    return rows


def list_categories(session):
    """names of the ftrack list categories (ftrack lists need one), sorted"""
    if session is None:
        return []
    try:
        return sorted(str(c['name']) for c in session.query('select id, name from ListCategory').all())
    except Exception as e:
        log.error(f"Reading ftrack list categories failed: {e}")
        return []


def _write_session(session):
    """
    A new session for writing (the shared one can hold a large cache, merging
    into it hit 'maximum recursion depth'); the shared one when a new one
    can't be made. :return: (session, is_new)
    """
    url = getattr(session, 'server_url', None)
    user = getattr(session, 'api_user', None)
    key = getattr(session, 'api_key', None)
    if not (url and user and key):
        return session, False
    try:
        return ftrack_api.Session(server_url=url, api_key=key, api_user=user,
                                  auto_connect_event_hub=False, timeout=15), True
    except Exception as e:
        log.debug(f"New ftrack session failed ({e}), using the shared one")
        return session, False


def _find_list(session, project_id, name):
    """
    the project's list with this name in any category (ayon-ftrack pairs
    lists by name and may have made one in another category):
    (list entity, set of its entity ids), or (None, set())
    """
    found = session.query(
        'select id, name, category_id from List where project_id is "{0}" '
        'and name is "{1}"'.format(project_id, str(name).replace('"', '\\"'))).first()
    if found is None:
        return None, set()
    objects = session.query(
        'select entity_id from ListObject where list_id is "{0}"'.format(found['id'])).all()
    return found, {o['entity_id'] for o in objects}


def create_version_list(session, project_id, name, category, version_ids):
    """
    Create an ftrack version list (as ayon-ftrack does: List, system_type
    assetversion) with the AssetVersions, in this order. A list with this
    name already there (any category) gets the versions it doesn't have and
    the chosen category, so a second run doesn't make a duplicate.
    Written with a new session. When ftrack raises but the list is there
    with all the versions, it counts as done (logged as a warning).
    :return: the list id (raises on failure)
    """
    ws, is_new = _write_session(session)
    try:
        categories = {str(c['name']): c['id']
                      for c in ws.query('select id, name from ListCategory').all()}
        category_id = categories.get(category)
        if not category_id:
            raise ValueError(f"ftrack list category '{category}' not found")
        try:
            existing, present = _find_list(ws, project_id, name)
        except Exception as e:
            log.debug(f"Looking for ftrack list '{name}' failed: {e}")
            existing, present = None, set()
        try:
            if existing is not None:
                list_id = existing['id']
                log.info(f"ftrack list '{name}' exists: adding the versions it doesn't have")
                if existing['category_id'] != category_id:
                    existing['category_id'] = category_id
                    log.info(f"ftrack list '{name}': category set to '{category}'")
            else:
                list_id = ws.create("List", {
                    "project_id": project_id,
                    "name": name,
                    "is_open": True,
                    "category_id": category_id,
                    "system_type": "assetversion",
                })["id"]
            for version_id in version_ids:
                if version_id not in present:
                    ws.create("ListObject", {"list_id": list_id, "entity_id": version_id})
                    present.add(version_id)
            ws.commit()
            return list_id
        except Exception as e:
            log.debug("ftrack list write failed", exc_info=True)
            try:
                ws.rollback()
            except Exception:
                pass
            # it may be saved anyway (the error came after the commit): check
            try:
                found, objects = _find_list(ws, project_id, name)
            except Exception:
                found, objects = None, set()
            found_id = found['id'] if found is not None else None
            if found_id is not None and set(version_ids) <= objects:
                log.warning(f"ftrack reported an error ({e}), but list '{name}' is there with "
                            f"all {len(set(version_ids))} versions")
                return found_id
            raise
    finally:
        if is_new:
            try:
                ws.close()
            except Exception:
                pass


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

                # make path: ancestors come root first, sorting them
                # alphabetically scrambled the folder path
                anc = shot.get("ancestors")
                if anc is not None:
                    p = [a['name'] for a in anc]
                    one['path'] = "/" + "/".join(p + [one['name']])

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
        except Exception as e:
            log.error(f"Reading ftrack shots failed: {e}")
            s = []

        try:
            assets = self.ftrack['session'].query(
                'select id, name, incoming_links, outgoing_links, ancestors, descendants, parent_id from AssetBuild where project.id is "{0}"'.format(
                    self.ftrack['project_id'])
            ).all()
            a = traverse(assets, "Asset Build")
        except Exception as e:
            log.error(f"Reading ftrack asset builds failed: {e}")
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
                "Folder Path": one.get('path') or ('/' + str(one.get('name') or '')),
                "Folder Type": one.get('type', ''),
                "Tasks": one.get('desc', ''),
                "Links In": one.get('links_in', ''),
                "Links Out": one.get('links_out', '')
            }
            ftrack_table.append(line)
        if len(ftrack_table) == 0:
            return

        ftrack_table_sorted = sorted(ftrack_table, key=lambda d: d['Folder Path'] or '')

        log.debug(f"Ftrack shot list: {len(ftrack_table_sorted)} rows")

        try:
            with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=ftrack_table_sorted[0].keys())
                writer.writeheader()
                for row in ftrack_table_sorted:
                    writer.writerow(row)
            log.info(f"Ftrack shot list written to {csv_path} ({len(ftrack_table_sorted)} rows)")
        except OSError as e:
            log.error(f"Writing ftrack shot list {csv_path} failed: {e}")

    def _get_ftrack_assets_simple(self):
        assets = self.ftrack['session'].query(
            'AssetBuild where project.id is "{0}"'.format(self.ftrack['project_id'])
        ).all()
        for asset in assets:
            log.debug(asset['name'])
        self.ftrack['assets'] = assets

    def _get_ftrack_shots_simple(self):
        shots = self.ftrack['session'].query(
            'Shot where project.id is "{0}"'.format(self.ftrack['project_id'])
        ).all()
        for shot in shots:
            log.debug(shot['name'])
        self.ftrack['shots'] = shots

    def _get_ftrack_shot_links_simple(self):
        shots = self.ftrack['shots']
        for shot in shots:
            log.debug(f"--- Shot: {shot['name']}")
            for link in shot['incoming_links']:
                from_link = link.get('from')
                if from_link is not None:
                    log.debug(f"--- Incoming: {from_link['name']}")

    def _get_ftrack_asset_links_simple(self):
        assets = self.ftrack['assets']
        for asset in assets:
            log.debug(f"--- Asset: {asset['name']}")
            for link in asset['outgoing_links']:
                from_link = link.get('to')
                if from_link is not None:
                    log.debug(f"--- Outgoing: {from_link['name']}")

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
            self.ftrack['do_ftrack'] = bool((self.settings.get('ftrack_use') or {}).get('value'))
            self.ftrack['project'] = str((self.settings.get('ftrack_project') or {}).get('value') or '')

            self.ftrack['session'] = None
            self.ftrack['project_id'] = None
            self.ftrack['all_projects'] = None
            if self.ftrack['do_ftrack']:
                credentials.ensure_ftrack(self.paths)
                self.ftrack['url'] = self.paths.get('FTRACK_SERVER', '')
                self.ftrack['key'] = self.paths.get('FTRACK_API_KEY', '')
                self.ftrack['user'] = self.paths.get('FTRACK_API_USER', '')
                self.ftrack['session'] = open_session(
                    self.ftrack['url'], self.ftrack['user'], self.ftrack['key'])
                self.ftrack['project_id'] = find_project_id(
                    self.ftrack['session'], self.ftrack['project'])