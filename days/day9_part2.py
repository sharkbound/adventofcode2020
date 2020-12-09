from collections import deque

from day import Day
import numpy as np


class View:
    def __init__(self, data: list, look_back: int):
        self.preample = deque(data[:look_back])
        self.ahead = deque(data[look_back:])

    @property
    def current(self):
        return self.ahead[0]

    def advance(self):
        self.preample.popleft()
        self.preample.append(self.ahead.popleft())

    def __bool__(self):
        return bool(self.ahead)


class Day9Part2(Day):
    day = 9
    part = 2

    def get_sample_input(self):
        return '35\n20\n15\n25\n47\n40\n62\n55\n65\n95\n102\n117\n150\n182\n127\n219\n299\n277\n309\n576'

    def parse_input(self):
        return np.fromstring(self.input_text, dtype=np.int64, sep='\n')
        # return list(map(int, self.input_text_lines))

    def find_part1_solution(self, data):
        part1_view = View(data, 25)
        invalid_number = -1
        while part1_view:
            value = part1_view.current
            if not any(value - n in part1_view.preample for n in part1_view.preample):
                invalid_number = value
                break
            part1_view.advance()
        return invalid_number

    def solve(self):
        data = self.parse_input()
        LEN = len(data)
        invalid_number = self.find_part1_solution(data)

        for start_index in range(LEN):
            for end_index in range(LEN, start_index, -1):
                if (sum_ := (window := data[start_index:end_index]).sum()) > invalid_number:
                    continue
                if sum_ == invalid_number:
                    print('day 9 part 2 answer:', window.min() + window.max())
                    return
                break
