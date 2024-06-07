"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/two-characters/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations


def check(s):
    for i in range(len(s) - 1):
        if s[i] == s[i+1]: return False
    return True


def alternate(s):
    str_set = set(s)
    variants = combinations(str_set, 2)
    maxx = 0
    
    for combination in variants:
        t = [char for char in s if (char == combination[0]) or (char == combination[1])]
        if check(t):
            maxx = max(maxx, len(t))
        
    return maxx


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())
    s = input()
    result = alternate(s)

    fptr.write(str(result) + '\n')
    fptr.close()
