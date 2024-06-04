"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/flatland-space-stations/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def flatlandSpaceStations(n, c):
    c.sort()
    maxx = c[0]
    
    for i in range(1, len(c)):
        maxx = max(maxx, (c[i] - c[i-1])//2)
        
    maxx = max(maxx, n - 1 - c[-1])
    return maxx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
  
    c = list(map(int, input().rstrip().split()))
    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')
    fptr.close()
