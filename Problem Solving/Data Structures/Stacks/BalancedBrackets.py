"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/balanced-brackets/problem?isFullScreen=true
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def isBalanced(s):
    stack = []

    for char in s:
        if char in ["(", "{", "["]:
            stack.append(char)
          
        else:
            if not stack:  # If it's not an opening bracket, it must be a closing bracket i.e. the stack cannot be empty
                return "NO"
                
            current = stack.pop()
          
            # Opening brackets must match closing brackets
            if current == '(':
                if char != ")":
                    return "NO"
                    
            if current == '{':
                if char != "}":
                    return "NO"
                    
            if current == '[':
                if char != "]":
                    return "NO"

    if stack:
        return "NO"
    return "YES"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
