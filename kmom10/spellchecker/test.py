#! usr/local/bin/env python3
"""
    Test och Trie Tree
"""

import unittest

# from error import NoRead #read file
from error import NoContent #content empty
from error import SearchError #unable to search
from error import EmptyTree #tree is empty
from error import SomethingWrong #error error


from spellchecker import SpellChecker as SC
from trie import Trie
from node import TrieNode

class TestSpellChecker(unittest.TestCase):
    """ Test class SpellChecker from spellspechecker.py """

    def setUp(self):
        """ >> create default test object"""
        self.sc = SC()

    def tearDown(self):
        """teardown test"""
        self.sc = None

    def test_set_new_dict(self):
        """ >> should raise NoContent
            add dictionary with no content
        """
        with self.assertRaises(NoContent):
            self.sc.set_new_dict("test_empty.txt")

    def test_handle_search_word(self):
        """ >> should return KeyError
            no values in dictionary
        """
        with self.assertRaises(SearchError):
            self.sc.handle_search_word("")

    def test_handle_input(self):
        """ >> should raise SomethingWrong
            invalid user input
        """
        with self.assertRaises(SomethingWrong):
            self.sc.handle_input("%s")

class TestTrie(unittest.TestCase):
    """ Test class Trie from trie.py """

    def setUp(self):
        """create default test object"""
        self.trietest = Trie()
        self.emptytrie = Trie()

    def tearDown(self):
        """teardown test"""
        self.trietest = None

    def test_add(self):
        """ >> should be equal"""
        content = TestTrie._read_file("test_dict.txt") #get content
        words = content.split("\n") #skapar en lista med ord

        words_in_text = 0
        complete_words = []

        for word in words:
            self.trietest.add(word)
            words_in_text += 1

        node = self.trietest.root


        self._count_complete_words(node, complete_words)
        ret_sum = sum(complete_words)

        # print('complete words: {}'.format(ret_sum))

        self.assertEqual(ret_sum, words_in_text)

    @staticmethod
    def _count_complete_words(node, complete_words):

        if node.is_complete_word():
            complete_words.append(1)

        for value in node.children.values():
            node = value
            TestTrie._count_complete_words(node, complete_words)

    @staticmethod
    def _read_file(filename):
        """
            private method read file
        """

        fh = open(filename)
        content = fh.read().strip() #läser innehåll utan whitespace
        fh.close()
        return content

    def test_search_word(self):
        """ >> return False and True
            addes "te" and "ta"
            try to find "find me"
            try to find "ta"
        """
        self.trietest.add("te")
        self.trietest.add("ta")

        wontfind = self.trietest.search_word("find me")
        willfind = self.trietest.search_word("ta")
        self.assertFalse(wontfind, False)
        self.assertTrue(willfind, True)

    def test_start_with(self):
        """ >> should raise SearchError
            with not searchable value
        """
        with self.assertRaises(SearchError):
            self.trietest.start_with("search")

    def test_print_nodes(self):
        """ >> should raise EmptyTree
        """
        with self.assertRaises(EmptyTree):
            self.emptytrie.print_nodes()



class TestTrieNode(unittest.TestCase):
    """ Test class TrieNode from node.py """

    def setUp(self):
        """default testobject of class TrieNode"""
        self.tn = TrieNode('a')

    def test_get_letter(self):
        """ >> should return false"""
        result = self.tn.get_letter() #should return a

        self.assertIs(result, 'a')

    def test_is_complete_word(self):
        """ >>should return false since there is only one object"""
        result = self.tn.is_complete_word()

        self.assertFalse(result, False)


if __name__ == '__main__':
    unittest.main(verbosity=3)
