def parse_input(filename):
    text = open(filename)
    lines = text.read().split('\n')
    adapters = [int(adapter) for adapter in lines]
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    return adapters

def part_1(adapters):
    one_volt_count = 0
    three_volt_count = 0
    for i in range(len(adapters) - 1):
        if adapters[i] == adapters[i + 1] - 1:
            one_volt_count += 1
        if adapters[i] == adapters[i + 1] - 3:
            three_volt_count += 1
    print('One', one_volt_count)
    print('Three', three_volt_count)
    print('Part 1:', one_volt_count * three_volt_count)

if __name__ == "__main__":
    filename = 'example1.txt'
    filename = 'example2.txt'
    filename = 'input.txt'
    adapters = parse_input(filename)
    part_1(adapters)
    