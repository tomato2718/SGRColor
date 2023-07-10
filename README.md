# Select Graphic Rendition Color
## Summary
SGRColor module let you color your output with Select Graphic Rendition Code.

![example]

## Requirements
### System
- `python >= 3.10.10`

### Python
- Nothing

## Setup
### Installation
- Install with Python pip
```sh
>>> pip install sgrcolor-1.0.0-py3-none-any.whl
```

## Usage
### Start Up
- Import this Project as a module.
```py
from sgrcolor import (
    Reset,
    Font,
    FG,
    BG,
    SGRColor
)
print(FG.BLUE, 'foobar', FG.RESET)
font1 = SGRColor(
    font = 'bold',
    fg = 'black',
    bg = 'white',
)
print(font1('barfoo'))
```

## Run the tests
- Unit tests
```sh
>>> python -m tests
```

## Support
### Author
- `yveschen2718@gmail.com`
### Maintainer
- `yveschen2718@gmail.com`

<!--links-->
[example]: ./docs/source/example.png