#! usr/local/bin/env python3
"""
    Node object.
    Kmom04
"""

class Node:
    """
    Node class
    """
    def __init__(self, data, next_node=None):
        """
        Initialize object with the data and set next to None.
        next will be assigned later when new data needs to be added.
        """
        self.data = data
        self.next = next_node

    def get_data(self):
        """return object data"""
        return self.data

    def get_next(self):
        """return object next"""
        return self.next

    def set_data(self, new_data):
        """set newdata to object"""
        self.data = new_data

    def set_next(self, new_next):
        """set newnext to object, redirecting"""
        self.next = new_next
