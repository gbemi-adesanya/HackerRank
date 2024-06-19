"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/insertionsort1/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def insertionSort1(n, arr):
    item = arr[n-1]
    i = n - 2
  
    while i > -1 and arr[i] > item:
        arr[i + 1] = arr[i]
        i -= 1
        print(" ".join(map(str, arr)))
      
    else:
        arr[i + 1] = item
        print(" ".join(map(str, arr)))
        

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)
