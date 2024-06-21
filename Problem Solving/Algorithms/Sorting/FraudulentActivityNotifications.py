"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def find_median(count, d):
    cum_count = 0
    median1, median2 = None, None
    
    if d % 2 == 1:
        median_pos = d // 2 + 1
        for i in range(len(count)):
            cum_count += count[i]
            if cum_count >= median_pos:
                return i
    else:
        median_pos1 = d // 2
        median_pos2 = d // 2 + 1
        for i in range(len(count)):
            cum_count += count[i]
            if median1 is None and cum_count >= median_pos1:
                median1 = i
            if cum_count >= median_pos2:
                median2 = i
                break
        return (median1 + median2) / 2
        

def activityNotifications(expenditure, d):
    notifications = 0
    count = [0] * 201
    n = len(expenditure)
    
    for i in range(d):
        count[expenditure[i]] += 1
    
    for i in range(d, n):
        if expenditure[i] >= 2 * find_median(count, d):
            notifications += 1
        
        count[expenditure[i]] += 1
        count[expenditure[i - d]] -= 1
        
    return notifications


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
  
    expenditure = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')
    fptr.close()
