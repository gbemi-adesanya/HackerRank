"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/re-start-re-end/problem
"""

import re

if __name__ == "__main__":
    S, k = input(), input()
    pattern = re.compile(f'(?=({k}))')
    x = list(pattern.finditer(S))    
    
    if x:
        for i in x:
            print((i.start(1), i.end(1)-1))
    else:
        print((-1,-1))
