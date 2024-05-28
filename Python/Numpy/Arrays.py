"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/np-arrays/problem
"""

import numpy

def arrays(arr):
    arr.reverse()
    float_arr = [float(i) for i in arr]
    new = numpy.array(float_arr, float)
    return new

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
