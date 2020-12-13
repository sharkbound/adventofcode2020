import re
from enum import Enum
import numpy as np
from day import Day, util


class Dir(Enum):
    forward = 'F'
    right = 'R'
    left = 'L'
    north = 'N'
    south = 'S'
    east = 'E'
    west = 'W'


class Day12Part2(Day):
    day = 12
    part = 2

    def get_sample_input(self):
        return 'F10\nN3\nF7\nR90\nF11'

    def parse_input(self):
        return [
            util.DotDict(dir=Dir(match[1]), amount=int(match[2]))
            for line in self.input_text.splitlines()
            if (match := re.search('(.)(\d+)', line))
        ]

    def advance(self, dir, x, y, amount):
        if dir is Dir.north:
            return x, y + amount
        if dir is Dir.south:
            return x, y - amount
        if dir is Dir.east:
            return x + amount, y
        if dir is Dir.west:
            return x - amount, y
        raise ValueError(f'bad direction for advance: {dir}')

    # taken from a solution in the day 12 part 2 megathread
    # code: https://topaz.github.io/paste/#XQAAAQBmBwAAAAAAAAA7mkrvHeIvDZUizuO2LI0KXESDEii/+PPLbkSnOPdHL91oz6UXO+wxEeAjikzvPWK2j16DMDQn+GPas4MdIJ9O+3YcqgVt3cT0Onk5rSM+6pBa6P89rK0yip60owDcpspOKWIaSTxmPzGXHTl8/x0Jbav0IB+D3ciBwcnPzYLKRmXrnG4Usg+wd/0XgGwPAv5AgZzpZBAVNkMcf3XOITFAqzLGAIt123KLYHVAy7XxSgBkInGfSyAgci92RbH4g4o93fPbbdI/PLtDrjXEanq9/W4f1x9gWOOL49277oQDQudZdGclT8sbBcIGdEjVbAg3GazbU9kqu6DWHCCjoH/Ojh0nWt4aExm3/tUDP0mA0D9HRlXTSKSKE2OqRO9aGrwp7czf/lDwEXW4E9X4Wp8dcCM/Zzy4yDG53DFW/TGHHx8qRntGHZbDcrg2sshKCp9TZlfvuoPURqRnfwQPzZxQB8c0LDFD2yo0KAR9vU/zwAwUavOTCxfskf8eSLpMT1ZUHNDSd782E8y0eaLlfzUZgRNZ8s7J9sV06WJ53am7hxoolfBe1Vuo11Ap7+kiVpV0CITk64kz7pfI0Ykx6MeMRE+KETI7UYOOuhvuOVs9ymbQUkXniaE2B1tzau86cnchpVRaUKzuz2dn2DNgv/+6eeFl
    def rotate(self, orientation, degrees):
        theta = np.radians(degrees)
        c, s = np.cos(theta), np.sin(theta)
        rotation_matrix = np.array(((c, -s), (s, c)))
        new_orient = np.matmul(rotation_matrix, orientation)
        return new_orient

    def solve(self):
        data = self.parse_input()
        waypoint = [10, 1]
        ship = [0, 0]

        for instr in data:
            if instr.dir in {Dir.north, Dir.south, Dir.west, Dir.east}:
                waypoint[:] = self.advance(instr.dir, waypoint[0], waypoint[1], instr.amount)
            elif instr.dir is Dir.forward:
                ship[0] += waypoint[0] * instr.amount
                ship[1] += waypoint[1] * instr.amount
            elif instr.dir is Dir.left:
                # note to self, converting to a int at this stage causes a lot of errors that makes the result WAY off
                waypoint[:] = self.rotate(waypoint, instr.amount)
            elif instr.dir is Dir.right:
                waypoint[:] = self.rotate(waypoint, -instr.amount)

        answer = int(sum(map(abs, ship))) + 1
        print(f'day 12 part 2 answer: {answer}')
