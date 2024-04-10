"""
difficulty: easy
problem: https://www.hackerrank.com/challenges/finding-the-percentage/problem
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    marks = student_marks.get(query_name)
    avg = sum(marks)/len(marks)
    print("{:.2f}".format(avg))
