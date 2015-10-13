#!/usr/bin/env python
# trees.py
# implementation of various trees

import random

# binary search trees
class Node:
    def __init__(self, payload):
        self.payload = payload
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return 'Node with payload <{}>'.format(self.payload)

class BST:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        return 'BST with head {}'.format(self.head)

    def find(self, payload, curnode=None):
        # tree doesn't exist
        if self.head is None:
            return None
        # start on head
        elif curnode is None:
            self.find(payload, curnode=self.head)
        # found it!
        elif curnode.payload == payload:
            return curnode
        # look on left subtree
        elif curnode.payload > payload and curnode.left is not None:
            return self.find(payload, curnode=curnode.left)
        # look on right subtree
        elif curnode.payload < payload and curnode.right is not None:
            return self.find(payload, curnode=curnode.right)
        # can't find it!
        else:
            return None

    # find minimum element in tree
    # min element is the leftmost elem of the tree
    def findMin(self, curnode=None):
        if self.head is None:
            return None
        elif curnode is None:
            return self.findMin(curnode=self.head)
        elif curnode.left is None:
            return curnode
        elif curnode.left is not None:
            return self.findMin(curnode=curnode.left)

    # find maximum element in tree
    # max element is the rightmost elem of the tree
    def findMax(self, curnode=None):
        if self.head is None:
            return None
        elif curnode is None:
            return self.findMin(curnode=self.head)
        elif curnode.right is None:
            return curnode
        elif curnode.right is not None: return self.findMin(curnode=curnode.right)

    def insert(self, payload, curnode=None):
        if self.head is None:
            n = Node(payload)
            self.head = n
            return n

        elif curnode is None:
            return self.insert(payload, curnode=self.head)

        elif payload < curnode.payload:
            if curnode.left is None:
                n = Node(payload)
                n.parent = curnode.left
                curnode.left = n
                return n
            else:
                return self.insert(payload, curnode=curnode.left)

        elif payload > curnode.payload:
            if curnode.right is None:
                n = Node(payload)
                n.parent = curnode.right
                curnode.right = n
                return n
            else:
                return self.insert(payload, curnode=curnode.right)

        else:
            # no duplicates!
            return None

    def remove(self, payload, curnode=None):
        n = self.find(payload)

        # nothing to remove
        if n is None:
            return None
        # case 1: no children. just remove node from parent
        elif n.left is None and n.right is None:
            # node is head; nothing to do
            if n is self.head:
                self.head = None
                return n
            # node is left child
            elif n is n.parent.left:
                n.parent.left = None
                n.parent = None
                return n
            # node is right child
            elif n is n.parent.right:
                n.parent.right = None
                n.parent = None
                return n

        # case 2: one child. move child to parent
        elif n.left is not None and n.right is None:
            # node is head; make child head
            if n.parent is self.head:
                n.left.parent = None
                self.head = n.left
                return n
            # node is left child; make node child the left child of parent
            elif n is n.parent.left:
                n.left.parent = n.parent
                n.parent.left = n.left
                return n
            # node is right child; make node child the right child of parent
            elif n is n.parent.right:
                n.left.parent = n.parent
                n.parent.right = n.left
                return n

        # case 2: symmetric to left above
        elif n.left is None and n.right is not None:
            # node is head; make child head
            if n.parent is self.head:
                n.right.parent = None
                self.head = n.right
                return n
            # node is left child; make node child the left child of parent
            elif n is n.parent.left:
                n.right.parent = n.parent
                n.parent.left = n.right
                return n
            # node is right child; make node child the right child of parent
            elif n is n.parent.right:
                n.right.parent = n.parent
                n.parent.right = n.right
                return n

        # case 3: two children. replace node with the nearest elem
        # from one of the subtrees. this can be either:
        # - greatest lower elem (max of left subtree)
        # - lowest greater elem (min of right subtree)
        # we arbitrarily use the the gle here
        elif n.left is not None and n.right is not None:
            gle = self.findMax(n.left)
            gle.parent = None

            if n.left is gle:
                gle.parent = None
            else:
                gle.left = n.left
                gle.left.parent = gle

            gle.right = n.right
            gle.right.parent = gle
            return n

    # preorder traversal: node first, then children
    def preorder(self, curnode=None):
        if self.head is None: return

        if curnode is None:
            curnode = self.head

        yield curnode

        if curnode.left is not None:
            for lnode in self.preorder(curnode.left):
                yield lnode

        if curnode.right is not None:
            for rnode in self.preorder(curnode.right):
                yield rnode

    # inorder traversal: left child, node, right child
    def inorder(self, curnode=None):
        if self.head is None: return

        if curnode is None:
            curnode = self.head

        if curnode.left is not None:
            for lnode in self.inorder(curnode.left):
                yield lnode

        yield curnode

        if curnode.right is not None:
            for rnode in self.inorder(curnode.right):
                yield rnode

    # postorder traversal: left child, right child, node
    def postorder(self, curnode=None):
        if self.head is None: return

        if curnode is None:
            curnode = self.head

        if curnode.left is not None:
            for lnode in self.postorder(curnode.left):
                yield lnode

        if curnode.right is not None:
            for rnode in self.postorder(curnode.right):
                yield rnode

        yield curnode


def main():
    tree = BST()
    for i in xrange(100):
        tree.insert(random.randint(1,100))

    for n in tree.inorder():
        print n.payload,

if __name__ == '__main__':
    main()
