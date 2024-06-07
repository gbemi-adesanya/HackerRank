"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/weighted-uniform-string/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import string

    
def weightedUniformStrings(s, queries):
    n = len(s)
    weights = set()

    i = 0
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            weight = (ord(s[i]) - ord('a') + 1) * (j - i + 1)
            weights.add(weight)
            j += 1
        i = j

    result = ["Yes" if i in weights else "No" for i in queries]
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    queries_count = int(input().strip())
    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()
