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
        data = self.get_sample_input().splitlines()
        stamp = int(data[0])
        offset = 0
        for bus_id in data[1].split(','):
            if bus_id != 'x':
                yield DotDict(id=int(bus_id), offset=offset, initial_time=stamp, is_bus=True)
            else:
                yield DotDict(is_bus=False)
            offset += 1

    def bus_id_diff(self, bus_id, timestamp):
        return bus_id * ceil(timestamp / bus_id) - timestamp

    def check(self, data, timestamp):
        for v in data:
            if not v.is_bus:
                continue
            if v.id * ceil(timestamp / v.id) - timestamp != v.offset:
                return False
        return True

    def solve(self):
        data = list(self.parse_input())
        buses = [bus for bus in data if bus.is_bus]
        max_bus = max(buses, key=lambda x: x.id)
        _off = max_bus.offset
        # https://adventofcode.com/2020/day/13
        for i in count(0, max_bus.id):
            if not i % 3_000_000:
                print(i)
            if self.check(data, i - _off):
                print(f'day 13 part 2 answer: {i - _off}')
                return
