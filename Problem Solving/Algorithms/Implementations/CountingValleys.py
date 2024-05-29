"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/counting-valleys/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    # Write your code here
    sea_level, count = 0, 0
    for i in range(steps):
        if path[i] == "U":
            sea_level += 1
            if sea_level == 0: count += 1
        else:
            sea_level -= 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')
    fptr.close()
