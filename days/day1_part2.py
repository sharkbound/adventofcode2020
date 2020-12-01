from day import Day
from itertools import combinations


class Day1Part2(Day):
    day = 1
    part = 2

    def parse_input(self):
        return list(map(int, self.input_text_lines))

    def solve(self):
        seen = set()
        for n1, n2 in combinations(self.parse_input(), 2):
            if (n3 := 2020 % (n1 + n2)) in seen:
                print(f'day 1 part 2 answer: {n1 * n2 * n3}')
                return
            seen.update((n1, n2))
