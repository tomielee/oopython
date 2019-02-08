#!/usr/bin/env python3
""" Module for unittests """

import unittest
from war import War
from hand import Hand
from deck import Deck

class TestWar(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    def setUp(self):
        """ Create object for all tests """
        self.testgame = War()

    def tearDown(self):
        """ Remove dependencies after test """
        self.testgame = None

    def test_conv_str(self):
        """ Test staticmethod. conv_str. Should return integer"""
        self.assertIsInstance(self.testgame.conv_str('knight'), int)

    def test_if_card_in_hand(self):
        """ Test method. card in hand. Should return bool val false """
        self.testgame.player1.cards = []
        self.testgame.player2.cards = []
        self.assertFalse(self.testgame.if_card_in_hand())


class TestDeck(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    def setUp(self):
        """ Create object for all tests """
        self.testdeck = Deck()

    def tearDown(self):
        """ Remove dependencies after test """
        self.testdeck = None

    def test_deck(self):
        """Test if length of new Deck object is 56."""
        result = Deck()
        self.assertIs(len(result.deck), 56)

    def test_deck_new_values(self):
        """Test if correct value in deck list"""
        result = self.testdeck.deck[1]
        self.assertEqual(repr(result), "2 of diamonds")

class TestHand(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    def setUp(self):
        """ Create object for all tests """
        self.testhand = Hand('Namnet', [1, 2, 3])

    def tearDown(self):
        """ Remove dependencies after test """
        self.testhand = None

    def test_hand(self):
        """Test return __repr__ from Hand object """
        self.assertEqual(repr(self.testhand), "Namnet has: 3 cards in hand.")


if __name__ == '__main__':
    unittest.main(verbosity=3)
