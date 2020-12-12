import re
from enum import Enum

from day import Day, util


class Dir(Enum):
    forward = 'F'
    right = 'R'
    left = 'L'
    north = 'N'
    south = 'S'
    east = 'E'
    west = 'W'

    def turn(self, left=False, right=False):
        if left:
            return {self.north: self.west, self.west: self.south, self.south: self.east, self.east: self.north}[self]
        if right:
            return {self.north: self.east, self.east: self.south, self.south: self.west, self.west: self.north}[self]
        raise ValueError(f'bad turn call: {self} -> {left=} {right=}')


class Day12Part1(Day):
    day = 12
    part = 1

    def get_sample_input(self):
        return 'F10\nN3\nF7\nR90\nF11'

    def parse_input(self):
        return [
            util.DotDict(dir=Dir(match[1]), amount=int(match[2]))
            for line in self.input_text.splitlines()
            if (match := re.search('(.)(\d+)', line))
        ]

    def advance(self, dir, x, y, amount):
        if dir is Dir.north:
            return x, y + amount
        if dir is Dir.south:
            return x, y - amount
        if dir is Dir.east:
            return x + amount, y
        if dir is Dir.west:
            return x - amount, y
        raise ValueError(f'bad direction for advance: {dir}')

    def solve(self):
        data = self.parse_input()
        facing = Dir.east
        x = 0
        y = 0
        for instr in data:
            if instr.dir in {Dir.north, Dir.south, Dir.west, Dir.east}:
                x, y = self.advance(instr.dir, x, y, instr.amount)
                continue
            elif instr.dir is Dir.forward:
                x, y = self.advance(facing, x, y, instr.amount)
            elif instr.dir is Dir.left:
                for _ in range(instr.amount // 90):
                    facing = facing.turn(left=True)
            elif instr.dir is Dir.right:
                for _ in range(instr.amount // 90):
                    facing = facing.turn(right=True)
        print(abs(x) + abs(y))
