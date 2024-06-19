"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/quicksort1/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def quickSort(arr):
    p = arr[0]
    right, left, equal = list(), list(), list()
    for i in arr:
        if i < p:
            left.append(i)
        elif i == p:
            equal.append(i)
        else:
            right.append(i)
            
    left.extend(equal)
    left.extend(right)
    return left


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
