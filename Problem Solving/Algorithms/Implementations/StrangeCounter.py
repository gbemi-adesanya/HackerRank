"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/strange-code/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def strangeCounter(t):
    value = 3
    while t > value:
        t -= value
        value *= 2
        
    return value - t + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    result = strangeCounter(t)

    fptr.write(str(result) + '\n')
    fptr.close()
