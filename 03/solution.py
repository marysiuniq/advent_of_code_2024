# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 06:03:59 2024

@author: mariapasz

Puzzle 1 from https://adventofcode.com/2024/day/3
"""

def solve_part_one(in_string):
    result = 0
    ind_start = in_string.find('mul(')
    new_str = in_string[ind_start:]
    while ('(' in new_str) and (')' in new_str) and (',' in new_str):
        ind_coma = new_str.find(',')
        ind_end = new_str.find(')')
        num_one = new_str[4:ind_coma]
        num_two = new_str[ind_coma+1:ind_end]
        if num_one.isdigit() and num_two.isdigit():
            result += int(num_one)*int(num_two)
            ind_start = new_str[ind_end+1:].find('mul(')
            new_str = new_str[ind_end+1+ind_start:]
        else:
            ind_start = new_str[5:].find('mul(')
            new_str = new_str[5+ind_start:]
    return result

def solve_part_two(in_string):
    pass

with open('input.txt', 'r', encoding="utf-8") as file:
    DATA = file.read()

if __name__ == "__main__":   
    print(solve_part_one(DATA))
    #print(solve_part_two(DATA))
