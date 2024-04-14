"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/exceptions/problem
"""

if __name__ == "__main__":
    t = int(input())
  
    for _ in range(t):
        next_line = input()
        a, b = next_line.split()
      
        try:
            print(int(a)//int(b))
          
        except ZeroDivisionError:
            print("Error Code: integer division or modulo by zero")
          
        except ValueError:
            if a.isdigit():
                wrong_value = b
            else:
                wrong_value = a
            print("Error Code: invalid literal for int() with base 10: '{}'".format(wrong_value))
