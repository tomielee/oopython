"""
Example from föreläsning kmom01. Toss a coin.
"""
import random

class Coin():
    """Create coin object. """

    def __init__(self):
        self.sideup = "heads"

    def toss(self):
        """Return random head och tails"""

        side = random.randint(0, 1)
        if side == 0:
            self.sideup = "heads"
        else:
            self.sideup = "tails"

coin1 = Coin()
coin1.toss()
print(coin1.sideup)
