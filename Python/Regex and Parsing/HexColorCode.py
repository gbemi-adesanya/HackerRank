"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/hex-color-code/problem
"""

import re

if __name__ == "__main__":
    n = int(input())
    check = False
  
    for _ in range(n):
        line = input().strip()
        if "{" in line:
            check = True
        elif "}" in line:
            check = False
        elif check:
            for color in re.findall(r"#[\da-fA-F]{3,6}", line):
                print(color)
