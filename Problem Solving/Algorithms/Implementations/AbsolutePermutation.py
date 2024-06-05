"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/absolute-permutation
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def absolutePermutation(n, k):
    result = list()
    switch = k
    
    if k == 0:
        return [x for x in range(1, n+1)]
        
    if n % (2*k) != 0:
        return [-1]
        
    for position in range(1, n+1):
        result.append(position + switch)
        
        if position % k == 0:
            switch *= -1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
    fptr.close()
