from day import Day
from itertools import combinations


class Day1Part1(Day):
    day = 1
    part = 2

    def parse_input(self):
        return list(map(int, self.input_text_lines))

    def solve(self):
        data = self.parse_input()
        for n1, n2, n3 in combinations(data, 3):
            if n1 + n2 + n3 == 2020:
                print(f'day 1 part 2 answer: {n1 * n2 * n3}')
                break
