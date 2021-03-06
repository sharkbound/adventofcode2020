import re
from collections import defaultdict, deque
from dataclasses import dataclass
from typing import List

from day import Day

RE_RULE = re.compile(r'(?P<color>\w+ \w+) bags contain (?P<other>.+)')
SHINY_GOLD = 'shiny gold'


class Day7Part1(Day):
    day = 7
    part = 1

    def get_sample_input(self):
        return ('light red bags contain 1 bright white bag, 2 muted yellow bags.\n'
                'dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n'
                'bright white bags contain 1 shiny gold bag.\n'
                'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n'
                'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n'
                'dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n'
                'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n'
                'faded blue bags contain no other bags.\n'
                'dotted black bags contain no other bags.')

    def _parse_contains(self, contains: str):
        return tuple(
            (int(match[1]), match[2])
            for v in contains.split(',')
            if (match := re.match(r'^(?P<count>\d+) (?P<color>\w+ \w+) bags?$', v.strip(' .,')))
        )

    def parse_input(self):
        data = defaultdict(list)
        for line in self.input_text.split('\n'):
            match = RE_RULE.match(line)
            color = match['color']
            contains = self._parse_contains(match['other'])
            data[color].extend(contains)
        return data

    def iter_direct_sub_bags(self, key, paths):
        for (number, bag) in paths.get(key, []):
            yield bag

    def has_shiny_gold_bag(self, key, paths):
        seen = set()
        search = deque([key])
        while search:
            name = search.popleft()
            if name in seen:
                continue
            if name == SHINY_GOLD:
                return True
            seen.add(name)
            search.extend(self.iter_direct_sub_bags(name, paths))
        return False

    def solve(self):
        paths = self.parse_input()
        print('day 7 part 1 answer:', sum(1 for path in paths if path != SHINY_GOLD and self.has_shiny_gold_bag(path, paths)))
