"""
Personal ftrack / Ayon credentials (credentials.py): order of the sources,
keyring storage under Submission Helper's own names, Ayon token renewal,
ftrack browser sign-in.
"""
import sys
import threading
import types
import unittest
import urllib.request
from unittest import mock

from tests import _stubs  # noqa: F401
import credentials


class FakeKeyring:
    """keyring module stand-in: {(service, item): value}"""

    def __init__(self):
        self.store = {}

    def get_password(self, service, item):
        return self.store.get((service, item))

    def set_password(self, service, item, value):
        self.store[(service, item)] = value

    def delete_password(self, service, item):
        del self.store[(service, item)]


class FakeAyonApi(types.ModuleType):
    """ayon_api stand-in: one valid user / password, tokens expire on demand"""

    def __init__(self):
        super().__init__('ayon_api')
        self.valid_tokens = set()
        self.logins = 0

    def login_to_server(self, url, username, password):
        if (username, password) != ('jan', 'secret'):
            return None
        self.logins += 1
        token = f"token{self.logins}"
        self.valid_tokens.add(token)
        return token

    def is_token_valid(self, url, token):
        return token in self.valid_tokens

    def logout_from_server(self, url, token):
        self.valid_tokens.discard(token)


class Base(unittest.TestCase):

    def setUp(self):
        self.keyring = FakeKeyring()
        credentials.set_keyring_backend(self.keyring)
        credentials.set_prompt_handler(None)
        credentials._declined.clear()
        self.ayon = FakeAyonApi()
        patcher = mock.patch.dict(sys.modules, {'ayon_api': self.ayon})
        patcher.start()
        self.addCleanup(patcher.stop)

    def tearDown(self):
        credentials.set_keyring_backend(None)
        credentials.set_prompt_handler(None)
        credentials._declined.clear()


class Storage(Base):

    def test_own_names_per_host(self):
        credentials.save_ftrack('https://studio.ftrackapp.com/', 'jan', 'k1')
        self.assertEqual(self.keyring.store, {
            ('SubmissionHelper/ftrack/studio.ftrackapp.com', 'username'): 'jan',
            ('SubmissionHelper/ftrack/studio.ftrackapp.com', 'api_key'): 'k1'})
        self.assertEqual(credentials.get_ftrack('studio.ftrackapp.com'), ('jan', 'k1'))
        credentials.clear_ftrack('https://studio.ftrackapp.com')
        self.assertEqual(self.keyring.store, {})

    def test_ayon_launcher_entries_are_not_read(self):
        self.keyring.set_password('AYON/ftrack/studio.ftrackapp.com/api_key', 'api_key', 'x')
        self.assertEqual(credentials.get_ftrack('https://studio.ftrackapp.com'), (None, None))

    def test_no_keyring_is_not_an_error(self):
        credentials.set_keyring_backend(None)
        self.assertEqual(credentials.get_ftrack('https://a'), (None, None))
        self.assertFalse(credentials.save_ftrack('https://a', 'u', 'k'))


class Resolve(Base):

    INSTALL = {'ftrack_server_url': 'https://f', 'ftrack_api_user': 'studio',
               'ftrack_api_key': 'install-key', 'ayon_server_url': 'https://a',
               'ayon_api_key': 'install-token'}

    def test_environment_first(self):
        credentials.save_ftrack('https://f', 'jan', 'kr-key')
        envs = {'FTRACK_SERVER': 'https://f', 'FTRACK_API_USER': 'env', 'FTRACK_API_KEY': 'env-key',
                'AYON_SERVER_URL': 'https://a', 'AYON_API_KEY': 'env-token'}
        p = credentials.resolve({}, envs, self.INSTALL)
        self.assertEqual((p['FTRACK_API_USER'], p['FTRACK_API_KEY']), ('env', 'env-key'))
        self.assertEqual(p['AYON_API_KEY'], 'env-token')
        self.assertEqual(p['_credentials_source'], {'ftrack': 'environment', 'ayon': 'environment'})

    def test_keyring_before_install_json(self):
        credentials.save_ftrack('https://f', 'jan', 'kr-key')
        credentials.save_ayon('https://a', 'jan', 'secret', 'kr-token')
        p = credentials.resolve({}, {}, self.INSTALL)
        self.assertEqual((p['FTRACK_API_USER'], p['FTRACK_API_KEY']), ('jan', 'kr-key'))
        self.assertEqual((p['AYON_API_KEY'], p['AYON_USERNAME']), ('kr-token', 'jan'))
        self.assertEqual(p['_credentials_source'], {'ftrack': 'keyring', 'ayon': 'keyring'})

    def test_install_json_is_the_fallback(self):
        p = credentials.resolve({}, {}, self.INSTALL)
        self.assertEqual((p['FTRACK_API_USER'], p['FTRACK_API_KEY']), ('studio', 'install-key'))
        self.assertEqual(p['AYON_API_KEY'], 'install-token')
        self.assertEqual(p['_credentials_source'], {'ftrack': 'install.json', 'ayon': 'install.json'})

    def test_nothing_anywhere(self):
        p = credentials.resolve({}, {}, {'ftrack_server_url': 'https://f'})
        self.assertEqual((p['FTRACK_SERVER'], p['FTRACK_API_USER'], p['FTRACK_API_KEY']),
                         ('https://f', '', ''))
        self.assertEqual(p['_credentials_source'], {'ftrack': None, 'ayon': None})

    def test_url_typed_in_the_dialog(self):
        credentials.save_server_url('ayon', 'https://typed')
        p = credentials.resolve({}, {}, {})
        self.assertEqual(p['AYON_SERVER_URL'], 'https://typed')


class StartupEnvironment(Base):

    def test_token_set_by_the_app_itself_is_not_taken_as_environment(self):
        # ayon_api / AyonShotlist write AYON_API_KEY into os.environ when they connect
        with mock.patch.dict('os.environ', {'AYON_API_KEY': 'set-by-sh'}):
            self.assertEqual(credentials.startup_env()['AYON_API_KEY'],
                             credentials._STARTUP_ENV['AYON_API_KEY'])
            self.assertNotEqual(credentials.startup_env()['AYON_API_KEY'], 'set-by-sh')


class Ayon(Base):

    def _paths(self):
        return credentials.resolve({}, {'AYON_SERVER_URL': 'https://a'}, {})

    def test_expired_token_is_renewed_with_the_stored_password(self):
        token, _ = credentials.ayon_login('https://a', 'jan', 'secret')
        credentials.save_ayon('https://a', 'jan', 'secret', token)
        self.ayon.valid_tokens.clear()            # session expired
        p = self._paths()
        self.assertTrue(credentials.ensure_ayon(p, ask=False))
        self.assertEqual(p['AYON_API_KEY'], 'token2')
        self.assertEqual(credentials.get_ayon('https://a')[2], 'token2')

    def test_valid_token_is_not_renewed(self):
        token, _ = credentials.ayon_login('https://a', 'jan', 'secret')
        credentials.save_ayon('https://a', 'jan', 'secret', token)
        p = self._paths()
        credentials.ensure_ayon(p, ask=False)
        self.assertEqual(self.ayon.logins, 1)

    def test_no_credentials_asks_once(self):
        asked = []

        def handler(kind, url):
            asked.append((kind, url))
            token, _ = credentials.ayon_login(url, 'jan', 'secret')
            return credentials.save_ayon(url, 'jan', 'secret', token)

        credentials.set_prompt_handler(handler)
        p = self._paths()
        self.assertTrue(credentials.ensure_ayon(p))
        self.assertEqual(asked, [('ayon', 'https://a')])
        self.assertEqual(p['_credentials_source']['ayon'], 'keyring')

    def test_cancelled_sign_in_is_not_asked_again(self):
        asked = []
        credentials.set_prompt_handler(lambda kind, url: asked.append(kind) or False)
        p = self._paths()
        self.assertFalse(credentials.ensure_ayon(p))
        self.assertFalse(credentials.ensure_ayon(p))
        self.assertEqual(asked, ['ayon'])
        self.assertTrue(credentials.prompt('ayon', 'https://a', force=True) is False)
        self.assertEqual(asked, ['ayon', 'ayon'])

    def test_headless_never_asks(self):
        self.assertFalse(credentials.ensure_ayon(self._paths()))

    def test_environment_token_is_used_as_is(self):
        p = credentials.resolve({}, {'AYON_SERVER_URL': 'https://a', 'AYON_API_KEY': 'launcher'}, {})
        self.assertTrue(credentials.ensure_ayon(p, ask=False))
        self.assertEqual(p['AYON_API_KEY'], 'launcher')

    def test_wrong_password(self):
        token, message = credentials.ayon_login('https://a', 'jan', 'nope')
        self.assertIsNone(token)
        self.assertIn('wrong', message)

    def test_logout_forgets_everything(self):
        token, _ = credentials.ayon_login('https://a', 'jan', 'secret')
        credentials.save_ayon('https://a', 'jan', 'secret', token)
        credentials.ayon_logout('https://a')
        self.assertEqual(credentials.get_ayon('https://a'), (None, None, None))
        self.assertNotIn(token, self.ayon.valid_tokens)


class Ftrack(Base):

    def test_ensure_asks_and_uses_the_stored_key(self):
        def handler(kind, url):
            return credentials.save_ftrack(url, 'jan', 'personal')

        credentials.set_prompt_handler(handler)
        p = credentials.resolve({}, {'FTRACK_SERVER': 'https://f'}, {})
        self.assertTrue(credentials.ensure_ftrack(p))
        self.assertEqual((p['FTRACK_API_USER'], p['FTRACK_API_KEY']), ('jan', 'personal'))

    def test_browser_sign_in_receives_the_personal_key(self):
        received = []
        done = threading.Event()

        def browser(url):
            # what ftrack does: redirect the browser to redirect_url with the credentials
            self.assertTrue(url.startswith('https://f/user/api_credentials?redirect_url=http://localhost:'))
            redirect = url.split('redirect_url=', 1)[1]

            def visit():
                body = urllib.request.urlopen(f"{redirect}/?api_user=jan&api_key=personal", timeout=5).read()
                received.append(body)
            threading.Thread(target=visit, daemon=True).start()

        def callback(user, key):
            received.append((user, key))
            done.set()

        login = credentials.FtrackBrowserLogin('https://f/', callback, open_browser=browser)
        login.start()
        self.assertTrue(done.wait(5))
        login.join(5)
        self.assertIn(('jan', 'personal'), received)


if __name__ == '__main__':
    unittest.main()
