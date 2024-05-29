"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/sock-merchant/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    count = 0
    while len(ar) > 1:
        element = ar[0]
        if ar.count(element) > 1:
            ar.remove(element)
            ar.remove(element)
            count += 1
        else:
            ar.remove(element)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')
    fptr.close()
