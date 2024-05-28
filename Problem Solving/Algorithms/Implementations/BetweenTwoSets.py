"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/between-two-sets/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def getTotalX(a, b):
    array = [i for i in range(max(a), min(b) + 1)]
    filtered = [i for i in array if all(i % j == 0 for j in a)]
    final = [i for i in filtered if all(j % i == 0 for j in b)]
    
    return len(final)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')
    fptr.close()
