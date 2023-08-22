'''
Color your output with Select Graphic Rendition Code.
'''
__all__ = [
    'Reset',
    'Font',
    'FG',
    'BG',
    'SGRColor',
    'types',
]

from ._base import (
    Reset,
    Font,
    FG,
    BG,
)
from ._sgrcolor import SGRColor

from . import types