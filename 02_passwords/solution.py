def count_letters(input, letter):
    count = 0
    for possible_letter in list(input):
        if possible_letter == letter:
            count += 1
    return count

def validate_password_part_1(loc_1, loc_2, letter, password):
    count = count_letters(password, letter)
    if loc_1 <= count <= loc_2:
        return True
    return False

def validate_password_part_2(loc_1, loc_2, letter, password):
    loc_1_matches = (letter == password[loc_1 - 1])
    loc_2_matches = (letter == password[loc_2 - 1])
    if loc_1_matches and loc_2_matches:
        return False
    elif not loc_1_matches and not loc_2_matches:
        return False
    return True

def parse_input(filename):
    text = open(filename)
    lines = text.read().splitlines()
    passwords = []
    for line in lines:
        parts = line.split(' ')
        minmax = parts[0].split('-')
        loc_1 = int(minmax[0])
        loc_2 = int(minmax[1])
        letter = parts[1][:-1]
        password = parts[2]
        passwords.append({
            'loc_1': loc_1,
            'loc_2': loc_2,
            'letter': letter,
            'password': password
        })
    return passwords

if __name__ == "__main__":
    filename = './input.txt'
    passwords = parse_input(filename)
    count_part_1 = 0
    count_part_2 = 0
    for password in passwords:
        if validate_password_part_1(**password):
            count_part_1 += 1
        if validate_password_part_2(**password):
            count_part_2 += 1
    print("Part 1:", count_part_1)
    print("Part 2:", count_part_2)