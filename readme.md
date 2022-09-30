# easyselect by gmanka

simple and pretty tool for selecting items by keyboard in terminal

## navigation

- [installation](#installation)
- [usage](#usage)
- [rich styles support](#rich-styles-support)
- [long items list support](#long-items-list-support)
- [page size](#page-size)
- [supported buttons](#supported-buttons)

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

### rich styles support[^](#navigation)

[documentation](https://rich.readthedocs.io/en/stable/style.html)

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

### long items list support[^](#navigation)

```py
nums = Sel(
    items = list(range(50))
)
answer = nums.choose()
print(answer)
```

### page size[^](#navigation)

page_size arg allows to specify how much lines will be rendered on screen
default value is 15

```py
nums = Sel(
    items = list(range(50)),
    page_size = 3
)
answer = nums.choose()
print(answer)
```

### supported buttons[^](#navigation)

- up, down, left, right
- w, a, s, d
- home, end
- page up, page down
