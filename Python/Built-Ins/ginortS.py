"""
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/ginorts/problem
"""

if __name__ == "__main__":
    S = input()
    first = sorted(S, key=lambda x:
    # Working backwards:
    (x.isdigit() and int(x) % 2 == 0,  # even digits at the end
    x.isdigit(),  # odd digits before even digits 
    x.isupper(),  # upper case letters before odd digits
    x.islower(),  # lower case letters before upper case letters
    x)) # sort
    print("".join(first))
