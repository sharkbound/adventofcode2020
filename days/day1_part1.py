from day import Day
from itertools import combinations


class Day1Part1(Day):
    day = 1
    part = 1

    def parse_input(self):
        return list(map(int, self.input_text_lines))

    def solve(self):
        data = self.parse_input()
        for n1, n2 in combinations(data, 2):
            if n1 + n2 == 2020:
                print(f'day 1 part 1 answer: {n1 * n2}')
                break
