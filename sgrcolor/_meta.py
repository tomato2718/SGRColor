'''
Not for import.
'''

__all__ = [
    'SGRMeta'
]

from typing import Any

class SGRMeta(type):
    '''
    Meta class of SGRs.
    '''
    def __getattribute__(self, __name: str) -> Any:
        res = object.__getattribute__(self, __name)
        if isinstance(res, str) and __name.isupper():
            res = '\033[' + res + 'm'
        return res

    def getvalue(self, __name: str) -> str:
        '''
        Return requested value.

        :param str __name: Name of the requested attribute.
        :return: Value of the requested attribute.
        :rtype: `str`
        :raise ValueError: When attribute do not existed.
        '''
        if hasattr(self, __name):
            return object.__getattribute__(self, __name)
        else:
            raise ValueError(f'{__name} do not existed.')