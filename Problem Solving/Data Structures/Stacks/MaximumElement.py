"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/maximum-element/problem?isFullScreen=true
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def getMax(operations):
    stack, maxx, result = list(), list(), list()
    # The maximum is always the last thing in maxx
    
    for op in operations:
        op = list(map(int, op.split()))
          
        if op[0] == 1:
            value = op[1]
            stack.append(value)
            if not maxx or value >= maxx[-1]:  # first item or new maximum
                maxx.append(value)
                
        elif op[0] == 2:
            popped = stack.pop()
            if maxx and popped == maxx[-1]:  # current maximum is removed from stack
                maxx.pop()
        else:
            if maxx:
                result.append(maxx[-1])
            
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
