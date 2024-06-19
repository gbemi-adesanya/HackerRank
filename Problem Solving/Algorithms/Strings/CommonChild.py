"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/common-child/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def commonChild(s1, s2):
    result = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
    
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                result[i][j] = result[i - 1][j - 1] + 1
            else:
                result[i][j] = max(result[i - 1][j], result[i][j - 1])
                
    return result[-1][-1]
                
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()
    s2 = input()
    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')
    fptr.close()
