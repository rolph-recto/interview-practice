#!/usr/bin/env python
# heap.py
# max/min-heap data structure

class Node:
    def __init__(self, payload):
        self.payload = payload
        self.parent = None
        self.left = None
        self.right = None

class Heap:
    INIT_SIZE = 100
    def __init__(self):
        self.array = [0 for i in xrange(INIT_SIZE)]
        self.size = 0

    def insert(self, elem):
        if 
    
    def findMin(self):
        if self.size >= 1:
            return self.array[0]
        else:
            return None

