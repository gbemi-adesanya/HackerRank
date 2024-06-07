"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def hackerrankInString(s):
    ideal = list("hackerrank")
    i = 0
  
    for char in s:
        if i == len(ideal):
            break
        if char == ideal[i]:
            i += 1
            
    return "YES" if i == len(ideal) else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = hackerrankInString(s)

        fptr.write(result + '\n')
    fptr.close()
