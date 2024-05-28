"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/np-polynomials/problem
"""

import numpy as np

if __name__ == "__main__":
    coefficients = list(map(float, input().split()))
    x = float(input())
    
    print(np.polyval(coefficients, x))
