#! usr/local/bin/env python3
"""
    Datastructure Trie for Nodes to handle words in spellchecker.py
    kmom10 - oopython
"""

from node import TrieNode

class Trie():
    """
        Datastructure to handle words as a trie object
    """

    def __init__(self):
        """constructor for Trie object"""
        self.root = TrieNode(None)

    def add(self, word):
        """add a new node"""

        if self.root is None:
            self.root = TrieNode(word)
        else:
            self._add(word, self.root)

    @staticmethod
    def _add(word, node):
        """add word"""

        for letter in word:
            if letter not in node.children:
                # print('letter: {} finns inte så skapar, ny'.format(letter))
                new_node = TrieNode(letter)
                node.children[letter] = new_node
            node = node.children[letter]

        node.completeword = True

    def search_word(self, word):
        """search for a word"""

        if self.root is None:
            raise KeyError
        else:
            node = self.root
            for letter in word:
                if letter not in node.children:
                    return False
                    break
                node = node.children[letter]

            return node.completeword

    def start_with(self, prefix):
        """return 10 words that starts with user prefix"""

        if self.root is None:
            raise KeyError
        else:
            node = self.root
            for letter in prefix:
                if letter not in node.children:
                    return False
                    break
                node = node.children[letter]

            

    def print_nodes(self):
        """print nodes"""
        if self.root is None:
            raise KeyError
        else:
            self._print_nodes(self.root)

    @staticmethod
    def _print_nodes(node):
        """return list of word to print"""
        list_of_words = []
        list_of_words.append("test")

        for child in node.children.keys():
            print(child)
            if not node.is_complete_word():
                print('values: {}, child: {}'.format(node.letter, child))
                list_of_words.append(child)
            else:
                print('finns inte')
                list_of_words.append(" ")

        node = node.children[child]

        print('list of words: {}'.format(list_of_words))
        return list_of_words
