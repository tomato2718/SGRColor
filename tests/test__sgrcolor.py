import pytest

from sgrcolor._sgrcolor import SGRColor

##### FIXTURES #####


##### TESTS #####
class TestSGRColor:
    @staticmethod
    @pytest.mark.parametrize(
        "testcase",
        [
            {
                'font': 'apple',
                'fg': 'black',
                'bg': 'black',
            },
            {
                'font': 'bold',
                'fg': 'banana',
                'bg': 'black',
            },
            {
                'font': 'bold',
                'fg': 'black',
                'bg': 'cherry',
            },
            {
                'font': 1,
                'fg': 'black',
                'bg': 'black',
            },
            {
                'font': 'bold',
                'fg': [1],
                'bg': 'black',
            },
            {
                'font': 'bold',
                'fg': 'black',
                'bg': {2: 3},
            },
        ]
    )
    def test___init__(testcase):
        with pytest.raises((TypeError, ValueError)):
            SGRColor(**testcase)
    
    @staticmethod
    def test___call__():
        text = 'foo'
        # bold cyan None
        testcase1 = '\033[1;36m' + text + '\033[0m'
        # italic black white
        testcase2 = '\033[3;30;47m' + text + '\033[0m'
        # bold strike green None
        testcase3 = '\033[1;9;32m' + text + '\033[0m'

        test1 = SGRColor(
            font='bold',
            fg='cyan'
        )
        test2 = SGRColor(
            font='italic',
            fg='black',
            bg='white'
        )
        test3 = SGRColor(
            font=('bold', 'strike'),
            fg='green'
        )

        assert test1(text) == testcase1
        assert test2(text) == testcase2
        assert test3(text) == testcase3
        with pytest.raises(TypeError):
            test1(123)