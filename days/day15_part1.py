from collections import Counter, deque, defaultdict

from day import Day, util

import numpy as np


class Day15Part1(Day):
    day = 15
    part = 1

    def get_sample_input(self):
        return '0,3,6'

    def parse_input(self):
        return deque(map(int, self.input_text.split(',')))

    def solve(self):
        numbers = self.parse_input()
        number_len = len(numbers)
        turn_history = defaultdict(lambda: deque(maxlen=2))
        last = 0

        for i, n in enumerate(numbers, 1):
            turn_history[n].append(i)
            last = n

        for turn in range(number_len, 2020):
            if last not in turn_history:
                turn_history[last].append(turn)
                last = 0
            else:
                hist = turn_history[last]
                hist.append(turn)
                last = hist[1] - hist[0]

        print(last)
