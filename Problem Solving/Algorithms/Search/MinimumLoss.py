"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/minimum-loss/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def minimumLoss(price):
    n = len(price)
    minn = math.inf

    p_index = [[price[i], i] for i in range(n)]
    p_index.sort()
    
    for i in range(1, n):
        if p_index[i][1] < p_index[i - 1][1]:
            loss = p_index[i][0] - p_index[i - 1][0]
            if loss < minn:
                minn = loss
                
    return minn


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))
    result = minimumLoss(price)

    fptr.write(str(result) + '\n')
    fptr.close()
