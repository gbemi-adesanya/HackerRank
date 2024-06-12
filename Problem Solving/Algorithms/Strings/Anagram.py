"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/anagram/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def anagram(s):
    n = len(s)
    if n % 2 == 1:  # string cannot be split into two equal substrings
        return -1
        
    s1, s2 = s[:n//2], s[n//2:]
    s1_count, s2_count = Counter(s1), Counter(s2)
    count = 0
    
    for char in s1_count:
        if s1_count[char] > s2_count[char]:
            count += s1_count[char] - s2_count[char]
            
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = anagram(s)

        fptr.write(str(result) + '\n')
    fptr.close()
