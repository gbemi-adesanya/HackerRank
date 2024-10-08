"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/day-of-the-programmer/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def is_leap(year, system):
    if system == "Julian":
        return year % 4 == 0
    else:
        return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))
    
def dayOfProgrammer(year):
    if year == 1918:
        return "26.09.1918"
    
    if year <= 1917:
        system = "Julian"
    elif year >= 1919:
        system = "Gregorian"
        
    check = is_leap(year, system)
    if check:
        return "12.09." + str(year)
    else:
        return "13.09." + str(year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())
    result = dayOfProgrammer(year)

    fptr.write(result + '\n')
    fptr.close()
