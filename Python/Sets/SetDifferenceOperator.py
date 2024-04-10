"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/py-set-difference-operation/problem
"""

def find_difference(set1, set2):
    difference = set1.difference(set2)
    return len(difference)

if __name__ == '__main__':
    n = int(input())
    e_set = set(map(int, input().split()))
    m = int(input())
    f_set = set(map(int, input().split()))

    result = find_difference(e_set, f_set)
    print(result)
