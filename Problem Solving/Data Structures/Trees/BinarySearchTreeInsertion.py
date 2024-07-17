"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem?isFullScreen=true
"""

class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
          
        else:
            current = self.root
            while True:
                if val < current.info:
                    if current.left is None:
                        current.left = Node(val)
                        break
                    current = current.left
                  
                elif val > current.info:
                    if current.right is None:
                        current.right = Node(val)
                        break
                    current = current.right

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
