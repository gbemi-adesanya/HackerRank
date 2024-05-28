"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/grading/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def gradingStudents(grades):
    for i in range(len(grades)):
        grade = grades[i]
        next_multiple = (grade//5 + 1) * 5
        
      if (grade < 38) or (next_multiple - grade > 2):
            continue
        else:
            grades[i] = next_multiple
            
    return grades
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())
    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
