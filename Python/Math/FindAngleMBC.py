"""
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/find-angle/problem
"""

import math
if __name__ == "__main__":
    ab = float(input())
    bc = float(input())
    
    theta = round(math.degrees(math.atan2(ab, bc)))
    print((str(theta)), chr(176), sep='')
