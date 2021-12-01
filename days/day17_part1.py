import itertools
from collections import deque
from copy import deepcopy
from typing import Deque, Tuple, Generator

from day import Day, util
import re
import numpy as np

ACTIVE = '#'
INACTIVE = '.'


class Day17Part1(Day):
    day = 17
    part = 1

    NEIGHBOR_OFFSETS = tuple(offsets for offsets in itertools.product((-1, 0, 1), repeat=3) if any(offsets))

    def get_sample_input(self):
        return (".#.\n"
                "..#\n"
                "###")

    def solve(self):
        data = self.parse_input()
        for loop in itertools.count(1):
            # create a blank array that is +2 length of the current data, this is to expand its z axis
            data = self.fill_mid_section(self.expand_array_z(data, 2), data)
            print(f'===========\nPRE_PROCESSED: {data}\n=============')
            blank = np.zeros(data.shape)

            for indexes, value in np.ndenumerate(data):
                _, alive, dead = self.get_neighbors(data, *indexes)
                if value == 1:
                    blank[indexes] = 1 if alive in {2, 3} else 0
                elif value == 0:
                    blank[indexes] = 1 if alive == 3 else 0

            print(data)
            data = self.expand_inner_arrays(blank)

            if loop == 3:
                exit()

    def parse_input(self):
        lines = [[int(symbol == ACTIVE) for symbol in row] for row in self.input_sample_lines]
        #               the inner array is needed because of the 3D array requirement
        return np.array([np.array(lines)], dtype=np.bool)

    def get_neighbors(self, data: np.ndarray, z: int, y: int, x: int):
        # noinspection PyUnboundLocalVariable
        return (
            neighbors := tuple(data[actual_z, actual_y, actual_x]
                               for zoff, yoff, xoff in self.NEIGHBOR_OFFSETS
                               if 0 <= (actual_z := z + zoff) < data.shape[0]
                               and 0 <= (actual_y := y + yoff) < data.shape[1]
                               and 0 <= (actual_x := x + xoff) < data.shape[2]),
            sum(neighbors),
            len(neighbors) - sum(neighbors)
        )

    @staticmethod
    def expand_array_z(data: np.ndarray, times: int = 2):
        return np.full(((s := data.shape)[0] + times, s[1], s[2]), fill_value=0)

    @staticmethod
    def fill_mid_section(to_fill: np.ndarray, fill_data: np.ndarray):
        to_fill[1:-1] = fill_data
        return to_fill

    @staticmethod
    def expand_inner_arrays(data: np.ndarray):
        shape = data.shape
        output = np.full((shape[0], shape[1] + 2, shape[2] + 2), fill_value=0)
        for i, row in enumerate(data):
            output[i] = np.pad(row, 1, constant_values=0)
        return output
