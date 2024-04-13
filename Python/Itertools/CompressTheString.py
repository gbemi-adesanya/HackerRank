"""
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/compress-the-string/problem
"""

from itertools import groupby

if __name__ == "__main__":
    string = input()
    for i, j in groupby(string):
        print("(%d, %d)" % (len(list(j)), int(i)), end=" ")
