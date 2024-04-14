"""
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/python-time-delta/problem
"""

import os
from datetime import datetime
    
def time_delta(t1, t2):
    time_format = "%a %d %b %Y %H:%M:%S %z"
    # Create the datatime objects based on the string format
    t_one = datetime.strptime(t1, time_format)
    t_two = datetime.strptime(t2, time_format)

    time = abs(t_one - t_two)
    return str(int(time.total_seconds()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
