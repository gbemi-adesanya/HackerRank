"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
"""

import collections

if __name__ == "__main__":
    n, m = map(int, input().split())
    
    dictionary = collections.defaultdict(list)
    for i in range(n):
        a = input()
        dictionary[a].append(str(i + 1))  # Append the position of the character
    
    for _ in range(m):
        b = input()
        array = dictionary.get(b, -1)  # If value is 0, return -1 instead
        if array != -1:
            print(" ".join(array))
        else:
            print(array)
