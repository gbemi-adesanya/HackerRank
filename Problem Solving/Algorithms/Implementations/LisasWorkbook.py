"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/lisa-workbook/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def workbook(n, k, arr):
    special = 0
    page = 1
    
    for i in range(n):
        p = math.ceil(arr[i] / k)
        for j in range(p):
            if page in [x for x in range(j*k + 1, min(arr[i]+1, (j+1) * k + 1))]:
                special += 1
            page += 1
            
    return special

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))
    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')
    fptr.close()
