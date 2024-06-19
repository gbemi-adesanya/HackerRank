"""
Language: Python
Difficulty: expert
Problem: https://www.hackerrank.com/challenges/morgan-and-a-string/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def morganAndString(a, b):
    string = ""
    a += "z"
    b += "z"
    
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i:] < b[j:]:
            string += a[i]
            i += 1
        else:
            string += b[j]
            j += 1
            
    return string[:-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a = input()
        b = input()
        result = morganAndString(a, b)

        fptr.write(result + '\n')
    fptr.close()
