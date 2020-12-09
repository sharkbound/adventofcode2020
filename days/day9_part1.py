from collections import deque

from day import Day


class View:
    def __init__(self, data: list, look_back: int):
        self.raw = data.copy()
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


class Day9Part1(Day):
    day = 9
    part = 1

    def get_sample_input(self):
        return '35\n20\n15\n25\n47\n40\n62\n55\n65\n95\n102\n117\n150\n182\n127\n219\n299\n277\n309\n576'

    def parse_input(self):
        return list(map(int, self.input_text_lines))

    def solve(self):
        view = View(self.parse_input(), 25)
        while view:
            value = view.current
            if not any(value - n in view.preample for n in view.preample):
                print(f'day 9 part 1 answer: {value}')
                return
            view.advance()
