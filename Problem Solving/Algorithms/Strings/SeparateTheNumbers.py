"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/separate-the-numbers/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def separateNumbers(s):
    if len(s) == 1 or s[0] == "0":
        print("NO")
        return
        
    for i in range(1, len(s)//2 + 1):
        x = s[:i]
        prev = int(x)
        
        while len(x) < len(s):
            nextt = prev+1
            x += str(nextt)
            prev = nextt
        
        if x == s:
            print("YES", s[:i])
            return
    
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        separateNumbers(s)
