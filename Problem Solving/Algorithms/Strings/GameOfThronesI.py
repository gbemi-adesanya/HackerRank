"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/game-of-thrones/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def gameOfThrones(s):
    s_count = Counter(s)
    odd = [count for count in s_count.values() if count % 2 == 1]
    return "YES" if len(odd) <= 1 else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = gameOfThrones(s)

    fptr.write(result + '\n')
    fptr.close()
