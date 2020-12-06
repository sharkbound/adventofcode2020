from day import Day
from util.dotdict import DotDict


class Day6Part1(Day):
    day = 6
    part = 1

    def get_sample_input(self):
        return 'abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb'

    def parse_input(self):
        for lines in self.input_text.split('\n\n'):
            answers = set()
            for line in map(str.strip, lines.splitlines()):
                if not line:
                    break
                answers.update(line)
            yield answers

    def solve(self):
        print(sum(map(len, self.parse_input())))
