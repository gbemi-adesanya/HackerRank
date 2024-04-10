"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/python-string-split-and-join/problem
"""

def split_and_join(line):
    array = line.split()
    string = "-".join(array)
    return string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
