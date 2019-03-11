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
                node = node.children[letter]

            return node.completeword

    def start_with(self, prefix):
        """
            return list of words starting with user prefix
            prefix: user input
            return: words [] a list of 10 words
        """

        if self.root is None:
            raise KeyError
        else:
            node = self.root

            if self._check_prefix(prefix, node):
                words = [] #får vara max 10
                word = ""

                for letter in prefix:
                    for key, value in node.children.items():
                        if letter == key:
                            node = value

                self._get_words(prefix, node, word, words)

            else:
                return False

            return words


    @staticmethod
    def _get_words(prefix, node, word, words):
        """traverse the node until node is complete word"""


        # print('-----\nnodens: {}'.format(node.get_letter()))
        # print('och nodens barn: {}'.format(node.get_list_of_children()))
        # print('är den complete?: {}'.format(node.is_complete_word()))

        if node.is_complete_word():
            # print('\ncompleteword så här: {}'.format(prefix+word))
            # print('first letter in word: {}'.format(word[0]))

            words.append(prefix[:-1]+word+node.get_letter())


        word = word + node.get_letter()
        # print('word so far: {}'.format(word))

        for key, value in node.children.items():
            node = value
            if len(words) > 10:
                break
            else:
                Trie._get_words(prefix, node, word, words)


    @staticmethod
    def _check_prefix(prefix, node):
        """
            private method.
            return True if prefix is in dictionary
        """
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]

        return True


    def print_nodes(self):
        """
            Call method _print_nodes() for list of words.
            Return: list of string.
        """
        if self.root is None:
            raise KeyError
        else:
            node = self.root
            all_words = []
            word = ""
            for key, value in node.children.items():
                node = value
                self._print_nodes(node, word, all_words)

        return all_words

    @staticmethod
    def _print_nodes(node, word, all_words):
        """
            private recursive method to create list of words.
        """

        if node.is_complete_word():
            all_words.append(word)


        word = word + node.get_letter()

        for key, value in node.children.items():
            node = value
            Trie._print_nodes(node, word, all_words)
