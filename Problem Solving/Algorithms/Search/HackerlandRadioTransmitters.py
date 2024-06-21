"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def hackerlandRadioTransmitters(x, k):
    x.sort()
    n = len(x)
    count = 0
    i = 0

    while i < n:
        count += 1
        loc = x[i] + k
        
        while i < n and x[i] <= loc:
            i += 1
        
        loc = x[i - 1] + k
        
        while i < n and x[i] <= loc:
            i += 1

    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
  
    x = list(map(int, input().rstrip().split()))
    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')
    fptr.close()
