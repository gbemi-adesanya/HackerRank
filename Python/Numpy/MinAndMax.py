"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/np-min-and-max/problem
"""

import numpy as np

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list()
    for _ in range(n):
        row = list(map(int, input().split()))
        arr.append(row)
        
    array = np.array(arr)
    minimum = np.min(array, axis=1)
    maximum = np.max(minimum)
    print(maximum)
