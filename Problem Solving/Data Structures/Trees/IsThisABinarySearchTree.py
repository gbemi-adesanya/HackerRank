"""
Language: Python
Difficulty: medium
Problem: https://www.hackerrank.com/challenges/is-binary-search-tree/problem?isFullScreen=true
"""

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

def isBST(root, min_range, max_range):
    if not root:
        return True
    
    if root.data <= min_range or root.data >= max_range:
        return False
    
    return isBST(root.left, min_range, root.data) and isBST(root.right, root.data, max_range)

def check_binary_search_tree_(root):
    min_range, max_range = -10000, 10000
    return isBST(root, min_range, max_range)
