"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/find-digits/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def findDigits(n):
    count = 0
    for i in str(n):
        i = int(i)
        if i != 0 and n % i == 0:
            count += 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        result = findDigits(n)

        fptr.write(str(result) + '\n')
    fptr.close()