"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/dynamic-array/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    answers = list()
    lastAnswer = 0
    
    for qtype, x, y in queries:
        idx = ((x ^ lastAnswer) % n)
      
        if qtype == 1:
            arr[idx].append(y)
          
        else:
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)
            
    return answers


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
