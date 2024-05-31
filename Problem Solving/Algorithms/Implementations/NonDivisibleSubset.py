"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/non-divisible-subset/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

    
def nonDivisibleSubset(k, s):
    x = [0 for _ in range(k)]
    for element in s:
        x[element % k] += 1
        
    result = min(1, x[0])
    x = x[1:]
    for i in range(len(x)//2):
        result += max(x[i], x[-(i+1)])
    if len(x) % 2 == 1:
        result += min(1, x[len(x) // 2])
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')
    fptr.close()
