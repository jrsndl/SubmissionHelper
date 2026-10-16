"""
Sign-in dialogs for ftrack and Ayon, and the Accounts group on the
Preferences tab. The credentials themselves are handled in credentials.py.
"""
import logging

from PySide2 import QtCore, QtGui, QtWidgets

import credentials

log = logging.getLogger("Credentials")


class _Invoker(QtCore.QObject):
    """runs a callable in the GUI thread (the browser login calls back from its thread)"""
    call = QtCore.Signal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.call.connect(lambda fn: fn(), QtCore.Qt.QueuedConnection)


class _SignInDialog(QtWidgets.QDialog):
    """common parts: server url, message line, buttons"""

    def __init__(self, title, intro, url, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumWidth(460)
        self.layout_main = QtWidgets.QVBoxLayout(self)
        intro_label = QtWidgets.QLabel(intro)
        intro_label.setWordWrap(True)
        self.layout_main.addWidget(intro_label)

        self.form = QtWidgets.QFormLayout()
        self.layout_main.addLayout(self.form)
        self.url_edit = QtWidgets.QLineEdit(url or "")
        self.url_edit.setPlaceholderText("https://...")
        # a configured url (environment / install.json) is not changed here
        self.url_edit.setReadOnly(bool(url))
        self.form.addRow("Server:", self.url_edit)

        self.message = QtWidgets.QLabel("")
        self.message.setWordWrap(True)
        self.layout_main.addWidget(self.message)

        self.buttons = QtWidgets.QDialogButtonBox()
        self.cancel_button = self.buttons.addButton(QtWidgets.QDialogButtonBox.Cancel)
        self.cancel_button.clicked.connect(self.reject)
        self.layout_main.addWidget(self.buttons)

    def url(self):
        return self.url_edit.text().strip().rstrip("/")

    def show_message(self, text, error=False):
        self.message.setStyleSheet("color: #ff6060;" if error else "")
        self.message.setText(text)

    def busy(self, on):
        if on:
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        else:
            QtWidgets.QApplication.restoreOverrideCursor()
        QtWidgets.QApplication.processEvents()


class FtrackSignInDialog(_SignInDialog):
    """
    Personal ftrack API key: from the ftrack web app in the browser (one
    click when the user is signed in there), or typed in.
    """

    def __init__(self, url, parent=None):
        super().__init__(
            "Sign in to ftrack",
            "Submission Helper uses your personal ftrack API key. It is stored in the "
            "Windows Credential Manager, only for your Windows user.",
            url, parent)
        self._login_thread = None
        self._invoker = _Invoker(self)

        self.browser_button = QtWidgets.QPushButton("Sign in with web browser")
        self.browser_button.setToolTip(
            "Opens ftrack in your web browser. When you are signed in there\n"
            "(or sign in), ftrack sends your personal API key back to\n"
            "Submission Helper.")
        self.browser_button.clicked.connect(self._browser_login)
        self.layout_main.insertWidget(2, self.browser_button)

        user, _ = credentials.get_ftrack(url) if url else (None, None)
        self.user_edit = QtWidgets.QLineEdit(user or "")
        self.key_edit = QtWidgets.QLineEdit()
        self.key_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.key_edit.setToolTip("ftrack web app: My Account > Security > Personal API key")
        manual = QtWidgets.QGroupBox("Or enter it yourself")
        manual_form = QtWidgets.QFormLayout(manual)
        manual_form.addRow("User name:", self.user_edit)
        manual_form.addRow("API key:", self.key_edit)
        self.layout_main.insertWidget(3, manual)

        self.sign_in_button = self.buttons.addButton("Sign in", QtWidgets.QDialogButtonBox.AcceptRole)
        self.sign_in_button.clicked.connect(self._manual_login)
        self.sign_in_button.setDefault(True)

    def _browser_login(self):
        url = self.url()
        if not url:
            self.show_message("Enter the ftrack server first.", error=True)
            return
        self._stop_thread()
        self.show_message("Waiting for the web browser... finish the sign-in there.")

        def received(api_user, api_key):
            # browser thread -> GUI thread
            self._invoker.call.emit(lambda: self._finish(api_user, api_key))

        self._login_thread = credentials.FtrackBrowserLogin(url, received)
        self._login_thread.start()

    def _manual_login(self):
        self._finish(self.user_edit.text().strip(), self.key_edit.text().strip())

    def _finish(self, user, key):
        url = self.url()
        self.busy(True)
        try:
            ok, message = credentials.check_ftrack(url, user, key)
        finally:
            self.busy(False)
        if not ok:
            self.show_message(f"Sign-in failed: {message}", error=True)
            return
        if not credentials.save_ftrack(url, user, key):
            self.show_message("Signed in, but the credentials could not be stored "
                              "(see the Log tab).", error=True)
            return
        if not self.url_edit.isReadOnly():
            credentials.save_server_url(credentials.FTRACK, url)
        self.accept()

    def _stop_thread(self):
        if self._login_thread is not None:
            self._login_thread.stop()
            self._login_thread = None

    def done(self, result):
        self._stop_thread()
        super().done(result)


class AyonSignInDialog(_SignInDialog):
    """Ayon user name and password, logged in once, renewed when it expires"""

    def __init__(self, url, parent=None):
        super().__init__(
            "Sign in to Ayon",
            "Your Ayon login is stored in the Windows Credential Manager, only for your "
            "Windows user. When the Ayon session expires, Submission Helper logs in again "
            "by itself.",
            url, parent)
        user, _, _ = credentials.get_ayon(url) if url else (None, None, None)
        self.user_edit = QtWidgets.QLineEdit(user or credentials.windows_user())
        self.password_edit = QtWidgets.QLineEdit()
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.form.addRow("User name:", self.user_edit)
        self.form.addRow("Password:", self.password_edit)
        self.password_edit.setFocus()

        self.sign_in_button = self.buttons.addButton("Sign in", QtWidgets.QDialogButtonBox.AcceptRole)
        self.sign_in_button.clicked.connect(self._login)
        self.sign_in_button.setDefault(True)

    def _login(self):
        url = self.url()
        user = self.user_edit.text().strip()
        password = self.password_edit.text()
        self.busy(True)
        try:
            token, message = credentials.ayon_login(url, user, password)
        finally:
            self.busy(False)
        if token is None:
            self.show_message(f"Sign-in failed: {message}", error=True)
            return
        if not credentials.save_ayon(url, user, password, token):
            self.show_message("Signed in, but the credentials could not be stored "
                              "(see the Log tab).", error=True)
            return
        if not self.url_edit.isReadOnly():
            credentials.save_server_url(credentials.AYON, url)
        self.accept()


def ask_sign_in(kind, url, parent=None):
    """credentials.prompt handler: show the dialog, True when signed in"""
    if kind == credentials.FTRACK:
        dialog = FtrackSignInDialog(url, parent)
    else:
        dialog = AyonSignInDialog(url, parent)
    return dialog.exec_() == QtWidgets.QDialog.Accepted


class AccountsGroup(QtWidgets.QGroupBox):
    """
    Preferences tab: who is signed in to ftrack / Ayon and where the
    credentials come from, Sign in and Sign out buttons.
    on_change() is called after a sign-in or sign-out (reload the credentials).
    """

    def __init__(self, get_paths, on_change, parent=None):
        super().__init__("Accounts:", parent)
        self.setObjectName("prefs_accounts_group")
        self.get_paths = get_paths
        self.on_change = on_change
        grid = QtWidgets.QGridLayout(self)
        self.rows = {}
        for row, (kind, title) in enumerate(((credentials.FTRACK, "ftrack"),
                                             (credentials.AYON, "Ayon"))):
            label = QtWidgets.QLabel(f"{title}:")
            status = QtWidgets.QLabel("")
            sign_in = QtWidgets.QPushButton("Sign in...")
            sign_in.setObjectName(f"prefs_{kind}_sign_in")
            sign_in.setToolTip(f"Sign in to {title} with your own account. The credentials are\n"
                               "stored in the Windows Credential Manager.")
            sign_out = QtWidgets.QPushButton("Sign out")
            sign_out.setObjectName(f"prefs_{kind}_sign_out")
            sign_out.setToolTip(f"Remove your stored {title} credentials from this computer.")
            sign_in.clicked.connect(lambda _=False, k=kind: self._sign_in(k))
            sign_out.clicked.connect(lambda _=False, k=kind: self._sign_out(k))
            grid.addWidget(label, row, 0)
            grid.addWidget(status, row, 1)
            grid.addWidget(sign_in, row, 2)
            grid.addWidget(sign_out, row, 3)
            self.rows[kind] = (status, sign_in, sign_out)
        grid.setColumnStretch(1, 1)
        self.refresh()

    def _url(self, kind):
        paths = self.get_paths() or {}
        key = "FTRACK_SERVER" if kind == credentials.FTRACK else "AYON_SERVER_URL"
        return paths.get(key) or credentials.get_server_url(kind)

    def refresh(self):
        paths = self.get_paths() or {}
        sources = paths.get("_credentials_source") or {}
        for kind, (status, sign_in, sign_out) in self.rows.items():
            url = self._url(kind)
            source = sources.get(kind)
            if kind == credentials.FTRACK:
                user = paths.get("FTRACK_API_USER")
                stored = credentials.get_ftrack(url)[1] if url else None
            else:
                user = paths.get("AYON_USERNAME")
                stored = credentials.get_ayon(url)[1] if url else None
            host = credentials.hostname(url) or "no server set"
            if source:
                text = f"{user or 'signed in'} @ {host} (from the {source})"
            else:
                text = f"not signed in ({host})"
            status.setText(text)
            sign_out.setEnabled(bool(stored))

    def _sign_in(self, kind):
        if credentials.prompt(kind, self._url(kind), force=True):
            self.on_change()
        self.refresh()

    def _sign_out(self, kind):
        url = self._url(kind)
        if kind == credentials.FTRACK:
            credentials.clear_ftrack(url)
        else:
            credentials.ayon_logout(url)
        self.on_change()
        self.refresh()
