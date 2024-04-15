"""
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
"""

import re

def fun(s):
    """
    ^      : starts with
    \w     : contains a-z, A-Z, 0-9, _
    +      : one or more of
    \d     : 0-9
    {1,3}  : minimum 1 maximum 3
    $      : ends with
    """
    return re.search(r"^[\w-]+@[a-zA-Z\d]+\.[a-zA-Z]{1,3}$", s)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
