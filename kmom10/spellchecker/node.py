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

    def get_list_of_children(self):
        """return children"""
        list_of_children = []
        for key in self.children:
            list_of_children.append(key)

        return list_of_children

    def is_complete_word(self):
        """return true if word is completeword"""
        return self.completeword

    def has_children(self):
        """retrurn True if node has children"""
        return bool(self.children)
