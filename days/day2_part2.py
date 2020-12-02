from day import Day
import re
from typing import NamedTuple

Policy = NamedTuple('Policy', (('min', int), ('max', int), ('char', str), ('text', str)))


class Day2Part2(Day):
    day = 2
    part = 2

    def parse_input(self):
        return [
            Policy(int(min), int(max), char, text)
            for (min, max, char, text) in (re.search(r'(\d+)-(\d+) (.): ([^ ]+)', line).groups() for line in self.input_text_lines)
        ]

    def solve(self):
        print(sum(
            1
            for p in self.parse_input()
            if (p.text[p.min - 1] == p.char) ^ (p.text[p.max - 1] == p.char)
        ))
