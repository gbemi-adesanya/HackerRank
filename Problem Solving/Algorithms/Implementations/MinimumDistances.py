"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/minimum-distances/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import collections


def minimumDistances(a):
    x = collections.Counter(a)
    check = False
    for i in x.values():
        if i == 1:
            check = True
        else:
            check = False
            break
    
    if check: return -1
    
    minn = list()
    for element, count in x.items():
        if count % 2 == 0:
            i = a.index(element)
            a[i] = -1
            j = a.index(element)
            a[j] = -1
            minn.append(abs(i-j))
    
    return min(minn)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = minimumDistances(a)

    fptr.write(str(result) + '\n')
    fptr.close()
