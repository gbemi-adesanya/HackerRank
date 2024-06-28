"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/short-palindrome/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def shortPalindrome(s):
    arr1 = [0] * 26
    arr2 = [[0] * 26 for _ in range(26)]
    arr3 = [0] * 26
    count = 0
    
    for i in range(len(s)):
        index = ord(s[i]) - ord('a')
        count += arr3[index]
        
        for j in range(26):
            arr3[j] += arr2[j][index]
            
        for j in range(26):
            arr2[j][index] += arr1[j]
            
        arr1[index] += 1
        
    return count % (10**9 + 7)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = shortPalindrome(s)

    fptr.write(str(result) + '\n')
    fptr.close()
