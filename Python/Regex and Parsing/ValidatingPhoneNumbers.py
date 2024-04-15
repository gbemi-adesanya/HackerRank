"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/validating-the-phone-number/problem
"""

import re            
            
if __name__ == "__main__":
    num = int(input())
  
    for _ in range(num):
        phone_no = input()
        x = re.compile(r"^[789]\d{9}$")
        check = re.match(x, phone_no)
        
        if check:
            print("YES")
        else:
            print("NO")
