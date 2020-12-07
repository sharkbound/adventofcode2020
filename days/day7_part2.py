import re
from collections import defaultdict, namedtuple, deque
from typing import Set

from day import Day

RE_RULE = re.compile(r'(?P<color>\w+ \w+) bags contain (?P<other>.+)')
SHINY_GOLD = 'shiny gold'
SubBag = namedtuple('SubBag', 'required color')


class Day7Part2(Day):
    day = 7
    part = 2

    def get_sample_input(self):
        return ('shiny gold bags contain 2 dark red bags.\n'
                'dark red bags contain 2 dark orange bags.\n'
                'dark orange bags contain 2 dark yellow bags.\n'
                'dark yellow bags contain 2 dark green bags.\n'
                'dark green bags contain 2 dark blue bags.\n'
                'dark blue bags contain 2 dark violet bags.\n'
                'dark violet bags contain no other bags.')

    def _parse_contains(self, contains: str):
        return tuple(
            SubBag(int(match[1]), match[2])
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

    def count_required_bags(self, key, paths):
        bags = deque(paths[key])
        while bags:
            bag = bags.popleft()
            yield bag.required
            for _ in range(bag.required):
                bags.extend(paths.get(bag.color, []))

    def solve(self):
        paths = self.parse_input()
        print('day 7 part 2 answer:', sum(self.count_required_bags(SHINY_GOLD, paths)))
