"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/sherlock-and-squares/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def squares(a, b):
    # Write your code here
    a = math.ceil(math.sqrt(a))
    b = math.floor(math.sqrt(b))
    
    array = [i**2 for i in range(a, b+1)]
    return len(array)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        a = int(first_multiple_input[0])
        b = int(first_multiple_input[1])
        result = squares(a, b)

        fptr.write(str(result) + '\n')
    fptr.close()
