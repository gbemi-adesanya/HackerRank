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


def sherlockAndAnagrams(s):
    result, n = 0, len(s)
    
    for i in range(n):
        for j in range(i+1, n):
            sub = "".join(sorted(s[i:j]))
            n_sub = len(sub)

            for k in range(i+1, n):
                if k + n_sub > n:
                    break

                subb = "".join(sorted(s[k : k + n_sub]))
                if sub == subb:
                    result += 1
    
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')
    fptr.close()
