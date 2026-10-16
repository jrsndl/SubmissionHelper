"""
Personal ftrack / Ayon credentials of the user, kept in the system keyring
(Windows: Credential Manager), never in a file.

Where credentials come from, first found wins:

1. environment: FTRACK_SERVER / FTRACK_API_USER / FTRACK_API_KEY and
   AYON_SERVER_URL / AYON_API_KEY (studio launcher, AYON launcher, farm)
2. the keyring: what the user entered in Submission Helper's sign-in dialog
3. install.json: ftrack_api_user / ftrack_api_key, ayon_api_key (fallback,
   kept for existing setups)
4. nothing: in the GUI the sign-in dialog asks, headless runs log an error

Server urls come from the environment, else install.json, else the url the
user typed in the sign-in dialog.

Everything is stored under Submission Helper's own names
("SubmissionHelper/ftrack/<host>", "SubmissionHelper/ayon/<host>"); the
AYON launcher's or anybody else's entries are never read or written.

ftrack: personal API key, received from the ftrack web app in the browser
(see FtrackBrowserLogin) or typed in. API keys don't expire.

Ayon: user name and password, logged in once; the session token, the user
name and the password are stored. The token is checked before use and
renewed with the stored password when it has expired.

This module has no Qt dependency; the dialogs are in credentials_dialog.py.
"""
import functools
import html
import logging
import os
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse

log = logging.getLogger("Credentials")

KEYRING_PREFIX = "SubmissionHelper"

FTRACK = "ftrack"
AYON = "ayon"

# sources of the credentials in use
SOURCE_ENV = "environment"
SOURCE_KEYRING = "keyring"
SOURCE_INSTALL = "install.json"

# The credential variables as they were when the app started: Submission
# Helper (and ayon_api) set AYON_API_KEY in its own environment when it
# connects, a renewed keyring token must not look like one from the launcher.
CREDENTIAL_ENV_KEYS = ("FTRACK_SERVER", "FTRACK_API_USER", "FTRACK_API_KEY",
                       "AYON_SERVER_URL", "AYON_API_KEY", "AYON_USERNAME")
_STARTUP_ENV = {k: os.environ.get(k, "") for k in CREDENTIAL_ENV_KEYS}


def startup_env():
    """credential environment variables of the app start (see above)"""
    return dict(_STARTUP_ENV)


# ---------------------------------------------------------------- keyring

_keyring_module = None
_keyring_failed = False


def _keyring():
    """the keyring module (Windows Credential Manager on Windows), or None"""
    global _keyring_module, _keyring_failed
    if _keyring_module is not None or _keyring_failed:
        return _keyring_module
    try:
        import keyring
        if sys.platform == "win32":
            # a frozen app (PyInstaller) doesn't always find the backend by
            # itself: set it explicitly
            from keyring.backends import Windows
            keyring.set_keyring(Windows.WinVaultKeyring())
        _keyring_module = keyring
    except Exception as e:
        _keyring_failed = True
        log.warning(f"The system keyring is not available, credentials can't be stored: {e}")
    return _keyring_module


def set_keyring_backend(module):
    """tests: use a fake keyring module (get/set/delete_password)"""
    global _keyring_module, _keyring_failed
    _keyring_module = module
    _keyring_failed = module is None


def hostname(url):
    """'https://studio.ftrackapp.com/' -> 'studio.ftrackapp.com'"""
    if not url:
        return ""
    if "//" not in url:
        url = "//" + url
    return (parse.urlparse(url).hostname or "").lower()


def _service(kind, url):
    return f"{KEYRING_PREFIX}/{kind}/{hostname(url)}"


def _get(kind, url, item):
    kr = _keyring()
    if kr is None or not hostname(url):
        return None
    try:
        return kr.get_password(_service(kind, url), item)
    except Exception as e:
        log.warning(f"Reading {kind} credentials from the keyring failed: {e}")
        return None


def _set(kind, url, item, value):
    kr = _keyring()
    if kr is None or not hostname(url):
        return False
    try:
        kr.set_password(_service(kind, url), item, value)
        return True
    except Exception as e:
        log.error(f"Storing {kind} credentials in the keyring failed: {e}")
        return False


def _delete(kind, url, item):
    kr = _keyring()
    if kr is None or not hostname(url):
        return
    try:
        if kr.get_password(_service(kind, url), item) is not None:
            kr.delete_password(_service(kind, url), item)
    except Exception as e:
        log.warning(f"Removing {kind} credentials from the keyring failed: {e}")


def get_server_url(kind):
    """server url the user typed in the sign-in dialog (no url configured)"""
    kr = _keyring()
    if kr is None:
        return ""
    try:
        return kr.get_password(f"{KEYRING_PREFIX}/{kind}", "server_url") or ""
    except Exception:
        return ""


def save_server_url(kind, url):
    kr = _keyring()
    if kr is None or not url:
        return
    try:
        kr.set_password(f"{KEYRING_PREFIX}/{kind}", "server_url", url)
    except Exception as e:
        log.warning(f"Storing the {kind} server url failed: {e}")


# ---------------------------------------------------------------- ftrack

def get_ftrack(url):
    """(username, api_key) stored for this ftrack server, or (None, None)"""
    return _get(FTRACK, url, "username"), _get(FTRACK, url, "api_key")


def save_ftrack(url, username, api_key):
    ok = _set(FTRACK, url, "username", username)
    ok = _set(FTRACK, url, "api_key", api_key) and ok
    if ok:
        log.info(f"ftrack credentials of {username} stored for {hostname(url)}")
    return ok


def clear_ftrack(url):
    _delete(FTRACK, url, "username")
    _delete(FTRACK, url, "api_key")
    log.info(f"ftrack credentials removed for {hostname(url)}")


def check_ftrack(url, username, api_key):
    """
    True when the server accepts the user and key. Never raises.
    :return: (ok, message)
    """
    if not url or not username or not api_key:
        return False, "server, user name and API key are needed"
    try:
        import ftrack_api
        session = ftrack_api.Session(server_url=url, api_key=api_key, api_user=username,
                                     auto_connect_event_hub=False, timeout=15)
        try:
            user = session.query(f'User where username is "{username}"').first()
        finally:
            session.close()
        if user is None:
            return False, f"user {username} not found"
        return True, ""
    except Exception as e:
        return False, str(e)


class _FtrackLoginHandler(BaseHTTPRequestHandler):
    """receives the redirect from the ftrack web app with the credentials"""

    def __init__(self, on_credentials, *args, **kwargs):
        self.on_credentials = on_credentials
        super().__init__(*args, **kwargs)

    def log_message(self, format_str, *args):
        log.debug("ftrack sign-in: " + (format_str % args))

    def do_GET(self):
        query = parse.parse_qs(parse.urlparse(self.path).query)
        api_user = (query.get("api_user") or [None])[0]
        api_key = (query.get("api_key") or [None])[0]
        if api_user and api_key:
            body = (f"<html><body style='font-family:sans-serif'><h2>Signed in to ftrack as "
                    f"{html.escape(api_user)}</h2><p>You can close this tab and return to "
                    f"Submission Helper.</p></body></html>")
        else:
            body = "<html><body><h2>ftrack sign-in failed</h2></body></html>"
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))
        if api_user and api_key:
            self.on_credentials(api_user, api_key)


class FtrackBrowserLogin(threading.Thread):
    """
    Sign in to ftrack in the web browser, the way the ftrack addon of AYON does
    it (ynput/ayon-ftrack, Apache-2.0): a one-shot web server on localhost,
    the browser opens <server>/user/api_credentials?redirect_url=<that server>,
    the ftrack web app (where the user is signed in, or signs in) redirects
    back with api_user and the user's personal api_key.

    callback(api_user, api_key) runs in this thread; it is not called when the
    user never finishes (stop() ends the wait).
    """

    def __init__(self, url, callback, open_browser=webbrowser.open_new_tab):
        super().__init__(daemon=True)
        self.url = url.rstrip("/")
        self.callback = callback
        self.open_browser = open_browser
        self._server = HTTPServer(("localhost", 0),
                                  functools.partial(_FtrackLoginHandler, self._received))
        self.login_url = (f"{self.url}/user/api_credentials"
                          f"?redirect_url=http://localhost:{self._server.server_port}")
        self._stopped = False

    def _received(self, api_user, api_key):
        self.callback(api_user, api_key)

    def run(self):
        self.open_browser(self.login_url)
        try:
            self._server.handle_request()
        except Exception as e:
            if not self._stopped:
                log.warning(f"ftrack browser sign-in failed: {e}")
        finally:
            self._server.server_close()

    def stop(self):
        self._stopped = True
        try:
            self._server.server_close()
        except Exception:
            pass


# ---------------------------------------------------------------- Ayon

def get_ayon(url):
    """(username, password, token) stored for this Ayon server"""
    return _get(AYON, url, "username"), _get(AYON, url, "password"), _get(AYON, url, "token")


def save_ayon(url, username, password, token):
    ok = _set(AYON, url, "username", username)
    ok = _set(AYON, url, "password", password) and ok
    ok = _set(AYON, url, "token", token) and ok
    if ok:
        log.info(f"Ayon credentials of {username} stored for {hostname(url)}")
    return ok


def clear_ayon(url):
    for item in ("username", "password", "token"):
        _delete(AYON, url, item)
    log.info(f"Ayon credentials removed for {hostname(url)}")


def ayon_login(url, username, password):
    """
    Log in to Ayon. Never raises.
    :return: (token or None, message)
    """
    if not url or not username or not password:
        return None, "server, user name and password are needed"
    try:
        import ayon_api
        token = ayon_api.login_to_server(url.rstrip("/"), username, password)
    except Exception as e:
        return None, str(e)
    if not token:
        return None, "wrong user name or password"
    return token, ""


def ayon_token_valid(url, token):
    if not url or not token:
        return False
    try:
        import ayon_api
        return bool(ayon_api.is_token_valid(url.rstrip("/"), token))
    except Exception as e:
        log.warning(f"Checking the Ayon login failed: {e}")
        return False


def renew_ayon_token(url):
    """
    The stored token when it is still valid, else a new one from the stored
    user name and password (stored again). None when there is nothing stored
    or the login fails.
    """
    username, password, token = get_ayon(url)
    if token and ayon_token_valid(url, token):
        return token
    if not username or not password:
        return None
    new_token, message = ayon_login(url, username, password)
    if new_token is None:
        log.warning(f"Renewing the Ayon login of {username} failed: {message}")
        return None
    _set(AYON, url, "token", new_token)
    log.info(f"Ayon login of {username} renewed")
    return new_token


def ayon_logout(url):
    """end the stored session on the server and forget the credentials"""
    _, _, token = get_ayon(url)
    if token:
        try:
            import ayon_api
            ayon_api.logout_from_server(url.rstrip("/"), token)
        except Exception as e:
            log.debug(f"Ayon logout failed: {e}")
    clear_ayon(url)


# ---------------------------------------------------------------- resolve

def _install(settings_inst, *names):
    for name in names:
        value = (settings_inst or {}).get(name)
        if value:
            return value
    return ""


def resolve(paths, envs, settings_inst):
    """
    Fill the credential keys of paths (Sequencer.paths) by the order in the
    module docstring and record where they came from in
    paths['_credentials_source'] = {'ftrack': ..., 'ayon': ...}.

    Network free: an Ayon token from the keyring is checked (and renewed)
    later, by ensure_ayon().
    """
    sources = {FTRACK: None, AYON: None}

    # ftrack
    url = (envs.get("FTRACK_SERVER") or _install(settings_inst, "ftrack_server_url", "server_url")
           or get_server_url(FTRACK))
    user, key = envs.get("FTRACK_API_USER"), envs.get("FTRACK_API_KEY")
    if user and key:
        sources[FTRACK] = SOURCE_ENV
    else:
        user, key = get_ftrack(url) if url else (None, None)
        if user and key:
            sources[FTRACK] = SOURCE_KEYRING
        else:
            user = _install(settings_inst, "ftrack_api_user", "api_user")
            key = _install(settings_inst, "ftrack_api_key", "api_key")
            if user and key:
                sources[FTRACK] = SOURCE_INSTALL
            else:
                user, key = "", ""
    paths["FTRACK_SERVER"] = url or ""
    paths["FTRACK_API_USER"] = user
    paths["FTRACK_API_KEY"] = key

    # Ayon
    url = (envs.get("AYON_SERVER_URL") or _install(settings_inst, "ayon_server_url")
           or get_server_url(AYON))
    token = envs.get("AYON_API_KEY")
    username = envs.get("AYON_USERNAME") or ""
    if token:
        sources[AYON] = SOURCE_ENV
    else:
        stored_user, _, token = get_ayon(url) if url else (None, None, None)
        if token:
            sources[AYON] = SOURCE_KEYRING
            username = stored_user or username
        else:
            token = _install(settings_inst, "ayon_api_key")
            if token:
                sources[AYON] = SOURCE_INSTALL
                username = username or _install(settings_inst, "ayon_username")
            else:
                token = ""
    paths["AYON_SERVER_URL"] = url or ""
    paths["AYON_API_KEY"] = token
    paths["AYON_USERNAME"] = username

    paths["_credentials_source"] = sources
    for kind, source in sources.items():
        if source:
            log.debug(f"{kind} credentials from the {source}")
    return paths


# ---------------------------------------------------------------- sign-in

# GUI: function(kind, url) -> bool that shows the sign-in dialog
# (credentials_dialog); None in headless runs
_prompt_handler_holder = [None]
# kinds the user cancelled this session: don't ask on every refresh
_declined = set()


def set_prompt_handler(handler):
    _prompt_handler_holder[0] = handler


def can_prompt():
    return _prompt_handler_holder[0] is not None


def prompt(kind, url, force=False):
    """
    Ask the user to sign in (GUI only). Once cancelled, it asks again only
    with force (the Sign in button on the Preferences tab).
    :return: True when the user signed in
    """
    handler = _prompt_handler_holder[0]
    if handler is None:
        return False
    if kind in _declined and not force:
        return False
    ok = bool(handler(kind, url))
    if ok:
        _declined.discard(kind)
    else:
        _declined.add(kind)
    return ok


def ensure_ftrack(paths, ask=True):
    """
    ftrack credentials in paths, asking the user to sign in when there are
    none (GUI). :return: True when user and key are set
    """
    if paths.get("FTRACK_API_USER") and paths.get("FTRACK_API_KEY"):
        return True
    url = paths.get("FTRACK_SERVER")
    if not url:
        return False
    if ask and prompt(FTRACK, url):
        user, key = get_ftrack(url)
        if user and key:
            paths["FTRACK_API_USER"], paths["FTRACK_API_KEY"] = user, key
            paths.setdefault("_credentials_source", {})[FTRACK] = SOURCE_KEYRING
            return True
    return False


def ensure_ayon(paths, ask=True):
    """
    A working Ayon token in paths: a keyring token is checked and renewed with
    the stored password, without credentials the user is asked to sign in
    (GUI). Tokens from the environment or install.json are used as they are.
    :return: True when a token is set
    """
    url = paths.get("AYON_SERVER_URL")
    source = (paths.get("_credentials_source") or {}).get(AYON)
    if paths.get("AYON_API_KEY") and source != SOURCE_KEYRING:
        return True
    if not url:
        return False
    token = renew_ayon_token(url)
    if token is None and ask and prompt(AYON, url):
        token = renew_ayon_token(url)
    if token:
        paths["AYON_API_KEY"] = token
        stored_user = get_ayon(url)[0]
        if stored_user:
            paths["AYON_USERNAME"] = stored_user
        paths.setdefault("_credentials_source", {})[AYON] = SOURCE_KEYRING
        return True
    paths["AYON_API_KEY"] = ""
    return False


def windows_user():
    """the login name of the user, to pre-fill the Ayon user name"""
    return os.environ.get("USERNAME") or os.environ.get("USER") or ""
