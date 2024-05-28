"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/np-linear-algebra/problem
"""

import numpy as np
np.set_printoptions(legacy='1.13')

if __name__ == "__main__":
    n = int(input())
    arr = list()
    
    for _ in range(n):
        row = list(map(float, input().split()))
        arr.append(row)
    
    M = np.array(arr)
    print(np.linalg.det(M))
