"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/happy-ladybugs/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import collections


def check(b):
    if b[0] != b[1] or b[-1] != b[-2]:
        return False
        
    for index in range(1, len(b)-1):
        if b[index] != b[index - 1] and b[index] != b[index + 1]:
            return False
        
    return True

def happyLadybugs(b):
    count_dict = collections.Counter(b)
    singles = list(filter(lambda x: x[0] != "_" and x[1] == 1, count_dict.items()))
    spaces = b.count("_")
    
    if len(singles) == 0 and spaces > 0:
        return "YES"
    if len(b) > 2 and check(b):
        return "YES"
      
    return "NO"       
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())
    for g_itr in range(g):
        n = int(input().strip())
        b = input()
        result = happyLadybugs(b)

        fptr.write(result + '\n')
    fptr.close()
