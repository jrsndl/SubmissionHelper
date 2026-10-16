#-*- coding: utf-8 -*-
import os
import struct
import logging

log = logging.getLogger('parse_metadata')


class EXR_ATTRIBUTES:
    COMPRESSION_VALUES = ('NO_COMPRESSION', 'RLE_COMPRESSION',
                          'ZIPS_COMPRESSION', 'ZIP_COMPRESSION',
                          'PIZ_COMPRESSION', 'PXR24_COMPRESSION',
                          'B44_COMPRESSION', 'B44A_COMPRESSION',
                          'DWAA_COMPRESSION', 'DWAB_COMPRESSION')

    LINE_ORDER = ('INCREASING_Y', 'DECREASING_Y', 'RANDOM_Y')

    ENVMAP_TYPES = ('ENVMAP_LATLONG', 'ENVMAP_CUBE')


def read_until_null(filebuffer, maxbytes=1024):
    """Reads a file until a null character

    Args:
        filebuffer (obj): a file that was opened with open()
        maxbytes (int): number of bytes that will be read if no null byte is found
        Avoids infinite loops.

    Returns:
        bytes: the bytes read, without the null byte
        int: how many bytes were read, the null byte included; 0 at the end
             of the file
    """

    current_string = b''
    bytes_read = 0
    while True:
        current_byte = filebuffer.read(1)
        if not current_byte:
            # end of file before the null byte
            return current_string, bytes_read
        bytes_read += 1
        if current_byte == b'\x00':
            break
        current_string += current_byte
        if bytes_read > maxbytes:
            log.warning('EXR header string too long, stopped reading (corrupt file?)')
            break

    return current_string, bytes_read


def _cstring(buf, pos):
    """null terminated string in buf at pos: (bytes, position after the null)"""
    end = buf.find(b'\x00', pos)
    if end < 0:
        return buf[pos:], len(buf)
    return buf[pos:end], end + 1


def convert_to_unicode_string(data):
    """Recursively convert dictionary keys and values to unicode strings"""
    if isinstance(data, dict):
        return {
            convert_to_unicode_string(k): convert_to_unicode_string(v)
            for k, v in data.items()
        }
    elif isinstance(data, list):
        return [convert_to_unicode_string(v) for v in data]
    elif isinstance(data, bytes):
        try:
            _r = str(data, encoding='utf-8')
        except Exception:
            try:
                _r = "".join(chr(x) for x in bytearray(data))
            except Exception:
                _r = ''
        return _r
    else:
        return data


EXR_MAGIC = 20000630


def _parse_chlist(value):
    channel_data = {}
    pos = 0
    while pos < len(value):
        channel_name, pos = _cstring(value, pos)
        if not channel_name:
            # null name: end of the channel list
            break
        if pos + 16 > len(value):
            break
        pixel_type, p_linear, r1, r2, r3, x_sampling, y_sampling = struct.unpack_from('<iBBBBii', value, pos)
        pos += 16
        channel_data[channel_name] = {
            'pixel_type': pixel_type,
            'pLinear': p_linear,
            'reserved': [r1, r2, r3],
            'xSampling': x_sampling,
            'ySampling': y_sampling
        }
    return channel_data


def _parse_value(attribute_type, value):
    """
    Value of one header attribute from its bytes. Unknown types return None
    (the attribute is skipped, the rest of the header is still read).
    """
    t = attribute_type

    def box(fmt):
        v = struct.unpack_from('<' + fmt * 4, value)
        return {'xMin': v[0], 'yMin': v[1], 'xMax': v[2], 'yMax': v[3]}

    if t == b'box2i':
        return box('i')
    if t == b'box2f':
        return box('f')
    if t == b'chlist':
        return _parse_chlist(value)
    if t == b'chromaticities':
        c = struct.unpack_from('<8f', value)
        return dict(zip(('redX', 'redY', 'greenX', 'greenY', 'blueX', 'blueY', 'whiteX', 'whiteY'), c))
    if t == b'compression':
        try:
            return EXR_ATTRIBUTES.COMPRESSION_VALUES[value[0]]
        except IndexError:
            return 'unknown'
    if t == b'double':
        return struct.unpack_from('<d', value)[0]
    if t == b'envmap':
        try:
            return EXR_ATTRIBUTES.ENVMAP_TYPES[value[0]]
        except IndexError:
            return 'unknown'
    if t == b'float':
        return struct.unpack_from('<f', value)[0]
    if t == b'int':
        return int(struct.unpack_from('<i', value)[0])
    if t == b'keycode':
        k = struct.unpack_from('<7i', value)
        return dict(zip(('filmMfcCode', 'filmType', 'prefix', 'count', 'perfOffset',
                         'perfsPerFrame', 'perfsPerCount'), k))
    if t == b'lineOrder':
        try:
            return EXR_ATTRIBUTES.LINE_ORDER[value[0]]
        except IndexError:
            return 'unknown'
    if t in (b'm33f', b'm33d', b'm44f', b'm44d'):
        n = 9 if t.startswith(b'm33') else 16
        return struct.unpack_from('<%d%s' % (n, 'f' if t.endswith(b'f') else 'd'), value)
    if t == b'preview':
        width, height = struct.unpack_from('<II', value)
        return {'width': width, 'height': height, 'pixel_data': tuple(value[8:8 + 4 * width * height])}
    if t == b'rational':
        first, second = struct.unpack_from('<iI', value)
        return {'first_num': first, 'second_num': second}
    if t == b'string':
        return bytes(value)
    if t == b'stringvector':
        out = []
        pos = 0
        while pos + 4 <= len(value):
            length = struct.unpack_from('<i', value, pos)[0]
            pos += 4
            out.append(bytes(value[pos:pos + length]))
            pos += length
        return out
    if t == b'tiledesc':
        x_size, y_size, mode = struct.unpack_from('<IIB', value)
        return {'xSize': x_size, 'ySize': y_size, 'mode': mode}
    if t == b'timecode':
        time_and_flags, user_data = struct.unpack_from('<II', value)
        return {'timeAndFlags': time_and_flags, 'userData': user_data}
    vectors = {b'v2i': 'ii', b'v2f': 'ff', b'v2d': 'dd', b'v3i': 'iii', b'v3f': 'fff', b'v3d': 'ddd'}
    if t in vectors:
        return list(struct.unpack_from('<' + vectors[t], value))
    return None


def read_exr_header(exrpath, maxreadsize=2000):
    """Parses the header of an exr file using the official specification :
    https://www.openexr.com/documentation/openexrfilelayout.pdf

    Every attribute is read by its declared size, so an attribute of an
    unknown type (or one that fails to parse) is skipped and the rest of the
    header is still read. A truncated file returns what was read so far.

    Args:
        exrpath (str): absolute path to the exr file
        maxreadsize (int, optional): Avoids infinite loops in case a final null
            byte is never encountered or the exr is formatted in a bad way.
            Defaults to 2000.

    Raises:
        OSError: if the exr does not exist
        ValueError: if the file is not an exr (wrong magic number)

    Returns:
        dict: with the metadata
    """

    if not os.path.exists(exrpath):
        raise OSError('given EXR path does not exist ({})'.format(exrpath))

    metadata = {}
    with open(exrpath, 'rb') as exr_file:
        head = exr_file.read(8)
        if len(head) < 8 or struct.unpack_from('<i', head)[0] != EXR_MAGIC:
            raise ValueError('not an EXR file ({})'.format(exrpath))

        for _ in range(maxreadsize):
            # attribute name and type are null terminated, then the size and
            # the value follow; an empty name ends the header
            attribute_name, name_read = read_until_null(exr_file)
            if name_read == 0:
                log.debug('EXR header ended early (truncated file?): %s', exrpath)
                break
            if not attribute_name:
                break
            attribute_type, type_read = read_until_null(exr_file)
            size_bytes = exr_file.read(4)
            if type_read == 0 or len(size_bytes) < 4:
                log.debug('EXR header ended early (truncated file?): %s', exrpath)
                break
            attribute_size = struct.unpack('<i', size_bytes)[0]
            if attribute_size < 0:
                log.debug('EXR header: invalid size of %s in %s', attribute_name, exrpath)
                break
            value = exr_file.read(attribute_size)
            if len(value) < attribute_size:
                log.debug('EXR header ended early (truncated file?): %s', exrpath)
                break

            try:
                parsed = _parse_value(attribute_type, value)
            except (struct.error, IndexError, ValueError) as e:
                log.debug('EXR header: %s (%s) not readable: %s', attribute_name, attribute_type, e)
                continue
            if parsed is None:
                log.debug('EXR header: skipped attribute %s of unknown type %s', attribute_name, attribute_type)
                continue
            if attribute_type == b'compression':
                metadata['compression'] = parsed
            else:
                metadata[attribute_name] = parsed

    return convert_to_unicode_string(metadata)
