"""
Advent of code
Day 3
"""

def parse_input(filename):
    text = open(filename)
    lines = text.read().splitlines()
    puzzle = [[square for square in list(line)] for line in lines]
    return puzzle

def add_pattern(puzzle, loops):
    for _ in range(loops):
        puzzle = [line * 2 for line in puzzle]
    return puzzle

def find_trees(puzzle, slope):
    loc = {"x": 0, "y": 0}
    trees = 0
    try:
        failsafe = 0
        while True:
            loc["x"] += slope["x"]
            loc["y"] += slope["y"]
            if puzzle[loc["y"]][loc["x"]] == "#":
                trees += 1

            failsafe += 1
            if failsafe > 10000:
                print("oopsie")
                break
    except IndexError:
        pass
    return trees

if __name__ == "__main__":
    filename = "input.txt"
    puzzle = parse_input(filename)
    modified_puzzle = add_pattern(puzzle, 8)
    # part 1
    slope = {"x": 3, "y": 1}
    trees = find_trees(modified_puzzle, slope)

    # part 2
    part_2_slopes = [
        {"x": 1, "y": 1},
        {"x": 3, "y": 1},
        {"x": 5, "y": 1},
        {"x": 7, "y": 1},
        {"x": 1, "y": 2},
    ]
    part_2_answer = 1
    for slope in part_2_slopes:
        part_2_answer *= find_trees(modified_puzzle, slope)
    
    print("Part 1:", trees)
    print("Part 2:", part_2_answer)
