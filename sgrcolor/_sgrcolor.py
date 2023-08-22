'''
Not for import.
'''

__all__ = [
    'SGRColor'
]

from ._base import (
    Reset,
    Font,
    FG,
    BG,
)
from .types import (
    Colors,
    FontStyles
)

class SGRColor:
    '''
    Generate an object to format input string.

    Usage::

        >>> important = SGRColor(
                font=('BOLD', 'ITALIC'),
                fg='YELLOW',
            )
        >>> print(important('Something IMPORTANT.'))
    '''
    _format: str

    def __init__(self,
                 font: FontStyles|tuple[FontStyles, ...]|None = None,
                 fg: Colors|None = None,
                 bg: Colors|None = None,
                 ) -> None:
        '''
        Constructor method.

        FontStyles:
        
        - BOLD
        - DIM
        - ITALIC
        - UNDERLINE
        - STRIKE
        - NORMAL
        - DOUBLE_UNDERLINE

        Colors:

        - BLACK
        - RED
        - GREEN
        - YELLOW
        - BLUE
        - MAGENTA
        - CYAN
        - WHITE
        - BRIGHT_BLACK
        - BRIGHT_RED
        - BRIGHT_GREEN
        - BRIGHT_YELLOW
        - BRIGHT_BLUE
        - BRIGHT_MAGENTA
        - BRIGHT_CYAN
        - BRIGHT_WHITE

        :param FontStyles|tuple[FontStyles, ...]|None font: String or Tuple of the font to use.
        :param Colors fg: String of the foreground color to use.
        :param Colors bg: String of the background color to use.
        '''
        prefix = []
        if isinstance(font, str):
            prefix.append(
                Font.getvalue(font)
            )
        elif isinstance(font, tuple):
            prefix.extend(
                [Font.getvalue(i) for i in font]
            )
        
        if fg:
            prefix.append(
                FG.getvalue(fg)
            )
        
        if bg:
            prefix.append(
                BG.getvalue(bg)
            )

        self._format = ''.join(
            [
                '\033[',
                ';'.join(prefix),
                'm',
                '{text}',
                Reset.ALL,
            ]
        )


    def __call__(self, text: str) -> str:
        '''
        Return colored text.

        :param str text: The text to be colored.
        :return: Colored text.
        :rtype: `str`
        '''
        return self._format.format(text=text)