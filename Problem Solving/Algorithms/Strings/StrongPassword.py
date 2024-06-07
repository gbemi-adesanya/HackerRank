"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/strong-password/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def minimumNumber(n, password):
    minimum = 0
    special = "!@#$%^&*()-+"
  
    if not any(char.isdecimal() for char in password): minimum += 1
    if not any(char.islower() for char in password): minimum += 1
    if not any(char.isupper() for char in password): minimum += 1
    if not any(char in special for char in password): minimum += 1
    if n + minimum < 6: minimum += 6 - (n + minimum)
    
    return minimum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    password = input()
    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')
    fptr.close()
