from day import Day
from util.dotdict import DotDict

FRONT, BACK, LEFT, RIGHT = 'FBLR'


class Day5Par2(Day):
    day = 5
    part = 2

    def find_seat_position(self, line):
        current = DotDict(upper=0, lower=127, seat_upper=0, seat_lower=7)
        running_row = 128
        running_column = 8
        last_row_input = last_column_input = ''
        for char in line:
            if char == FRONT:
                running_row //= 2
                current.lower -= running_row
            elif char == BACK:
                running_row //= 2
                current.upper += running_row
            elif char == LEFT:
                running_column //= 2
                current.seat_lower -= running_column
            elif char == RIGHT:
                running_column //= 2
                current.seat_upper += running_column
            if char in (FRONT, BACK):
                last_row_input = char
            elif char in (LEFT, RIGHT):
                last_column_input = char

        row = {FRONT: current.upper, BACK: current.lower}[last_row_input]
        seat = {LEFT: current.seat_upper, RIGHT: current.seat_lower}[last_column_input]

        return row, seat

    def solve(self):
        # this somehow works
        # int('BBFFBBF'.replace('F', '0').replace('B', '1'), 2) * 8 + int('RLL'.replace('L', '0').replace('R', '1'), 2)
        tests = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
        print(max(row * 8 + column for row, column in map(self.find_seat_position, self.input_text_lines)))
