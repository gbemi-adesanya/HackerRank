"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
"""

import numpy as np

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list()
    for _ in range(n):
        row = list(map(int, input().split()))
        arr.append(row)
    
    array = np.array(arr)
    mean = np.mean(array, axis=1)
    var = np.var(array, axis=0)
    std = np.std(array)
    
    print("{}\n{}\n{}".format(mean, var, round(std, 11)))
