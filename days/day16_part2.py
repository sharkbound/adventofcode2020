import math
import operator
import re
from collections import namedtuple
from functools import reduce
from typing import List

import numpy as np
from dataclasses import dataclass

from day import Day, util

Field = namedtuple('Field', 'name a b c d')


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

    def parse_field_line(self, line):
        key, *nums = re.search(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', line).groups()
        return Field(key, *map(int, nums))  # the *map unpacks the number constraints

    def parse_input(self):
        raw = self.input_text.split('\n\n')
        validators = [self.parse_field_line(line) for line in raw[0].splitlines()]
        my_ticket = util.find_all_ints(raw[1])
        nearby_tickets = np.array([util.find_all_ints(line) for line in raw[-1].splitlines()[1:]])
        return validators, my_ticket, nearby_tickets

    def is_invalid(self, value, fields):
        return not any(
            f.a <= value <= f.b or f.c <= value <= f.d
            for f in fields
        )

    def solve(self):
        fields, my_ticket, raw_tickets = self.parse_input()
        util.print_all(*fields, sep='\n')
        tickets = np.array([ticket for ticket in raw_tickets if not any(self.is_invalid(n, fields) for n in ticket)])
        unused_columns = set(range(len(tickets[0])))

        found_cols = {}
        for name, a, b, c, d in fields:
            matches = [col for col in unused_columns if all(a <= value <= b or c <= value <= d for value in tickets[:, col])]
            if len(matches) == 1:
                print(matches)
                found_cols[name] = matches[0]
                unused_columns.discard(matches[0])

        answer = reduce(operator.mul, (my_ticket[found_cols[field.name]] for field in fields if field.name.startswith('departure')))
        print('16:2 =>', answer)
