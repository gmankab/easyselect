# license: gnu gpl 3 https://gnu.org/licenses/gpl-3.0.en.html
# sources: https://github.com/gmankab/reposter

from rich import pretty
from rich import traceback
from rich.console import Console
from dataclasses import dataclass
from io import StringIO
import subprocess
import platform
import os

traceback.install(show_locals=True)
pretty.install()
co = Console()
p = co.print
run = subprocess.getstatusoutput
system = platform.system()
import curses as c


class Sel:
    def __init__(
        self,
        items: list | tuple,
        styles: list | tuple = [],
        chosen: int = 0,
        page_size: int = 15,
        text = None,
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
        self.parsed_text = None

    def print(
        self,
        stdscr = None,
    ):
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
            self.start: end
        ]


        extra_index = 0
        result = ''
        if system == 'Windows':
            stdscr.clear()
        if self.text:
            if system == 'Windows':
                co2 = Console(
                    record = True,
                    file = StringIO(),
                )
                co2.print(self.text)
                parsed_text = co2.export_text()

                for extra_index, text in enumerate(
                    parsed_text.split('\n')
                ):
                    stdscr.addstr(extra_index, 0, text)
                extra_index += 2
            else:
                with co.capture() as capture:
                    co.print(
                        self.text,
                        highlight = False,
                    )
                result += capture.get()

        for index, item in enumerate(to_print):
            index = self.start + index
            if index == self.chosen:
                if system == 'Windows':
                    item = f'>   {item}'
                else:
                    item = f'[deep_sky_blue1]➜[/deep_sky_blue1]  [reverse]{item}[/reverse]'
            else:
                item = f'    {item}'

            if system == 'Windows':
                stdscr.addstr(
                    index + extra_index, 0, item
                )
            else:
                with co.capture() as capture:
                    co.print(
                        item,
                        highlight = False,
                        style=self.styles[index],
                    )
                result += capture.get()
            if system != 'Windows':
                print(
                    "\033[H\033[J" + result.replace(
                        '\n',
                        '\n\r',
                    )
                )

    def choose(
        self,
        text = None
    ):
        if text:
            self.text = text
        if system != 'Windows':
            os.system('tput civis')
        stdscr = c.initscr()
        stdscr.keypad(True)
        c.noecho()
        c.cbreak()
        c.ungetch(0)
        key = None
        while True:
            self.print(stdscr)
            key = stdscr.getch()
            match key:
                case Keys.esc:
                    self.chosen = None
                    break
                case c.KEY_ENTER | Keys.enter:
                    break
                case c.KEY_UP | c.KEY_LEFT | Keys.w | Keys.a | Keys.k:
                    self.chosen -= 1
                case c.KEY_DOWN | c.KEY_RIGHT | Keys.s | Keys.d | Keys.j:
                    self.chosen += 1
                case Keys.s | Keys.d:
                    self.chosen += 1
                case Keys.page_up:
                    self.chosen -= self.page_size - 1
                    self.chosen = max(
                        self.chosen,
                        0
                    )
                case Keys.page_down:
                    self.chosen += self.page_size - 1
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
        stdscr.keypad(False)
        c.endwin()

        if system != 'Windows':
            os.system('tput cnorm')
        if self.text:
            co.print(
                self.text,
                highlight = False,
            )

        if self.chosen is None:
            return None
        else:
            item = self.items[self.chosen]
            if system != 'Windows':
                co.print(
                    f'[deep_sky_blue1]➜[/deep_sky_blue1]  [reverse]{item}[/reverse]'
                )
            else:
                co.print(
                    f'[deep_sky_blue1]>[/deep_sky_blue1]   [reverse]{item}'
                )
            return item


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
