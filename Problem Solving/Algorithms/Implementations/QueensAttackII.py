"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/queens-attack-2/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def queensAttack(n, k, r_q, c_q, obstacles):
    if n == 1: return 0

    moves = [
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0),  # Up
        (-1, 0),  # Down
        (1, -1),  # Upper-left diagonal
        (1, 1),  # Upper-right diagonal
        (-1, -1),  # Lower-left diagonal
        (-1, 1)  # Lower-right diagonal
    ]
  
    obstacles = set(tuple(obstacle) for obstacle in obstacles)
    squares = 0
    for row, col in moves:
        next_row, next_col = r_q + row, c_q + col
        while 1 <= next_row <= n and 1 <= next_col <= n and (next_row, next_col) not in obstacles:
            next_row += row
            next_col += col
            squares += 1

    return squares
      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()
    r_q = int(second_multiple_input[0])
    c_q = int(second_multiple_input[1])
    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')
    fptr.close()
