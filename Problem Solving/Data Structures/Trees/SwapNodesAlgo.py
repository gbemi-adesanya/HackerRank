"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/swap-nodes-algo/problem?isFullScreen=true
"""

#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(15000)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

def build_tree(indexes):
    nodes = {1: Node(1)}
    
    for i, (left, right) in enumerate(indexes):
        node = nodes[i + 1]
        
        if left != -1:
            if left not in nodes:
                nodes[left] = Node(left)
            node.left = nodes[left]
            
        if right != -1:
            if right not in nodes:
                nodes[right] = Node(right)
            node.right = nodes[right]
    
    return nodes[1]


def swap_helper(root, k):
    def swap_at_level(node, depth):
        if not node: return
        
        if depth % k == 0:
            node.left, node.right = node.right, node.left
        swap_at_level(node.left, depth + 1)
        swap_at_level(node.right, depth + 1)
      
    swap_at_level(root, 1)


def inorder(node, result):
    if not node:
        return
      
    inorder(node.left, result)
    result.append(node.data)
    inorder(node.right, result)
    
    return result


def swapNodes(indexes, queries):
    root = build_tree(indexes)
    results = list()
  
    for k in queries:
        swap_helper(root, k)
        result = list()
      
        inorder(root, result)
        results.append(result)
      
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
