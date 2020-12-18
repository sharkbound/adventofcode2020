import re
from collections import defaultdict

from day import Day

RE_MEM_SET = re.compile(r'^mem\[(\d+)] = (\d+)$')
RE_MASK = re.compile(r'^mask = ([X01]+)$')


class Day14Part1(Day):
    BITS_36 = int('1' * 36, 2)
    day = 14
    part = 1

    def get_sample_input(self):
        return '''\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
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

    def solve(self):
        data = self.parse_input()
        memory = defaultdict(int)
        for mask, mem_sets in data:
            for index, value in mem_sets:
                memory[index] = int(''.join(mask_bit if mask_bit != 'X' else bit for mask_bit, bit in zip(mask, f'{value:0>36b}')), 2)

        print(sum(memory.values()))
