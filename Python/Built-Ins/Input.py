"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/input/problem
"""

if __name__ == "__main__":
    x, k = map(int, input().split())
    polynomial = input()
    print(eval(polynomial) == k)
