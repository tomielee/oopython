#! usr/local/bin/env python3
"""
    Datastructure Trie for Nodes to handle words in spellchecker.py
    kmom10 - oopython
"""

from node import TrieNode

from error import SearchError
from error import EmptyTree

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
        """
            search for a word
            iterate letter by letter in word
            if found in nodes children then continue
                node set to node.child
            if the whole word is found and last node is completeword return True

            word: user input
            return: bool. True if word exists in dictionary.
        """

        if self.root is None:
            raise KeyError
        else:
            node = self.root
            for letter in word:
                if letter not in node.children:
                    return False
                node = node.children[letter]

            return node.is_complete_word()

            # node = self.root
            # if len(word) >= 1:
            #     for letter in word:
            #         if letter not in node.children:
            #             return False
            #         node = node.children[letter]
            #
            #     return node.is_complete_word()
            # else:
            #     raise SearchError


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
                raise SearchError
                # return False

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

        for value in node.children.values():
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
            for value in node.children.values():
                node = value
                self._print_nodes(node, word, all_words)

        if len(all_words) <= 0:
            raise EmptyTree
        else:
            return all_words
    

    @staticmethod
    def _print_nodes(node, word, all_words):
        """
            private recursive method to create list of words.
        """

        word = word + node.get_letter()
        # print('ordet so far {}'.format(word))

        if node.is_complete_word():
            all_words.append(word)

        for value in node.children.values():
            node = value
            Trie._print_nodes(node, word, all_words)

    def j_t(self):
        """
            testning things
        """
        if self.root is None:
            raise KeyError
        else:
            node = self.root
            return node.get_list_of_children()
