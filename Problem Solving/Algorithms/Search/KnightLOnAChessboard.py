"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/knightl-on-chessboard/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


def bfs(n, a, b):
    directions = [(a,b), (a,-b), (-a,b), (-a,-b), (b,a), (b,-a), (-b,a), (-b,-a)]
    q = deque([(0,0)])
    visited = set([(0,0)])
    level = 0

    while q:
        size = len(q)

        for _ in range(size):
            i, j = q.popleft()
            if i == n - 1 and j == n - 1:
                return level
            
            for x, y in directions:
                ii, jj = i + x, j + y
                if 0 <= ii < n and 0 <= jj < n and (ii, jj) not in visited:
                    visited.add((ii, jj))
                    q.append((ii, jj))
                    
        level += 1
    
    return -1


def knightlOnAChessboard(n):
    result = [[0]* (n - 1) for _ in range(n - 1)]
    
    for i in range(1, n):
        for j in range(1, n):
            if result[j - 1][i - 1] == 0:
                r = bfs(n, i, j)
                result[i - 1][j - 1] = r
                result[j - 1][i - 1] = r

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')
    fptr.close()
