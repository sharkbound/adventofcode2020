from day import Day
import numpy as np


class Day3Part1(Day):
    day = 3
    part = 1

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

    def solve(self):
        data = self.parse_input()
        height, width = data.shape
        trees = 0
        x = y = 0
        while True:
            x = (x + 3) % width
            y += 1
            if y >= height:
                break
            if data[y, x] == '#':
                trees += 1
        print(f'day 3 part 1 answer: {trees}')
