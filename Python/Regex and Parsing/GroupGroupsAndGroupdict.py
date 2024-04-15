"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/re-group-groups/problem
"""

import re

if __name__== "__main__":
    x = re.search(r"([^\W_])\1", input())  # Search for two consecutive and identical alnum characters that are not _
    if x:
        print(x.group(1))
    else:
        print(-1)
