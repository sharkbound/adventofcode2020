import re
from dataclasses import dataclass

from day import Day

ALL_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}

BIRTH_YEAR = 'byr'
ISSUE_YEAR = 'iyr'
EXPIRATION_YEAR = 'eyr'
HEIGHT = 'hgt'
HAIR_COLOR = 'hcl'
EYE_COLOR = 'ecl'
PASSPORT_ID = 'pid'
COUNTRY_ID = 'cid'


class Day4Part1(Day):
    day = 4
    part = 1

    def get_sample_input(self):
        return ('ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n'
                'byr:1937 iyr:2017 cid:147 hgt:183cm\n'
                '\n'
                'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\n'
                'hcl:#cfa07d byr:1929\n'
                '\n'
                'hcl:#ae17e1 iyr:2013\n'
                'eyr:2024\n'
                'ecl:brn pid:760753108 byr:1931\n'
                'hgt:179cm\n'
                '\n'
                'hcl:#cfa07d eyr:2025 pid:166559648\n'
                'iyr:2011 ecl:brn hgt:59in').splitlines()

    def parse_input(self):
        passports = []
        current = []

        for line in map(str.strip, self.input_text_lines):
            if line:
                current.extend(re.findall(r'([^:]+):([^ ]+)', line))
            else:
                passports.append({key.strip(): value.strip() for key, value in current})
                current.clear()

        if current:
            passports.append({key.strip(): value.strip() for key, value in current})

        return passports

    def solve(self):
        data = self.parse_input()
        total = 0
        for passport in data:
            xor = ALL_FIELDS ^ set(passport)
            if not xor or len(xor) == 1 and COUNTRY_ID in xor:
                total += 1
        print(total)
