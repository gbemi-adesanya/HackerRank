"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/np-concatenate/problem
"""

import numpy as np

if __name__ == "__main__":
    n, m, p = map(int, input().split())
    n_array = list()
    for _ in range(n):
        row = list(map(int, input().split()))
        n_array.append(row)
        
    m_array = list()
    for _ in range(m):
        row = list(map(int, input().split()))
        m_array.append(row)
        
    x = np.array(n_array)
    y = np.array(m_array)
    print(np.concatenate((x, y)))
