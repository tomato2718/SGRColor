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
>>> pip install sgrcolor-2.0.0-py3-none-any.whl
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

important = SGRColor(
    font=('BOLD', 'ITALIC'),
    fg='YELLOW',
)
print(important('Something IMPORTANT.'))
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