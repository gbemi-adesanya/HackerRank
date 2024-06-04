"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem
"""


#!/bin/python3

import math
import os
import random
import re
import sys


def organizingContainers(container):
    # Write your code here
    types = [0] * len(container)
    containers = [sum(i) for i in container]
    
    for i in container:
        for j in range(len(i)):
            types[j] += i[j]
            
    types.sort()
    containers.sort()     

    return "Possible" if types == containers else "Impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')
    fptr.close()
