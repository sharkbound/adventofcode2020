from inspect import isclass
from pathlib import Path
from typing import Optional
from importlib import import_module


class DayInputFileNotFoundError(Exception):
    def __init__(self, day, part, search_path):
        super().__init__(f'could not find input file for day {day}\n\t[day: {day}, part: {part}, path: {search_path}]')


class Day:
    day = 0
    part = 1

    def _read_input_from_file(self) -> str:
        file = Path(f'inputs/{self.day}.txt')
        if not file.exists():
            raise DayInputFileNotFoundError(self.day, self.part, file)

        with file.open() as reader:
            return reader.read()

    def parse_input(self):
        return self._read_input_from_file()

    def solve(self):
        raise NotImplementedError(f'solve() is not implemented for [day: {self.day}, part: {self.part}]')


class DayNotFoundError(Exception):
    def __init__(self, day, part, search_path) -> None:
        super().__init__(f'failed to load day file\n\t[day: {day}, part: {part}, path: {search_path}]')


class MissingDayFileError(Exception):
    def __init__(self, day, part, search_path) -> None:
        super().__init__(f'day python does not exist\n\t[day: {day}, part: {part}, path: {search_path}]')


def run_day(day, part):
    days_folder = Path('./days/')
    day_py_file = days_folder / f'day{day}_part{part}.py'
    day_to_run: Optional[Day] = None

    if not day_py_file.exists():
        raise MissingDayFileError(day, part, day_py_file)

    module = import_module(f'days.{day_py_file.name.replace(".py", "")}')
    for value in module.__dict__.values():
        if value is not Day and isclass(value) and issubclass(value, Day) and value.day == day and value.part == part:
            day_to_run = value()
            break

    if day_to_run is None:
        raise DayNotFoundError(day, part, day_py_file)

    day_to_run.solve()
