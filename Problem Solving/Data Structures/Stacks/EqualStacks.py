"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/equal-stacks/problem?isFullScreen=true
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def equalStacks(h1, h2, h3):
    sum1, sum2, sum3 = sum(h1), sum(h2), sum(h3)
    t1 = t2 = t3 = 0
    
    while 1:
        if sum1 == sum2 and sum2 == sum3: # already equal
            return sum1
            
        if t1 == n1 or t2 == n2 or t3 == n3: # a stack is empty
            return 0
        
        # Pop from the highest stack
        if sum1 >= sum2 and sum1 >= sum3:
            sum1 -= h1[t1]
            t1 += 1
            
        elif sum2 >= sum1 and sum2 >= sum3:
            sum2 -= h2[t2]
            t2 += 1
            
        elif sum3 >= sum1 and sum3 >= sum2:
            sum3 -= h3[t3]
            t3 += 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])
    n2 = int(first_multiple_input[1])
    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))
    h2 = list(map(int, input().rstrip().split()))
    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')
    fptr.close()
