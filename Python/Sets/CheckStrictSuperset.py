"""
Difficulty: easy
Problem:
"""

if __name__ == "__main__":
    a_set = set(map(int, input().split()))
    n = int(input())
    check = True
    for i in range(n):
        n_set = set(map(int, input().split()))
        if not a_set.issuperset(n_set):
            check = False
            break
    print(check)
