from collections import defaultdict, deque, Counter
from itertools import count
from pprint import pprint

from day import Day, util
import numpy as np

OCCUPIED = '#'
EMPTY = 'L'
FLOOR = '.'


class Day11Part2(Day):
    day = 11
    part = 2

    OFFSETS = (
        (0, -1), (0, 1),  # left/right
        (-1, 0), (1, 0),  # top/down
        (1, 1), (-1, -1), (-1, 1), (1, -1),  # diagonal
    )

    def get_sample_input(self):
        return ('L.LL.LL.LL\n'
                'LLLLLLL.LL\n'
                'L.L.L..L..\n'
                'LLLL.LL.LL\n'
                'L.LL.LL.LL\n'
                'L.LLLLL.LL\n'
                '..L.L.....\n'
                'LLLLLLLLLL\n'
                'L.LLLLLL.L\n'
                'L.LLLLL.LL')

    def get_neighbors(self, grid: np.ndarray, pos: tuple):
        for y, x in self.OFFSETS:
            for i in count(1):
                offset_y = y * i
                offset_x = x * i
                if not (0 <= pos[0] + offset_y < grid.shape[0] and 0 <= pos[1] + offset_x < grid.shape[1]):
                    break
                if (char := grid[pos[0] + offset_y, pos[1] + offset_x]) == FLOOR:
                    continue
                yield char
                break

    def parse_input(self):
        return np.array(tuple(map(list, self.input_text.splitlines())))

    def solve(self):
        grid = self.parse_input()
        buffer = np.full(grid.shape, fill_value=FLOOR)
        while True:
            for index, char in np.ndenumerate(grid):
                if char == FLOOR:
                    continue

                neighbors = tuple(self.get_neighbors(grid, index))
                if char == EMPTY and OCCUPIED not in neighbors:
                    buffer[index] = OCCUPIED
                elif char == OCCUPIED and neighbors.count(OCCUPIED) >= 5:
                    buffer[index] = EMPTY

            # print('====================', *map(''.join, buffer), sep='\n')

            if (grid == buffer).all():
                grid = buffer.copy()
                break
            grid = buffer.copy()

        print('day 11 part 2 answer:', (grid == OCCUPIED).sum())
