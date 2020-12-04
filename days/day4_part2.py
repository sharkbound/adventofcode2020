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

RE_HEIGHT = re.compile(r'(\d+)(in|cm)')
RE_HEX = re.compile(r'#[a-f0-9]{6}')

VALIDATORS = {
    BIRTH_YEAR: lambda value: len(value) == 4 and value.isnumeric() and 1920 <= int(value) <= 2002,
    ISSUE_YEAR: lambda value: len(value) == 4 and value.isnumeric() and 2010 <= int(value) <= 2020,
    EXPIRATION_YEAR: lambda value: len(value) == 4 and value.isnumeric() and 2020 <= int(value) <= 2030,
    HEIGHT: lambda value: (
            (m := RE_HEIGHT.match(value))
            and m[2] in ('cm', 'in')
            and ((150 <= int(m[1]) <= 193) if m[2] == 'cm' else (59 <= int(m[1]) <= 76))
    ),
    HAIR_COLOR: lambda value: bool(RE_HEX.match(value)),
    EYE_COLOR: lambda value: value in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    PASSPORT_ID: lambda value: len(value) == 9 and value.isnumeric()
}


class Day4Part2(Day):
    day = 4
    part = 2

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
        append = lambda: passports.append({key.strip(): value.strip() for key, value in current})

        for line in map(str.strip, self.input_text_lines):
            if line:
                current.extend(re.findall(r'([^:]+):([^ ]+)', line))
            else:
                append()
                current.clear()

        if current:
            append()

        return passports

    def validate(self, passport):
        passport_copy = passport.copy()
        xor = ALL_FIELDS ^ set(passport)
        xor.discard(COUNTRY_ID)
        return not xor and all(VALIDATORS[key](value) for key, value in passport_copy.items() if key != COUNTRY_ID)

    def solve(self):
        data = self.parse_input()
        print(sum(1 for passport in data if self.validate(passport)))
