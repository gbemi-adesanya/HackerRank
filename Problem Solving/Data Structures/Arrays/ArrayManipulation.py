"""
Language: Python
Difficulty: hard
Problem: https://www.hackerrank.com/challenges/crush/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def arrayManipulation(n, queries):
    result = [0] * (n + 1)
    for a, b, k in queries:
        result[a - 1] += k
        if b < n:
            result[b] -= k
      
    maxx = 0
    current = 0
    for value in result:
        current += value
        if current > maxx:
            maxx = current

    return maxx


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')
    fptr.close()
