"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/sherlock-and-array
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def balancedSums(arr):
    total, left = sum(arr), 0
    
    for num in arr:
        if left == (total - left - num):
            return "YES"
            
        left += num
    
    return "NO"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')
    fptr.close()
