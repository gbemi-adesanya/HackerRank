"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/itertools-product/problem
"""

import itertools
if __name__ == "__main__":
    A, B = list(map(int, input().split())), list(map(int, input().split()))
    
    cartesian_product = tuple(itertools.product(A, B))
    for i in cartesian_product:
        print(i, end=" ")
