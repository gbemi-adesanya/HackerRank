"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/append-and-delete/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def minimum_moves(s, t):
    if s == t:
        return 0

    i = 0
    similar = ""
    while i < min(len(s), len(t)) and s[i] == t[i]:
        similar += s[i]
        i += 1

    n = len(similar)
    moves = len(s) + len(t) if n == 0 else len(s[n:]) + len(t[n:])

    return moves
    
    
def appendAndDelete(s, t, k):
    moves = minimum_moves(s, t)
    
    if moves == k or (moves < k and (k - moves) % 2 == 0):
        return "Yes"
    
    if len(s) + len(t) <= k:
        return "Yes"

    return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    t = input()
    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')
    fptr.close()
