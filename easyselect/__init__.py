#!/bin/python

'''
https://github.com/gmankab/easyselect
'''

from rich import pretty
from rich import traceback
from rich.console import Console
from dataclasses import dataclass
import subprocess
import platform
import sys
import os
import curses as c
import time

traceback.install(show_locals=True)
pretty.install()
co = Console()
p = co.print
run = subprocess.getstatusoutput
system = platform.system()


class Sel:
    def __init__(
        self,
        items: list | tuple,
        styles: list | tuple = [],
        chosen: int = 0,
        page_size: int = 15,
        text = None
    ) -> None:
        self.items = items
        self.chosen = chosen
        self.page_size = page_size
        self.len = len(items)
        self.start = 0
        self.text = text
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

        result = ''
        for index, item in enumerate(to_print):
            index = self.start + index
            if index == self.chosen:
                if system == 'Windows':
                    item = f'[blue]➜[/blue]   [reverse]{item}[/reverse]'
                else:
                    item = f'[blue]➜[/blue]  [reverse]{item}[/reverse]'
            else:
                item = f'    {item}'
            with co.capture() as capture:
                co.print(
                    item,
                    highlight = False,
                    style = self.styles[index],
                )
            result += capture.get() + '\r'
        if self.text:
            with co.capture() as capture:
                co.print(
                    self.text
                )

            result = capture.get() + '\r' + result

        print(
            "\033[H\033[J" + result.replace(
                '\n',
                '\n\r',
            )
        )

    def choose(
        self,
        text = None,
    ):
        if text:
            self.text = text
        stdscr = c.initscr()
        c.noecho()
        c.cbreak()
        os.system('tput civis')
        stdscr.keypad(True)
        c.ungetch(0)
        key = None
        while True:
            self.print()
            key = stdscr.getch()
            match key:
                case Keys.esc:
                    self.chosen = None
                    break
                case c.KEY_ENTER | Keys.enter:
                    break
                case c.KEY_UP | c.KEY_LEFT | Keys.w | Keys.a:
                    self.chosen -= 1
                case c.KEY_DOWN | c.KEY_RIGHT | Keys.s | Keys.d:
                    self.chosen += 1
                case Keys.s | Keys.d:
                    self.chosen += 1
                case Keys.page_up:
                    self.chosen -= self.page_size
                    self.chosen = max(
                        self.chosen,
                        0
                    )
                case Keys.page_down:
                    self.chosen += self.page_size
                    self.chosen = min(
                        self.chosen,
                        self.len - 1
                    )
                case c.KEY_HOME:
                    self.chosen = 0
                case c.KEY_END:
                    self.chosen = self.len - 1

        c.echo()
        c.nocbreak()
        os.system('tput cnorm')
        stdscr.keypad(False)
        c.endwin()

        if self.chosen is None:
            return None
        else:
            return self.items[self.chosen]


@dataclass
class Keys:
    w = ord('w')
    a = ord('a')
    s = ord('s')
    d = ord('d')
    j = ord('j')
    k = ord('k')
    page_down = 338
    page_up = 339
    enter = 10
    esc = 96
