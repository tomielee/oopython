#! usr/local/bin/env python3
"""
    Test exceptions
    Kmom04, assignment 2.
"""
import unittest
from unorderedlist import UnorderedList
from error import NoValue
from error import AttError
from error import OutOfIndex

class TestEx(unittest.TestCase):
    """test exeptions in method in undorderlist.py"""

    def setUp(self):
        """setup object to test"""
        self.ll = UnorderedList()
        #create a list with max index 3
        self.ll.add("ett")
        self.ll.add("två")
        self.ll.add("tre")

    #insert, set, get, index_of och remove.

    def test_insert(self):
        """test exceptions in method insert"""
        #test insert value at index 4
        with self.assertRaises(AttError):
            self.ll.insert("fjärde värdet", 4)

    def test_set(self):
        """test exception in method set """
        #test replace at index 4.
        with self.assertRaises(AttError):
            self.ll.set("new fourth value", 4)

    def test_get(self):
        """test exception in method get """
        #test get data from index 4
        with self.assertRaises(OutOfIndex):
            self.ll.get(4)

    def test_index_of(self):
        """test exception method index_of"""
        #test with random value
        with self.assertRaises(NoValue):
            self.ll.index_of("find me")

    def test_remove(self):
        """test exception method remove"""
        #test with no value
        with self.assertRaises(NoValue):
            self.ll.remove("remove me")
        #add the value
        self.ll.add("remove me")
        with self.assertRaises(NoValue):
            #remove the value. should result in fail in test.
            self.ll.remove("remove me")

if __name__ == '__main__':
    unittest.main(verbosity=3)
