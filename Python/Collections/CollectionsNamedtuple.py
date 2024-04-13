"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
"""

from collections import namedtuple

if __name__ == "__main__":
    n = int(input())
    Student = namedtuple("Student", input().split())
    
    marks = 0
    for i in range(n):
        fields = input().split()
        s = Student(fields[0], fields[1], fields[2], fields[3])
        marks += int(s.MARKS)  # MARKS now exists
        
    print("{:.2f}".format(marks/n))
