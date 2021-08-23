import re
from collections import namedtuple

import numpy as np

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

    def check_column(self, col, tickets, field):
        return all(field.a <= value <= field.b or field.c <= value <= field.d for value in tickets[:, col])

    def solve(self):
        fields, my_ticket, raw_tickets = self.parse_input()
        tickets = np.array([ticket for ticket in raw_tickets if not any(self.is_invalid(n, fields) for n in ticket)])

        answer = 1
        columns_left = set(range(tickets.shape[1]))
        while columns_left:
            for field in fields:
                matches = [col for col in columns_left if self.check_column(col, tickets, field)]
                if len(matches) != 1:
                    continue

                columns_left.discard(matches[0])
                if field.name.lower().startswith('departure'):
                    answer *= my_ticket[matches[0]]

        print('16:2 =>', answer)
