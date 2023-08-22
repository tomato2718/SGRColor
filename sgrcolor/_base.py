'''
Not for import.
'''

__all__ = [
    'Font',
    'FG',
    'BG',
    'Reset',
]

from ._meta import SGRMeta

class Reset(metaclass = SGRMeta):
    '''
    Reset Style or color.

    Attributes:

    - ALL
    - FG (Also available as FG.RESET)
    - BG (Also available as BG.RESET)
    '''
    ALL = '0'
    FG = '39'
    BG = '49'

class Font(metaclass = SGRMeta):
    '''
    Font style.

    Attributes:

    - ``BOLD``
    - ``DIM``
    - ``ITALIC``
    - ``UNDERLINE``
    - ``STRIKE``
    - ``NORMAL``
    - ``DOUBLE_UNDERLINE``
    '''
    BOLD = '1'
    DIM = '2'
    ITALIC = '3'
    UNDERLINE = '4'
    STRIKE = '9'
    NORMAL = '22'
    DOUBLE_UNDERLINE = '21'

class FG(metaclass = SGRMeta):
    '''
    Foreground Colors.

    Attributes:

    - ``RESET``
    - ``(BRIGHT_)BLACK``
    - ``(BRIGHT_)RED``
    - ``(BRIGHT_)GREEN``
    - ``(BRIGHT_)YELLOW``
    - ``(BRIGHT_)BLUE``
    - ``(BRIGHT_)MAGENTA``
    - ``(BRIGHT_)CYAN``
    - ``(BRIGHT_)WHITE``
    '''
    RESET = '39'
    BLACK = '30'
    RED = '31'
    GREEN = '32'
    YELLOW = '33'
    BLUE = '34'
    MAGENTA = '35'
    CYAN = '36'
    WHITE = '37'
    BRIGHT_BLACK = '90'
    BRIGHT_RED  = '91'
    BRIGHT_GREEN = '92'
    BRIGHT_YELLOW = '93'
    BRIGHT_BLUE = '94'
    BRIGHT_MAGENTA = '95'
    BRIGHT_CYAN = '96'
    BRIGHT_WHITE = '97'

class BG(metaclass = SGRMeta):
    '''
    Background Colors.

    Attributes:
    
    - ``RESET``
    - ``(BRIGHT_)BLACK``
    - ``(BRIGHT_)RED``
    - ``(BRIGHT_)GREEN``
    - ``(BRIGHT_)YELLOW``
    - ``(BRIGHT_)BLUE``
    - ``(BRIGHT_)MAGENTA``
    - ``(BRIGHT_)CYAN``
    - ``(BRIGHT_)WHITE``
    '''
    RESET = '49'
    BLACK = '40'
    RED = '41'
    GREEN = '42'
    YELLOW = '43'
    BLUE = '44'
    MAGENTA = '45'
    CYAN = '46'
    WHITE = '47'
    BRIGHT_BLACK = '100'
    BRIGHT_RED = '101'
    BRIGHT_GREEN = '102'
    BRIGHT_YELLOW = '103'
    BRIGHT_BLUE = '104'
    BRIGHT_MAGENTA = '105'
    BRIGHT_CYAN = '106'
    BRIGHT_WHITE = '107'