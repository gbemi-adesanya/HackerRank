"""
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/python-quest-1/problem
"""

for i in range(1, int(input())):
    print(int((i*(pow(10, i) - 1)) / 9 ))
