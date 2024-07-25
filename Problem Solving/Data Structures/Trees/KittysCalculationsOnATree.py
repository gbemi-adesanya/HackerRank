"""
Language: Python
Difficulty: advanced
Problem: https://www.hackerrank.com/challenges/kittys-calculations-on-a-tree/problem?isFullScreen=true
Comments: Time limit exceeded (cases 16, 17, 18)
"""

n, q = map(int, input().split())

# Setting up the parent list and initial values
parents = [0] * (n + 1)
valuesSet = [False] * (n + 1)
children = [0] * (n + 1)

# Reading edges and setting up the parent-child relationship
for _ in range(n-1):
    a, b = map(int, input().split())
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

parents[1] = 0

for _ in range(q):
    k = int(input())
    values = list(map(int, input().split()))

    # Reset valuesSet and children for each query
    valuesSet = [False] * (n + 1)
    children = [0] * (n + 1)
    valuesSum = sum(values)

    for v in values:
        valuesSet[v] = True

    sum_val = 0
    MOD = 10**9 + 7

    # Bottom-up traversal from leaf to root
    for j in range(n, 0, -1):
        a = children[j]

        if valuesSet[j]:
            a += j

        if a:
            x = ((a % MOD) * ((valuesSum - a) % MOD)) % MOD
            sum_val = (sum_val + x) % MOD

        children[parents[j]] += a

    print(sum_val)
