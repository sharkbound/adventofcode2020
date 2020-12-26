from pathlib import Path

day = int(input('enter day: '))
part = int(input('enter part: '))

py_file = Path(f'days/day{day}_part{part}.py')
if py_file.exists():
    print('that day file already exists!')
    exit()

txt_input_file = Path(f'inputs/{day}.txt')
if not txt_input_file.exists():
    txt_input_file.write_text('')

py_file.write_text(f'''
from day import Day, util
import re
import numpy as np


class Day{day}Part{part}(Day):
    day = {day}
    part = {part}
    
    def get_sample_input(self):
        return ''
    
    def parse_input(self):
        return ''
        
    def solve(self):
        data = self.parse_input()
''')

print('DONE')
