import re
from dataclasses import dataclass

from day import Day, util

RE_KEY_VALUE = re.compile(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)')


@dataclass()
class Validator:
    key: str
    index: int
    range1: range
    range2: range
    all_valid = set()

    def __post_init__(self):
        self.all_valid = {*self.range1, *self.range2}


class Day16Part1(Day):
    day = 16
    part = 1

    def get_sample_input(self):
        return ('class: 1-3 or 5-7\n'
                'row: 6-11 or 33-44\n'
                'seat: 13-40 or 45-50\n\n'
                'your ticket:\n'
                '7,1,14\n\n'
                'nearby tickets:\n'
                '7,3,47\n'
                '40,4,50\n'
                '55,2,20\n'
                '38,6,12')

    def parse_validator_line(self, index: int, line: str):
        key, *nums = RE_KEY_VALUE.search(line).groups()
        r1_min, r1_max, r2_min, r2_max = map(int, nums)
        return Validator(key, index, range(r1_min, r1_max + 1), range(r2_min, r2_max + 1))

    def parse_input(self):
        raw = self.input_text.split('\n\n')
        validators = [self.parse_validator_line(i, line) for i, line in enumerate(raw[0].splitlines())]
        my_ticket = [int(x) for x in re.findall('\d+', raw[1])]
        nearby_tickets = [util.find_all_ints(line) for line in raw[-1].splitlines()[1:]]
        return validators, my_ticket, nearby_tickets

    def solve(self):
        validators, my_ticket, tickets = self.parse_input()
        invalid = [
            number
            for ticket in tickets
            for number in ticket
            if not any(number in v.all_valid for v in validators)
        ]

        print('16:1 =>', sum(invalid))
