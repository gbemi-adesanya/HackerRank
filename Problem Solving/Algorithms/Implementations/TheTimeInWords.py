"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/the-time-in-words/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def timeInWords(h, m):
    wlist = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]
    hour = wlist[h-1]
    
    if m == 0:
        return hour + " o' clock"
    elif m == 15:
        return "quarter past " + hour
    elif m == 30:
        return "half past " + hour
    elif m == 45:
        return "quarter to " + wlist[h]
    elif m == 1:
        return wlist[m-1] + " minute past " + hour
    elif m == 59:
        return wlist[60 - m - 1] + " minute to " + wlist[h]
    elif 2 <= m < 30:
        return wlist[m-1] + " minutes past " + hour
    elif m > 30:
        return wlist[60 - m - 1] + " minutes to " + wlist[h]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())
    m = int(input().strip())
    result = timeInWords(h, m)

    fptr.write(result + '\n')
    fptr.close()
