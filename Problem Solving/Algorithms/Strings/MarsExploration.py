"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/mars-exploration/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def marsExploration(s):
    ideal = "SOS" * (len(s) // 3)
    count = sum(i != j for i, j in zip(s, ideal))
       
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = marsExploration(s)

    fptr.write(str(result) + '\n')
    fptr.close()
