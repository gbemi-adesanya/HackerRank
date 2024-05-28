"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/diagonal-difference/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    positive, negative = 0, 0
    for i in range(len(arr)):
        negative += arr[i][i]
        positive += arr[i][len(arr) - i - 1]
            
    return abs(positive - negative)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')
    fptr.close()
