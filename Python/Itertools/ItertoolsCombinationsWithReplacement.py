"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
"""

from itertools import combinations_with_replacement

if __name__ == "__main__":
    first = input()
    string, k = first.split()
    string = sorted(string)
    k = int(k)
    
    for i in list(combinations_with_replacement(string, k)):
        print(*i, sep="")
