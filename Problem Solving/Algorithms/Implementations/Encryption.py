"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/encryption/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def encryption(s):
    for _ in range(s.count(" ")):
        s = s.replace(" ", "")

    l = len(s)
    root = math.sqrt(l)
    rows, columns = math.floor(root), math.ceil(root)
    if rows * columns < l: rows += 1

    string = ""
    for i in range(columns):
        for j in range(rows):
            string += s[i] if i < l else ""
            i += columns
        string += " "

    return string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = encryption(s)

    fptr.write(result + '\n')
    fptr.close()
