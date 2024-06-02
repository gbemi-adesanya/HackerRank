"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def jumpingOnClouds(c):
    n = len(c)
    current = count = 0
    while current < n-1:
        current += 2 if ((current + 2 < n) and (c[current + 2] == 0 )) else 1
        count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')
    fptr.close()
