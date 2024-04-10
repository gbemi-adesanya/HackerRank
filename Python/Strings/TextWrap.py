"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/text-wrap/problem
"""

import textwrap

def wrap(string, max_width):
    m = textwrap.wrap(string, max_width)
    return "\n".join(m)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
