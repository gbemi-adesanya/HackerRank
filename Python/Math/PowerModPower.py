"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/python-power-mod-power/problem
"""

if __name__ == "__main__":
    a, b, m = int(input()), int(input()), int(input())
    print(pow(a,b))
    print(pow(a,b,m))