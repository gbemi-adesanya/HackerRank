"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/richie-rich/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def highestValuePalindrome(s, n, k):
    palindrome = list(s)
    changes = [0] * n
    
    left, right = 0, n-1
    while left <= right:  # Create a palindrome with minimum changes
        if palindrome[left] != palindrome[right]:
            palindrome[left] = palindrome[right] = max(palindrome[left], palindrome[right])
            changes[left] = changes[right] = 1
            k -= 1
        
        left += 1
        right -= 1
        
    if k < 0: return "-1"
    
    
    left, right = 0, n-1
    while left <= right:  # Maximize the palindrome
        if left == right and k > 0: palindrome[left] = "9"
            
        if palindrome[left] < "9":
            if k >= 2 and changes[left] == 0 and changes[right] == 0:
                k -= 2
                palindrome[left] = palindrome[right] = "9"
            elif k >= 1 and (changes[left] == 1 or changes[right] == 1):
                k -= 1
                palindrome[left] = palindrome[right] = "9"
        
        left += 1
        right -= 1
        
    return "".join(palindrome)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = input()
    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')
    fptr.close()
