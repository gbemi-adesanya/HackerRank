"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/itertools-combinations/problem
"""

from itertools import combinations

if __name__ == "__main__":
    first = input()
    string, k = first.split()
    k = int(k)
    
    for i in range(1, k+1):
        for j in combinations(sorted(string), i):
            print("".join(j))
