"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/find-the-median/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def findMedian(arr):
    arr.sort()
    n = len(arr)//2
    return arr[n]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    result = findMedian(arr)

    fptr.write(str(result) + '\n')
    fptr.close()
