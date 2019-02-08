#! usr/local/bin/env python3
"""
    Main card game.
    Play game.
    Kmom03
"""

from hand import Hand
from deck import Deck

class War():
    """play war game"""

    def __init__(self):
        """war object - a game set"""
        self.playing_cards = []
        self.create_player()

    def create_player(self):
        """players with cards from Hand"""
        deck = Deck().shuffle_deck()
        cards1 = deck[:len(deck)//2] #half of deck from 0 to half of length
        cards2 = deck[len(deck)//2:]

        self.player1 = Hand("Player 1", cards1)
        self.player2 = Hand("Player 2", cards2)

    def play_game(self):
        """play game"""

        while self.if_card_in_hand():
            print("> {name} draws {card}\n".format(name=self.player1.name,\
                card=self.player1.cards[0]))
            self.playing_cards.append(self.player1.cards[0])

            input("Press any key to continue.\n")

            print("> {name} draws {card}\n".format(name=self.player2.name, \
                card=self.player2.cards[0]))
            self.playing_cards.append(self.player2.cards[0])


            # if suits are the same, check value of card to set winner.
            if self.player1.cards[0].suit == self.player2.cards[0].suit:
                self.check_card(self.player1.cards[0].value, \
                self.player2.cards[0].value)
            elif self.player2.cards[0].suit == self.player1.cards[0].suit:
                self.check_card(self.player1.cards[0].value, \
                self.player2.cards[0].value)

            input("Press any key to continue.\n")
            self.player1.cards.pop(0)
            self.player2.cards.pop(0)

        self.winner(len(self.player1.cards), len(self.player2.cards))

    @staticmethod
    def winner(len1, len2):
        """return winner"""
        if len1 == 0 and len2 == 0:
            input(">>>>No winner. \n>>>>Press any key to end game.")
        elif len1 == 0:
            input(">>>>Player 2 wins!!! \n>>>>Press any key to end game.")
        elif len2 == 0:
            input(">>>>Player 1 wins!!! \n>>>>Press any key to end game.")

    def check_card(self, value1, value2):
        """check values of cards"""
        # print("Här är de spelade korten {korten}".
        #format(korten=self.playing_cards))

        if isinstance(value1, str):
            value1 = self.conv_str(value1)

        if isinstance(value2, str):
            value2 = self.conv_str(value2)

        if value1 > value2:
            print(">> Player 1 wins and picks upp all the cards.\n")

            for card in self.playing_cards:
                self.player1.cards.append(card)
            print(self.player1)
            print(self.player2)
        elif value2 > value1:
            print(">> Player 2 wins and picks upp all the cards.\n")

            for card in self.playing_cards:
                self.player2.cards.append(card)
            print(self.player1)
            print(self.player2)

        self.playing_cards.clear() #empty playing cards.

    @staticmethod
    def conv_str(val):
        """return string to corr int"""
        if val == 'knight':
            return 11
        elif val == 'queen':
            return 12
        elif val == 'king':
            return 13
        elif val == 'ace':
            return 14


    def if_card_in_hand(self):
        """return true if there are cards in hand"""
        return bool((len(self.player1.cards) > 0) and \
            (len(self.player2.cards) > 0))

# game = War()

if __name__ == '__main__':
    game = War()
    game.play_game()
