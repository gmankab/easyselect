# easyselect by gmanka

<img src="https://github.com/gmankab/easyselect/raw/main/img/transparent.png">

a useful library that allows the user to select between multiple items in the console using the keyboard. Supports very long lists that don't fit on the screen, [rich styles](https://rich.readthedocs.io/en/stable/style.html), control with buttons `up`, `down`, `left`, `right`, `wasd`, `j`, `h`, `home`, `end`, `page up`, `page down`

## navigation

- [installation](#installation)
- [usage](#usage)
- [print text while choosing](#print-text-while-choosing)
- [rich styles support](#rich-styles-support)
- [long items list support](#long-items-list-support)
- [page size](#page-size)
- [supported buttons](#supported-buttons)
- [changelog](#changelog)
- [license](#license)

### installation[^](#navigation)

```sh
pip install easyselect
```

### usage[^](#navigation)

```py
from easyselect import Sel

yes_or_no = Sel(
    items = [
        'yes',
        'no',
    ]
)

answer = yes_or_no.choose()
print(answer)
```

### print text while choosing[^](#navigation)

```py
yes_or_no = Sel(
    items = [
        'yes',
        'no',
    ],
    text = 'please select yes or no'
)
```

### rich styles support[^](#navigation)

linux only

```py
yes_or_no = Sel(
    items = [
        'yes',
        'no',
    ],
    styles = [
        'green',
        'red'
    ]
)
```

[rich styles documentation](https://rich.readthedocs.io/en/stable/style.html)

### very long items list support[^](#navigation)

```py
nums = Sel(
    items = list(range(50))
)
```

### page size[^](#navigation)

page_size arg allows to specify how much lines will be rendered on screen

default value is 15

```py
nums = Sel(
    items = list(range(50)),
    page_size = 3
)
```

### supported buttons[^](#navigation)

user will able to use these buttons

- up, down, left, right
- w, a, s, d, j, k
- home, end
- page up, page down

### changelog[^](#navigation)

you can read changelog [here](https://github.com/gmankab/easyselect/blob/main/changelog.md)


### license[^](#navigation)

[gnu gpl 3](https://gnu.org/licenses/gpl-3.0.en.html)
