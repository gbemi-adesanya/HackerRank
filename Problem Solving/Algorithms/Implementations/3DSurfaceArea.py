"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/3d-surface-area/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def surfaceArea(A):
    area = 2 * H * W
    for i in range(H):
        for j in range(W):
            area += A[i][j] if i == 0 else max(0, A[i][j] - A[i-1][j])
            area += A[i][j] if j == 0 else max(0, A[i][j] - A[i][j-1])
            area += A[i][j] if i == H - 1 else max(0, A[i][j] - A[i+1][j])
            area += A[i][j] if j == W - 1 else max(0, A[i][j] - A[i][j+1])
                
    return area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    H = int(first_multiple_input[0])
    W = int(first_multiple_input[1])
    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))
    result = surfaceArea(A)

    fptr.write(str(result) + '\n')
    fptr.close()
