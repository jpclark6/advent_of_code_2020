from itertools import combinations 

def parse_input(filename):
    text = open(filename)
    lines = text.read().split('\n')
    code = [int(line) for line in lines]
    return code

def part_1(data, preamble):
    for i in range(preamble, len(data)):
        arr = data[i - preamble:i]
        combos = list(combinations(set(arr), 2)) 
        combos = [combo[0] + combo[1] for combo in combos]
        if data[i] not in combos:
            print("Part 1:", data[i])
            return data[i]
    print("Not found")

def part_2(data, value):
    for i in range(len(data)):
        for j in range(len(data) - i):
            if value == sum(data[i:i+j]) and j > 1:
                chunk = data[i:i+j]
                chunk.sort()
                answer = chunk[0] + chunk[-1]
                print("Part 2:", answer)

if __name__ == "__main__":
    filename = 'input.txt'
    # filename = 'example.txt'
    data = parse_input(filename)
    # value = part_1(data, 5)
    value = part_1(data, 25)
    part_2(data, value)