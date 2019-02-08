#! usr/local/bin/env python3
"""
    Class object for card game.
    Create deck of 52 cards.
"""
from random import shuffle
from card import Card

class Deck():
    """create a deck with instances from Card()"""

    def __init__(self):
        """constructor for deck object"""

        self.deck = []
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'knight', \
            'queen', 'king', 'ace']
        self.suits = ['diamonds', 'clubs', 'hearts', 'spades']

        self.create_deck()

    def create_deck(self):
        """create a deck"""
        for suit in self.suits:
            for value in self.values:
                self.deck.append(Card(value, suit))

    def shuffle_deck(self):
        """return shuffled list, shuffled deck"""
        shuffle(self.deck)
        return self.deck
