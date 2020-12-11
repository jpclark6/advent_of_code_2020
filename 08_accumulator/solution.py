def parse_instructions(filename):
    text = open(filename)
    instructions = text.read().split('\n')
    instructions = [{'op': instruction.split(' ')[0], 'value': int(instruction.split(' ')[1])} for instruction in instructions]
    return instructions

def part_1(instructions):
    acc = 0
    loc = 0
    visited = set()
    safety = 0
    while True:
        if loc in visited:
            break
        else:
            visited.add(loc)

        if instructions[loc]['op'] == 'nop':
            loc += 1
        elif instructions[loc]['op'] == 'jmp':
            loc += instructions[loc]['value']
        elif instructions[loc]['op'] == 'acc':
            acc += instructions[loc]['value']
            loc += 1
        else:
            print('something went wrong')

        safety += 1
        if safety > 100000:
            print('error')
            break

    print('Part 1:', acc)




if __name__ == "__main__":
    filename = 'input.txt'
    # filename = 'example.txt'
    instructions = parse_instructions(filename)
    part_1(instructions)