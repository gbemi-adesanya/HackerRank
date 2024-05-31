"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

def climbingLeaderboard(ranked, player):
    ranked = sorted(list(set(ranked)), reverse=True)
    result = list()
    n = len(ranked)
    
    for score in player:
        while n > 0 and score >= ranked[n - 1]:
            n -= 1
        result.append(n + 1)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
