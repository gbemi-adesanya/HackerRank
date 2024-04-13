"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/collections-counter/problem
"""

from collections import Counter

if __name__ == "__main__":
    x = int(input())
    shoe_sizes = Counter(map(int, input().split()))
    n = int(input())
    
    total = 0
    for _ in range(n):
        size, price = map(int, input().split())
        if shoe_sizes[size]:  # If the shoe size exists or is not sold out
            total += price
            shoe_sizes[size] -= 1  # Reduce the stock of the size if a pair is sold           
    print(total)
