"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
"""

import numpy as np

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list()
    for _ in range(n):
        row = list(map(int, input().split()))
        arr.append(row)
        
    x = np.array(arr)
    print(np.transpose(x))
    print(x.flatten())
