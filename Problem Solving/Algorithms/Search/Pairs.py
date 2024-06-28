"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/pairs/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def pairs(k, arr):
    count = 0
    elements = set(arr)
    
    for num in arr:
        if num + k in elements:
            count += 1
        if num - k in elements:
            count += 1
        elements.remove(num)
                
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
  
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)

    fptr.write(str(result) + '\n')
    fptr.close()
