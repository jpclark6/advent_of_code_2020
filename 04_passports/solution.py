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
    if valid:
        valid_passports += 1