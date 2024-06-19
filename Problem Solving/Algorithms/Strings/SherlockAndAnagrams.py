"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


def sherlockAndAnagrams(s):
    n = len(s)
    freq = defaultdict(int)
    
    for i in range(n):
        for j in range(i+1, n+1):
            sub = "".join(sorted(s[i:j]))
            freq[sub] += 1
            
    result = 0
    for count in freq.values():
        result += count * (count - 1) // 2
    
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')
    fptr.close()
