"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/big-sorting/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def bigSorting(unsorted):
    unsorted.sort(key=lambda x: (len(x), x))
    return unsorted


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()
