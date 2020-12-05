from day import Day

FRONT, BACK, LEFT, RIGHT = 'FBLR'


class Day5Part1(Day):
    day = 5
    part = 1

    # OLD: this is what i wrote before i found the faster way via binary to base 10
    # def find_seat_position(self, line):
    #     current = DotDict(upper=0, lower=127, seat_upper=0, seat_lower=7)
    #     running_row = 128
    #     running_column = 8
    #     last_row_input = last_column_input = ''
    #     for char in line:
    #         if char == FRONT:
    #             running_row //= 2
    #             current.lower -= running_row
    #         elif char == BACK:
    #             running_row //= 2
    #             current.upper += running_row
    #         elif char == LEFT:
    #             running_column //= 2
    #             current.seat_lower -= running_column
    #         elif char == RIGHT:
    #             running_column //= 2
    #             current.seat_upper += running_column
    #         if char in (FRONT, BACK):
    #             last_row_input = char
    #         elif char in (LEFT, RIGHT):
    #             last_column_input = char
    #
    #     row = {FRONT: current.upper, BACK: current.lower}[last_row_input]
    #     seat = {LEFT: current.seat_upper, RIGHT: current.seat_lower}[last_column_input]
    #
    #     return row, seat

    BINARY_TRANS = str.maketrans('FBLR', '0101')

    def find_seat_id_fast(self, line: str):
        return int(line[:-3].translate(self.BINARY_TRANS), 2) * 8 + int(line[-3:].translate(self.BINARY_TRANS), 2)

    def iter_seat_ids(self):
        yield from map(self.find_seat_id_fast, self.input_text_lines)

    def solve(self):
        print('day 5 part 1 answer:', max(self.iter_seat_ids()))
