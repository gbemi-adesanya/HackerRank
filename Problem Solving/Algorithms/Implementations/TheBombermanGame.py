"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/bomber-man/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def new(r, c, grid):
    x = [["O"]*c for _ in range(r)]
    
    for row in range(r):
        for col in range(c):
            if grid[row][col] == "O":
                x[row][col] = "."
                if row - 1 >= 0: x[row - 1][col] = "."
                if row + 1 <= r - 1: x[row + 1][col] = "."
                if col - 1 >= 0: x[row][col - 1] = "."
                if col + 1 <= c - 1: x[row][col + 1] = "."

    return x

def bomberMan(n, grid):
    first = new(r, c, grid)
    if n % 2 == 0:
        result = [["O"]*c for _ in range(r)]
    elif n < 4:
        result = grid if n == 1 else first
    else:
        second = new(r, c, first)
        third = new(r, c, second)
        result = second if n % 4 == 1 else third
    
    return ["".join(row) for row in result]

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    r = int(first_multiple_input[0])
    c = int(first_multiple_input[1])
    n = int(first_multiple_input[2])

    grid = []
    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()
