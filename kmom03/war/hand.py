#! usr/local/bin/env python3
"""
    Player hand.
    Kmom03
"""
from deck import Deck

class Hand():
    """create player hand"""

    def __init__(self, name, cards):
        """constructor for hand/player. holding deck obj."""

        self.name = name
        self.cards = cards

    def __repr__(self):
        """return number of cards"""
        # return "{name} has {num} cards in hand.".format(name=self.name, num=len(self.cards))
        return "the cards {cards}.".format(cards=self.cards)
