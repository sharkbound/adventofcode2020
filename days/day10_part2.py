from day import Day, util
import numpy as np


class Day10Part2(Day):
    day = 10
    part = 2

    def get_sample_input(self):
        return '16\n10\n15\n5\n1\n11\n7\n19\n6\n12\n4'

    def parse_input(self):
        # return np.fromstring(self.input_text, dtype=np.int64, sep='\n')
        return [0] + (lst := list(map(int, self.get_sample_input().splitlines()))) + [max(lst) + 3]

    def solve(self):
        data = self.parse_input()
        data.sort()

        print(*data, sep='\n')
        valid = 0
        print('day 10 part 2 answer:', valid)
