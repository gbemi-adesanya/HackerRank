"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/closest-numbers/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def closestNumbers(arr):
    result = list()
    n = len(arr)
    arr.sort()
    minn = math.inf
  
    for i in range(1, n):
        current = arr[i] - arr[i - 1]
      
        if current < minn:
            minn = current
            result = [arr[i - 1], arr[i]]
          
        elif current == minn:  # more than one pair with the same difference
            result.extend([arr[i - 1], arr[i]])
        
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
