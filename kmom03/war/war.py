#! usr/local/bin/env python3
"""
    Main card game.
    Play game.
    Kmom03
"""

from hand import Hand
from deck import Deck
from card import Card

class War():
    """play war game"""

    def __init__(self):
        """war object - a game set"""
        self.playing_cards = []
        self.create_player()
        self.play_game()


    def create_player(self):
        """players with cards from Hand"""
        deck = Deck().shuffle_deck()
        cards1 = deck[:len(deck)//2] #half of deck from 0 to half of length
        cards2 = deck[len(deck)//2:]

        self.player1 = Hand("Player 1", cards1)
        self.player2 = Hand("Player 2", cards2)

    def check_card(self, value1, value2):
        """check values of cards"""
        # print("Här är de spelade korten {korten}".format(korten=self.playing_cards))

        if isinstance(value1, str):
            value1 = self.conv_str(value1)

        if isinstance(value2, str):
            value2 = self.conv_str(value2)

        if value1 > value2:
            print(">> Player 1 wins and picks upp all the cards.\n")

            for card in self.playing_cards:
                self.player1.cards.append(card) #append all the played cards to winner hands.
            print(self.player1)
            print(self.player2)
        elif value2 > value1:
            print(">> Player 2 wins and picks upp all the cards.\n")

            for card in self.playing_cards:
                self.player2.cards.append(card) #append all the played cards to winner hands.
            print(self.player1)
            print(self.player2)

        self.playing_cards.clear() #empty playing cards.

    def conv_str(self, val):
        """return string to corr int"""
        if val == 'knight':
            val = 11
        elif val == 'queen':
            val = 12
        elif val == 'king':
            val = 13
        elif val == 'ace':
            val = 14

        return val


    def play_game(self):
        """play game"""
        i = 0
        while (len(self.player1.cards) > 0) and (len(self.player2.cards) > 0):
                print("> {name} draws {card}\n".format(name=self.player1.name, card=self.player1.cards[i]))
                self.playing_cards.append(self.player1.cards[i])

                input("Press any key to continue.\n")

                print("> {name} draws {card}\n".format(name=self.player2.name, card=self.player2.cards[i]))
                self.playing_cards.append(self.player2.cards[i])

                # print("Här är de spelade korten {korten}".format(korten=self.playing_cards))

                if self.player1.cards[i].suit == self.player2.cards[i].suit:
                    self.check_card(self.player1.cards[i].value, self.player2.cards[i].value)
                elif self.player2.cards[i].suit == self.player1.cards[i].suit:
                    self.check_card(self.player1.cards[i].value, self.player2.cards[i].value)

                input("Press any key to continue.\n")
                self.player1.cards.pop(i)
                self.player2.cards.pop(i)

        self.winner(len(self.player1.cards), len(self.player2.cards))

    def winner(self, len1, len2):
        """return winner"""
        if len1 == 0 and len2 == 0:
            input(">>>>No winner, no more cards. \n>>>>Press any key to end game.")
        elif len1 == 0:
            input(">>>>Player 2 wins!!! \n>>>>Press any key to end game.")
        elif len2 == 0:
            input(">>>>Player 1 wins!!! \n>>>>Press any key to end game.")

game = War()