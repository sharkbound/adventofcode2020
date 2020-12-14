from collections import namedtuple
from math import ceil
from typing import NamedTuple, List

from day import Day, util

import numpy as np

Notes = NamedTuple('Notes', (('timestamp', int), ('ids', List[int])))


class Day13Part1(Day):
    day = 13
    part = 1

    def get_sample_input(self):
        return '939\n7,13,x,x,59,x,31,19'

    def parse_input(self):
        data = self.input_text.splitlines()
        return Notes(int(data[0]), [int(x) for x in data[1].split(',') if x.isnumeric()])

    def solve(self):
        data = self.parse_input()
        best_id = min(data.ids, key=lambda x: data.timestamp // x)
        diff = (best_id * ceil(data.timestamp / best_id)) - data.timestamp
        answer = best_id * diff
        print('day 13 part 1 answer:', answer)
