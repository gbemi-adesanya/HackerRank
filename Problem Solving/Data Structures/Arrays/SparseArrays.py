"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/sparse-arrays/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def matchingStrings(stringList, queries):
    count = Counter(stringList)  
    return [count[q] for q in queries]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')
    fptr.close()
