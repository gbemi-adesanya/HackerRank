"""
Language: Python
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def sortedInsert(llist, data):
    new_node = DoublyLinkedListNode(data)
    
    if llist is None:
        return new_node
        
    if data < llist.data:
        new_node.next = llist
        llist.prev = new_node
        return new_node
    
    current = llist
    while current.next is not None and current.next.data < data:  # Find insertion point
        current = current.next
        
    if current.next is None:  # insert at end
        current.next = new_node
        new_node.prev = current
    else:  # insert in middle
        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node
    
    return llist
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')
    fptr.close()
