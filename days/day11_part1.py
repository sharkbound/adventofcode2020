from collections import defaultdict, deque, Counter
from pprint import pprint

from day import Day, util
import numpy as np

OCCUPIED = '#'
EMPTY = 'L'
FLOOR = '.'


class Day11Part1(Day):
    day = 11
    part = 1

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
        return tuple(
            grid[pos[0] + y, pos[1] + x]
            for y, x in self.OFFSETS
            if 0 <= pos[1] + x < grid.shape[1] and 0 <= pos[0] + y < grid.shape[0])

    def parse_input(self):
        return np.array(tuple(map(list, self.input_text.splitlines())), dtype=str)

    def solve(self):
        grid = self.parse_input()
        buffer = grid.copy()
        while True:
            for indexes, char in np.ndenumerate(grid):
                neighbors = self.get_neighbors(grid, indexes)
                if char == EMPTY and OCCUPIED not in neighbors:
                    buffer[indexes] = OCCUPIED
                elif char == OCCUPIED and neighbors.count(OCCUPIED) >= 4:
                    buffer[indexes] = EMPTY

            if (grid == buffer).all():
                grid = buffer.copy()
                break
            grid = buffer.copy()

        print('day 11 part 1 answer:', (grid == OCCUPIED).sum())
