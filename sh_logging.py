"""
Central logging for Submission Helper.

Every module logs through the standard ``logging`` module
(``logging.getLogger(__name__)`` or a named logger). ``setup_logging`` adds:

* a console handler (stderr) with its own level, or none at all
* an optional log file (always full detail, DEBUG)
* an in-memory buffer (``LOG_BUFFER``) that keeps the last records so the
  GUI log tab can show them, re-filter them by level / text and save them

The buffer has no Qt dependency. The GUI subscribes with
``LOG_BUFFER.add_listener(callback)``; the callback may be called from worker
threads, so the GUI forwards it through a Qt signal to the main thread.
"""
import collections
import contextlib
import itertools
import logging
import sys
import threading

# below DEBUG, for very chatty messages (every gui keystroke). Not recorded
# unless the root logger is set to TRACE explicitly.
TRACE = 5
logging.addLevelName(TRACE, 'TRACE')

LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL,
}
LEVEL_NAMES = ['DEBUG', 'INFO', 'WARNING', 'ERROR']

# third party libraries that are chatty at INFO / DEBUG
NOISY_LOGGERS = ['httpx', 'httpcore', 'urllib3', 'requests', 'ftrack_api', 'ayon_api',
                 'PIL', 'asyncio']

CONSOLE_FORMAT = '%(asctime)s %(levelname)-7s %(name)s: %(message)s'
CONSOLE_DATEFMT = '%H:%M:%S'
FILE_FORMAT = '%(asctime)s %(levelname)-7s %(name)s [%(threadName)s]: %(message)s'


def level_from_name(name, default=logging.INFO):
    """
    'debug' / 'INFO' / 'warning' ... -> logging level, None for 'none' / 'off'
    """
    if name is None:
        return default
    if isinstance(name, int):
        return name
    name = str(name).strip().lower()
    if name in ('none', 'off', 'quiet'):
        return None
    return LEVELS.get(name, default)


class LogBuffer(logging.Handler):
    """
    Keeps the last ``capacity`` formatted records and notifies listeners.
    Thread safe: records may arrive from metadata worker threads.
    """

    def __init__(self, capacity=20000):
        super().__init__(level=logging.DEBUG)
        # entries are (seq, levelno, line); seq lets listeners skip
        # records they already drew from a snapshot
        self.records = collections.deque(maxlen=capacity)
        self._seq = itertools.count(1)
        self._last = 0
        self.counts = collections.Counter()
        self._listeners = []
        self._lock_listeners = threading.Lock()
        self.setFormatter(logging.Formatter(CONSOLE_FORMAT, CONSOLE_DATEFMT))

    def emit(self, record):
        try:
            line = self.format(record)
        except Exception:
            self.handleError(record)
            return
        with self.lock:
            entry = (next(self._seq), record.levelno, line)
            self._last = entry[0]
            self.records.append(entry)
            if record.levelno >= logging.WARNING:
                self.counts[record.levelno >= logging.ERROR and 'error' or 'warning'] += 1
        with self._lock_listeners:
            listeners = list(self._listeners)
        for one in listeners:
            try:
                one(entry)
            except Exception:
                # a broken listener must never break logging
                pass

    def add_listener(self, callback):
        with self._lock_listeners:
            self._listeners.append(callback)

    def remove_listener(self, callback):
        with self._lock_listeners:
            if callback in self._listeners:
                self._listeners.remove(callback)

    def snapshot(self, min_level=logging.DEBUG, text=''):
        """
        Records at or above min_level, optionally containing text (case insensitive)
        :return: list of (seq, levelno, line)
        """
        text = (text or '').lower()
        with self.lock:
            items = list(self.records)
        return [r for r in items if r[1] >= min_level and (not text or text in r[2].lower())]

    def last_seq(self):
        """Sequence number of the newest record ever logged (not reset by clear)"""
        with self.lock:
            return self._last

    def clear(self):
        with self.lock:
            self.records.clear()
            self.counts.clear()


LOG_BUFFER = LogBuffer()

_console_handler = None
_file_handler = None


def setup_logging(console_level=logging.INFO, log_file=None):
    """
    Configure the root logger. Safe to call more than once.
    :param console_level: level for stderr output, None to disable console output
    :param log_file: optional path, gets everything from DEBUG up
    :return: the root logger
    """
    global _console_handler, _file_handler
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    # remove handlers from earlier calls / basicConfig
    for h in list(root.handlers):
        if h is LOG_BUFFER or h is _console_handler or h is _file_handler \
                or type(h) is logging.StreamHandler:
            root.removeHandler(h)

    root.addHandler(LOG_BUFFER)

    _console_handler = None
    # sys.stderr is None under pythonw / a windowed build
    if console_level is not None and sys.stderr is not None:
        _console_handler = logging.StreamHandler(sys.stderr)
        _console_handler.setLevel(console_level)
        _console_handler.setFormatter(logging.Formatter(CONSOLE_FORMAT, CONSOLE_DATEFMT))
        root.addHandler(_console_handler)

    if _file_handler is not None:
        _file_handler.close()
    _file_handler = None
    if log_file:
        _file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
        _file_handler.setLevel(logging.DEBUG)
        _file_handler.setFormatter(logging.Formatter(FILE_FORMAT))
        root.addHandler(_file_handler)

    for name in NOISY_LOGGERS:
        logging.getLogger(name).setLevel(logging.WARNING)
    return root


def install_excepthook():
    """
    Log uncaught exceptions (with traceback) instead of only printing them,
    so they show in the GUI log tab and the log file.
    """
    log = logging.getLogger('SubmissionHelper')

    def _hook(exc_type, exc, tb):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc, tb)
            return
        log.critical("Unhandled error: %s", exc, exc_info=(exc_type, exc, tb))

    sys.excepthook = _hook

    def _thread_hook(args):
        if args.exc_type is SystemExit:
            return
        log.critical("Unhandled error in thread %s: %s",
                     getattr(args.thread, 'name', '?'), args.exc_value,
                     exc_info=(args.exc_type, args.exc_value, args.exc_traceback))

    threading.excepthook = _thread_hook


_qt_suppress = threading.local()


@contextlib.contextmanager
def qt_messages_suppressed():
    """
    Drop Qt messages raised while the body runs. The log view uses this while
    drawing, so a Qt warning caused by drawing a log line can't feed itself.
    """
    prev = getattr(_qt_suppress, 'on', False)
    _qt_suppress.on = True
    try:
        yield
    finally:
        _qt_suppress.on = prev


def uninstall_qt_message_handler(QtCore):
    """
    Call after app.exec_() returns: Qt prints while tearing down, Python may
    be finalizing by then.
    """
    try:
        QtCore.qInstallMessageHandler(None)
    except Exception:
        pass


def install_qt_message_handler(QtCore):
    """
    Route Qt's own messages (qt.gui.icc ..., QPainter warnings) to logging
    under the 'Qt' logger.
    """
    log = logging.getLogger('Qt')
    mapping = {
        QtCore.QtMsgType.QtDebugMsg: logging.DEBUG,
        QtCore.QtMsgType.QtWarningMsg: logging.WARNING,
        QtCore.QtMsgType.QtCriticalMsg: logging.ERROR,
        QtCore.QtMsgType.QtFatalMsg: logging.CRITICAL,
    }
    info = getattr(QtCore.QtMsgType, 'QtInfoMsg', None)
    if info is not None:
        mapping[info] = logging.INFO

    def _handler(mode, context, message):
        if getattr(_qt_suppress, 'on', False):
            return
        category = getattr(context, 'category', None)
        if category and category != 'default':
            message = f"{category}: {message}"
        log.log(mapping.get(mode, logging.WARNING), message)

    QtCore.qInstallMessageHandler(_handler)
