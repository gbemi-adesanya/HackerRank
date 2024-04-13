"""
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/word-order/problem
"""

from collections import OrderedDict

if __name__ == "__main__":
    n = int(input())
    ordered = OrderedDict()
    
    for _ in range(n):
        word = input()
        if word not in ordered.keys():
            # Add the word to the dictionary with a count of 1 if it has not been encountered
            ordered.update({word: 1})  
        else:
            # Update the count of the word in the dictionary
            count = ordered.get(word)
            count += 1
            ordered.update({word: count})
            
    print(len(ordered.keys()))
    for value in ordered.values():
        print(value, end=" ")
