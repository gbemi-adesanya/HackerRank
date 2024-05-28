"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/np-dot-and-cross/problem
"""

import numpy as np

if __name__ == "__main__":
    n = int(input())
    a_arr = list()
    for _ in range(n):
        row = list(map(int, input().split()))
        a_arr.append(row)
    
    b_arr = list()
    for _ in range(n):
        row = list(map(int, input().split()))
        b_arr.append(row)
        
    A = np.array(a_arr)
    B = np.array(b_arr)
    
    print(np.dot(A, B))
