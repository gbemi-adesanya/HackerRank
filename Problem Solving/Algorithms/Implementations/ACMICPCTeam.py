"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/acm-icpc-team/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def acmTeam(topic):
    n = len(topic)
    maxx, count = 0, 0
    
    for a in range(n):
        for b in range(a+1, n):
            one, two = topic[a], topic[b]
            team = sum(i == "1" or j == "1" for i, j in zip(one, two))
            if team > maxx:
                maxx = team
                count = 1
            elif team == maxx:
                count += 1

    return [maxx, count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
