"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/equality-in-a-array/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def equalizeArray(arr):
    counter = Counter(arr)
    maxx = max(counter.values())
    return len(arr) - maxx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')
    fptr.close()
