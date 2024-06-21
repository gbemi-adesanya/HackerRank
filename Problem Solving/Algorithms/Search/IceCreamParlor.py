"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/icecream-parlor/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def icecreamParlor(m, arr):
    one, two = -1, -1
    for i in arr:
        one = arr.index(i) + 1
        arr[one - 1] = None
      
        try:
            two = arr.index(m - i) + 1
            break
          
        except ValueError:
            continue
    
    return [one, two]
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())
        n = int(input().strip())
      
        arr = list(map(int, input().rstrip().split()))
        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
    fptr.close()
