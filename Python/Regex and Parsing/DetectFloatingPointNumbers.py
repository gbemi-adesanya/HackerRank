"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/introduction-to-regex/problem
"""

import re

if __name__ == "__main__":
    t = int(input())
  
    for i in range(t):
        n = input()
        pattern = re.compile(r"^[-+]?\d*\.\d+$")
        x = pattern.match(n)
        print(bool(x))
