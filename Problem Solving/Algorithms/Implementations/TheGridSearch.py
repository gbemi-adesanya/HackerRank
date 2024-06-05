"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/the-grid-search/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def gridSearch(G, P):
    grow, gcol, prow, pcol = len(G), len(G[0]), len(P), len(P[0])

    for i in range(grow - prow + 1):
        for j in range(gcol - pcol + 1):
            match = True
            for x in range(prow):
                for y in range(pcol):
                    if G[i + x][j + y] != P[x][y]:
                        match = False
                        break
                if not match: break
            if match: return "YES"
              
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        R = int(first_multiple_input[0])
        C = int(first_multiple_input[1])

        G = []
        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()
        r = int(second_multiple_input[0])
        c = int(second_multiple_input[1])

        P = []
        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)
        fptr.write(result + '\n')
    fptr.close()
