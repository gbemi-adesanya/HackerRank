"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def isValid(s):
    char_freq = Counter(s)
    freq_freq = Counter(char_freq.values())
    
    if len(freq_freq) == 1:  # each character has the same frequency
        return "YES"
    elif len(freq_freq) == 2:  # at least one of the characters has a different frequency
        key1, key2 = freq_freq.keys()
        if (freq_freq[key1] == 1 and (key1 - 1 == key2 or key1 - 1 == 0)) or (freq_freq[key2] == 1 and (key2 - 1 == key1 or key2 - 1 == 0)):  # one character can be removed to make the string valid
            return "YES"
            
    return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = isValid(s)

    fptr.write(result + '\n')
    fptr.close()
