"""
Language: Python
Difficulty: hard
Problem: https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def matrixRotation(matrix, r):
    n, m = len(matrix), len(matrix[0])
  
    for layer in range(min(n, m) // 2):
        elements = []
        rotation = r % (2 * (n + m - 2 - 4 * layer))

        for j in range(layer, m - layer):
            elements.append(matrix[layer][j])
        for i in range(layer + 1, n - layer - 1):
            elements.append(matrix[i][m - layer - 1])
        for j in range(m - layer - 1, layer - 1, -1):
            elements.append(matrix[n - layer - 1][j])
        for i in range(n - layer - 2, layer, -1):
            elements.append(matrix[i][layer])

        rotated_elements = elements[rotation:] + elements[:rotation]

        k = 0
        for j in range(layer, m - layer):
            matrix[layer][j] = rotated_elements[k]
            k += 1
        for i in range(layer + 1, n - layer - 1):
            matrix[i][m - layer - 1] = rotated_elements[k]
            k += 1
        for j in range(m - layer - 1, layer - 1, -1):
            matrix[n - layer - 1][j] = rotated_elements[k]
            k += 1
        for i in range(n - layer - 2, layer, -1):
            matrix[i][layer] = rotated_elements[k]
            k += 1
            
    for i in matrix:
        print(" ".join(map(str, i)))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    m = int(first_multiple_input[0])
    n = int(first_multiple_input[1])
    r = int(first_multiple_input[2])

    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
