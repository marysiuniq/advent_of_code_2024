# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 06:10:05 2024

@author: mariapasz

Puzzle 1 from https://adventofcode.com/2024/day/2
"""
import collections
import numpy as np

def solve_part_one(in_string):
    reports_list = parse_input(in_string)
    return count_safe_reports(reports_list)
    
def count_safe_reports(in_list):
    count_safe = 0
    for report in in_list:
        levels = [int(_) for _ in report]
        if check_if_safe(levels):
            count_safe += 1
    return count_safe

def check_if_safe(in_levels):
    differences = [in_levels[_+1]-in_levels[_] for _ in range(len(in_levels)-1)]
    if all(0<_<4 for _ in differences) or all(-4<_<0 for _ in differences):
        return True
    else:
        return False
    
def parse_input(in_string):
    check = in_string.splitlines()
    return [_.split() for _ in check]

with open('input.txt', 'r', encoding="utf-8") as file:
    DATA = file.read()

if __name__ == "__main__":
    print(solve_part_one(DATA))
    #print(solve_part_two(DATA))