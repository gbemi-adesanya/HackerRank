"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/validating-uid/problem
"""

import re

def validate_uid(uid):
    no_repeats = r"(?!.*(.).*\1)"
    two_plus_uppercase = r"(?=(?:.*[A-Z]+){2,})"
    three_plus_digits = r"(?=(?:.*\d){3,})"
    ten_alphanumeric = r"[\w]{10}"
    filters = [no_repeats, two_plus_uppercase, three_plus_digits, ten_alphanumeric]
    
    print('Valid') if all([re.match(f, uid) for f in filters]) else print('Invalid')
    
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        uid = input()
        validate_uid(uid)
