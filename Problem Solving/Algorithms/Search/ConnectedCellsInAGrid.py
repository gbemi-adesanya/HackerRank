"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def dfs(i, j):
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    matrix[i][j] = 2
    area = 1
    for u, v in directions:
        x, y = i + u, j + v
        if 0 <= x < n and 0 <= y < m and matrix[x][y] == 1:
            area += dfs(x, y)
    return area


def connectedCell(matrix):
    count = 0
    n, m = len(matrix), len(matrix[0])
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                count = max(count, dfs(i, j))
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')
    fptr.close()
