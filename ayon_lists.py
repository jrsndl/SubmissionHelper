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
            "Folder Path": str(folder.get('path') or ''),
            "Task": str(task.get('name') or ''),
            "Product": str(product.get('name') or ''),
            "Version": number if isinstance(number, int) else str(number or ''),
        })
    rows.sort(key=lambda r: (r["Folder Path"].lower(), r["Product"].lower(),
                             r["Version"] if isinstance(r["Version"], int) else -1))
    return rows
