"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/py-check-subset/problem
"""


if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        a_num = int(input())
        A_set = set(map(int, input().split()))
        b_num = int(input())
        B_set = set(map(int, input().split()))

        print(A_set.issubset(B_set))
