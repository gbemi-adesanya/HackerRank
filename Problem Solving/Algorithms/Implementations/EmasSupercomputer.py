"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/two-pluses/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import itertools


def twoPluses(grid):
    def isGood(row, col, step):
        if row - step < 0 or row + step >= height or col - step < 0 or col + step >= width:
            return False
        for d in range(step + 1):
            if grid[row + d][col] != 'G' or grid[row - d][col] != 'G' or grid[row][col + d] != 'G' or grid[row][col - d] != 'G':
                return False
        return True

    height, width = len(grid), len(grid[0])
    pluses = []

    for row in range(height):
        for col in range(width):
            step = 0
            while isGood(row, col, step):
                size = 4 * step + 1
              
                coordinates = {(row, col)}
                coordinates |= {(row + d, col) for d in range(1, step + 1)}
                coordinates |= {(row - d, col) for d in range(1, step + 1)}
                coordinates |= {(row, col + d) for d in range(1, step + 1)}
                coordinates |= {(row, col - d) for d in range(1, step + 1)}
                pluses.append((size, coordinates))
                step += 1

    if not pluses:
        return 0
    if len(pluses) == 1:
        return pluses[0][0]

    max_product = 0
    for (size1, coords1), (size2, coords2) in itertools.combinations(pluses, 2):
        if coords1.isdisjoint(coords2):
            max_product = max(max_product, size1 * size2)

    return max_product

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')
    fptr.close()
