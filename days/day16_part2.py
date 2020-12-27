import re
import numpy as np
from dataclasses import dataclass

from day import Day, util

RE_KEY_VALUE = re.compile(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)')


@dataclass()
class Validator:
    key: str
    range1: range
    range2: range
    all_valid = set()
    index: int = None

    def has_index(self):
        return self.index is not None

    def __post_init__(self):
        self.all_valid = {*self.range1, *self.range2}


class Day16Part2(Day):
    day = 16
    part = 2

    def get_sample_input(self):
        return ('class: 0-1 or 4-19\n'
                'row: 0-5 or 8-19\n'
                'seat: 0-13 or 16-19\n\n'
                'your ticket:\n'
                '11,12,13\n\n'
                'nearby tickets:\n'
                '3,9,18\n'
                '15,1,5\n'
                '5,14,9')

    def parse_validator_line(self, line: str):
        key, *nums = RE_KEY_VALUE.search(line).groups()
        r1_min, r1_max, r2_min, r2_max = map(int, nums)
        return Validator(key, range(r1_min, r1_max + 1), range(r2_min, r2_max + 1))

    def iter_column(self, tickets, column_index):
        for ticket in tickets:
            yield ticket[column_index]

    def parse_input(self):
        raw = self.input_text.split('\n\n')
        validators = [self.parse_validator_line(line) for line in raw[0].splitlines()]
        my_ticket = util.find_all_ints(raw[1])
        nearby_tickets = [util.find_all_ints(line) for line in raw[-1].splitlines()[1:]]
        return validators, my_ticket, nearby_tickets

    def assign_validator_index(self, tickets: np.ndarray, validator: Validator):
        for column in range(tickets.shape[1]):
            if all(number in validator.all_valid for number in tickets[:, column]):
                validator.index = column
                return validator
        return validator

    def solve(self):
        validators, my_ticket, raw_tickets = self.parse_input()
        valid_tickets = np.array([ticket for ticket in raw_tickets if any(number in v.all_valid for number in ticket for v in validators)])
        # https://adventofcode.com/2020/day/16
        for validator in validators:
            print(self.assign_validator_index(valid_tickets, validator))

        answer = sum(my_ticket[validator.index] for validator in validators if validator.key.startswith('departure'))
        print('16:2 =>', answer)
