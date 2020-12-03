"""
Advent of code
Day 1
"""

from itertools import combinations
from math import prod # must have python 3.8 installed


def find_solution(expenses, qty_to_sum):
    for combo in combinations(expenses, qty_to_sum):
        if sum(combo) == 2020:
            return prod(combo)

def get_expenses(path):
    text = open(path)
    expenses = [int(expense) for expense in text.read().splitlines()]
    return expenses

if __name__ == "__main__":
    path = './input.txt'
    expenses = get_expenses(path)
    print('Part 1:', find_solution(expenses, 2))
    print('Part 2:', find_solution(expenses, 3))