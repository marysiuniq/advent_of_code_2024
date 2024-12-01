# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 05:47:59 2024

@author: Marysia

Puzzle 1 from https://adventofcode.com/2023/day/1
"""
import pytest

import solution

with open('input.txt', 'r', encoding="utf-8") as file:
    DATA = file.read()
    
with open('sample.txt', 'r', encoding="utf-8") as file:
    SAMPLE = file.read()

@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        (SAMPLE, 11),
        (DATA, 3569916),
    ],
) 
def test_part_one(input_str, expected):
    assert solution.solve_part_one(input_str) == expected

@pytest.mark.parametrize(
    ("input_str", "expected"),
    [
        (SAMPLE, 31),
        (DATA, 26407426),
    ],
)
def test_part_two(input_str, expected):
    assert solution.solve_part_two(input_str) == expected