"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def designerPdfViewer(h, word):     
    heights = [h[ord(letter) - 97] for letter in word]
    return max(heights) * len(word)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))
    word = input()
    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')
    fptr.close()
