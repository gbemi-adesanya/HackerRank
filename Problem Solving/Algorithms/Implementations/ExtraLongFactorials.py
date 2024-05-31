"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/extra-long-factorials/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


def extraLongFactorials(n):
    print(factorial(n))
    

if __name__ == '__main__':
    n = int(input().strip())
    extraLongFactorials(n)
