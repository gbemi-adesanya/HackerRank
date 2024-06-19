"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/countingsort2/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def countingSort(arr):
    result = [0] * (max(arr) + 1)
    for i in arr:
        result[i] += 1
    
    x = list()
    for i in range(len(result)):
        x.extend([str(i)] * result[i])
        
    return x


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
