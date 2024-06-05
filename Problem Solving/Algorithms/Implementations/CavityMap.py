"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/cavity-map/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

    
def cavityMap(grid):
    # Write your code here
    n = len(grid)
    grid = [list(row) for row in grid]

    for i in range(1, n-1):
        for j in range(1, n-1):
            cell = grid[i][j]
            top, bottom, left, right = grid[i-1][j], grid[i+1][j], grid[i][j-1], grid[i][j+1]
            if cell > max([top, bottom, left, right]):
                grid[i][j] = "X"

    grid = ["".join(row) for row in grid]
    return grid
      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()
