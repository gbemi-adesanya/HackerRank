"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
"""

import re

if __name__ == "__main__":
    s = input()
    # Find overlapping vowel groups between consonants
    x = re.findall("(?=[^aeiouAEIOU]([aeiouAEIOU]{2,})[^aeiouAEIOU])", s)
    if x:
        [print(i) for i in x]
    else:
        print(-1)
