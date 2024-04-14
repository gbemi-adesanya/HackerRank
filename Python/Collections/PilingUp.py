"""
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/piling-up/problem
"""

from collections import deque

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        
        blocks = deque(map(int, input().split()))
        # input().split() gives a list of the cube sizes
        # map() converts each element in the list to an integer
        
        stackable = True
        old_current = 2 ** 31 + 1  # Initialize old current to a number greater than the maximum cube size (2 ** 31)
        
        for _ in range(len(blocks)):
            current = max(blocks[0], blocks[-1])
            
            if old_current < current:
                # If the cube already stacked is smaller than either the first or the last, it is not stackable 
                stackable = False
                break
   
            if len(blocks) == 1:  # There's only one cube left; calculate stackable
                stackable = current >= blocks[0]
            # Remove the stacked cube and calculate stackable
            elif current == blocks[0]:
                blocks.popleft()  
                stackable = current >= blocks[-1]
            elif current == blocks[-1]:
                blocks.pop()
                stackable = current >= blocks[0]
  
            # Change old_current because current will be recalculated at the beginning of the next iteration
            old_current = current
            
        if stackable:
            print("Yes")
        else:
            print("No")
