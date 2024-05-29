"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/electronics-shop/problem
"""

#!/bin/python3

import os
import sys

def getMoneySpent(keyboards, drives, b):
    array = list()
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            price = keyboards[i] + drives[j]
            if price <= b:
                array.append(price)

    if len(array) > 0:
        return max(array)
    else:
        return -1
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')
    fptr.close()
