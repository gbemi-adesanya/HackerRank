"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def jumpingOnClouds(c, k):
    energy = 100
    n = len(c) if len(c) % k == 0 else k * len(c)
    
    for i in range(0, n, k):
        if c[i % len(c)] == 1:
            energy -= 3
        else:
            energy -= 1
            
    return energy
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')
    fptr.close()
