"""
Language: Python
Difficulty: hard
Problem: https://www.hackerrank.com/challenges/maximum-subarray-sum/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import bisect


def maximumSum(a, m):
    prefix_sums = []
    prefix_sum = 0
    max_sum = 0
    
    for num in a:
        prefix_sum = (prefix_sum + num) % m
        max_sum = max(max_sum, prefix_sum)
        
        i = bisect.bisect_right(prefix_sums, prefix_sum)
        
        if i < len(prefix_sums):
            max_sum = max(max_sum, (prefix_sum - prefix_sums[i] + m) % m)
            
        bisect.insort(prefix_sums, prefix_sum)
        
    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))
        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')
    fptr.close()
