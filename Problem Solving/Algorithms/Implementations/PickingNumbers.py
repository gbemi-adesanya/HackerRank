"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/picking-numbers/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import collections

def pickingNumbers(a):
    count = collections.Counter(a)
    maxx = 0
    for i in range(1, 100):
        maxx = max(maxx, count[i] + count[i+1])
        
    return maxx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')
    fptr.close()
