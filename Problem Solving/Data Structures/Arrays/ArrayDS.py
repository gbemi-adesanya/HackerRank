"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/arrays-ds/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def reverseArray(a):
    a.reverse()
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')
    fptr.close()
