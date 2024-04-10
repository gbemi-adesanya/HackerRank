"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/string-validators/problem
"""

if __name__ == '__main__':
    s = input()
    
    alnum = alpha = digit = lower = upper = False
    for char in s:  # If any character in the string is True for any of the categories, the category is True
        if char.isalnum():
            alnum = True
        if char.isalpha():
            alpha = True
        if char.isdigit():
            digit = True
        if char.islower():
            lower = True
        if char.isupper():
            upper = True
            
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
