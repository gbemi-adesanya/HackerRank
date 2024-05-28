"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def breakingRecords(scores):
    best, worst = 0, 0
    current_max, current_min = scores[0], scores[0]
  
    for i in range(1, len(scores)):
        if scores[i] > current_max:
            current_max = scores[i]
            best += 1
        elif scores[i] < current_min:
            current_min = scores[i]
            worst += 1
            
    return [best, worst]
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
