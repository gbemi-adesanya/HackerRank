"""
Language: Python
Difficulty: 
Problem: https://www.hackerrank.com/challenges/game-of-two-stacks/problem?isFullScreen=true
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def twoStacks(maxSum, a, b):
    summ = count = i = j = 0
    
    # Take elements from the first stack while the sum does not exceed x
    while i < len(a) and summ + a[i] <= maxSum:
        summ += a[i]
        i += 1
    count = i
    
    # Adjust by replacing elements from stack A with elements from stack B
    while j < len(b) and i >= 0:
        summ += b[j]
        j += 1
        
        # If the sum exceeds x, remove the top element from stack A
        while summ > maxSum and i > 0:
            i -= 1
            summ -= a[i]
        
        # Update the maximum count
        if summ <= maxSum and count < i + j:
            count = i + j
            
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))
        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')
    fptr.close()
