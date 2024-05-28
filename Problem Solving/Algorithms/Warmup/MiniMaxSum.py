"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/mini-max-sum/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    minimum = sum(arr) - max(arr)
    maximum = sum(arr) - min(arr)
    print(minimum, maximum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
