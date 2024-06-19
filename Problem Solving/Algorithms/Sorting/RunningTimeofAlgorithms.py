"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/runningtime/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def runningTime(arr):
    shifts = 0
    for i in range(1, len(arr)):
        j = i - 1
        current = arr[i]
        while j >= 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            shifts += 1
        arr[j + 1] = current
        
    return shifts
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = runningTime(arr)

    fptr.write(str(result) + '\n')
    fptr.close()
