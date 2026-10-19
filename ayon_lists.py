"""
AYON tab > AYON Lists: the project's entity lists by list category, and the
versions in a list. No Qt (the widget is ayon_lists_widget.py).

The category is the list's 'category' attribute, else 'category' in its data;
list folders are not used. Works with ayon-python-api versions with and
without get_entity_lists: plain GraphQL / REST calls are the fallback.
"""
import json
import logging
import os
import uuid

log = logging.getLogger("AyonLists")

LIST_COLUMNS = ("Folder Path", "Task", "Product", "Version")
NO_CATEGORY = "(no category)"
# the widget groups by the 'folder' key of query_lists
NO_FOLDER = NO_CATEGORY
# ids per get_versions / get_products ... call
_ID_CHUNK = 200

_LISTS_QUERY = """
query EntityLists($projectName: String!, $after: String) {
  project(name: $projectName) {
    entityLists(first: 100, after: $after) {
      pageInfo { hasNextPage endCursor }
      edges { node { %s } }
    }
  }
}
"""


def connect(paths):
    """
    AYON connection with the sign-in of paths (credentials.resolve /
    ensure_ayon). :return: the ayon_api connection or None (logged)
    """
    try:
        import ayon_api
    except Exception as e:
        log.error(f"AYON Lists: ayon_api can't be imported: {e}")
        return None
    url = paths.get('AYON_SERVER_URL', '') or ''
    key = paths.get('AYON_API_KEY', '') or ''
    if not url or not key:
        log.warning("AYON Lists: AYON server or login is not set. "
                    "Sign in on the Preferences tab (Accounts).")
        return None
    # ayon_api reads the server and key from the environment (as AyonShotlist)
    os.environ["AYON_SERVER_URL"] = url
    os.environ["AYON_API_KEY"] = key
    try:
        ayon_api.change_token(url, key)
        return ayon_api.get_server_api_connection()
    except Exception as e:
        log.error(f"AYON Lists: connecting to {url} failed: {e}")
        return None


# ---------------------------------------------------------------- lists

def _data(response):
    """data of an ayon_api RestApiResponse (or a plain dict in tests)"""
    if response is None:
        return None
    if isinstance(response, dict):
        return response
    try:
        response.raise_for_status()
    except Exception:
        return None
    return getattr(response, 'data', None)


def _as_dict(value):
    """attrib / data as a dict: the GraphQL fields come as json strings"""
    if isinstance(value, str):
        try:
            value = json.loads(value)
        except ValueError:
            return {}
    return value if isinstance(value, dict) else {}


def list_category(entity_list):
    """the list's category: attrib category, else data category, else ''"""
    for key in ('attrib', 'allAttrib', 'data'):
        value = _as_dict(entity_list.get(key)).get('category')
        if value not in (None, ''):
            return str(value)
    return ''


def _raw_lists(con, project, fields):
    """entity lists by plain GraphQL (ayon_api without get_entity_lists)"""
    out = []
    after = None
    while True:
        response = con.query_graphql(_LISTS_QUERY % " ".join(fields),
                                     {"projectName": project, "after": after})
        errors = getattr(response, 'errors', None)
        if errors:
            raise RuntimeError(str(errors))
        data = getattr(response, 'data', None) or {}
        lists = (((data.get('data') or data).get('project') or {}).get('entityLists') or {})
        out.extend(e['node'] for e in lists.get('edges') or [])
        info = lists.get('pageInfo') or {}
        if not info.get('hasNextPage'):
            return out
        after = info.get('endCursor')


def _fetch_lists(con, project):
    """entity list dicts with their attributes and data (for the category)"""
    if hasattr(con, 'get_entity_lists'):
        tries = (("id", "label", "entityType", "active", "attrib", "data"),
                 ("id", "label", "entityType", "active", "attrib"),
                 ("id", "label", "entityType", "active"))
    else:
        tries = (("id", "label", "entityType", "active", "allAttrib", "data"),
                 ("id", "label", "entityType", "active", "allAttrib"),
                 ("id", "label", "entityType", "active"))
    for fields in tries:
        try:
            if hasattr(con, 'get_entity_lists'):
                return list(con.get_entity_lists(project, fields=set(fields)))
            return _raw_lists(con, project, fields)
        except Exception as e:
            # a server / api that refuses a field: ask for less
            err = e
    raise err


def query_lists(con, project):
    """
    The project's entity lists: [{'id', 'name', 'folder', 'entity_type'}],
    'folder' being the list category; sorted by category (lists without
    one last), then name. Never raises.
    """
    if con is None or not project:
        return []
    try:
        lists = _fetch_lists(con, project)
    except Exception as e:
        log.error(f"Reading AYON lists of {project} failed: {e}")
        return []
    out = []
    for one in lists:
        if one.get('active') is False:
            continue
        folder = list_category(one) or NO_CATEGORY
        out.append({'id': one.get('id'), 'name': str(one.get('label') or one.get('id') or ''),
                    'folder': folder, 'entity_type': one.get('entityType') or ''})
    out.sort(key=lambda d: (d['folder'] == NO_FOLDER, d['folder'].lower(), d['name'].lower()))
    return out


# ---------------------------------------------------------------- versions

def _list_items(con, project, list_id):
    """[(entity type, entity id)] of a list, in list order"""
    items = None
    if hasattr(con, 'get_entity_lists'):
        try:
            for one in con.get_entity_lists(
                    project, list_ids=[list_id],
                    fields={"id", "entityType", "items.entityId", "items.entityType",
                            "items.position"}):
                items = one.get('items')
                default_type = one.get('entityType')
                break
        except Exception as e:
            log.debug(f"AYON Lists: GraphQL items failed, using REST ({e})")
            items = None
    if items is None:
        data = _data(con.get(f"projects/{project}/lists/{list_id}")) or {}
        items = data.get('items') or []
        default_type = data.get('entityType')
    items = sorted(items, key=lambda i: (i.get('position') is None, i.get('position') or 0))
    return [(i.get('entityType') or default_type, i.get('entityId')) for i in items
            if i.get('entityId')]


def _chunks(ids):
    ids = list(ids)
    for start in range(0, len(ids), _ID_CHUNK):
        yield ids[start:start + _ID_CHUNK]


def _by_id(getter, project, ids, kwarg, fields):
    out = {}
    ids = [i for i in set(ids) if i]
    for chunk in _chunks(ids):
        for one in getter(project, **{kwarg: chunk, 'fields': set(fields)}):
            out[one.get('id')] = one
    return out


def query_list_versions(con, project, list_id):
    """
    Rows of the versions in an AYON list (LIST_COLUMNS keys), sorted by
    folder path, product, version. Items that aren't versions are skipped (logged once).
    Never raises.
    """
    if con is None or not project or not list_id:
        return []
    try:
        items = _list_items(con, project, list_id)
    except Exception as e:
        log.error(f"Reading AYON list items failed: {e}")
        return []
    version_ids = [eid for etype, eid in items if (etype or '').lower() == 'version']
    others = len(items) - len(version_ids)
    if others:
        log.info(f"AYON Lists: {others} item(s) of the list are not versions, not shown")
    if not version_ids:
        return []
    try:
        versions = _by_id(con.get_versions, project, version_ids, 'version_ids',
                          ("id", "name", "version", "productId", "taskId"))
        products = _by_id(con.get_products, project,
                          [v.get('productId') for v in versions.values()], 'product_ids',
                          ("id", "name", "folderId"))
        folders = _by_id(con.get_folders, project,
                         [p.get('folderId') for p in products.values()], 'folder_ids',
                         ("id", "path"))
        tasks = _by_id(con.get_tasks, project,
                       [v.get('taskId') for v in versions.values()], 'task_ids',
                       ("id", "name"))
    except Exception as e:
        log.error(f"Reading AYON list versions failed: {e}")
        return []
    rows = []
    for vid in version_ids:
        v = versions.get(vid)
        if v is None:
            continue
        product = products.get(v.get('productId')) or {}
        folder = folders.get(product.get('folderId')) or {}
        task = tasks.get(v.get('taskId')) or {}
        number = v.get('version')
        rows.append({
            "_id": vid,
            "Folder Path": str(folder.get('path') or ''),
            "Task": str(task.get('name') or ''),
            "Product": str(product.get('name') or ''),
            "Version": number if isinstance(number, int) else str(number or ''),
        })
    rows.sort(key=lambda r: (r["Folder Path"].lower(), r["Product"].lower(),
                             r["Version"] if isinstance(r["Version"], int) else -1))
    return rows


# ---------------------------------------------------------------- package matching

EXACT = 'exact'
ALMOST = 'almost'


def list_version_ids(con, project, lists):
    """
    {list id: set of version ids} of the lists (query_lists rows) that can
    hold versions. A list that can't be read is left out (logged).
    """
    out = {}
    if con is None or not project:
        return out
    for one in lists or []:
        if (one.get('entity_type') or 'version').lower() != 'version':
            continue
        try:
            items = _list_items(con, project, one['id'])
        except Exception as e:
            log.warning(f"AYON Lists: reading list '{one.get('name')}' failed: {e}")
            continue
        out[one['id']] = {eid for etype, eid in items if (etype or '').lower() == 'version'}
    return out


def overlap(list_ids, package_ids):
    """shared versions / versions in the list or the package (0..1)"""
    list_ids, package_ids = set(list_ids or ()), set(package_ids or ())
    union = list_ids | package_ids
    return len(list_ids & package_ids) / len(union) if union else 0.0


def match_kind(list_ids, package_ids, threshold):
    """
    EXACT: the list has exactly the package's versions; ALMOST: overlap()
    >= threshold (0..1); None otherwise or when either side is empty
    """
    list_ids, package_ids = set(list_ids or ()), set(package_ids or ())
    if not list_ids or not package_ids:
        return None
    if list_ids == package_ids:
        return EXACT
    return ALMOST if overlap(list_ids, package_ids) >= threshold else None


def category_options(con):
    """
    allowed values of the AYON list attribute 'category' (when it is an
    enum), [] when there is no such attribute or it is free text
    """
    try:
        attrs = con.get_attributes_for_type("list")
    except Exception as e:
        log.debug(f"AYON Lists: list attributes can't be read ({e})")
        return []
    if isinstance(attrs, list):
        attrs = {a.get('name'): a.get('data', a) for a in attrs if isinstance(a, dict)}
    cat = (attrs or {}).get('category') or {}
    enum = cat.get('enum') or (cat.get('data') or {}).get('enum') or []
    out = []
    for one in enum:
        value = one.get('value') if isinstance(one, dict) else one
        if value not in (None, '') and str(value) not in out:
            out.append(str(value))
    return out


def find_list_by_label(con, project, label):
    """
    id of the project's list with this label (AYON labels are unique in a
    project), compared exactly, then not case sensitive; None if there is none
    """
    if con is None or not project or not label:
        return None
    lists = _fetch_lists(con, project)
    for same in (lambda a: a == label, lambda a: a.lower() == label.lower()):
        for one in lists:
            if same(str(one.get('label') or '')):
                return one.get('id')
    return None


def _create_tries(category, ftrack_id):
    """
    attrib / data variants to create a list with: the category in the
    'category' attribute, else in data; the ftrack list id in the 'ftrackId'
    attribute (ayon-ftrack pairs lists by it), else in data
    """
    tries = []
    for cat_in in ('attrib', 'data'):
        for ftrack_in in ('attrib', 'data'):
            extra = {}
            if category:
                extra.setdefault(cat_in, {})['category'] = category
            if ftrack_id:
                extra.setdefault(ftrack_in, {})['ftrackId'] = ftrack_id
            if extra not in tries:
                tries.append(extra)
    return tries


def create_version_list(con, project, label, version_ids, category='', ftrack_id=None):
    """
    Create an AYON version list with the versions, in this order. The
    category goes to the list's 'category' attribute, else (a server without
    that attribute) to 'category' in its data. ftrack_id: the ftrack list it
    mirrors, as the 'ftrackId' attribute the AYON ftrack sync pairs lists by.
    :return: the new list id (raises on failure)
    """
    items = [{"entityId": vid, "position": i} for i, vid in enumerate(version_ids)]
    tries = _create_tries(category, ftrack_id)
    err = None
    list_id = None
    for extra in tries:
        try:
            if hasattr(con, 'create_entity_list'):
                list_id = con.create_entity_list(project, "version", label, items=items, **extra)
            else:
                list_id = uuid.uuid4().hex
                response = con.post(f"projects/{project}/lists", id=list_id, entityType="version",
                                    label=label, items=items, **extra)
                response.raise_for_status()
            if category and 'category' not in (extra.get('attrib') or {}):
                log.warning(f"AYON Lists: '{category}' is not accepted as the list's category "
                            f"attribute (not one of its options?), it is only in the list data")
            break
        except Exception as e:
            err = e
            list_id = None
            log.debug(f"AYON Lists: create with {extra or 'no category'} failed: {e}")
    if list_id is None:
        raise err
    add_missing_items(con, project, list_id, version_ids)
    return list_id


def add_missing_items(con, project, list_id, version_ids):
    """
    Some servers / ayon-python-api versions create the list but ignore the
    items sent with it: read the list back and add the versions that aren't
    in it, one by one (POST .../lists/<id>/items). Raises when versions are
    still missing. :return: number of versions added here
    """
    try:
        present = {eid for _, eid in _list_items(con, project, list_id)}
    except Exception as e:
        log.debug(f"AYON Lists: reading the new list back failed ({e}), adding all items")
        present = set()
    missing = [vid for vid in dict.fromkeys(version_ids) if vid not in present]
    if not missing:
        return 0
    start = len(present)
    failed = []
    for offset, vid in enumerate(missing):
        try:
            if hasattr(con, 'create_entity_list_item'):
                con.create_entity_list_item(project, list_id, vid, position=start + offset)
            else:
                response = con.post(f"projects/{project}/lists/{list_id}/items",
                                    id=uuid.uuid4().hex, entityId=vid, position=start + offset)
                response.raise_for_status()
        except Exception as e:
            failed.append(vid)
            last = e
    added = len(missing) - len(failed)
    log.info(f"AYON Lists: {added} version(s) added to the new list item by item")
    if failed:
        raise RuntimeError(f"{len(failed)} of {len(version_ids)} versions could not be added "
                           f"to the list: {last}")
    return added


def version_ftrack_ids(con, project, version_ids):
    """
    {AYON version id: ftrack AssetVersion id} from the versions' ftrackId
    attribute (set by the AYON ftrack integration); versions without one
    are not in the result. Raises when AYON can't be read.
    """
    ids = [i for i in dict.fromkeys(version_ids or []) if i]
    err = None
    for fields in (("id", "attrib.ftrackId"), ("id", "attrib")):
        out = {}
        try:
            for chunk in _chunks(ids):
                for v in con.get_versions(project, version_ids=chunk, fields=set(fields)):
                    ftrack_id = (_as_dict(v.get('attrib'))).get('ftrackId')
                    if ftrack_id:
                        out[v.get('id')] = str(ftrack_id)
            return out
        except Exception as e:
            err = e
    raise err
