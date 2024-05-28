"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/time-conversion/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    array = s.split(":")
    hh, mm, ss, meridiem = int(array[0]), int(array[1]), int(array[2][:2]), array[2][2:]
  
    if meridiem == "AM":
        if hh == 12:
            hh = 0
    else:
        if hh != 12:
            hh += 12
    
    converted = "{:02}:{:02}:{:02}".format(hh, mm, ss)
    return converted

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = timeConversion(s)

    fptr.write(result + '\n')
    fptr.close()
