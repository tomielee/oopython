#! usr/local/bin/env python3
"""
    TrieNode for TrieObject
    Kmom10 oophython 2019
"""

class TrieNode():
    """Nodes for TrieObject"""

    def __init__(self, letter):
        """constructor for nodes"""

        self.letter = letter
        self.children = {}
        self.completeword = False

    def get_letter(self):
        """return letter"""
        return self.letter

    def set_letter(self, new_letter):
        """set new letter"""
        self.letter = new_letter

    def get_list_of_children(self):
        """return children"""
        list_of_children = []

        for key in self.children.keys():
            list_of_children.append(key)

        return list_of_children


    def is_complete_word(self):
        """return true if word is completeword"""
        return self.completeword

    def has_children(self):
        """retrurn True if node has children"""
        return bool(self.children)

    def found_child(self, l):
        """return True if letter is found in child"""
        for child in self.children:
            return bool(child == l)
