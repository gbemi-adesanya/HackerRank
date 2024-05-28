"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/np-shape-reshape/problem
"""

import numpy as np


if __name__ == "__main__":
    array = list(map(int, input().split()))
    n = np.array(array)
    x = np.reshape(n, (3,3))
    print(x)
