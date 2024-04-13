"""
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/most-commons/problem
"""

from collections import Counter

if __name__ == '__main__':
    s = input()
    
    count = Counter(sorted(s))
    for char, occ in count.most_common(3):  # Returns the 3 most common
        print(char, occ)
