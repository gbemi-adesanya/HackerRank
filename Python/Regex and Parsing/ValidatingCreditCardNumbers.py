"""
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/validating-credit-card-number/problem
"""

import re

def validate_credit_no(num):
    structure = r"[456]\d{3}(-?\d{4}){3}$"
    repetition = r"((\d)-?(?!(-?\2){3})){16}"
    filters = [structure, repetition]
    
    print('Valid') if all(re.match(filt, num) for filt in filters) else print('Invalid')

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        num = input()
        validate_credit_no(num)
