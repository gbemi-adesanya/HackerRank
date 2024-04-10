"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/polar-coordinates/problem
"""

import cmath

if __name__ == "__main__":
    num = (input())
    c_num = complex(num)
    
    r = abs(c_num)
    phi = cmath.phase(c_num)
    print(r)
    print(phi)
