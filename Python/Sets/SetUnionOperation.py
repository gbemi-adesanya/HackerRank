"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/py-set-union/problem
"""

if __name__ == "__main__":
    n = int(input())
    english = set(map(int, input().split()))
    b = int(input())
    french = set(map(int, input().split()))
    
    at_least = english.union(french)
    print(len(at_least))
