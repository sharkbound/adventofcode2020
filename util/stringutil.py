from typing import Iterable


def striplines(lines: Iterable[str]):
    return map(str.strip, lines)


def striplines_aslist(lines: Iterable[str]):
    return list(striplines(lines))
