#!/bin/python

'''
https://github.com/gmankab/easyselect
'''

from rich import pretty
from rich import traceback
from rich.console import Console
from pynput import keyboard
import subprocess
import platform
import sys

traceback.install(show_locals=True)
pretty.install()
console = Console()
print = console.print
run = subprocess.getstatusoutput
Key = keyboard.Key
system = platform.system()


class Sel:
    def __init__(
        self,
        items: list | tuple,
        styles: list | tuple = [],
        chosen: int = 0,
        page_size: int = 10,
    ) -> None:
        self.items = items
        self.chosen = chosen
        self.page_size = page_size
        self.len = len(items)
        self.start = 0
        if not styles:
            styles = [None] * len(self.items)
        self.styles = styles

    def print(self):
        if self.chosen < 0:
            self.chosen = self.len - 1
        elif self.chosen >= self.len:
            self.chosen = 0
        if self.chosen < self.start:
            self.start = self.chosen
        end = self.start + self.page_size
        if self.chosen >= end:
            end = self.chosen + 1
            self.start = end - self.page_size
        to_print = self.items[
            self.start : end
        ]

        for index, item in enumerate(to_print):
            index = self.start + index
            if index == self.chosen:
                if system == 'Windows':
                    item = f'[blue]➜[/blue]   [reverse]{item}[/reverse]'
                else:
                    item = f'[blue]➜[/blue]  [reverse]{item}[/reverse]'
            else:
                item = f'    {item}'
            print(
                item,
                style = self.styles[index],
                highlight = False,
            )
        print()

    def update(self):
        up_one = '\x1b[1A'
        erase_line = '\x1b[2K'
        sys.stdout.write(
            (
                up_one + erase_line
            ) * (
                min(self.page_size, self.len) + 1
            )
        )
        self.print()

    def choose(self):
        def on_press(key):
            if 'char' in key.__dict__.keys():
                key = key.char
            match key:
                case Key.esc:
                    self.chosen = None
                    return False
                case Key.enter:
                    return False
                case Key.up | Key.left | 'w' | 'a':
                    self.chosen -= 1
                case Key.down | Key.right | 's' | 'd':
                    self.chosen += 1
                case Key.page_up:
                    self.chosen -= self.page_size
                    self.chosen = max(
                        self.chosen,
                        0
                    )
                case Key.page_down:
                    self.chosen += self.page_size
                    self.chosen = min(
                        self.chosen,
                        self.len - 1
                    )
                case Key.home:
                    self.chosen = 0
                case Key.end:
                    self.chosen = self.len - 1
            self.update()

        run('stty -echo')
        self.print()
        with keyboard.Listener(
            on_press=on_press,
        ) as listener:
            listener.join()
        input()
        run('stty echo')

        if self.chosen is None:
            return None
        else:
            return self.items[self.chosen]
