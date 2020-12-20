from collections import defaultdict

def parse_input(filename):
    text = open(filename)
    lines = text.read().split('\n')
    adapters = [int(adapter) for adapter in lines]
    adapters.sort()
    adapters = [0] + adapters + [adapters[-1] + 3]
    return adapters

def part_1(adapters):
    one_volt_count = 0
    three_volt_count = 0
    for i in range(len(adapters) - 1):
        if adapters[i] == adapters[i + 1] - 1:
            one_volt_count += 1
        if adapters[i] == adapters[i + 1] - 3:
            three_volt_count += 1
    print('Part 1:', one_volt_count * three_volt_count)

def part_2(adapters):
    counts = defaultdict(int, {0: 1})
    for a, b in zip(adapters[1:], adapters):
        # how many ways to reach the last item in the current iteration
        counts[a] = counts[a - 3] + counts[a - 2] + counts[a - 1]
    print('Part 2:', counts[adapters[-1]])

if __name__ == "__main__":
    filename = 'example1.txt'
    filename = 'example2.txt'
    filename = 'input.txt'
    adapters = parse_input(filename)
    part_1(adapters)
    part_2(adapters)
    