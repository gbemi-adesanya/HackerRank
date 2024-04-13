"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/itertools-permutations/problem
"""

import itertools

if __name__ == "__main__":
    first = input()
    string, r = first.split()
    r = int(r)
    
    print(*list(sorted(map("".join, itertools.permutations(string, r)))), sep = "\n")
