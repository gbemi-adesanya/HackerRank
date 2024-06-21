"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/gridland-metro/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


def gridlandMetro(n, m, k, track):
    empty = n * m
    if k == 0: return empty
    
    tdict = defaultdict(list)
    
    for r, c1, c2 in track:
        if r not in tdict:
            tdict[r].extend([c1, c2])
          
        else:
            start, end = tdict[r][0], tdict[r][1]
            tdict[r][1] = tdict[r][1] + c2 - c1 + 1 if c1 > end else max(c2, end)
            tdict[r][0] = tdict[r][0] - (c2 - c1 + 1) if c2 < start else min(c1, start)
            
    for start, end in tdict.values():
        empty -= end - start + 1
            
    return empty
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')
    fptr.close()
