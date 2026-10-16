"""
Grouping tab widgets (grouping_widget.py) on a tiny fake Qt, so the logic
(definitions round trip, add / move / remove, change signals, settings
widget names) is tested without PySide2 or a display.
"""
import importlib
import sys
import types
import unittest

from tests import _stubs  # noqa: F401
import grouping


class _Signal:
    def __init__(self, *types_):
        self.name = None

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, owner):
        if obj is None:
            return self
        bound = obj.__dict__.get('_sig_' + self.name)
        if bound is None:
            bound = _Bound(obj)
            obj.__dict__['_sig_' + self.name] = bound
        return bound


class _Bound:
    def __init__(self, owner):
        self.owner = owner
        self.slots = []

    def connect(self, slot):
        self.slots.append(slot)

    def emit(self, *args):
        if getattr(self.owner, '_blocked', False):
            return
        for s in list(self.slots):
            s(*args)


class _Obj:
    def __init__(self, *args, **kwargs):
        self._blocked = False
        self._visible = True
        self._name = ''

    def __getattr__(self, name):
        if name.startswith('__'):
            raise AttributeError(name)
        return lambda *a, **k: None

    def blockSignals(self, on):
        self._blocked = bool(on)

    def setObjectName(self, n):
        self._name = n

    def objectName(self):
        return self._name

    def isVisible(self):
        return self._visible

    def setVisible(self, v):
        self._visible = v


class QLineEdit(_Obj):
    textChanged = _Signal(str)

    def __init__(self, *a):
        super().__init__()
        self._text = ''

    def setText(self, t):
        self._text = str(t)
        self.textChanged.emit(self._text)

    def text(self):
        return self._text


class QCheckBox(_Obj):
    clicked = _Signal(bool)
    toggled = _Signal(bool)

    def __init__(self, *a):
        super().__init__()
        self._on = False

    def setChecked(self, on):
        changed = bool(on) != self._on
        self._on = bool(on)
        if changed:
            self.toggled.emit(self._on)

    def isChecked(self):
        return self._on

    def click(self):
        self.setChecked(not self._on)
        self.clicked.emit(self._on)


class QPushButton(_Obj):
    clicked = _Signal(bool)

    def click(self):
        self.clicked.emit(False)


class QVBoxLayout(_Obj):
    def __init__(self, *a):
        super().__init__()
        self.items = []

    def addStretch(self, *a):
        self.items.append('stretch')

    def insertWidget(self, i, w):
        self.items.insert(i, w)

    def removeWidget(self, w):
        if w in self.items:
            self.items.remove(w)

    def count(self):
        return len(self.items)


class QMessageBox(_Obj):
    Yes, No = 1, 0
    answer = 1

    @classmethod
    def question(cls, *a):
        return cls.answer


def fake_qt():
    core = types.ModuleType('PySide2.QtCore')
    core.Signal = _Signal
    core.QSize = lambda *a: None
    widgets = types.ModuleType('PySide2.QtWidgets')
    for name in ('QWidget', 'QFrame', 'QLabel', 'QHBoxLayout', 'QGridLayout', 'QScrollArea'):
        setattr(widgets, name, type(name, (_Obj,), {}))
    widgets.QFrame.StyledPanel = widgets.QFrame.NoFrame = 0
    for cls in (QLineEdit, QCheckBox, QPushButton, QVBoxLayout, QMessageBox):
        setattr(widgets, cls.__name__, cls)
    pkg = types.ModuleType('PySide2')
    pkg.QtCore, pkg.QtWidgets = core, widgets
    return {'PySide2': pkg, 'PySide2.QtCore': core, 'PySide2.QtWidgets': widgets}


class GroupingTabTest(unittest.TestCase):

    def setUp(self):
        self.saved = {k: sys.modules.get(k) for k in ('PySide2', 'PySide2.QtCore', 'PySide2.QtWidgets',
                                                      'grouping_widget')}
        sys.modules.update(fake_qt())
        sys.modules.pop('grouping_widget', None)
        self.gw = importlib.import_module('grouping_widget')
        self.tab = self.gw.GroupingTab()
        self.now, self.later = [], []
        self.tab.changed_now.connect(self.now.append)
        self.tab.changed_later.connect(self.later.append)

    def tearDown(self):
        for k, v in self.saved.items():
            if v is None:
                sys.modules.pop(k, None)
            else:
                sys.modules[k] = v

    def test_settings_widgets_match_defaults(self):
        self.assertEqual(set(self.tab.settings_widgets), set(grouping.DEFAULTS))
        for key, w in self.tab.settings_widgets.items():
            self.assertEqual(w.objectName(), key)
            value = w.isChecked() if isinstance(w, QCheckBox) else w.text()
            self.assertEqual(value, grouping.DEFAULTS[key])
        self.assertEqual(set(self.gw.TIPS), set(grouping.DEFAULTS))
        self.assertEqual(set(self.gw.DEF_TIPS), set(grouping.DEFINITION_FIELDS) - {'enabled'})

    def test_round_trip_without_signals(self):
        defs = [dict(grouping.new_definition('Lighting'), task_types='Lighting', always_repres='exr'),
                dict(grouping.new_definition('Comp'), enabled=False, inherit_columns='Frame Range, Notes')]
        self.tab.set_definitions(defs)
        self.assertEqual(self.tab.definitions(), defs)
        self.assertEqual(self.now + self.later, [])
        self.tab.set_definitions([])
        self.assertEqual(self.tab.definitions(), [])

    def test_add_edit_move_remove(self):
        self.tab.add_button.click()
        self.tab.add_button.click()
        self.assertEqual([d['name'] for d in self.tab.definitions()], ['Group 1', 'Group 2'])
        self.assertEqual(self.now, ['group_definitions'] * 2)

        second = self.tab.definition_widgets[1]
        second.edits['always_repres'].setText('exr')
        self.assertEqual(self.later, ['group_definitions'])
        second.enabled.setChecked(False)
        self.assertEqual(self.now[-1], 'group_definitions')

        second.up.click()
        self.assertEqual([d['name'] for d in self.tab.definitions()], ['Group 2', 'Group 1'])
        self.assertEqual(self.tab.list_layout.items[:2], self.tab.definition_widgets)
        self.tab.definition_widgets[0].up.click()      # already first: nothing happens
        self.assertEqual(self.tab.definitions()[0]['always_repres'], 'exr')

        QMessageBox.answer = QMessageBox.No
        self.tab.definition_widgets[0].delete.click()
        self.assertEqual(len(self.tab.definitions()), 2)
        QMessageBox.answer = QMessageBox.Yes
        self.tab.definition_widgets[0].delete.click()
        self.assertEqual([d['name'] for d in self.tab.definitions()], ['Group 1'])
        self.assertEqual(self.tab.list_layout.items, self.tab.definition_widgets + ['stretch'])

    def test_top_controls_signal(self):
        self.tab.settings_widgets['group_on'].click()
        self.tab.settings_widgets['group_by'].setText('{shot}')
        self.assertEqual(self.now, ['group_on'])
        self.assertEqual(self.later, ['group_by'])


if __name__ == '__main__':
    unittest.main()
