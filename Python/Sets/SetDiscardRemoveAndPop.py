"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
"""

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    next_line = list(map(str, input().split()))
    command = next_line[0]
    if command == "remove":
        s.remove(int(next_line[1]))
    elif command == "discard":
        s.discard(int(next_line[1]))
    elif command == "pop":
        s.pop()
        
total = sum(s)
print(total)
