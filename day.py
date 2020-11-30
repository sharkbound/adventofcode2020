from inspect import isclass
from pathlib import Path
from typing import Optional


class Day:
    day = 0
    part = 1

    def _read_input_from_file(self) -> str:
        file = Path(f'inputs/{self.day}.txt')
        if not file.exists():
            raise RuntimeError(f'{str(file)} does not exists!')
        with file.open() as reader:
            return reader.read()

    def parse_input(self):
        return self._read_input_from_file()

    def solve(self):
        pass


class DayNotFoundError(Exception):
    def __init__(self, day, part, search_path) -> None:
        super().__init__(f'failed to load day file\n\t[day: {day}, part: {part}, path: {search_path}]')


class MissingDayFileError(Exception):
    def __init__(self, day, part, search_path) -> None:
        super().__init__(f'day python does not exists\n\t[day: {day}, part: {part}, path: {search_path}]')


def run_day(day, part):
    days_folder = Path('./days/')
    day_py_file = days_folder / f'day{day}_part{part}.py'
    day_to_run: Optional[Day] = None

    if not day_py_file.exists():
        raise MissingDayFileError(day, part, day_py_file)

    with day_py_file.open() as reader:
        module_globals = {}
        module_locals = {}
        exec(reader.read(), module_globals, module_locals)
        for key, value in {**module_globals, **module_locals}.items():
            if value is not Day and isclass(value) and issubclass(value, Day):
                day_to_run = value()
                break
    if day_to_run is None:
        raise DayNotFoundError(day, part, day_py_file)

    day_to_run.solve()
