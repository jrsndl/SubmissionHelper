import os
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
    
    frames = int(frames)
    fps = float(fps)

    hours = int(frames / 3600 / fps)
    minutes = int((frames - hours * 3600 * fps) / 60 / fps)
    seconds = int((frames - (hours * 3600 * fps) - (minutes * 60 * fps)) / fps)
    frames = int(frames - (hours * 3600 * fps) - (minutes * 60 * fps) - (seconds * fps))
    ms = int(1000 / fps)
    miliseconds = frames * ms
    __timecode = str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2) + '.' + str(
        miliseconds)

    return __timecode


def frames_to_seconds(frames, fps):

    frames = int(frames)
    try:
        fps = float(fps)
    except:
        if '/' in fps:
            a = float(fps.split('/')[0])
            b = float(fps.split('/')[1])
            fps = float(a) / float(b)
        else:
            fps = None

    if fps:
        hours = int(frames / 3600 / fps)
        minutes = int((frames - hours * 3600 * fps) / 60 / fps)
        seconds = int((frames - (hours * 3600 * fps) - (minutes * 60 * fps)) / fps)
        frames = int(frames - (hours * 3600 * fps) - (minutes * 60 * fps) - (seconds * fps))
        ms = int(1000 / fps)
        miliseconds = frames * ms
        total_seconds = float(hours * 3600 + minutes * 60 + seconds) + float(0.001 * miliseconds)
    else:
        total_seconds = 0

    return str(total_seconds)

def seconds_to_frames(seconds, fps):

    seconds = float(seconds)
    try:
        fps = float(fps)
    except:
        if '/' in fps:
            a = float(fps.split('/')[0])
            b = float(fps.split('/')[1])
            fps = float(a) / float(b)
        else:
            fps = None

    if fps:
        total_frames = fps * seconds
    else:
        total_frames = 0

    return str(total_frames)

def tc_to_frames(tc, fps_a, fps_b):

    def _seconds(value, fr_int):
        _zip_ft = zip((3600, 60, 1, 1 / fr_int), value.split(':'))
        return sum(f * float(t) for f, t in _zip_ft)

    def _frames(secs, fr_int):
        return secs * fr_int

    fr_int = int(round(float(float(fps_a) / float(fps_b))))
    return round(_frames(_seconds(tc, fr_int), fr_int))

def frames_to_tc(frames, fps_a, fps_b):

    fps = int(round(float(float(fps_a) / float(fps_b))))
    h = int(frames / (3600 * fps))
    m = int(frames / (60 * fps)) % 60
    s = int((frames % (60 * fps)) / fps)
    f = frames % (60 * fps) % fps
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

    if sys.platform.startswith('darvin'):
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
    except:
        pass
    return '{} {}{}'.format(r, unit, suffix)

if __name__ == "__main__":
    tc_to_frames('00:00:41:16', 24000, 1001)
