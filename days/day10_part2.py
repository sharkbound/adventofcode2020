from collections import Counter
from day import Day


class Day10Part2(Day):
    day = 10
    part = 2

    def get_sample_input(self):
        return '16\n10\n15\n5\n1\n11\n7\n19\n6\n12\n4'

    def parse_input(self):
        return [0] + list(map(int, self.input_text.splitlines()))

    def _check_can_connect(self, data, index, offset):
        return index + offset < len(data) and data[index + offset] - data[index] <= 3

    def _get_next_three_adapters(self, data, index):
        return [data[index + i] for i in (1, 2, 3) if self._check_can_connect(data, index, i)]

    def solve(self):
        data = self.parse_input()
        data.sort()

        # referenced from reddit comment: https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gfcxuxf?utm_source=share&utm_medium=web2x&context=3
        # this problem threw me in a very hard to escape mental block in understanding HOW to solve it
        # while i didnt really write this myself, i did come up with (_get_next_three_adapters, and _check_can_connect) myself while struggling
        # but this solution from the reddit comment finally made it click for me mentally HOW to solve it, and WHY this solved it
        connection_counter = Counter({0: 1})
        for i, current_node in enumerate(data):
            for next_node in self._get_next_three_adapters(data, i):
                connection_counter[next_node] += connection_counter[current_node]

        print('day 10 part 2 answer:', connection_counter[data[-1]])
