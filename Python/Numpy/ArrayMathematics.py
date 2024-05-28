"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/np-array-mathematics/problem
"""

import numpy as np

if __name__ == "__main__":
    n, m = map(int, input().split())
    n_arr = list()
    for _ in range(n):
        row = list(map(int, input().split()))
        n_arr.append(row)
        
    m_arr = list()
    for _ in range(n):
        row = list(map(int, input().split()))
        m_arr.append(row)
        
    n_array = np.array(n_arr)
    m_array = np.array(m_arr)
    
    print(np.add(n_array, m_array))
    print(np.subtract(n_array, m_array))
    print(np.multiply(n_array, m_array))
    print(np.floor_divide(n_array, m_array))
    print(np.mod(n_array, m_array))
    print(np.power(n_array, m_array))
