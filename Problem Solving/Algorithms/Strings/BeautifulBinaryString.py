"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/beautiful-binary-string/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def beautifulBinaryString(b):
    count = 0
    while "010" in b:
        b = b.replace("010", "111", 1)
        count += 1
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    b = input()
    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')
    fptr.close()
