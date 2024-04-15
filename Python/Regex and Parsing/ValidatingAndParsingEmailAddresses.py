"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
"""

import re
import email.utils

if __name__ == "__main__":
    n = int(input())
    pattern = r"^[a-z][\w\-\.]+@[a-z]+\.[a-z]{1,3}$"
  
    for _ in range(n):
        string = input()
        parsed = email.utils.parseaddr(string)
      
        if re.search(pattern, parsed[1]):
            formatted = email.utils.formataddr(parsed)
            print(formatted)
