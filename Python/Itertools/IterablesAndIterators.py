"""
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/iterables-and-iterators/problem
"""

from itertools import combinations

if __name__ == "__main__":
    n = int(input())
    string = list(input().split(" "))
    k = int(input())
    
    letter_comb = list(combinations(string, k))
    contain = [word for word in letter_comb if "a" in word]
    print(len(contain)/len(letter_comb))
