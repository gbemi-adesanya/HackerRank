"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/plus-minus/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    n = len(arr)
    negative, positive, zero = 0, 0, 0
  
    for i in arr:
        if i < 0:
            negative += 1
        elif i > 0:
            positive += 1
        else:
            zero += 1
          
    print("{:.6f}\n{:.6f}\n{:.6f}".format(positive/n, negative/n, zero/n))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
