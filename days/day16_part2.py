import math
import operator
import re
from functools import reduce
from typing import List

import numpy as np
from dataclasses import dataclass

from day import Day, util

RE_KEY_VALUE = re.compile(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)')


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
        a, b, c, d = map(int, nums)
        return key, lambda value: a <= value <= b or c <= value <= d

    def parse_input(self):
        raw = self.input_text.split('\n\n')
        validators = [self.parse_validator_line(line) for line in raw[0].splitlines()]
        my_ticket = util.find_all_ints(raw[1])
        nearby_tickets = np.array([util.find_all_ints(line) for line in raw[-1].splitlines()[1:]])
        return validators, my_ticket, nearby_tickets

    def filter_valid_tickets(self, tickets: np.ndarray, validators: List[tuple]):
        invalid = set()
        for index, value in np.ndenumerate(tickets):
            for valid in validators:
                if not valid[1](value):
                    print(end=f'bad: {index[0]}, ')
                    invalid.add(index[0])
                    break

        return np.array([v for i, v in enumerate(tickets) if i not in invalid])

    def solve(self):
        validators, my_ticket, raw_tickets = self.parse_input()
        tickets = self.filter_valid_tickets(raw_tickets, validators)
        print(tickets.shape[0], 190)

        answer = reduce(operator.mul, (my_ticket[validator.index] for validator in validators if validator))
        print('16:2 =>', answer)
