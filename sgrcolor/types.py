'''
Specific types used in sgrcolor module.
'''

__all__ = [
    'Colors',
    'FontStyles',
]

from typing import (
    Literal,
    TypeAlias
)

Colors: TypeAlias = Literal[
    'BLACK',
    'RED',
    'GREEN',
    'YELLOW',
    'BLUE',
    'MAGENTA',
    'CYAN',
    'WHITE',
    'BRIGHT_BLACK',
    'BRIGHT_RED',
    'BRIGHT_GREEN',
    'BRIGHT_YELLOW',
    'BRIGHT_BLUE',
    'BRIGHT_MAGENTA',
    'BRIGHT_CYAN',
    'BRIGHT_WHITE',
]

FontStyles: TypeAlias = Literal[
    'BOLD',
    'DIM',
    'ITALIC',
    'UNDERLINE',
    'STRIKE',
    'NORMAL',
    'DOUBLE_UNDERLINE',
]