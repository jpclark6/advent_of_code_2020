COUNT = 0

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
    return bag_data

class Bag:
    def __init__(self, color, qty=None):
        self.color = color
        self.qty = qty
        self.children = []
        self.has_gold = False

    def __repr__(self):
        return f'< Bag - {self.qty} {self.color} - {len(self.children)}c>'

    def add_children(self, bag_data):
        for child in bag_data[self.color]:
            if child['color'] == 'shiny gold':
                global COUNT 
                COUNT += 1
            self.add_child(child['color'], child['qty'])
        else:
            pass

    def add_child(self, color, qty):
        if color == 'shiny gold':
            self.contains_shiny_gold = True
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

def make_bags_dict(bags):
    bag_dict = {}
    for bag in bags:
        bag_dict[bag.color] = bag.children
    return bag_dict

def part_1(bags_dict):
    total = 0
    for bag in bags_dict:
        if check_children_for_gold(bag, bags_dict):
            total += 1
    print("TOTAL", total)


def part_2(bags_dict):
    total = find_shiny_bags('shiny gold', bags_dict) - 1
    print("TOTAL", total)

def find_qty_children(parent_color, bags_dict):
    return len(bags_dict[parent_color.color])


def find_shiny_bags(color, bags_dict, qty=1):
    if len(bags_dict[color]) == 0:
        # print(color, 1, "(no inside bags)")
        return 1
    else:
        total = 1
        for child in bags_dict[color]:
            total += child.qty * find_shiny_bags(child.color, bags_dict, child.qty)
            # print(color, child.qty * find_shiny_bags(child.color, bags_dict), total)
        return total
    

def replace_inside_bags(bag_color, bags):
    if not bags[bag_color]:
        return
    new_inside_bags = []
    for inside_bag in bags[bag_color]:
        color = inside_bag['color']
        if bags[color]:
            bags[color] = replace_inside_bags(color, bags)
        x = 1
        
            


if __name__ == "__main__":
    filename = './example.txt'
    filename = './example2.txt'
    filename = './input.txt'
    bag_data = parse_data(filename)
    bags = make_bags(bag_data)
    bags_dict = make_bags_dict(bags)
    part_1(bags_dict)
    part_2(bags_dict)

