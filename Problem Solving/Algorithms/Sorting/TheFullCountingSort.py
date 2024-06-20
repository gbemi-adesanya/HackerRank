"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/countingsort4/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def countSort(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i][1] = "-"

    arr.sort(key=lambda x: int(x[0]))
    print(" ".join(sub[1] for sub in arr))


if __name__ == '__main__':
    n = int(input().strip())

    arr = []
    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
