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

class SGRColor:
    '''
    Generate an object to format input string.

    Usage::

        >>> important = SGRColor(
                font=('bold', 'italic'),
                fg='yellow',
            )
        >>> print(important('Something IMPORTANT.'))
    '''
    _prefix: str

    def __init__(self, font: str|tuple[str] = '', fg: str = '', bg: str = '') -> None:
        '''
        Constructor method.

        :param str|tuple[str] font: String or Tuple of the font to use, value MUST be same as the attributes in `Font` class.
        :param str fg: String of the foreground color to use, value MUST be same as the attribute in `FG` class.
        :param str bg: String of the background color to use, value MUST be same as the attribute in `BG` class.
        :raise TypeError: When type of font is not `str` or `tuple`, or type of fg, bg is not `str`.
        :raise ValueError: When font, fg or bg do not existed.
        '''
        tmp = []
        if not font:
            pass
        elif isinstance(font, str):
            tmp.append(
                Font.getvalue(
                    font.upper()
                )
            )
        elif isinstance(font, tuple):
            for i in font:
                tmp.append(
                    Font.getvalue(
                        i.upper()
                    )
                )
        else:
            raise TypeError('Type of font MUST be str or tuple.')
        
        if not fg:
            pass
        elif not isinstance(fg, str):
            raise TypeError('Type of fg MUST be str.')
        else:
            tmp.append(
                FG.getvalue(
                    fg.upper()
                )
            )
        
        if not bg:
            pass
        elif not isinstance(bg, str):
            raise TypeError('Type of bg MUST be str.')
        else:
            tmp.append(
                BG.getvalue(
                    bg.upper()
                )
            )
        
        self._prefix = '\033[' + ';'.join(tmp) + 'm'


    def __call__(self, text: str) -> str:
        '''
        Return colored text.

        :param str text: The text to be colored.
        :return: Colored text.
        :rtype: `str`
        :raise TypeError: When type of text is not `str`.
        '''

        if not isinstance(text, str):
            raise TypeError('Type of text MUST be str.')
        return self._prefix + text + Reset.ALL