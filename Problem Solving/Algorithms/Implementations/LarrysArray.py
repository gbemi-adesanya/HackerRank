"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/larrys-array/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def larrysArray(A):
    x = sum([sum([1 if A[i] > A[j] else 0 for j in range(i+1, len(A))]) for i in range(len(A))])
    return "YES" if x % 2 == 0 else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        A = list(map(int, input().rstrip().split()))
        result = larrysArray(A)

        fptr.write(result + '\n')
    fptr.close()
