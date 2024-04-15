"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/zipped/problem
"""

if __name__ == "__main__":
    n, x = map(int, input().split())
    
    scores = list()
    for _ in range(x):
        student = list(map(float, input().split()))
        scores.append(student)
        
    zipped = zip(*scores)
    for i in zipped:
        print(sum(i)/x)
