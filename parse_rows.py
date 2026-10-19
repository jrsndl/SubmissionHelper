"""
Parsing tab rows as a list of tuples (name, pattern, repl, source, filter):
the row operations of the Parsing table (parse_rows_widget.py), without Qt.

Presets keep the rows as parse_<field>_01 .. parse_<field>_48 (PARSE_ROWS);
the table shows only the rows in use, in order, and writes them back
compacted from row 01.
"""
import re

FIELDS = ('name', 'pattern', 'repl', 'source', 'filter')
TITLES = ('Name', 'Pattern', 'Repl', 'Source', 'Filter')
EMPTY = ('',) * len(FIELDS)


def clean(row):
    """a row as a tuple of len(FIELDS) strings"""
    row = [str(v) if v is not None else '' for v in (row or ())][:len(FIELDS)]
    return tuple(row + [''] * (len(FIELDS) - len(row)))


def is_empty(row):
    return not any(str(v).strip() for v in clean(row))


def used_rows(rows):
    """the rows that aren't empty, in order"""
    return [clean(r) for r in rows if not is_empty(r)]


def field_key(row, field):
    """settings key of a parse field: parse_name_01 ..."""
    return f"parse_{field}_{row:02d}"


def slot_values(settings, defaults, count):
    """
    The count parse rows a preset sets, as rows of values in row order.
    A field the preset doesn't have (presets from before rows 33-48 or the
    Filter column) gets its default from the .ui file (defaults, as
    ui_defaults.load_defaults), else '' - never the value of the preset
    loaded before. Like the command line, which lays presets over the defaults.
    """
    settings = settings or {}
    defaults = defaults or {}
    rows = []
    for row in range(1, count + 1):
        values = []
        for field in FIELDS:
            key = field_key(row, field)
            one = settings.get(key)
            if not isinstance(one, dict):
                one = defaults.get(key)
            value = one.get('value') if isinstance(one, dict) else None
            values.append('' if value is None else str(value))
        rows.append(tuple(values))
    return rows


def to_slots(rows, count):
    """count rows for the parse_*_NN fields: rows first, then empty rows"""
    rows = [clean(r) for r in rows][:count]
    return rows + [EMPTY] * (count - len(rows))


def delete(rows, indexes):
    drop = set(indexes)
    return [r for i, r in enumerate(rows) if i not in drop]


def move(rows, indexes, delta):
    """
    Move the rows at indexes up (delta -1) or down (+1) by one, as a block
    that stops at the top / bottom. :return: (rows, new indexes)
    """
    rows = list(rows)
    sel = sorted(set(i for i in indexes if 0 <= i < len(rows)))
    if not sel or delta not in (-1, 1):
        return rows, sel
    if (delta < 0 and sel[0] == 0) or (delta > 0 and sel[-1] == len(rows) - 1):
        return rows, sel
    order = sel if delta < 0 else list(reversed(sel))
    for i in order:
        rows[i], rows[i + delta] = rows[i + delta], rows[i]
    return rows, [i + delta for i in sel]


def insert(rows, at, new_rows, limit=None):
    """
    Insert new_rows at position at. limit: max number of rows; rows that
    don't fit are dropped. :return: (rows, indexes of the inserted rows, dropped count)
    """
    rows = list(rows)
    new_rows = [clean(r) for r in new_rows]
    at = max(0, min(at, len(rows)))
    room = len(new_rows) if limit is None else max(0, limit - len(rows))
    fit = new_rows[:room]
    rows[at:at] = fit
    return rows, list(range(at, at + len(fit))), len(new_rows) - len(fit)


def to_tsv(rows):
    """rows as tab separated lines (Excel, a text editor, Paste)"""
    return "\n".join("\t".join(_one_line(v) for v in clean(r)) for r in rows)


def _one_line(value):
    return str(value).replace("\t", " ").replace("\r", " ").replace("\n", " ")


def from_tsv(text):
    """
    Rows from tab separated lines; a line with fewer fields gets empty ones.
    Empty lines are skipped. A pasted header line (Name, Pattern...) is skipped.
    """
    rows = []
    for line in str(text or '').replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        if not line.strip():
            continue
        row = clean(line.split("\t"))
        if tuple(v.strip().lower() for v in row) == tuple(t.lower() for t in TITLES):
            continue
        rows.append(row)
    return rows


def is_rows_text(text):
    """clipboard text that is rows (tabs or several lines), not one value"""
    text = str(text or '').strip("\r\n")
    return "\t" in text or "\n" in text or "\r" in text


def row_problem(row):
    """
    Why the sequencer skips or can't use the row, '' when it is fine.
    (Sequencer.prepare_regex uses a row with Name, Pattern and Source and a
    valid Pattern.)
    """
    name, pattern, _repl, source, _filter = clean(row)
    if is_empty(row):
        return ''
    missing = [t for t, v in (('Name', name), ('Pattern', pattern), ('Source', source)) if not v]
    if missing:
        return f"Skipped: {', '.join(missing)} empty"
    return pattern_error(pattern)


def pattern_error(pattern):
    """'' or the regex error of the pattern"""
    if not pattern:
        return ''
    try:
        re.compile(pattern)
    except re.error as e:
        return f"Invalid pattern: {e}"
    return ''
