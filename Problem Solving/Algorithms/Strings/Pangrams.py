"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/pangrams/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import string


def pangrams(s):
    if len(s) < 26:
        return "not pangram"
    
    alphabet = string.ascii_lowercase
    return "pangram" if all(i in s.lower() for i in alphabet) else "not pangram"
      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = pangrams(s)

    fptr.write(result + '\n')
    fptr.close()
