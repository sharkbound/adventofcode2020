from collections import Counter

from day import Day, util
import numpy as np


class Day10Part1(Day):
    day = 10
    part = 1

    def get_sample_input(self):
        return '28\n33\n18\n42\n31\n14\n46\n20\n48\n47\n24\n23\n49\n45\n19\n38\n39\n11\n1\n32\n25\n35\n8\n17\n7\n9\n4\n2\n34\n10\n3'

    def parse_input(self):
        return np.fromstring(self.input_text, dtype=np.int64, sep='\n')

    def solve(self):
        (data := self.parse_input()).sort()
        counter = Counter(data[i + 1] - data[i] for i in range(len(data) - 1))
        counter[data.max() + 3 - data[-1]] += 1
        counter[data[0]] += 1
        print('day 10 part 1 answer:', counter[1] * counter[3])
