"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/permutation-equation/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def permutationEquation(p):       
    y = [p.index(p.index(i) + 1) + 1 for i in range(1, len(p) + 1)]
    return y


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    p = list(map(int, input().rstrip().split()))
    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
