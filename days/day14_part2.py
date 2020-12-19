import re
from collections import defaultdict
from itertools import permutations, combinations_with_replacement, product
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
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
'''

    def parse_input(self):
        mask_block = ()
        for line in self.input_text.splitlines():
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
        return 'X'

    def apply_mask(self, mask_bits: str, value_bits: int):
        bin_value = format(value_bits, 'b')
        return (ret := ''.join(map(self.transform_bit, zip(mask_bits, format(bin_value, '0>36'))))), [i for i, v in enumerate(ret) if v == 'X']

    def iter_addresses(self, bits: str, x_indexes: list):
        if not x_indexes:
            yield int(bits, 2)
            return

        bits = bits.replace('X', '{}')
        for replacements in product('10', repeat=len(x_indexes)):
            yield int(bits.format(*replacements), 2)

    def solve(self):
        memory = defaultdict(int)
        data = self.parse_input()
        for mask, mem_sets in data:
            for index, value in mem_sets:
                masked, x_indexes = self.apply_mask(mask, index)
                memory.update({address: value for address in self.iter_addresses(masked, x_indexes)})

        print(sum(memory.values()))
