from functools import reduce
from operator import and_
from day import Day


class Day6Part2(Day):
    day = 6
    part = 2

    def get_sample_input(self):
        return 'abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb'

    def parse_input(self):
        for lines in self.input_text.split('\n\n'):
            answers = []
            for line in map(str.strip, lines.splitlines()):
                if not line:
                    break
                answers.append(set(line))
            yield answers

    def solve(self):
        print(sum(len(reduce(and_, group)) for group in self.parse_input()))
