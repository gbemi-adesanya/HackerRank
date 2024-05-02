"""
Difficulty: Hard
Problem: https://www.hackerrank.com/challenges/matrix-script/problem
"""

import re

n, m = map(int, input().split())

matrix = []
string = ""
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
for z in zip(*matrix):
    string += ''.join(z)
    
output = re.sub(r'(?<=\w)([^\w]+)(?=\w)', " ", string)
print(output)
