def count_letters(input, letter):
    count = 0
    for possible_letter in list(input):
        if possible_letter == letter:
            count += 1
    return count

def validate_password_part_1(minimum, maximum, letter, password):
    count = count_letters(password, letter)
    if minimum <= count <= maximum:
        return True
    return False

def validate_password_part_2(minimum, maximum, letter, password):
    loc_1_matches = letter == password[minimum - 1]
    loc_2_matches = letter == password[maximum - 1]
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
        minimum = int(minmax[0])
        maximum = int(minmax[1])
        letter = parts[1][:-1]
        password = parts[2]
        passwords.append({
            'minimum': minimum,
            'maximum': maximum,
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