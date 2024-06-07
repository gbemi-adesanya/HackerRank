"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/gem-stones/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def gemstones(arr):
    minerals = [set(rock) for rock in arr]
    gems = set.intersection(*minerals)
  
    return len(gems)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')
    fptr.close()
