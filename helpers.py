import os
import re
import sys
import inspect
import math


def get_script_path():
    """
    Get file path for running script
    """
    # get file path for running script
    script_path = os.path.dirname(os.path.abspath(inspect.stack()[-1][1])).replace("\\", "/")

    return script_path


def get_home_dir():
    hd = os.path.expanduser('~')
    if not hd:
        hd = ''
    return hd


def get_fps_ratio(in_fps):

    if 23.965 < in_fps < 23.981:
        fps_a = 24000
        fps_b = 1001
    elif 29.965 < in_fps < 29.981:
        fps_a = 30000
        fps_b = 1001
    elif 59.93 < in_fps < 59.95:
        fps_a = 60000
        fps_b = 1001
    else:
        fps_a = int(in_fps)
        fps_b = 1

    return fps_a, fps_b


def get_fps_for_PyTimeCode(in_fps):
    """
    expects string as argument, for example from ffprobe meta
    returns fps in string as expected for PyTimeCode
    """

    f_fps = float(in_fps)

    if 23.965 < f_fps < 23.981:
        return '23.98'
    if 29.965 < f_fps < 29.981:
        return '29.97'
    if 59.8 < f_fps < 59.95:
        return '59.94'
    if 23.99 < f_fps < 24.01:
        return '24'
    if 24.99 < f_fps < 25.01:
        return '25'
    if 29.99 < f_fps < 30.01:
        return '30'
    if 49.99 < f_fps < 50.01:
        return '50'
    if 59.99 < f_fps < 60.01:
        return '60'
    # some unsupported fps
    return ''


def frames_to_ffmpeg_tc(frames, fps):
    """frames to an ffmpeg time "HH:MM:SS.mmm" (milliseconds zero padded)"""
    frames = int(frames)
    fps = float(fps)
    total_ms = int(round(frames * 1000.0 / fps)) if fps else 0
    hours, rest = divmod(total_ms, 3600 * 1000)
    minutes, rest = divmod(rest, 60 * 1000)
    seconds, miliseconds = divmod(rest, 1000)
    return "{:02d}:{:02d}:{:02d}.{:03d}".format(hours, minutes, seconds, miliseconds)


def _fps_value(fps):
    """fps as float from a number, "25", "23.976" or "24000/1001"; None if unknown"""
    try:
        return float(fps)
    except (TypeError, ValueError):
        pass
    try:
        a, b = str(fps).split('/')
        return float(a) / float(b)
    except (TypeError, ValueError, ZeroDivisionError):
        return None


def frames_to_seconds(frames, fps):
    """seconds (as text, 3 decimals) of the frame count at the fps"""
    frames = int(frames)
    fps = _fps_value(fps)
    if fps:
        total_seconds = round(frames / fps, 3)
    else:
        total_seconds = 0
    return str(total_seconds)


def seconds_to_frames(seconds, fps):

    seconds = float(seconds)
    fps = _fps_value(fps)
    if fps:
        total_frames = fps * seconds
    else:
        total_frames = 0

    return str(total_frames)


def _nominal_fps(fps_a, fps_b):
    """whole frames per second used for timecode counting (23.976 -> 24)"""
    fps = _fps_value(f"{fps_a}/{fps_b}") if str(fps_b) not in ('', '1', '1.0') else _fps_value(fps_a)
    if not fps:
        raise ValueError(f"invalid frame rate {fps_a}/{fps_b}")
    return int(round(fps))


def tc_to_frames(tc, fps_a, fps_b):
    """
    Timecode to a frame count. Fields can be separated by ':' ';' '.' or ',';
    a ';' (or '.' / ',') before the frames means drop frame, which is counted
    the SMPTE way for 29.97 and 59.94.
    """
    text = str(tc).strip()
    parts = re.split(r'[:;.,]', text)
    if len(parts) != 4:
        raise ValueError(f"invalid timecode {tc!r}")
    h, m, s, f = (int(p) for p in parts)
    fps = _nominal_fps(fps_a, fps_b)
    frames = ((h * 3600) + (m * 60) + s) * fps + f
    drop = bool(re.search(r'[;.,]\d+$', text)) and fps in (30, 60)
    if drop:
        dropped = fps // 15     # 2 for 29.97, 4 for 59.94
        total_minutes = 60 * h + m
        frames -= dropped * (total_minutes - total_minutes // 10)
    return frames


def frames_to_tc(frames, fps_a, fps_b):
    """frame count to a non drop frame timecode HH:MM:SS:FF"""
    frames = int(frames)
    fps = _nominal_fps(fps_a, fps_b)
    h = frames // (3600 * fps)
    m = (frames // (60 * fps)) % 60
    s = (frames % (60 * fps)) // fps
    f = frames % fps
    return "{:02d}:{:02d}:{:02d}:{:02d}".format(h, m, s, f)


def get_pixel_aspect_ratio(in_pa):
    # pal fha 1.4222222
    if 1.41 < in_pa < 1.43:
        return 64, 45

    # pal 1.0666666
    if 1.05 < in_pa < 1.07:
        return 16, 15

    # ntsc 720*486 1.111
    if 1.1 < in_pa < 1.12:
        return 16, 15

    # 4:3
    if 1.32 < in_pa < 1.34:
        return 4, 3

    # 1.3 squeeze
    if 1.29 < in_pa < 1.31:
        return 13, 10

    # 2 squeeze
    if 1.99 < in_pa < 2.01:
        return 2, 1

    # fallback
    return in_pa, 1


def get_platform():

    platform = 'win'
    platform_exe_ext = '.exe'

    if sys.platform.startswith('darwin'):
        platform = 'mac'
        platform_exe_ext = ''
    if str(os.name).startswith('posix'):
        platform = 'nix'
        platform_exe_ext = ''

    return platform, platform_exe_ext

def humanize_file_size(size, suffix="B"):
    r = ''
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(size) < 1024.0:
            r = f"{size:3.1f}"
            break
        size /= 1024.0
    if r == '':
        r = f"{size:.1f}"
        unit = 'Yi'
    try:
        rr = r.split('.')
        if int(rr[1]) == 0:
            r = rr[0]
    except Exception:
        pass
    return '{} {}{}'.format(r, unit, suffix)

def no_window():
    """
    Popen keyword arguments that keep a console window from opening for
    console programs (ffprobe, oiiotool, converts, ayon) on Windows.
    Needed when the app runs without a console (the windowed exe).
    """
    if sys.platform == 'win32':
        import subprocess
        return {'creationflags': getattr(subprocess, 'CREATE_NO_WINDOW', 0x08000000)}
    return {}


if __name__ == "__main__":
    print(tc_to_frames('00:00:41:16', 24000, 1001))
