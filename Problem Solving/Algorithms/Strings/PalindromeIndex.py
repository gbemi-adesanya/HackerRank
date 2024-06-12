"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/palindrome-index/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def check(s, start, end):
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


def palindromeIndex(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
          
            if check(s, left + 1, right):
                return left
            if check(s, left, right - 1):
                return right
              
            return -1
        left += 1
        right -= 1
    
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')
    fptr.close()
