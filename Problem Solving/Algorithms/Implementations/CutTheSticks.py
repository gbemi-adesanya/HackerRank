"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/cut-the-sticks/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def cutTheSticks(arr):
    result = list()
    while len(arr) > 1:
        result.append(len(arr))
        minn = min(arr)
        arr = [i - minn for i in arr if i > minn]
        
        if len(set(arr)) == 1:
            result.append(len(arr))
            break
            
    return result
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
