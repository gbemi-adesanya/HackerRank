"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/halloween-sale/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def howManyGames(p, d, m, s):
    count = 0
    while s > 0:
        s -= p
        count += 1
        p = max(p-d, m)
        
    if s != 0:
        count -= 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    p = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    m = int(first_multiple_input[2])
    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')
    fptr.close()
