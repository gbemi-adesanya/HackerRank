"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/np-sum-and-prod/problem
"""

import numpy as np

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list()
    for _ in range(n):
        row = list(map(int, input().split()))
        arr.append(row)
        
    array = np.array(arr)
    one = np.sum(array, axis=0)
    prod = np.prod(one)
    print(prod)
