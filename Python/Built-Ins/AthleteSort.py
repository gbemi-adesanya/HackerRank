"""
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/python-sort-sort/problem
"""

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input()) 
    sort = sorted(arr, key=lambda x: x[k])  # Sort by the elements in the k-th index
    [print(*i) for i in sort]
