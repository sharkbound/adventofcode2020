from collections import deque
from copy import deepcopy
from typing import Deque, Tuple, Generator

from day import Day, util
import re
import numpy as np

ACTIVE = '#'
INACTIVE = '.'

CubeType = Deque[np.ndarray]


def get_neighbors(cubes: CubeType, x: int, y: int, z: int) -> Generator[str, None, None]:
    pass


def expand_cubes_z(cubes: CubeType):
    cubes.appendleft(np.full(cubes[0].shape, '.', dtype='U1'))
    cubes.append(np.full(cubes[0].shape, '.', dtype='U1'))


def pad_cubes(cubes: CubeType):
    for i in range(len(cubes)):
        cubes[i] = np.pad(cubes[i], 1, mode='constant', constant_values='.')


class Day17Part1(Day):
    day = 17
    part = 1

    def get_sample_input(self):
        return (".#.\n"
                "..#\n"
                "###")

    def parse_input(self):
        lines = self.input_sample_lines
        #                                     the len seems to be used to tell the length of each row
        #                                     <U1 means 'unicode (1 byte?)'
        return deque([np.array(lines, dtype=('<U1', len(lines[0])))])

    def solve(self):
        data = self.parse_input()
        expand_cubes_z(data)
        pad_cubes(data)
        pad_cubes(data)
        print(data[0])
