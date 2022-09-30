# easyselect by gmanka

simple and pretty tool for selecting items by keyboard in terminal
[github.com/gmankab/easyselect](https://github.com/gmankab/easyselect)

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

selection also support [rich styles](https://rich.readthedocs.io/en/stable/style.html)

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
