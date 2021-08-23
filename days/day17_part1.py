from day import Day, util
import re
import numpy as np

ACTIVE = '#'
INACTIVE = '.'


class Day17Part1(Day):
    day = 17
    part = 1

    def get_sample_input(self):
        return (".#.\n"
                "..#\n"
                "###")

    def parse_input(self):
        return self.input_sample

    def solve(self):
        data = self.parse_input()

