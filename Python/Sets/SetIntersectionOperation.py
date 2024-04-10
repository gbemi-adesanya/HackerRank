"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
"""

def find_intersection(set1, set2):
    intersection = set1.intersection(set2)    
    print(len(intersection))
    
    
if __name__ == '__main__':
    n = input()
    e_set = set(map(int, input().split()))
    b = input()
    f_set = set(map(int, input().split()))
    
    find_intersection(e_set, f_set)
