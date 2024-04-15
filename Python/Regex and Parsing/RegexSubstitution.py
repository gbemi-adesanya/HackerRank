"""
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
"""

import re

if __name__ == "__main__":
    n = int(input())
  
    for _ in range(n):
        j = input()

        while re.search(" && ", j):
            j = re.sub(" && ", " and ", j)

        while re.search(r" \|\| ", j):
            j = re.sub(r" \|\| ", " or ", j)
        
        print(j)
