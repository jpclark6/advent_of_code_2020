"""
Advent of code
Day 5
"""

def parse_row(boarding_pass):
    possible_seats = list(range(128))
    for rule in boarding_pass[:7]:
        if rule == 'F':
            possible_seats = possible_seats[:round(len(possible_seats) / 2)]
        else:
            possible_seats = possible_seats[round(len(possible_seats) / 2):]
    return possible_seats[0]

def parse_column(boarding_pass):
    possible_seats = list(range(8))
    for rule in boarding_pass[7:]:
        if rule == 'L':
            possible_seats = possible_seats[:round(len(possible_seats) / 2)]
        else:
            possible_seats = possible_seats[round(len(possible_seats) / 2):]
    return possible_seats[0]
    
def find_seat_id(boarding_pass):
    row = parse_row(boarding_pass)
    column = parse_column(boarding_pass)
    return row * 8 + column

def part_1(passes):
    highest = 0
    for boarding_pass in passes:
        seat_id = find_seat_id(boarding_pass)
        if seat_id > highest:
            highest = seat_id
    print('Part 1:', highest)

def part_2(passes):
    all_ids = [find_seat_id(boarding_pass) for boarding_pass in passes]
    all_ids.sort()
    for i in range(len(all_ids)):
        if all_ids[i] + 1 != all_ids[i + 1]:
            print('part 2:', all_ids[i] + 1)
            return
    

if __name__ == "__main__":
    filename = './input.txt'
    text = open(filename)
    lines = text.read().split('\n')
    part_1(lines)
    part_2(lines)