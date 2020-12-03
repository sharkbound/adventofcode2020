from day import Day
import numpy as np
from functools import reduce
from operator import mul


class Day3Part2(Day):
    day = 3
    part = 2

    def get_sample_input(self):
        return ("..##.......\n"
                "#...#...#..\n"
                ".#....#..#.\n"
                "..#.#...#.#\n"
                ".#...##..#.\n"
                "..#.##.....\n"
                ".#.#.#....#\n"
                ".#........#\n"
                "#.##...#...\n"
                "#...##....#\n"
                ".#..#...#.#\n")

    def parse_input(self):
        return np.array([list(line) for line in self.input_text_lines])

    def get_trees_hit(self, data):
        height, width = data.shape
        for offset_x, offset_y in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
            trees = 0
            x = y = 0
            while True:
                x = (x + offset_x) % width
                y += offset_y
                if y >= height:
                    break
                if data[y, x] == '#':
                    trees += 1
            yield trees

    def solve(self):
        print(f'day 3 part 2 answer: {reduce(mul, self.get_trees_hit(self.parse_input()))}')
