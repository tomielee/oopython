#! usr/local/bin/env python3
"""
    Assignment for kmom06 - oophython
    Create a binary search tree.
    Node class object.
"""

class Node():
    """ Node object for Binary Search Tree"""

    def __init__(self, key, value, parent=None):
        """constructor for Node object"""
        #key = för att orientera oss i trädet
        #value = värdet som ska sparas under det key.
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent #defaultvärdet None

    def has_left_child(self):
        """return True if node has child to left"""
        return self.left is not None

    def has_right_child(self):
        """return True if node has child  to right"""
        return self.right is not None

    def has_both_children(self):
        """return True if node has children to right and left"""
        if self.has_left_child() and self.has_right_child():
            return True

    def has_parent(self):
        """return True if node has parent"""
        return self.parent is not None

    def is_left_child(self):
        """return True if node is left child to parent"""
        if self.has_parent() and self.key < self.parent:
            return True

    def is_right_child(self):
        """return True if node is right child to parent"""
        if self.has_parent() and self.key > self.parent:
            return True

    def is_leaf(self):
        """return True if node has no children"""
        if self.left is None and self.right is None:
            return True

    # __lt__: returnera True om nodens key är mindre än other, annars False.
    # __gt__: returnera True om nodens key är större än other, annars False.
    # __eq__: returnera True om nodens key är lika med other, annars False.

    def __lt__(self, other):
        """ return True if self is less than other"""
        if isinstance(other, Node):
            return self.key < other.key

        return self.key < other

    def __gt__(self, other):
        """ return true if self is greater than other"""
        if isinstance(other, Node):
            return self.key > other.key

        return self.key > other

    def __eq__(self, other):
        """return True if self is equal to other"""
        if isinstance(other, Node):
            return self.key == other.key

        return self.key == other
