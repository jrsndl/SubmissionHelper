import io
import logging
import os
import tempfile
import threading
import unittest
from unittest import mock

from tests import _stubs  # noqa: F401
import sh_logging
from sh_logging import LogBuffer
import log_view
import submission_helper as sh


class LogBufferTest(unittest.TestCase):
    def setUp(self):
        self.buf = LogBuffer(capacity=100)
        self.log = logging.getLogger('test.buffer')
        self.log.setLevel(logging.DEBUG)
        self.log.propagate = False
        self.log.addHandler(self.buf)
        self.addCleanup(self.log.removeHandler, self.buf)

    def test_filter_by_level_and_text(self):
        self.log.debug('dbg one')
        self.log.info('info two')
        self.log.warning('warn three')
        self.log.error('err four')
        self.assertEqual(len(self.buf.snapshot()), 4)
        self.assertEqual([lv for _, lv, _ in self.buf.snapshot(logging.WARNING)],
                         [logging.WARNING, logging.ERROR])
        self.assertEqual(len(self.buf.snapshot(logging.DEBUG, 'TWO')), 1)

    def test_counts_and_clear(self):
        self.log.warning('w')
        self.log.warning('w')
        self.log.critical('c')
        self.assertEqual(self.buf.counts['warning'], 2)
        self.assertEqual(self.buf.counts['error'], 1)
        last = self.buf.last_seq()
        self.buf.clear()
        self.assertEqual(self.buf.snapshot(), [])
        # clear must not move the sequence back, the gui relies on it
        self.assertEqual(self.buf.last_seq(), last)
        self.assertEqual(self.buf.counts['error'], 0)

    def test_capacity(self):
        for i in range(150):
            self.log.info(f'line {i}')
        lines = self.buf.snapshot()
        self.assertEqual(len(lines), 100)
        self.assertIn('line 149', lines[-1][2])
        # sequence numbers keep increasing
        self.assertEqual(lines[-1][0], self.buf.last_seq())
        self.assertLess(lines[0][0], lines[-1][0])

    def test_listener_from_threads_and_broken_listener(self):
        got = []
        self.buf.add_listener(lambda e: 1 / 0)       # must not break logging
        self.buf.add_listener(got.append)
        threads = [threading.Thread(target=self.log.info, args=(f't{i}',)) for i in range(20)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.assertEqual(len(got), 20)


class SetupLoggingTest(unittest.TestCase):
    def tearDown(self):
        sh_logging.setup_logging(logging.WARNING)

    def test_console_level_and_file(self):
        with tempfile.TemporaryDirectory() as d:
            pth = os.path.join(d, 'sh.log')
            err = io.StringIO()
            with mock.patch('sys.stderr', err):
                sh_logging.setup_logging(logging.WARNING, pth)
                logging.getLogger('x').info('only in file')
                logging.getLogger('x').warning('everywhere')
            sh_logging.setup_logging(None)   # closes the file
            self.assertNotIn('only in file', err.getvalue())
            self.assertIn('everywhere', err.getvalue())
            with open(pth, encoding='utf-8') as f:
                content = f.read()
            self.assertIn('only in file', content)
            self.assertIn('everywhere', content)

    def test_no_console(self):
        err = io.StringIO()
        with mock.patch('sys.stderr', err):
            sh_logging.setup_logging(None)
            logging.getLogger('x').error('hidden')
        self.assertEqual(err.getvalue(), '')

    def test_repeated_setup_does_not_duplicate(self):
        sh_logging.setup_logging(logging.INFO)
        sh_logging.setup_logging(logging.INFO)
        root = logging.getLogger()
        self.assertEqual(sum(1 for h in root.handlers if h is sh_logging.LOG_BUFFER), 1)
        self.assertEqual(sum(1 for h in root.handlers if type(h) is logging.StreamHandler), 1)

    def test_trace_not_recorded(self):
        sh_logging.setup_logging(None)
        before = sh_logging.LOG_BUFFER.last_seq()
        logging.getLogger('x').log(sh_logging.TRACE, 'keystroke')
        self.assertEqual(sh_logging.LOG_BUFFER.last_seq(), before)

    def test_qt_suppression_flag(self):
        self.assertFalse(getattr(sh_logging._qt_suppress, 'on', False))
        with sh_logging.qt_messages_suppressed():
            self.assertTrue(sh_logging._qt_suppress.on)
        self.assertFalse(sh_logging._qt_suppress.on)

    def test_no_stderr(self):
        with mock.patch('sys.stderr', None):
            sh_logging.setup_logging(logging.INFO)
            logging.getLogger('x').error('nowhere to go')  # must not raise

    def test_noisy_libraries_quiet(self):
        sh_logging.setup_logging(logging.DEBUG)
        self.assertEqual(logging.getLogger('httpx').level, logging.WARNING)

    def test_level_names(self):
        self.assertEqual(sh_logging.level_from_name('DEBUG'), logging.DEBUG)
        self.assertIsNone(sh_logging.level_from_name('none'))
        self.assertEqual(sh_logging.level_from_name('bogus'), logging.INFO)


class CliLoggingArgsTest(unittest.TestCase):
    def level(self, *argv):
        return sh.console_level_from_args(vars(sh.get_args(list(argv))))

    def test_flags(self):
        self.assertEqual(self.level(), logging.INFO)
        self.assertEqual(self.level('-v'), logging.DEBUG)
        self.assertEqual(self.level('-q'), logging.WARNING)
        self.assertEqual(self.level('--log-level', 'error'), logging.ERROR)
        self.assertIsNone(self.level('--log-level', 'none'))

    def test_log_file_arg(self):
        a = vars(sh.get_args(['--log-file', 'x.log']))
        self.assertEqual(a['log_file'], 'x.log')


class LogViewHtmlTest(unittest.TestCase):
    def test_escaped_and_colored(self):
        h = log_view.record_to_html(logging.ERROR, '<b>&"x"')
        self.assertIn('&lt;b&gt;&amp;', h)
        self.assertIn(log_view.COLORS[logging.ERROR], h)
        self.assertIn('color:#123456', log_view.record_to_html(logging.INFO, 'plain', '#123456'))
        self.assertIn('white-space:pre', h)

    def test_log_widget_not_saved_to_presets(self):
        self.assertIn('log', sh.MainWindow.NOT_SETTINGS)


class AyonPublishLogMaskTest(unittest.TestCase):
    def test_api_keys_not_logged(self):
        from ayon_publish import AyonPublish
        a = AyonPublish({k: {'value': 'v'} for k in
                         ('dead_primpool', 'dead_group', 'dead_priority', 'dead_department', 'dead_limits')},
                        {'ayon': 'ayon', 'deadline': 'dl', 'AYON_API_KEY': 'SECRET123',
                         'FTRACK_API_KEY': 'SECRET456'})
        a.csv_path = 'x.csv'
        a.csv_name = 'x'
        a.ayon_csv = ['ayon', 'addon']
        buf = LogBuffer()
        lg = logging.getLogger('AyonPublish')
        lg.addHandler(buf)
        lg.setLevel(logging.DEBUG)
        self.addCleanup(lg.removeHandler, buf)
        with mock.patch.object(a, 'external_execute', return_value=0):
            a.publish_deadline()
        text = '\n'.join(line for _, _, line in buf.snapshot())
        self.assertNotIn('SECRET', text)
        self.assertIn('AYON_API_KEY=***', text)


if __name__ == '__main__':
    unittest.main()
