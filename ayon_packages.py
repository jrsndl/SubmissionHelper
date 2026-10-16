"""
Package tracking in Ayon.

A package sent to the client holds one or more Ayon versions, each with one or
more representations. This module

* pairs a package file with one representation of its Ayon version
  (by file extension first, then by file size), and
* records into the entity "data" which packages include a version (and which
  of its representations) and which packages include a representation.

Layout written to the entity data (keyed by package name, so recording the
same package again only updates it):

    version data:
        {"submissionHelper": {"packages": {
            "<package>": {"representations": ["exr", "mov"],
                          "date": "2026-10-16T13:50:00+02:00", "user": "jan"}}}}
    representation data:
        {"submissionHelper": {"packages": {
            "<package>": {"date": "...", "user": "..."}}}}

Everything here except write_package_records is plain data handling, so it can
be tested without an Ayon server.
"""
import copy
import fnmatch
import json
import logging
import os

DATA_KEY = "submissionHelper"
PACKAGES_KEY = "packages"

# spellings of the same file type
EXT_ALIASES = {
    'jpeg': 'jpg',
    'tiff': 'tif',
    'mpeg': 'mpg',
    'htm': 'html',
    'yml': 'yaml',
}


def norm_ext(ext):
    """'.EXR' -> 'exr', 'jpeg' -> 'jpg'"""
    ext = str(ext or '').strip().lower().lstrip('.')
    return EXT_ALIASES.get(ext, ext)


def _as_dict(value):
    """entity data comes as a dict or a json string"""
    if isinstance(value, dict):
        return value
    if isinstance(value, str) and value.strip():
        try:
            data = json.loads(value)
            return data if isinstance(data, dict) else {}
        except ValueError:
            return {}
    return {}


def repre_summary(repre):
    """
    What the pairing needs from an Ayon representation.
    :param repre: representation dict (id, name, files, context)
    :return: {'id', 'name', 'ext', 'size', 'files'}; size is the sum of the
             file sizes in bytes, None when Ayon has no size for some file
    """
    files = [f for f in (repre.get('files') or []) if isinstance(f, dict)]
    ext = ''
    for f in files:
        name = f.get('name') or os.path.basename(str(f.get('path') or ''))
        if '.' in name:
            ext = name.rsplit('.', 1)[-1]
            break
    if not ext:
        context = _as_dict(repre.get('context'))
        ext = context.get('ext') or ''
    if not ext:
        # representations are usually named by their extension
        ext = repre.get('name') or ''
    size = None
    if files:
        try:
            size = sum(int(f.get('size')) for f in files)
        except (TypeError, ValueError):
            size = None
    return {
        'id': repre.get('id'),
        'name': repre.get('name') or '',
        'ext': norm_ext(ext),
        'size': size,
        'files': len(files),
    }


def _size(value):
    try:
        size = int(value)
    except (TypeError, ValueError):
        return None
    return size if size > 0 else None


def pair_representation(ext, size, repres, allowed=None):
    """
    Pick the representation of a version that a package file is.

    1. representations with the file's extension; one -> done
    2. more than one (or none): the one whose size (sum of its files) equals
       the file size (sum of the frames for a sequence)

    :param ext: file extension
    :param size: file size in bytes (0 / None when sizes were not scanned)
    :param repres: repre_summary dicts of the version
    :param allowed: representation name patterns from the product filters
                    (wildcards, not case sensitive); empty means any
    :return: (summary or None, how) - how is 'extension', 'extension+size'
             or 'size' on success, otherwise the reason it failed
    """
    candidates = list(repres or [])
    patterns = [p for p in (allowed or []) if p]
    if patterns:
        candidates = [r for r in candidates
                      if any(fnmatch.fnmatchcase(r['name'].lower(), p.lower()) for p in patterns)]
    if not candidates:
        return None, 'no representations'
    size = _size(size)
    ext = norm_ext(ext)

    by_ext = [r for r in candidates if ext and r['ext'] == ext]
    if len(by_ext) == 1:
        return by_ext[0], 'extension'
    if by_ext:
        if size is None:
            return None, f"{len(by_ext)} representations with extension {ext}, file size unknown"
        by_size = [r for r in by_ext if r['size'] == size]
        if len(by_size) == 1:
            return by_size[0], 'extension+size'
        if by_size:
            return None, f"{len(by_size)} representations with extension {ext} and the same size"
        return None, f"{len(by_ext)} representations with extension {ext}, none with size {size}"

    # no extension match: an exact byte size is still a strong match
    if size is not None:
        by_size = [r for r in candidates if r['size'] == size]
        if len(by_size) == 1:
            return by_size[0], 'size'
        if by_size:
            return None, f"{len(by_size)} representations with size {size}"
    return None, f"no representation with extension {ext or '?'}" + \
        (f" or size {size}" if size is not None else "")


def collect_package_records(items):
    """
    What the package holds, from the paired files.
    :param items: dicts with '_ayon_version_id', and for paired files
                  '_ayon_repre_id' / '_ayon_repre_name'
    :return: {'versions': {version id: set of repre names},
              'repres': {repre id: version id}}
    """
    versions = {}
    repres = {}
    for item in items:
        vid = item.get('_ayon_version_id')
        if not vid:
            continue
        names = versions.setdefault(vid, set())
        rid = item.get('_ayon_repre_id')
        if rid:
            names.add(item.get('_ayon_repre_name') or '')
            repres[rid] = vid
    for names in versions.values():
        names.discard('')
    return {'versions': versions, 'repres': repres}


def _packages_of(data):
    sh = _as_dict(data).get(DATA_KEY)
    packages = _as_dict(sh).get(PACKAGES_KEY) if isinstance(sh, dict) else None
    return packages if isinstance(packages, dict) else {}


def recorded_packages(data):
    """package names recorded in an entity's data"""
    return sorted(_packages_of(data))


def merged_version_data(data, package, repre_names, info):
    """
    New version data with the package added, or None when it is already
    recorded with the same representations (nothing to write).
    The representations of an already recorded package are replaced: the
    package as it is now is what was sent.
    :param info: extra values for a new entry, e.g. {'date': ..., 'user': ...}
    """
    names = sorted(set(repre_names or []))
    old = _packages_of(data).get(package)
    if isinstance(old, dict) and sorted(old.get('representations') or []) == names:
        return None
    entry = dict(old) if isinstance(old, dict) else dict(info or {})
    if isinstance(old, dict):
        entry.update({k: v for k, v in (info or {}).items() if k == 'user'})
        if info and info.get('date'):
            entry['updated'] = info['date']
    entry['representations'] = names
    return _with_entry(data, package, entry)


def merged_repre_data(data, package, info):
    """New representation data with the package added, None if already there"""
    if package in _packages_of(data):
        return None
    return _with_entry(data, package, dict(info or {}))


def _with_entry(data, package, entry):
    new = copy.deepcopy(_as_dict(data))
    sh = new.get(DATA_KEY)
    if not isinstance(sh, dict):
        sh = {}
        new[DATA_KEY] = sh
    packages = sh.get(PACKAGES_KEY)
    if not isinstance(packages, dict):
        packages = {}
        sh[PACKAGES_KEY] = packages
    packages[package] = entry
    return new


def write_package_records(con, project, records, package, info, log=None, dry_run=False):
    """
    Record the package on its versions and representations.

    The current data is read right before writing and the package is merged
    into it, so data written by other tools stays. Entities that already
    have the package (with the same representations) are not written.

    :param con: ayon_api server connection
    :param records: from collect_package_records
    :param dry_run: only log what would be written
    :return: dict with counts: versions / repres written, already recorded,
             and errors (list of messages)
    """
    log = log or logging.getLogger("AyonPackages")
    result = {'versions': 0, 'repres': 0, 'versions_same': 0, 'repres_same': 0, 'errors': []}
    version_ids = set(records.get('versions') or {})
    repre_ids = set(records.get('repres') or {})
    if not version_ids and not repre_ids:
        return result

    current_versions = {}
    current_repres = {}
    try:
        if version_ids:
            for v in con.get_versions(project, version_ids=version_ids, fields={"id", "data"}):
                current_versions[v['id']] = v.get('data')
        if repre_ids:
            for r in con.get_representations(project, representation_ids=repre_ids,
                                             fields={"id", "data"}):
                current_repres[r['id']] = r.get('data')
    except Exception as e:
        result['errors'].append(f"reading current data failed: {e}")
        return result

    updates = []    # (entity type, id, new data)
    for vid, names in records['versions'].items():
        if vid not in current_versions:
            result['errors'].append(f"version {vid} not found")
            continue
        new = merged_version_data(current_versions[vid], package, names, info)
        if new is None:
            result['versions_same'] += 1
        else:
            updates.append(('version', vid, new))
    for rid in records['repres']:
        if rid not in current_repres:
            result['errors'].append(f"representation {rid} not found")
            continue
        new = merged_repre_data(current_repres[rid], package, info)
        if new is None:
            result['repres_same'] += 1
        else:
            updates.append(('representation', rid, new))

    if dry_run:
        for entity_type, eid, new in updates:
            log.info(f"Record package (dry run): {entity_type} {eid} data -> "
                     f"{json.dumps(new.get(DATA_KEY), sort_keys=True)}")
    elif updates:
        try:
            from ayon_api.operations import OperationsSession
            session = OperationsSession(con)
            for entity_type, eid, new in updates:
                session.update_entity(project, entity_type, eid, {"data": new})
            session.commit()
        except Exception as e:
            result['errors'].append(f"writing to Ayon failed: {e}")
            return result
    for entity_type, _, _ in updates:
        result['versions' if entity_type == 'version' else 'repres'] += 1
    return result
