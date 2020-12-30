import math
import operator
import re
from collections import namedtuple
from functools import reduce
from typing import List

import numpy as np
from dataclasses import dataclass

from day import Day, util

Field = namedtuple('Field', 'name a b c d is_valid')


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

    def parse_field_line(self, line: str):
        key, *nums = re.search(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', line).groups()
        a, b, c, d = map(int, nums)
        return Field(key, a, b, c, d, lambda value: a <= value <= b or c <= value <= d)

    def parse_input(self):
        raw = self.input_text.split('\n\n')
        validators = [self.parse_field_line(line) for line in raw[0].splitlines()]
        my_ticket = util.find_all_ints(raw[1])
        nearby_tickets = np.array([util.find_all_ints(line) for line in raw[-1].splitlines()[1:]])
        return validators, my_ticket, nearby_tickets

    def filter_valid_tickets(self, tickets: np.ndarray, fields: List[Field]):
        pass

    def solve(self):
        fields, my_ticket, raw_tickets = self.parse_input()
        util.print_all(*fields, sep='\n')
        tickets = self.filter_valid_tickets(raw_tickets, fields)
        print(tickets.shape[0], 190)

        answer = reduce(operator.mul, (my_ticket[validator.index] for validator in fields if validator))
        print('16:2 =>', answer)
