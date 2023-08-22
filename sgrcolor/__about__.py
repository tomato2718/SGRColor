'''
Informations about the project.
'''

__all__ = [
    '__project__',
    '__version__',
    '__author__',
    '__maintainer__',
    '__release__',
    '__summary__',
    '__usage__'
]

__project__ = 'sgrcolor'
__version__ = '2.0.0'
__author__ = 'yveschen2718@gmail.com'
__maintainer__ = 'yveschen2718@gmail.com'
__release__ = '2023/08/22'
__summary__ = 'Color your output with Select Graphic Rendition Code.'
__usage__ = f'''
Usage:
    >>> from sgrcolor import (
            Reset,
            Font,
            FG,
            BG,
            SGRColor
        )
    >>> print(FG.BLUE, 'foobar', FG.RESET)
    >>> important = SGRColor(
            font=('BOLD', 'ITALIC'),
            fg='YELLOW',
        )
    >>> print(important('Something IMPORTANT.'))
'''