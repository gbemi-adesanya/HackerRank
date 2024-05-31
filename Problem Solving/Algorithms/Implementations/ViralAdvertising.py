"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/strange-advertising/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def viralAdvertising(n):
    total = 0
    current = 5
    for i in range(1, n+1):
        add = math.floor(current/2)
        total += add
        current = add * 3
        
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')
    fptr.close()
