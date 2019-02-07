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

        if value1 > value2:
            print("player 1 win\n")

            self.player1.cards.append(self.playing_cards) #append all the played cards to winner hands.
            print(self.player1)
            print(self.player2)
        elif value2 > value1:
            print("player 2 win\n")
            self.player2.cards.append(self.playing_cards) #append all the played cards to winner hands.
            print(self.player1)
            print(self.player2)

        self.playing_cards.clear() #empty playing cards.



    def play_game(self):
        """play game"""
        i = 0
        while (len(self.player1.cards) > 0) or (len(self.player2.cards) > 0):
                print("{name} draws {card}\n".format(name=self.player1.name, card=self.player1.cards[i]))
                self.playing_cards.append(self.player1.cards[i])

                input("Press any key to continue\n")

                print("{name} draws {card}\n".format(name=self.player2.name, card=self.player2.cards[i]))
                self.playing_cards.append(self.player2.cards[i])

                print("Här är de spelade korten {korten}".format(korten=self.playing_cards))

                if self.player1.cards[i].suit == self.player2.cards[i].suit:
                    self.check_card(self.player1.cards[i].value, self.player2.cards[i].value)
                    print("här var det lika suits {s} och {ss}".format(s=self.player1.cards[i].suit, ss=self.player2.cards[i].suit))
                elif self.player2.cards[i].suit == self.player1.cards[i].suit:
                    self.check_card(self.player1.cards[i].value, self.player2.cards[i].value)
                    print("här var det lika suits {s} och {ss}".format(s=self.player1.cards[i].suit, ss=self.player2.cards[i].suit))
                input("Press any key to continue\n")
                self.player1.cards.pop(i)
                self.player2.cards.pop(i)



        # while (len(self.player1.cards) > 0) or (len(self.player2.cards) > 0):
        #     for card in self.player1.cards:
        #         print("tar bort en {c}".format(c=card))
        #         self.player1.cards.pop()
        #     for ca in self.player2.cards:
        #         print("tar bort från2 {c}".format(c=ca))
        #         self.player2.cards.pop()



game = War()
# print(game.play_game())
