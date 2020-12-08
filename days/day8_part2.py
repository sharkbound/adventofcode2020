from collections import namedtuple
from enum import Enum, auto
from typing import List

from day import Day

Instruction = namedtuple('Instruction', 'opcode data')
RunResult = namedtuple('RunResult', 'acc cycle_limit_reached')


class OPCode(Enum):
    jmp = auto()
    acc = auto()
    nop = auto()


def parse_instructions(code):
    return [Instruction(OPCode[opcode], int(data)) for opcode, data in map(str.split, code)]


class CPU:
    def __init__(self, code: List[Instruction]):
        self.code = code.copy()
        self.acc = 0
        self.ptr = 0

    def run(self, cycle_limit=-1):
        while cycle_limit == -1 or cycle_limit > 0:
            if not (0 <= self.ptr < len(self.code)):
                break

            cycle_limit -= 1
            opcode, data = self.code[self.ptr]
            if opcode is OPCode.acc:
                self.acc += data
                self.ptr += 1
            elif opcode is OPCode.nop:
                self.ptr += 1
            elif opcode is OPCode.jmp:
                self.ptr += data

        return RunResult(self.acc, cycle_limit == 0)


class Day8Part2(Day):
    day = 8
    part = 2

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
        return parse_instructions(self.input_text.splitlines())

    def solve(self):
        instructions = self.parse_input()
        for index, instr in enumerate(instructions):
            code = instructions.copy()
            if instr.opcode is OPCode.nop:
                code[index] = Instruction(OPCode.jmp, instr.data)
            elif instr.opcode is OPCode.jmp:
                code[index] = Instruction(OPCode.nop, instr.data)
            else:
                # because the opcode was not JMP or NOP, we ignore it and keep searching
                continue

            result = CPU(code).run(cycle_limit=90_000)
            if not result.cycle_limit_reached:
                print('day 8 part 2 answer:', result.acc)
                return
