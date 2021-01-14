"""
Advent of code
Day 11
Not dry, not fast (5 sec part 1, 10 sec part 2) but it works
Lots of room for refactor
"""

from copy import deepcopy
import hashlib

class modified_array(list):
    def __getitem__(self, n):
        if n < 0:
            raise IndexError("Negative index")
        return list.__getitem__(self, n)

def make_seats(filename):
    text = open(filename).read().split('\n')
    seats = modified_array(modified_array(seat for seat in seats) for seats in text)
    return seats

def part_1(seats):
    udrdddld = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    next_arrangement = [[]]
    prev_hash = ''
    safety = 0
    while True:
        safety += 1
        if safety > 500:
            return

        next_arrangement = deepcopy(seats)
        for y in range(len(seats)):
            for x in range(len(seats[y])):
                if seats[y][x] == '.':
                    continue
                if seats[y][x] == 'L':
                    adj_occupied = 0
                    for y_diff, x_diff in udrdddld:
                        try:
                            if seats[y + y_diff][x + x_diff] == '#':
                                adj_occupied += 1
                        except IndexError:
                            pass
                    if adj_occupied == 0:
                        next_arrangement[y][x] = '#'
                if seats[y][x] == '#':
                    adj_occupied = 0
                    for y_diff, x_diff in udrdddld:
                        try:
                            if seats[y + y_diff][x + x_diff] == '#':
                                adj_occupied += 1
                        except IndexError:
                            pass
                    if adj_occupied >= 4:
                        next_arrangement[y][x] = 'L'
        del seats
        seats = next_arrangement
        current_hash = hash_array(seats)
        if prev_hash == current_hash:
            print('Part 1:', count_occupied(seats))
            return
        else:
            prev_hash = current_hash


def part_2(seats):
    udrdddld = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    next_arrangement = [[]]
    prev_hash = ''
    safety = 0
    while True:
        safety += 1
        if safety > 500:
            return
        next_arrangement = deepcopy(seats)
        for y in range(len(seats)):
            for x in range(len(seats[y])):
                if seats[y][x] == '.':
                    continue
                if seats[y][x] == 'L':
                    adj_occupied = 0
                    for y_diff, x_diff in udrdddld:
                        try:
                            x_diff_total = x_diff
                            y_diff_total = y_diff
                            while True:
                                if seats[y + y_diff_total][x + x_diff_total] == '#':
                                    adj_occupied += 1
                                    break
                                if seats[y + y_diff_total][x + x_diff_total] == 'L':
                                    break
                                x_diff_total += x_diff
                                y_diff_total += y_diff
                        except IndexError:
                            pass
                    if adj_occupied == 0:
                        next_arrangement[y][x] = '#'
                if seats[y][x] == '#':
                    adj_occupied = 0
                    for y_diff, x_diff in udrdddld:
                        try:
                            x_diff_total = x_diff
                            y_diff_total = y_diff
                            while True:
                                if seats[y + y_diff_total][x + x_diff_total] == '#':
                                    adj_occupied += 1
                                    break
                                if seats[y + y_diff_total][x + x_diff_total] == 'L':
                                    break
                                x_diff_total += x_diff
                                y_diff_total += y_diff
                        except IndexError:
                            pass
                    if adj_occupied >= 5:
                        next_arrangement[y][x] = 'L'
        del seats
        seats = next_arrangement
        current_hash = hash_array(seats)
        if prev_hash == current_hash:
            print('Part 2:', count_occupied(seats))
            return
        else:
            prev_hash = current_hash

def hash_array(seats):
    return hashlib.sha256(str(seats).encode('utf-8')).hexdigest()

def count_occupied(seats):
    count = 0
    for y in seats:
        for x in y:
            if x == '#':
                count += 1

    return count

def print_array(ary):
    for y in range(len(ary)):
        print(''.join(ary[y]))

if __name__ == "__main__":
    filename = 'example1.txt'
    # filename = 'example2.txt'
    filename = 'input.txt'
    # seats = make_seats(filename)
    # part_1(seats)
    seats = make_seats(filename)
    part_2(seats)
