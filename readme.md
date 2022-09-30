# easyselect by gmanka

simple and pretty tool for selecting items by keyboard in terminal

## navigation

- [installation](#installation)
- [usage](#usage)
- [rich styles support](#rich-styles-support)

### installation

```sh
pip install easyselect
```

### usage

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

### rich styles support

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

### long items list support

```py
nums = Sel(
    items = list(range(50))
)
answer = nums.choose()
print(answer)
```

### page size

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
