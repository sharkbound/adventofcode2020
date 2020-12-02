from day import Day
import re
from typing import NamedTuple

Policy = NamedTuple('Policy', (('min', int), ('max', int), ('char', str), ('text', str)))


class Day2Part1(Day):
    day = 2
    part = 1

    def parse_input(self):
        return [
            Policy(int(min), int(max), char, text)
            for (min, max, char, text) in (re.search(r'(\d+)-(\d+) (.): ([^ ]+)', line).groups() for line in self.input_text_lines)
        ]

    def solve(self):
        print(sum(
            1
            for policy in self.parse_input()
            if policy.min <= policy.text.count(policy.char) <= policy.max
        ))
