"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/service-lane/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def serviceLane(n, cases):
    result = list()
    for i in cases:
        sub = list()
        for j in range(i[0], i[1]+1):
            sub.append(width[j])
        result.append(min(sub))
        
    return result
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))
    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
