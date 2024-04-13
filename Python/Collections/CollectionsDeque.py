"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/py-collections-deque/problem
"""

from collections import deque

if __name__ == "__main__":
    n = int(input())
    queue = deque()
    
    for _ in range(n):
        instruction = input().split()
        command = instruction[0]
      
        if command == "append":
            element = instruction[1]
            queue.append(element)
          
        elif command == "appendleft":
            element = instruction[1]
            queue.appendleft(element)
          
        elif command == "pop":
            queue.pop()
          
        elif command == "popleft":
            queue.popleft()
            
    print(" ".join(queue))
