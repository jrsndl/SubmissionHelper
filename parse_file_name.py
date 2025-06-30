# -*- coding: utf-8 -*-

"""
This module parses full file path and separates it to parts

"""
import os
import re


def parse(file_name):
    r"""
    Parses file path

    Replaces backslashes with slashes to normalise windows schizofreny
    For unc paths like //host/mount/dir/fname.ext, parts will return '//' as first part
    If path starts with drive letter, it is separated to seq.drive
    If filename ends with slash, last part will be empty string

    >>> parse("\\\\server\\directory\\filename.1234.ext")
    {'unc_host': '//server/directory', 'clean_name_no_sep': 'filename', 'number': 1234, 'padding': 4,
    'clean_name_sep_char': '.', 'path': '//server/directory', 'clean_name': 'filename.', 'number_string': '1234',
    'name': 'filename.1234', 'extension': 'ext', 'drive': '', 'parts': ['//', 'server', 'directory',
     'filename.1234.ext'], 'full_path': '//server/directory/filename.1234.ext'}

    >>> parse("c:\\dir\\cleanname.0001.JPG")
    {'unc_host': '', 'clean_name_no_sep': 'cleanname', 'number': 1, 'padding': 4, 'clean_name_sep_char': '.',
    'path': 'c:/dir', 'clean_name': 'cleanname.', 'number_string': '0001', 'name': 'cleanname.0001',
    'extension': 'JPG', 'drive': 'c:', 'parts': ['/', 'dir', 'cleanname.0001.JPG'], 'full_path': 'c:/dir/cleanname.0001.JPG'}
    """

    # Replaces backslashes with slashes to normalise windows schizophrenia
    fn = file_name.replace('\\', '/')
    try:
        filename = fn.decode("utf-8")
    except:
        filename = fn

    seq = dict(full_path=filename, drive=u'', unc_host=u'', path=u'', name=u'', extension='', clean_name=u'',
               number_string='', number=-1, padding=-1, clean_name_no_sep=u'', clean_name_sep_char='', parts=[])

    # detects UNC and drive letters
    #seq['unc_host'], path = os.path.splitunc(filename)
    seq['drive'], path = os.path.splitdrive(filename)

    # split path to directories and filename
    seq['parts'] = []
    while True:
        newpath, tail = os.path.split(path)
        if newpath == path:
            assert not tail
            if path: seq['parts'].append(path)
            break
        seq['parts'].append(tail)
        path = newpath
    seq['parts'].reverse()

    seq['path'] = os.path.dirname(filename)
    seq['name'] = os.path.basename(filename)

    if seq['path'] is None:
        seq['path'] = ''
        seq['name'] = seq["full_path"]

    seq['name'], seq['extension'] = os.path.splitext(seq['name'])
    if seq["extension"] is None:
        seq["extension"] = ''
    else:
        seq["extension"] = seq["extension"][1:]

    NM_RE = re.compile(r".*?(?P<snm>[0-9]+)$")
    m = NM_RE.search(seq["name"])
    if m is not None:
        seq["number_string"] = m.group("snm")
        seq["padding"] = len(seq["number_string"])
        seq["number"] = int(seq["number_string"])
        CN_RE = re.compile(r"(?P<cn>.*?)[0-9]+$")
        n = CN_RE.search(seq["name"])
        if n:
            seq["clean_name"] = n.group("cn")
    else:
        seq["clean_name"] = seq["name"]

    seq["clean_name_no_sep"] = seq["clean_name"]
    if seq["number"] != -1 and len(seq["clean_name"]) > 0:
        if seq["clean_name"][-1] == '.':
            seq["clean_name_no_sep"] = seq["clean_name"][:-1]
            seq["clean_name_sep_char"] = '.'
        if seq["clean_name"][-1] == '_':
            seq["clean_name_no_sep"] = seq["clean_name"][:-1]
            seq["clean_name_sep_char"] = '_'
        if seq["clean_name"][-1] == '-':
            seq["clean_name_no_sep"] = seq["clean_name"][:-1]
            seq["clean_name_sep_char"] = '-a'

    return seq


def pad_frame(frame, pad):
    """returns string with number with leading zeroes"""
    r = ''

    if frame is None:
        frame = -1

    if frame != -1 and pad != -1:
        r = '0' * (pad - len(str(frame))) + str(frame)

    return r


def printf_pattern(full_path):
    """
    Expects first frame from file sequence, returns file name with printf notation.
    Can handle file name with no path
    """

    prs = parse(full_path)

    # if normal
    r = prs['clean_name'] + '%0' + str(prs['padding']) + 'd.' + prs['extension']
    h = prs['clean_name'] + '#' * int(prs['padding']) + '.' + prs['extension']

    # check if there are leading zeroes
    # WARNING this will not work if it is not first frame of the sequence !!!
    if len(str(prs['number'])) == prs['padding']:
        r = prs['clean_name'] + '%' + str(prs['padding']) + 'd.' + prs['extension']
        h = prs['clean_name'] + '#' * int(prs['padding']) + '.' + prs['extension']

    # if no number (overwrites previous)
    if prs['padding'] == -1:
        r = prs['clean_name'] + '.' + prs['extension']
        h = r

    return r, h


def path_from_path_and_number(some_path, number):
    """
    Creates full path from other path and file number.
    For file sequence c:\test.1234.dpx and number 3 -> c:\test.0003.dpx
    """

    prs = parse(some_path)
    numstr = pad_frame(number, prs['padding'])
    return prs['paths'] + '/' + prs['clean_name'] + numstr + '.' + prs['extension']


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # print(parse("cleanname.1.JPG"))
    # print(printf_pattern("c:\\dir\\cleanname.JPG"))

