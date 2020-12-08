from collections import namedtuple
from enum import Enum, auto
from typing import List

from day import Day

Instruction = namedtuple('Instruction', 'opcode data')


class OPCode(Enum):
    jmp = auto()
    acc = auto()
    nop = auto()


class CPU:
    def __init__(self, code: List[str]):
        self.code: List[Instruction] = self._parse_code(code)
        self.acc = 0
        self.ptr = 0

    def _parse_code(self, code: List[str]) -> List[Instruction]:
        return [Instruction(OPCode[opcode], int(data)) for opcode, data in map(lambda l: l.split(), code)]

    def run(self):
        seen = set()
        while True:
            if self.ptr in seen:
                return self.acc

            seen.add(self.ptr)
            opcode, data = self.code[self.ptr]
            if opcode is OPCode.acc:
                self.acc += data
                self.ptr += 1
            elif opcode is OPCode.nop:
                self.ptr += 1
            elif opcode is OPCode.jmp:
                self.ptr += data


class Day8Part1(Day):
    day = 8
    part = 1

    def get_sample_input(self):
        return ('nop +0\n'
                'acc +1\n'
                'jmp +4\n'
                'acc +3\n'
                'jmp -3\n'
                'acc -99\n'
                'acc +1\n'
                'jmp -4\n'
                'acc +6')

    def parse_input(self):
        return CPU(self.input_text.splitlines())

    def solve(self):
        cpu = self.parse_input()
        print('day 8 part 1 answer:', cpu.run())
