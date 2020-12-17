from itertools import count
from math import ceil
from pprint import pprint
from typing import NamedTuple, List
import rich

from day import Day
from util import DotDict


class Day13Part2(Day):
    day = 13
    part = 2

    def get_sample_input(self):
        return '939\n7,13,x,x,59,x,31,19'

    def parse_input(self):
        data = self.input_text.splitlines()
        offset = 0
        for bus_id in data[1].split(','):
            if bus_id != 'x':
                yield DotDict(id=int(bus_id), offset=offset, is_bus=True)
            else:
                yield DotDict(is_bus=False)
            offset += 1

    def bus_id_diff(self, bus_id, timestamp):
        return bus_id * ceil(timestamp / bus_id) - timestamp

    def solve(self):
        data = list(self.parse_input())
        buses = sorted((bus for bus in data if bus.is_bus), key=lambda bus: bus.offset)
        # solution found on megathread for day 13 here:
        # https://www.reddit.com/r/adventofcode/comments/kc4njx/2020_day_13_solutions/gfr2uh6?utm_source=share&utm_medium=web2x&context=3
        #
        # explanation from reddit comment:
        # The basic idea is that you do not have to test every number for the time t.
        # First find a time that satisfies the condition for bus 1 (t % id1 ==0).
        # Then, you only have to check multiples of id1 for the next bus.
        # Then look for a time t with (t+1 % id2 == 0).
        # After that, the step size must be a multiple that satisfies both conditions and so on
        time = 0
        step = 1
        for bus in buses:
            while (time + bus.offset) % bus.id:
                time += step
            step *= bus.id

        print(f'day 13 part 2 answer: {time}')
