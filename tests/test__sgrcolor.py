import pytest

from sgrcolor._sgrcolor import SGRColor

##### FIXTURES #####


##### TESTS #####
class TestSGRColor:
    @staticmethod
    def test___call__():
        text = 'foo'
        # bold cyan None
        testcase1 = f'\033[1;36m{text}\033[0m'
        # italic black white
        testcase2 = f'\033[3;30;47m{text}\033[0m'
        # bold strike green None
        testcase3 = f'\033[1;9;32m{text}\033[0m'

        test1 = SGRColor(
            font='BOLD',
            fg='CYAN',
        )
        test2 = SGRColor(
            font='ITALIC',
            fg='BLACK',
            bg='WHITE',
        )
        test3 = SGRColor(
            font=('BOLD', 'STRIKE'),
            fg='GREEN'
        )

        assert test1(text) == testcase1
        assert test2(text) == testcase2
        assert test3(text) == testcase3