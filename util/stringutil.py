from typing import Iterable
import re

RE_ALL_INTS = re.compile(r'([+-]?\d+)')


def striplines(lines: Iterable[str]):
    return map(str.strip, lines)


def striplines_aslist(lines: Iterable[str]):
    return list(striplines(lines))


def find_all_ints(string: str):
    return [int(x) for x in RE_ALL_INTS.findall(string)]
