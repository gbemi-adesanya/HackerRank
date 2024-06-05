"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/manasa-and-stones/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def stones(n, a, b):
    return sorted(set([(n - 1) * min(a, b) + x * abs(a - b) for x in range(n)]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())
    for T_itr in range(T):
        n = int(input().strip())
        a = int(input().strip())
        b = int(input().strip())
        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
    fptr.close()
