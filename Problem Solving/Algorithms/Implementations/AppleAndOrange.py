"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/apple-and-orange/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples = [i+a for i in apples]
    oranges = [i+b for i in oranges]
    x = [i for i in apples if s <= i <= t]
    y = [i for i in oranges if s <= i <= t]
    print(len(x))
    print(len(y))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
