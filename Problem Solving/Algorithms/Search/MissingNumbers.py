"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/missing-numbers/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def missingNumbers(arr, brr):
    a, b = Counter(arr), Counter(brr)
    missing = set()
    
    for num in b.keys():
        if b[num] > a[num]:
            missing.add(num)
    
    return sorted(missing)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())
    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
