import pytest

from sgrcolor._base import (
    Reset,
    Font,
    FG,
    BG,
)

##### FIXTURES #####
@pytest.fixture(scope='module')
def reset_all():
    return '\033[0m'

@pytest.fixture(scope='module')
def font_bold():
    return '\033[1m'

@pytest.fixture(scope='module')
def fg_red():
    return '\033[31m'

@pytest.fixture(scope='module')
def bg_blue():
    return '\033[44m'

##### TESTS #####
def test_Reset(reset_all):
    assert Reset.ALL == reset_all

def test_Font(font_bold):
    assert Font.BOLD == font_bold

def test_FG(fg_red):
    assert FG.RED == fg_red

def test_BG(bg_blue):
    assert BG.BLUE == bg_blue