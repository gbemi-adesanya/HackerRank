"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/utopian-tree/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def utopianTree(n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        h = utopianTree(n-1) + 1
    else:
        h = utopianTree(n-1) * 2
    
    return h
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        result = utopianTree(n)

        fptr.write(str(result) + '\n')
    fptr.close()
