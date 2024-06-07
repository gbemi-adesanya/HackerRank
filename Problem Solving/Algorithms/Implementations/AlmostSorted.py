"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/almost-sorted/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def almostSorted(arr):
    if arr == sorted(arr):
        print("yes")
        return
    
    i, j = 0, len(arr) - 1
    while i < len(arr) - 1 and arr[i] < arr[i + 1]:
        i += 1
    while j > 0 and arr[j - 1] < arr[j]:
        j -= 1
        
    arr[i], arr[j] = arr[j], arr[i]
    if arr == sorted(arr):
        print("yes")
        print("swap {} {}".format(i+1, j+1))
        return
        
    l, r = i+1, j-1

    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    if arr == sorted(arr):
        print("yes")
        print("reverse {} {}".format(i+1, j+1))
        return

    print("no")
        

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    almostSorted(arr)
