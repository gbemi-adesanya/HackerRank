"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/capitalize/problem
"""

import math
import os
import random
import re
import sys


def solve(name):
    name_list = list(name)
    for i in range(len((name_list))):
        if i == 0 or name[i - 1] == " ":
            # i == 0 means it's the first letter of the first word
            # name[i - 1] == " " means the character before is a space
            name_list[i] = name_list[i].upper()
    capitalized = "".join(name_list)
    return capitalized

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
