"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/caesar-cipher-1/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def caesarCipher(s, k):
    new = ""
    k %= 26
  
    for i in s:
        if not i.isalpha():
            new += i
        else:
            x = ord(i) + k
            if i.isupper():
                if x > ord("Z"): x -= 26
            else:
                if x > ord("z"): x -= 26
            new += chr(x)

    return new
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    s = input()
    k = int(input().strip())
    result = caesarCipher(s, k)

    fptr.write(result + '\n')
    fptr.close()
