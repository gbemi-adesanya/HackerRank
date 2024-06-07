"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/funny-string/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def asciis(s):
    return [abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s) - 1)]


def funnyString(s):
    s_ = s[::-1]
    return "Funny" if asciis(s) == asciis(s_) else "Not Funny"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = funnyString(s)
      
        fptr.write(result + '\n')
    fptr.close()
