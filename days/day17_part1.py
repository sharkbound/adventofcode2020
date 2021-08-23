from collections import deque
from typing import Deque, Tuple, Generator

from day import Day, util
import re
import numpy as np

CubeType = Deque[dict]

ACTIVE = '#'
INACTIVE = '.'


def get_neighbors(cubes: CubeType, x: int, y: int, z: int) -> Generator[str, None, None]:
    pass


def expand_cubes(cubes: CubeType, center_z_index: int) -> Tuple[CubeType, int]:
    if not cubes:
        return deque(({}, {}, {})), 1

    cubes.appendleft({})
    cubes.append({})

    return cubes, center_z_index + 1


class Day17Part1(Day):
    day = 17
    part = 1

    def get_sample_input(self):
        return (".#.\n"
                "..#\n"
                "###")

    def parse_input(self):
        return self.input_sample_lines

    def solve(self):
        data = self.parse_input()
        cubes = expand_cubes(deque(), 0)
        print(cubes)


def test_cubes_expand_on_empty_input():
    assert len(expand_cubes(deque(), 0)[0]) == 3


def test_cubes_expand_on_one_cube_input():
    assert len(expand_cubes(deque(({},)), 0)[0]) == 3
