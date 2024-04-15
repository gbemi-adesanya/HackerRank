"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
"""


cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    array = [0, 1]
    if n < 2:
        return array[:n]  # Returns [0] when n = 0 and [0, 1] when n = 1
      
    for i in range(2, n):
        array.append(array[i - 1] + array[i - 2])
        
    return array
    

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
