"""
Log tab of the main window.

Shows records from ``sh_logging.LOG_BUFFER`` in the existing ``ui.log``
QPlainTextEdit and adds a small toolbar above it:
level filter, text filter, auto-scroll, Copy, Save..., Clear.
The tab title shows the number of warnings and errors.
"""
import html
import logging

from PySide2 import QtCore, QtGui, QtWidgets

from sh_logging import LOG_BUFFER, LEVEL_NAMES, qt_messages_suppressed

COLORS = {
    logging.DEBUG: '#8a8a8a',
    logging.INFO: None,           # default text color
    logging.WARNING: '#e0a030',
    logging.ERROR: '#ff5c5c',
    logging.CRITICAL: '#ff5c5c',
}


def _color_for(levelno):
    if levelno >= logging.ERROR:
        return COLORS[logging.ERROR]
    if levelno >= logging.WARNING:
        return COLORS[logging.WARNING]
    if levelno >= logging.INFO:
        return None
    return COLORS[logging.DEBUG]


def record_to_html(levelno, line, default_color=None):
    text = html.escape(line).replace('\n', '<br>')
    color = _color_for(levelno) or default_color
    style = 'white-space:pre;'
    if color:
        # always set a color, Qt can carry the previous line's color over
        style += f' color:{color};'
    if levelno >= logging.ERROR:
        style += ' font-weight:600;'
    return f'<span style="{style}">{text}</span>'


class LogView(QtCore.QObject):

    # emitted from any thread, delivered in the gui thread
    record_arrived = QtCore.Signal(object)

    def __init__(self, ui, tab_widget, tab_page, base_title="Log", parent=None):
        super().__init__(parent)
        self.ui = ui
        self.edit = ui.log
        self.tab_widget = tab_widget
        self.tab_page = tab_page
        self.base_title = base_title
        self.counts = {'warning': 0, 'error': 0}
        # highest record seq already drawn, avoids drawing queued records twice
        self._drawn_seq = 0

        self.edit.setReadOnly(True)
        self.edit.setMaximumBlockCount(LOG_BUFFER.records.maxlen or 20000)
        self.edit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        font = QtGui.QFontDatabase.systemFont(QtGui.QFontDatabase.FixedFont)
        self.edit.setFont(font)
        self.text_color = self.edit.palette().text().color().name()

        self._build_toolbar()

        self.record_arrived.connect(self._on_record, QtCore.Qt.QueuedConnection)
        LOG_BUFFER.add_listener(self._from_any_thread)
        # start from what was logged before the window existed
        self.counts = dict(LOG_BUFFER.counts)
        self.counts.setdefault('warning', 0)
        self.counts.setdefault('error', 0)
        self.rerender()

    # ---------------------------------------------------------------- ui
    def _build_toolbar(self):
        bar = QtWidgets.QHBoxLayout()
        bar.setContentsMargins(0, 0, 0, 0)

        bar.addWidget(QtWidgets.QLabel("Show:"))
        # stored on ui so the choice is saved with the gui settings
        self.level_combo = QtWidgets.QComboBox()
        self.level_combo.setObjectName("log_view_level")
        self.level_combo.addItems(LEVEL_NAMES)
        self.level_combo.setCurrentText('INFO')
        self.level_combo.setToolTip("Minimum level shown in this tab. "
                                    "Everything is still recorded, switching to DEBUG shows past debug messages too.")
        self.ui.log_view_level = self.level_combo
        bar.addWidget(self.level_combo)

        self.filter_edit = QtWidgets.QLineEdit()
        self.filter_edit.setPlaceholderText("Filter text...")
        self.filter_edit.setClearButtonEnabled(True)
        bar.addWidget(self.filter_edit, 1)

        self.autoscroll = QtWidgets.QCheckBox("Auto-scroll")
        self.autoscroll.setChecked(True)
        bar.addWidget(self.autoscroll)

        copy_btn = QtWidgets.QPushButton("Copy")
        copy_btn.setToolTip("Copy the shown lines to the clipboard")
        save_btn = QtWidgets.QPushButton("Save...")
        save_btn.setToolTip("Save the shown lines to a text file")
        clear_btn = QtWidgets.QPushButton("Clear")
        clear_btn.setToolTip("Clear the log and the warning / error counters")
        for b in (copy_btn, save_btn, clear_btn):
            bar.addWidget(b)

        layout = self.tab_page.layout()
        if isinstance(layout, QtWidgets.QBoxLayout):
            layout.insertLayout(0, bar)
        else:
            layout.addLayout(bar)

        self.level_combo.currentIndexChanged.connect(self.rerender)
        self.filter_edit.textChanged.connect(self.rerender)
        copy_btn.clicked.connect(self.copy_to_clipboard)
        save_btn.clicked.connect(self.save_to_file)
        clear_btn.clicked.connect(self.clear)

    # ------------------------------------------------------------ filters
    def min_level(self):
        return getattr(logging, self.level_combo.currentText() or 'INFO', logging.INFO)

    def _passes(self, levelno, line):
        if levelno < self.min_level():
            return False
        text = self.filter_edit.text().strip().lower()
        return not text or text in line.lower()

    # ------------------------------------------------------------ records
    def _from_any_thread(self, entry):
        self.record_arrived.emit(entry)

    def _on_record(self, entry):
        seq, levelno, line = entry
        if seq <= self._drawn_seq:
            # already shown by rerender(), it was queued before the redraw
            return
        self._drawn_seq = seq
        with qt_messages_suppressed():
            if levelno >= logging.WARNING:
                if levelno >= logging.ERROR:
                    self.counts['error'] += 1
                else:
                    self.counts['warning'] += 1
                self._update_title()
            if self._passes(levelno, line):
                self.edit.appendHtml(record_to_html(levelno, line, self.text_color))
                if self.autoscroll.isChecked():
                    sb = self.edit.verticalScrollBar()
                    sb.setValue(sb.maximum())

    # a full redraw shows at most this many of the newest lines (speed)
    RERENDER_MAX = 5000

    def rerender(self, *args):
        # everything up to here is drawn now, queued records up to it are skipped
        self._drawn_seq = LOG_BUFFER.last_seq()
        entries = LOG_BUFFER.snapshot(self.min_level(), self.filter_edit.text().strip())
        entries = [e for e in entries if e[0] <= self._drawn_seq]
        if len(entries) > self.RERENDER_MAX:
            skipped = len(entries) - self.RERENDER_MAX
            entries = [(0, logging.INFO, f"... {skipped} older line(s) not shown, use Save... to get all of them")] \
                + entries[-self.RERENDER_MAX:]
        with qt_messages_suppressed():
            self.edit.setUpdatesEnabled(False)
            try:
                self.edit.clear()
                # one block per line, so the max block count trims line by line
                for _, lv, ln in entries:
                    self.edit.appendHtml(record_to_html(lv, ln, self.text_color))
            finally:
                self.edit.setUpdatesEnabled(True)
        sb = self.edit.verticalScrollBar()
        sb.setValue(sb.maximum())
        self._update_title()

    def _update_title(self):
        idx = self.tab_widget.indexOf(self.tab_page)
        if idx < 0:
            return
        parts = []
        if self.counts.get('error'):
            parts.append(f"{self.counts['error']} err")
        if self.counts.get('warning'):
            parts.append(f"{self.counts['warning']} warn")
        title = self.base_title + (f" ({', '.join(parts)})" if parts else "")
        self.tab_widget.setTabText(idx, title)
        color = QtGui.QColor(COLORS[logging.ERROR]) if self.counts.get('error') else \
            QtGui.QColor(COLORS[logging.WARNING]) if self.counts.get('warning') else QtGui.QColor()
        self.tab_widget.tabBar().setTabTextColor(idx, color)

    # ------------------------------------------------------------ actions
    def shown_text(self):
        return '\n'.join(line for _, _, line in
                         LOG_BUFFER.snapshot(self.min_level(), self.filter_edit.text().strip()))

    def copy_to_clipboard(self, *args):
        QtWidgets.QApplication.clipboard().setText(self.shown_text())

    def save_to_file(self, *args):
        pth, _ = QtWidgets.QFileDialog.getSaveFileName(
            self.edit, "Save Log", "submission_helper.log", "Log files (*.log *.txt);;All files (*)")
        if not pth:
            return
        try:
            with open(pth, 'w', encoding='utf-8') as f:
                f.write(self.shown_text() + '\n')
            logging.getLogger('SubmissionHelper').info("Log saved to %s", pth)
        except OSError as e:
            logging.getLogger('SubmissionHelper').error("Saving log to %s failed: %s", pth, e)

    def clear(self, *args):
        LOG_BUFFER.clear()
        self.counts = {'warning': 0, 'error': 0}
        self.rerender()

    def detach(self):
        LOG_BUFFER.remove_listener(self._from_any_thread)
