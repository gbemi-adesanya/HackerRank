"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
"""

import numpy as np
np.set_printoptions(legacy='1.13')

if __name__ == "__main__":
    array = np.array(input().split(), float)
    print(np.floor(array))
    print(np.ceil(array))
    print(np.rint(array))
