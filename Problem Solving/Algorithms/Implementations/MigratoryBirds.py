"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/migratory-birds/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import collections

def migratoryBirds(arr):
    freq = collections.defaultdict(int)
    for i in arr:
        freq[i] += 1
       
    max_freq = max(freq.values())
    max_id = min([key for key, value in freq.items() if value == max_freq])
    
    return max_id

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')
    fptr.close()
