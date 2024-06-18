"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/maximum-palindromes/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


MODULO = (10**9) + 7
prefix_factorials, prefix_counts = list(), list()


def initialize(s):
    global prefix_factorials, prefix_counts
    
    n = len(s)
    prefix_factorials = [1] * (n + 1)
    prefix_counts = [[0] * 26 for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        prefix_factorials[i] = prefix_factorials[i - 1] * i % MODULO
    
    for i in range(1, n + 1):
        for j in range(26):
            prefix_counts[i][j] = prefix_counts[i - 1][j]
        prefix_counts[i][ord(s[i - 1]) - ord('a')] += 1


def answerQuery(l, r):
    global prefix_factorials, prefix_counts
    
    l -= 1
    r -= 1
    
    freq = {}
    for char in range(26):
        count = prefix_counts[r + 1][char] - prefix_counts[l][char]
        if count > 0:
            freq[chr(char + ord('a'))] = count
    
    odd_count = sum(1 for count in freq.values() if count % 2 == 1)
    half_length = sum(count // 2 for count in freq.values())
    
    perm = prefix_factorials[half_length]
    for count in freq.values():
        if count // 2 > 0:
            perm = perm * pow(prefix_factorials[count // 2], MODULO-2, MODULO) % MODULO
    
    if odd_count > 0:
        perm = perm * odd_count % MODULO
    
    return perm


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input(
    initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        l = int(first_multiple_input[0])
        r = int(first_multiple_input[1])
        result = answerQuery(l, r)

        fptr.write(str(result) + '\n')
    fptr.close()
