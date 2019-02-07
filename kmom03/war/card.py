#! usr/local/bin/env python3
"""
    Class for cards.
    For card game. Kmom03
"""

class Card():
    """ Create card """

    def __init__(self, value, suit):
        """constructor for card objeckt. attr: value and suit"""
        self.value = value
        self.suit = suit

    def __repr__(self):
        """return card as a striing"""
        return "{v} of {s}".format(v=self.value, s=self.suit)
