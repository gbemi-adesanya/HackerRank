"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/lilys-homework/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def swaps(arr):
    n = len(arr)
    sorted_positions = sorted(range(n), key=lambda x: arr[x])
    visited = [False] * n
    swaps = 0
    
    for i in range(n):
        if visited[i] or sorted_positions[i] == i:
            continue
        cycle_size = 0
        x = i
        
        while not visited[x]:
            visited[x] = True
            x = sorted_positions[x]
            cycle_size += 1
        if cycle_size > 0:
            swaps += cycle_size - 1
            
    return swaps
    
    
def lilysHomework(arr):
    return min(swaps(arr), swaps(arr[::-1]))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')
    fptr.close()
