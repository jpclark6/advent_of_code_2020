"""
Advent of code
Day 6
"""

def parse_input(filename):
    text = open(filename)
    groups = text.read().split('\n\n')
    return groups

def part_1(groups):
    total = 0
    for group in groups:
        answers = group.replace('\n', '')
        total += len(set(answers))
    print("Part 1:", total)

def part_2(groups):
    total = 0
    for group in groups:
        people = group.split('\n')
        answers = set(people[0])
        for person in people[1:]:
            answers.intersection_update(person)
        total += len(answers)
    print("Part 2:", total)

if __name__ == "__main__":
    filename = './input.txt'
    groups = parse_input(filename)
    part_1(groups)
    part_2(groups)