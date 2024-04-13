"""
Difficulty: hard
Problem: https://www.hackerrank.com/challenges/maximize-it/problem
"""

import itertools

def squared(element):  # function to calculate the square of a number
    return element ** 2
    
if __name__ == "__main__":
    k, m = input().split()
    k = int(k)
    m = int(m)
    big_list = list()
    
    for i in range(k):
        new_list = list(map(int, input().split()))
        big_list.append(new_list)     

    combs = list(itertools.product(*big_list))
    results = list()
    
    for i in combs:
        result_one = sum(map(squared, [a for a in i]))
        result_two = result_one % m
        results.append(result_two)
     
    print(max(results))
