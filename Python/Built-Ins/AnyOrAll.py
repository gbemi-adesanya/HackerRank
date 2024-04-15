"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/any-or-all/problem
"""

if __name__ == "__main__":
    n = int(input())
    array = input().split()
    print(all(int(i) > 0 for i in array) and any(i == i[::-1] for i in array)

    # all() checks that every element in the array is gt 0
    # any() checks that there is at least one palindromic number
        # the condition for palndromic numbers is i == i[::-1]
