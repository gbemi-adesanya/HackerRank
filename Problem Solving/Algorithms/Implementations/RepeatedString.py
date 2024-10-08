"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/repeated-string/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def repeatedString(s, n):
    return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    n = int(input().strip())
    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')
    fptr.close()
