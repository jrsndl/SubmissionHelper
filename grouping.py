"""
Grouping tab: files that belong to the same version (e.g. the exr sequence and
the mp4 review of sh010 compMain v003) form a group.

* Group by (a token template) gives every file its group key.
* The first enabled group definition whose Task Type(s) / Task Name(s) match
  the group says which representations the group needs:
    Always Repres            required, must be in the package
    Always/Convert Repres    required, in the package or made by a Convert row
    Optional Repres          allowed, not required
  A missing required representation is an error on every file of the group.
* Inherit Columns copy Submission column values between the files of a group
  (a value that is empty or has an unknown {token} takes the value of the
  first file, in Inheritance Repre Priority order, that has a good one).
* Review Repre / Thumbnail Source Repre: the tokens of that file are given to
  every file of the group as {group_review_<token>} / {group_thumb_<token>}.
* Collapse joins the rows of a group into one row.

Pure functions, no Qt: used by the Sequencer in the gui and the command line.
"""
import fnmatch
import re

from sh_tokens import format_keep, unresolved_tokens

# settings (widget names on the Grouping tab)
DEFAULTS = {
    'group_on': False,
    'group_by': '{shot}{task}{version}',
    'group_repre': '{extension}',
    'group_task_type': '{task_type}',
    'group_task_name': '{task}',
    'group_no_export_missing': True,
    'group_together': True,
    'group_colors': True,
    'group_colors_excel': False,
    'group_collapse_sub': False,
    'group_collapse_log': False,
    'group_collapse_sep': ', ',
}

# keys of one group definition (same as IngestDesktop presets)
DEFINITION_FIELDS = (
    'name', 'enabled', 'task_types', 'task_names',
    'always_repres', 'always_or_convert_repres', 'optional_repres',
    'inheritance_repre_priority', 'review_repre', 'thumb_source_repre',
    'inherit_columns',
)

# tokens every file gets (empty when the file is in no group)
TOKENS = (
    'group_key', 'group_name', 'group_number', 'group_size', 'group_repre',
    'group_repres', 'group_missing', 'group_to_convert',
    'group_error', 'group_warning',
)
REVIEW_PREFIX = 'group_review_'
THUMB_PREFIX = 'group_thumb_'

_CONVERT_PATH_RE = re.compile(r'^convert_path\d+$')

# muted row backgrounds for the dark gui tables (error maroon, warning sienna,
# size warning purple and the default #4d4d4d stay distinguishable)
GUI_COLORS = ('#34495e', '#3d5240', '#5a4a36', '#2f5552', '#56523a', '#45405a', '#5a3d48', '#3c4c5c')
# light fills for the Excel export
EXCEL_COLORS = ('#dce6f1', '#e2efda', '#fbe5d6', '#d9eeec', '#f2efd6', '#e4dff0', '#f3dde3', '#dfe7ee')
EXCEL_ERROR = '#f4b6b6'
EXCEL_WARNING = '#fbd5ad'
EXCEL_SIZE_WARNING = '#e3c8ef'


def new_definition(name='Group 1'):
    d = {k: '' for k in DEFINITION_FIELDS}
    d['name'] = name
    d['enabled'] = True
    return d


def clean_definitions(value):
    """definitions from a preset: a list of dicts with every field, anything else is dropped"""
    out = []
    if not isinstance(value, (list, tuple)):
        return out
    for one in value:
        if not isinstance(one, dict):
            continue
        d = new_definition('')
        for k in DEFINITION_FIELDS:
            if k in one and one[k] is not None:
                d[k] = bool(one[k]) if k == 'enabled' else str(one[k])
        # IngestDesktop's older key
        if not d['inheritance_repre_priority'] and one.get('inheritance_priority'):
            d['inheritance_repre_priority'] = str(one['inheritance_priority'])
        out.append(d)
    return out


def split_list(text, commas_only=False):
    """
    'exr, mp4 mov' -> ['exr', 'mp4', 'mov']. commas_only: split at commas and
    line breaks only (column titles can contain spaces).
    """
    if not text:
        return []
    pattern = r'[,\n\r]+' if commas_only else r'[,\s]+'
    return [p.strip() for p in re.split(pattern, str(text)) if p.strip()]


def norm_repre(value):
    return str(value or '').strip().lower().lstrip('.')


def repre_list(text):
    out = []
    for r in split_list(text):
        r = norm_repre(r)
        if r and r not in out:
            out.append(r)
    return out


def config(get):
    """
    :param get: get(key, default) of the settings
    :return: grouping config dict
    """
    cfg = {}
    for key, default in DEFAULTS.items():
        value = get(key, default)
        if isinstance(default, bool):
            if isinstance(value, str):
                value = value.strip().lower() not in ('', 'false', '0', 'off', 'no', 'none')
            value = bool(value)
        elif value is None:
            value = default
        else:
            value = str(value)
        cfg[key] = value
    cfg['definitions'] = clean_definitions(get('group_definitions', []))
    return cfg


def _expand(template, item):
    """template with the item's tokens; '' when a token is unknown"""
    if not template:
        return ''
    text = str(format_keep(template, item)).strip()
    if unresolved_tokens(text):
        return ''
    return text


def _matches(value, patterns):
    value = str(value or '').lower()
    return any(fnmatch.fnmatchcase(value, p.lower()) for p in patterns)


def find_definition(members, definitions, cfg):
    """first enabled definition whose task types and task names match a file of the group"""
    for d in definitions or []:
        if not d.get('enabled', True):
            continue
        types = split_list(d.get('task_types'))
        names = split_list(d.get('task_names'))
        if types and not any(_matches(_expand(cfg['group_task_type'], it), types) for it in members):
            continue
        if names and not any(_matches(_expand(cfg['group_task_name'], it), names) for it in members):
            continue
        return d
    return None


def convert_extensions(item):
    """extensions of the files the Convert rows make from this item (lower case, no dot)"""
    out = set()
    for k, v in item.items():
        if v and isinstance(v, str) and _CONVERT_PATH_RE.match(k):
            ext = v.rsplit('/', 1)[-1].rsplit('\\', 1)[-1]
            if '.' in ext:
                out.add(norm_repre(ext.rsplit('.', 1)[-1]))
    return out


def _join(*parts):
    return '; '.join(p for p in parts if p)


def _clear(item):
    for k in item.pop('_group_keys', None) or []:
        item.pop(k, None)
    for k in TOKENS:
        item[k] = ''
    item['_group_number'] = 0
    item['_group_missing'] = False
    # the check errors / warnings, without the group messages added last time
    if 'check_error' not in item:
        item['check_error'] = item.get('error', '') or ''
    if 'check_warning' not in item:
        item['check_warning'] = item.get('warning', '') or ''
    item['error'] = item['check_error']
    item['warning'] = item['check_warning']


def _copy_tokens(source, target, prefix, added):
    for k, v in list(source.items()):
        if k.startswith('_') or k.startswith(REVIEW_PREFIX) or k.startswith(THUMB_PREFIX):
            continue
        if isinstance(v, (str, int, float)) and not isinstance(v, bool) or v is None:
            target[prefix + k] = '' if v is None else v
            added.append(prefix + k)


def _pick(members, wanted, repre_of):
    for r in wanted:
        for it in members:
            if repre_of[id(it)] == r:
                return it
    return None


def assign(items, cfg):
    """
    Group the items and give them group tokens, errors and warnings.
    Runs again on every refresh: the previous group tokens and messages are
    removed first (check errors are kept in check_error / check_warning).
    :return: list of groups: {key, number, name, items, definition, missing,
             to_convert, error}
    """
    items = [it for it in (items or []) if isinstance(it, dict)]
    for it in items:
        _clear(it)
    if not cfg.get('group_on') or not cfg.get('group_by'):
        return []

    by_key = {}
    order = []
    for it in items:
        if it.get('vendor_skip'):
            continue
        key = _expand(cfg['group_by'], it)
        if not key:
            continue
        if key not in by_key:
            by_key[key] = []
            order.append(key)
        by_key[key].append(it)

    groups = []
    for number, key in enumerate(order, start=1):
        members = by_key[key]
        repre_of = {id(it): norm_repre(_expand(cfg['group_repre'], it)) for it in members}
        d = find_definition(members, cfg['definitions'], cfg)
        name = (d.get('name') or '').strip() if d else ''
        label = name or key
        group = {'key': key, 'number': number, 'name': name, 'items': members,
                 'definition': d, 'missing': [], 'to_convert': [], 'error': ''}
        direct = [repre_of[id(it)] for it in members if repre_of[id(it)]]
        group_errors = []
        item_errors = {id(it): [] for it in members}
        item_warnings = {id(it): [] for it in members}

        if d:
            always = repre_list(d.get('always_repres'))
            convertable = repre_list(d.get('always_or_convert_repres'))
            optional = repre_list(d.get('optional_repres'))
            made = set(direct)
            for it in members:
                made |= convert_extensions(it)
            missing = [r for r in always if r not in direct]
            missing += [r for r in convertable if r not in made and r not in missing]
            group['missing'] = missing
            group['to_convert'] = [r for r in convertable if r not in direct and r in made]
            if missing:
                group_errors.append(f"Group {label}: missing representation(s) {', '.join(missing)}")

            # a required representation with a (check) error fails the group
            required = set(always) | set(convertable)
            failed = sorted({repre_of[id(it)] for it in members
                             if repre_of[id(it)] in required and it.get('check_error')})
            if failed:
                for it in members:
                    if repre_of[id(it)] not in failed:
                        item_errors[id(it)].append(
                            f"Group {label}: required representation(s) {', '.join(failed)} have error(s)")

            defined = always + convertable + optional
            for it in members:
                r = repre_of[id(it)]
                if not r:
                    item_warnings[id(it)].append(f"Group {label}: no representation (Representation is empty)")
                elif defined and r not in defined:
                    item_warnings[id(it)].append(f"Group {label}: representation {r} is not defined in the group")
                elif direct.count(r) > 1:
                    item_warnings[id(it)].append(f"Group {label}: representation {r} is in the group more than once")

        group['error'] = _join(*group_errors)
        review = _pick(members, repre_list(d.get('review_repre')), repre_of) if d else None
        thumb = _pick(members, repre_list(d.get('thumb_source_repre')), repre_of) if d else None

        present = []
        for r in direct:
            if r not in present:
                present.append(r)
        for it in members:
            added = []
            if review is not None:
                _copy_tokens(review, it, REVIEW_PREFIX, added)
            if thumb is not None:
                _copy_tokens(thumb, it, THUMB_PREFIX, added)
            it['_group_keys'] = added
            g_err = _join(group['error'], *item_errors[id(it)])
            g_warn = _join(*item_warnings[id(it)])
            it.update({
                'group_key': key,
                'group_name': name,
                'group_number': number,
                'group_size': len(members),
                'group_repre': repre_of[id(it)],
                'group_repres': ', '.join(present),
                'group_missing': ', '.join(group['missing']),
                'group_to_convert': ', '.join(group['to_convert']),
                'group_error': g_err,
                'group_warning': g_warn,
                '_group_number': number,
                '_group_missing': bool(group['missing']),
            })
            it['error'] = _join(it['check_error'], g_err)
            it['warning'] = _join(it['check_warning'], g_warn)
        groups.append(group)
    return groups


# ------------------------------------------------------------------ rows
# A table row is a list of column values with the item dict as the last element.

def _row_item(row):
    return row[-1] if row and isinstance(row[-1], dict) else None


def _valid(value):
    text = '' if value is None else str(value).strip()
    return text != '' and not unresolved_tokens(text)


def inherit(rows, titles, groups):
    """
    Inherit Columns: in each group, a cell that is empty or has an unknown
    {token} takes the value of the same column from the first file (in
    Inheritance Repre Priority order, then table order) with a good value.
    :return: number of cells filled
    """
    filled = 0
    norm_titles = [str(t).strip().lower() for t in (titles or [])]
    rows_of = {}
    for row in rows or []:
        it = _row_item(row)
        if it is not None:
            rows_of.setdefault(id(it), []).append(row)
    for g in groups or []:
        d = g.get('definition')
        if not d:
            continue
        cols = [norm_titles.index(c.strip().lower()) for c in split_list(d.get('inherit_columns'), commas_only=True)
                if c.strip().lower() in norm_titles]
        if not cols:
            continue
        priority = repre_list(d.get('inheritance_repre_priority'))

        def rank(row, priority=priority):
            r = (_row_item(row) or {}).get('group_repre', '')
            return priority.index(r) if r in priority else len(priority)

        g_rows = [row for it in g['items'] for row in rows_of.get(id(it), [])]
        g_rows = sorted(g_rows, key=rank)   # stable: table order within a rank
        for c in cols:
            source = next((row[c] for row in g_rows if c < len(row) - 1 and _valid(row[c])), None)
            if source is None:
                continue
            for row in g_rows:
                if c < len(row) - 1 and not _valid(row[c]):
                    row[c] = source
                    filled += 1
    return filled


def keep_together(rows):
    """rows of one group follow its first row, other rows keep their order"""
    out = []
    seen = {}
    for row in rows or []:
        it = _row_item(row)
        number = it.get('_group_number', 0) if it else 0
        if not number:
            out.append([row])
            continue
        if number in seen:
            seen[number].append(row)
        else:
            seen[number] = [row]
            out.append(seen[number])
    return [row for block in out for row in block]


def _unique(values):
    out = []
    for v in values:
        if v is None:
            continue
        text = str(v)
        if text.strip() == '' or text in out:
            continue
        out.append(text)
    return out


def collapse(rows, separator=', '):
    """
    One row per group: in each column equal values are shown once, different
    values are joined by separator. The row's item is a summary of the group
    (errors and warnings of all its files) so it is colored like the worst file.
    """
    out = []
    blocks = {}
    for row in rows or []:
        it = _row_item(row)
        number = it.get('_group_number', 0) if it else 0
        if not number:
            out.append(('row', row))
            continue
        if number not in blocks:
            blocks[number] = []
            out.append(('block', blocks[number]))
        blocks[number].append(row)
    result = []
    for kind, entry in out:
        if kind == 'row':
            result.append(entry)
            continue
        if len(entry) == 1:
            result.append(entry[0])
            continue
        width = max(len(r) for r in entry) - 1
        merged = [separator.join(_unique(r[c] if c < len(r) - 1 else '' for r in entry)) for c in range(width)]
        members = [_row_item(r) for r in entry]
        first = members[0]
        summary = {
            'error': '; '.join(_unique(m.get('error', '') for m in members)),
            'warning': '; '.join(_unique(m.get('warning', '') for m in members)),
            'size_warning': '; '.join(_unique(m.get('size_warning', '') for m in members)),
            'group_key': first.get('group_key', ''),
            '_group_number': first.get('_group_number', 0),
            '_group_missing': any(m.get('_group_missing') for m in members),
            '_group_members': members,
        }
        result.append(merged + [summary])
    return result


def exportable(rows):
    """rows without the files of groups that miss a required representation"""
    return [row for row in rows or [] if not (_row_item(row) or {}).get('_group_missing')]


def row_state(item):
    """'error', 'warning', 'size_warning', 'group' or '' for a row's item: errors and warnings win"""
    if not item:
        return ''
    if item.get('error'):
        return 'error'
    if item.get('warning'):
        return 'warning'
    if item.get('size_warning'):
        return 'size_warning'
    if item.get('_group_number'):
        return 'group'
    return ''


def gui_color(item, use_groups=True):
    """background for a gui table row, None for the default"""
    state = row_state(item)
    if state == 'error':
        return 'maroon'
    if state == 'warning':
        return 'sienna'
    if state == 'size_warning':
        return 'purple'
    if state == 'group' and use_groups:
        return GUI_COLORS[(item['_group_number'] - 1) % len(GUI_COLORS)]
    return None


def excel_color(item):
    """fill for an Excel row, None for no fill"""
    state = row_state(item)
    if state == 'error':
        return EXCEL_ERROR
    if state == 'warning':
        return EXCEL_WARNING
    if state == 'size_warning':
        return EXCEL_SIZE_WARNING
    if state == 'group':
        return EXCEL_COLORS[(item['_group_number'] - 1) % len(EXCEL_COLORS)]
    return None
