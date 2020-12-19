import re
from collections import defaultdict
from itertools import permutations
from typing import Tuple

from day import Day

RE_MEM_SET = re.compile(r'^mem\[(\d+)] = (\d+)$')
RE_MASK = re.compile(r'^mask = ([X01]+)$')
FLOATING = 'X'
OVERRIDE_1 = '1'
UNCHANGED = '0'


class Day14Part2(Day):
    BITS_36 = int('1' * 36, 2)
    day = 14
    part = 2

    def get_sample_input(self):
        return '''\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
'''

    def parse_input(self):
        mask_block = ()
        for line in self.input_sample.splitlines():
            if match := RE_MASK.match(line):
                if mask_block:
                    yield mask_block
                mask_block = match[1], []
            elif match := RE_MEM_SET.match(line):
                mask_block[1].append((int(match[1]), int(match[2])))

        if mask_block and mask_block[1]:
            yield mask_block

    def transform_bit(self, bits_pair: Tuple[str, int]):
        if bits_pair[0] == '0':
            return bits_pair[1]
        if bits_pair[0] == '1':
            return bits_pair[0]
        # if mask_bit is 'X'
        return 'X'

    def apply_mask(self, mask_bits: str, value_bits: int):
        bin_value = format(value_bits, 'b')
        mask_bits = mask_bits[~len(bin_value) + 1:]
        return (ret := ''.join(map(self.transform_bit, zip(mask_bits, bin_value)))), [i for i, v in enumerate(ret) if v == 'X']

    def iter_addresses(self, bits: str, x_indexes: list):
        for replacements in permutations('011', r=len(x_indexes)):
            # note to self, combinations_with_replacements() was short by 1 permutation
            # perutations will generate too much is what i am thinking, TODO
            print(replacements)
            mutable_bits = list(bits)
            for x_index, repl in zip(x_indexes, replacements):
                mutable_bits[x_index] = repl
            yield ''.join(mutable_bits)

    def solve(self):
        print(*self.iter_addresses(*self.apply_mask('X1001X', 0b101010)), sep='\n')
        return
        data = self.parse_input()
        memory = defaultdict(int)
        for mask, mem_sets in data:
            for index, value in mem_sets:
                print(self.apply_mask(mask, value))

        print(sum(memory.values()))
