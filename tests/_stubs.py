"""
Make the non-Qt modules importable in a bare test environment.

Real packages are always preferred; a stub module is only inserted when the
import fails, so on a dev machine with requirements installed nothing is faked.
"""
import importlib
import os
import sys
import types

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO not in sys.path:
    sys.path.insert(0, REPO)


class _Anything(types.ModuleType):
    """Module whose every attribute is another stub (classes, submodules...)."""

    def __getattr__(self, name):
        if name.startswith('__'):
            raise AttributeError(name)
        child = _Anything(f"{self.__name__}.{name}")
        setattr(self, name, child)
        return child

    def __call__(self, *args, **kwargs):
        return _Anything(self.__name__ + "()")

    def __mro_entries__(self, bases):
        # used as a base class (e.g. QtWidgets.QMainWindow): give a plain class
        cls = self.__dict__.get('_as_class')
        if cls is None:
            cls = type(self.__name__.split('.')[-1], (), {})
            self.__dict__['_as_class'] = cls
        return (cls,)


def _ensure(name, submodules=()):
    try:
        importlib.import_module(name)
        return
    except Exception:
        pass
    mod = _Anything(name)
    sys.modules[name] = mod
    for sub in submodules:
        full = f"{name}.{sub}"
        child = _Anything(full)
        setattr(mod, sub, child)
        sys.modules[full] = child


_ensure('PySide2', ('QtCore', 'QtGui', 'QtWidgets'))
_ensure('ftrack_api', ('exception',))
_ensure('ayon_api')
_ensure('httpx')
_ensure('xlsxwriter')
try:
    import unidecode  # noqa: F401
except Exception:
    m = types.ModuleType('unidecode')
    m.unidecode = lambda s: s
    sys.modules['unidecode'] = m
