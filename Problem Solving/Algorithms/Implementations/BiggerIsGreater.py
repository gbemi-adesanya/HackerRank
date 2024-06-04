"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/bigger-is-greater/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def biggerIsGreater(w):
    array = list(w)
    index = len(w) - 1
    
    while index > 0 and array[index - 1] >= array[index]:
        index -= 1
    if index <= 0:
        return "no answer"

    new = len(w) - 1
    while array[new] <= array[index - 1]:
        new -= 1
    array[index - 1], array[new] = array[new], array[index - 1]

    array[index:] = array[len(array) - 1 : index - 1 : -1]
    return "".join(array)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())
    for T_itr in range(T):
        w = input()
        result = biggerIsGreater(w)

        fptr.write(result + '\n')
    fptr.close()
