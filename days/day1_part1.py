from day import Day


class Day1Part1(Day):
    day = 1
    part = 1

    def parse_input(self):
        return list(map(int, self.input_text_lines))

    def solve(self):
        seen = set()
        for number in self.parse_input():
            if 2020 - number in seen:
                print(f'day 1 part 1 answer: {number * (2020 - number)}')
                return
            seen.add(number)
