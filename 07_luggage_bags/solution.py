"""
Advent of code
Day 7
Harder - code isn't great but used recursion effectively
"""


class Bag:
    def __init__(self, color, qty=None):
        self.color = color
        self.qty = qty
        self.children = []

    def __repr__(self):
        return f'< Bag - {self.qty} {self.color} - {len(self.children)}c>'

    def add_children(self, bag_data):
        for child in bag_data[self.color]:
            self.add_child(child['color'], child['qty'], bag_data)

    def add_child(self, color, qty, bag_data):
        bag = Bag(color, qty)
        self.children.append(bag)
        bag.add_children(bag_data)

def check_children_for_gold(parent_color, lookup):
    has_gold = False
    children = lookup[parent_color]
    for child in children:
        if child.color == 'shiny gold':
            return True
        if check_children_for_gold(child.color, lookup):
            has_gold = True
    return has_gold

def make_bags(bag_data):
    bags = []
    for data in bag_data:
        bag = Bag(data)
        bag.add_children(bag_data)
        bags.append(bag)
    return bags

def make_bags_dict(bag_data):
    bags = make_bags(bag_data)
    bag_dict = {}
    for bag in bags:
        bag_dict[bag.color] = bag.children
    return bag_dict

def part_1(bags_dict):
    total = 0
    for bag in bags_dict:
        if check_children_for_gold(bag, bags_dict):
            total += 1
    print("Total part 1:", total)

def part_2(bags_dict):
    total = find_shiny_bags('shiny gold', bags_dict) - 1 # subtract top bag from total
    print("Total part 2:", total)

def find_shiny_bags(color, bags_dict, qty=1):
    if len(bags_dict[color]) == 0:
        return 1 # single bag without any bags inside
    else:
        total = 1 # count current bag plus children
        for child in bags_dict[color]:
            total += child.qty * find_shiny_bags(child.color, bags_dict, child.qty)
        return total
    
def parse_data(filename):
    text = open(filename)
    bags = text.read().split('\n')
    bag_data = {}
    for bag in bags:
        color = bag.split(' bags contain ')[0]
        inside_bags_temp = bag.split(' bags contain ')[1]
        inside_bags_temp = inside_bags_temp.split(', ')
        inside_bags = []
        for inside_bag in inside_bags_temp:
            if 'no other bags' in inside_bag:
                continue
            inside_bag = inside_bag.split(' bag')[0]
            inside_qty = int(inside_bag.split(' ')[0])
            inside_color = inside_bag.split(str(inside_qty) + ' ')[1]
            inside_bag = {'color': inside_color, 'qty': inside_qty}
            inside_bags.append(inside_bag)
        if inside_bags:
            contains_inside_bags = True
        else:
            contains_inside_bags = False
        bag_data[color] = inside_bags
    return make_bags_dict(bag_data)

if __name__ == "__main__":
    filename = './input.txt'
    bags_dict = parse_data(filename)
    part_1(bags_dict)
    part_2(bags_dict)

