import logging
import unittest
from unittest import mock

from tests import _stubs  # noqa: F401
import ftrack
import sequencer


class OpenSessionTest(unittest.TestCase):
    def setUp(self):
        ftrack._SESSIONS.clear()
        ftrack._FAILED.clear()
        ftrack._last_message = None

    def test_missing_settings_no_crash_one_warning(self):
        with mock.patch.object(ftrack.ftrack_api, 'Session') as S:
            with self.assertLogs('Ftrack', 'WARNING') as cm:
                self.assertIsNone(ftrack.open_session('', 'me', ''))
                self.assertIsNone(ftrack.open_session('', 'me', ''))   # repeated refresh
            S.assert_not_called()
        self.assertEqual(len(cm.output), 1)
        self.assertIn('server url, api key', cm.output[0])

    def test_connection_error_logged_and_not_retried_at_once(self):
        with mock.patch.object(ftrack.ftrack_api, 'Session', side_effect=TypeError('boom')) as S:
            with self.assertLogs('Ftrack', 'ERROR'):
                self.assertIsNone(ftrack.open_session('https://x', 'me', 'k'))
            self.assertIsNone(ftrack.open_session('https://x', 'me', 'k'))
            self.assertEqual(S.call_count, 1)

    def test_session_reused(self):
        with mock.patch.object(ftrack.ftrack_api, 'Session') as S:
            a = ftrack.open_session('https://x', 'me', 'k')
            b = ftrack.open_session('https://x', 'me', 'k')
            self.assertIs(a, b)
            self.assertEqual(S.call_count, 1)
            ftrack.open_session('https://x', 'other', 'k')
            self.assertEqual(S.call_count, 2)


class SequencerFtrackTest(unittest.TestCase):
    def setUp(self):
        ftrack._SESSIONS.clear()
        ftrack._FAILED.clear()
        ftrack._last_message = None

    def test_ftrack_on_without_server_does_not_crash(self):
        # the reported crash: TypeError Required "server_url" not specified
        s = sequencer.Sequencer.__new__(sequencer.Sequencer)
        s.log = logging.getLogger('test')
        s.settings = {'ftrack_use': {'value': True}, 'ftrack_project': {'value': 'P'},
                      'ftrack_label_use': {'value': True}, 'ftrack_label': {'value': 'client'}}
        s.ftrack = {}
        s.paths = {'FTRACK_SERVER': '', 'FTRACK_API_KEY': '', 'FTRACK_API_USER': ''}
        with mock.patch.object(ftrack.ftrack_api, 'Session',
                               side_effect=TypeError('Required "server_url" not specified')):
            with self.assertLogs('Ftrack', 'WARNING'):
                s.get_ftrack_session()
        self.assertIsNone(s.ftrack['session'])
        self.assertIsNone(s.ftrack['project_id'])
        self.assertIsNone(s.ftrack['label_obj'])


if __name__ == '__main__':
    unittest.main()
