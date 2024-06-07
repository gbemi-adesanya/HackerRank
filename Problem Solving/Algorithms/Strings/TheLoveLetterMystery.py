"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/the-love-letter-mystery/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def theLoveLetterMystery(s):
    count = 0
    for i in range(len(s) // 2):
        if s[-1 - i] != s[i]:
            count += abs(ord(s[-1-i]) - ord(s[i]))
    
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')
    fptr.close()
