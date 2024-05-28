"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
"""

def wrapper(f):
    def fun(l):
        # complete the function
        numbers = list()
        for i in l:
            x = i[len(i)-10:]
            numbers.append(x)
        numbers.sort()
        for i in numbers:
            print("+91 {} {}".format(i[:5], i[5:]))
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
