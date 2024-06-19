"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/bear-and-steady-gene/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def steadyGene(gene):
    n = len(gene)
    each = n // 4

    initial = Counter(gene)
    if all(count == each for count in initial.values()): return 0

    minn, left = n, 0
    for right in range(n):
        initial[gene[right]] -= 1

        while all(count <= each for count in initial.values()):
            minn = min(minn, right - left + 1)
            initial[gene[left]] += 1
            left += 1

    return minn
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    gene = input(

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')
    fptr.close()
