"""
Language: Python
Difficulty: hard
Problem: https://www.hackerrank.com/challenges/determining-dna-health/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import bisect  # efficient binary search operations
import collections


def getHealth(sequence, first, last, largest):
    health, ls = 0, len(sequence)
    for i in range(ls):
        for j in range(1, largest + 1):
            if i + j > ls: break
            sub = sequence[i:i + j]
          
            if sub not in subs: break
            if sub not in gene_dict: continue
            
            ids, healths = gene_dict[sub]
            health += healths[bisect.bisect_right(ids, last)] - healths[bisect.bisect_left(ids, first)]
            
    return health

if __name__ == '__main__':
    n = int(input().strip())
    genes = input().rstrip().split()
    health = list(map(int, input().rstrip().split()))

    gene_dict = collections.defaultdict(lambda: [[], [0]])
    subs = set()
    for i, gene in enumerate(genes):
        gene_dict[gene][0].append(i)
        for j in range(1, min(len(gene), 500)+1):
            subs.add(gene[:j])

    for v in gene_dict.values():
        for i, ix in enumerate(v[0]):
            v[1].append(v[1][i]+health[ix])

    largest = max(list(map(len, genes)))
    hMin, hMax = math.inf, 0
    
    s = int(input().strip())

    for s_itr in range(s):
        first_multiple_input = input().rstrip().split()
        first = int(first_multiple_input[0])
        last = int(first_multiple_input[1])
        d = first_multiple_input[2]
        
        h = getHealth(d, first, last, largest)
        hMin, hMax = min(hMin, h), max(hMax, h)
        
    print(hMin, hMax)
