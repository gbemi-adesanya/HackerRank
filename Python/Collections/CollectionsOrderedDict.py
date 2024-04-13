"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
"""

from collections import OrderedDict

if __name__ == "__main__":
    n = int(input())
    ordered = OrderedDict()
    
    for _ in range(n):
        field = input().split()
        length = len(field)
        item, price = " ".join(field[0:length - 1]), field[length - 1]
        # 0:length - 1 is everything element in the list but the last (price)
        # length - 1 is the index of the last element (price)

        if item not in ordered.keys():
            ordered.update({item: int(price)})
        else:
            old_price = ordered.get(item)
            new_price = old_price + int(price)
            ordered.update({item: new_price})
            
    for item, price in ordered.items():
        print(item, price)
