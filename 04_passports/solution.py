"""
Advent of code
Day 4
Code quality: Bad. Needs massive refactor. But it works
"""

import re

filename = './input.txt'
text = open(filename)
lines = text.read().split('\n\n')
lines = [line.replace('\n', ' ') for line in lines]
passports = [line.split(' ') for line in lines]

valid_passports = 0
for passport in passports:
    fields = {
        "byr": 0,
        "iyr": 0,
        "eyr": 0,
        "hgt": 0, 
        "hcl": 0,
        "ecl": 0,
        "pid": 0,
        "cid": 0,
    }
    valid = True
    for field in passport:
        attribute = field.split(":")[0]
        try:
            fields[attribute] += 1
        except:
            pass
    for field in fields:
        if fields[field] == 0 and field != "cid":
            valid = False
    if valid:
        valid_passports += 1
print('Part 1:', valid_passports)


valid_passports = 0
for passport in passports:
    fields = {
        "byr": 0,
        "iyr": 0,
        "eyr": 0,
        "hgt": 0, 
        "hcl": 0,
        "ecl": 0,
        "pid": 0,
        "cid": 0,
    }
    valid = True
    for field in passport:
        attribute = field.split(":")[0]
        try:
            fields[attribute] += 1
        except:
            pass
    for field in fields:
        if fields[field] == 0 and field != "cid":
            valid = False
    for field in passport:
        try:
            attribute = field.split(":")[0]
            value = field.split(":")[1]
            if attribute == 'byr':
                if not 1920 <= int(value) <= 2002:
                    valid = False
            if attribute == 'iyr':
                if not 2010 <= int(value) <= 2020:
                    valid = False
            if attribute == 'eyr':
                if not 2020 <= int(value) <= 2030:
                    valid = False
            if attribute == 'hgt':
                try:
                    height = int(value[:-2])
                    if value[-2:] == 'cm':
                        if not 150 <= height <= 193:
                            valid = False
                    elif value[-2:] == 'in':
                        if not 59 <= height <= 76:
                            valid = False
                    else:
                        valid = False
                except ValueError:
                    valid = False
            if attribute == 'hcl':
                if value[0] != '#' and len(value) != 7:
                    valid = False
                if not re.search("[a-f0-9]{6}", value[1:]):
                    valid = False
            if attribute == 'ecl':
                colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                if value not in colors:
                    valid = False
            if attribute == 'pid':
                if len(value) != 9:
                    valid = False
                if not re.search("[0-9]{9}", value):
                    valid = False
        except IndexError:
            pass
    
    if valid:
        valid_passports += 1

print('Part 2:', valid_passports)

# 157 too high