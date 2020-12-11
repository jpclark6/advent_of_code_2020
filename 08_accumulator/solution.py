"""
Advent of code
Day 8
"""


def parse_instructions(filename):
    text = open(filename)
    instructions = text.read().split('\n')
    instructions = [{'op': instruction.split(' ')[0], 'value': int(instruction.split(' ')[1])} for instruction in instructions]
    return instructions

def test_instruction(instructions):
    acc = 0
    loc = 0
    visited = set()
    inst_length = len(instructions)

    while True:
        # found end of file
        if loc == inst_length:
            return {'ended': True, 'acc': acc}
            
        # if visited already list is infinite
        if loc in visited:
            return {'ended': False, 'acc': acc}
        else:
            visited.add(loc)

        if instructions[loc]['op'] == 'nop':
            loc += 1
        elif instructions[loc]['op'] == 'jmp':
            loc += instructions[loc]['value']
        elif instructions[loc]['op'] == 'acc':
            acc += instructions[loc]['value']
            loc += 1

def part_1(instructions):
    acc = test_instruction(instructions)
    print('Part 1:', acc['acc'])

def part_2_runner(instructions):
    for inst in instructions:
        if inst['op'] == 'jmp':
            inst['op'] = 'nop'
            acc = test_instruction(instructions)
            if acc['ended']:
                return acc['acc']
            else:
                inst['op'] = 'jmp'
        elif inst['op'] == 'nop':
            inst['op'] = 'jmp'
            acc = test_instruction(instructions)
            if acc['ended']:
                return acc['acc']
            else:
                inst['op'] = 'nop'

def part_2(instructions):
    acc = part_2_runner(instructions)
    print('Part 2:', acc)

if __name__ == "__main__":
    filename = 'input.txt'
    # filename = 'example.txt'
    instructions = parse_instructions(filename)
    part_1(instructions)
    part_2(instructions)