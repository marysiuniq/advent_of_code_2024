# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 05:47:59 2024

@author: Marysia

Puzzle 1 from https://adventofcode.com/2023/day/1
"""
import collections

def solve_part_one(in_string):
    left_list, right_list = parse_input(in_string)
    return sum(abs(a-b) for a, b in zip(sorted(left_list), sorted(right_list)))

def solve_part_two(in_string):
    left_list, right_list = parse_input(in_string)
    appearance_count = collections.Counter(right_list)
    return sum(_*appearance_count[_] for _ in left_list)

def _create_lists(in_list):
    left_list = [int(_[0]) for _ in in_list]
    right_list = [int(_[1]) for _ in in_list]
    return left_list, right_list
    

def parse_input(in_string):
    check = in_string.splitlines()
    return _create_lists([_.split() for _ in check])

with open('input.txt', 'r', encoding="utf-8") as file:
    DATA = file.read()

if __name__ == "__main__":
    print(solve_part_one(DATA))
    print(solve_part_two(DATA))