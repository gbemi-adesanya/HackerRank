"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/kaprekar-numbers/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def kaprekarNumbers(p, q):
    result = list()
    for i in range(p, q+1):
        square = str(i**2)
        l = len(square)//2
        if l != 0:
            left, right = square[:l], square[l:]
            if int(left) + int(right) == i:
                result.append(str(i))
        else:
            if square == str(i):
                result.append(str(i))

    if len(result) != 0:
        print(" ".join(result))
    else:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input().strip())
    q = int(input().strip())
    kaprekarNumbers(p, q)
