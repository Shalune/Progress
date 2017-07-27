from Blackjack_260717 import cards
import random


class Deck:
    cards = {}
    drawnCards = {}


    def __init__(self, numPacks):
        for i in range(1,numPacks):
            self.createOnePack()


    def createOnePack(self):
        for suit in cards.cardsuits:
            for type in cards.cardvalues:
                cards.add(cards.Card(suit, type))
            for type in range(2,10):
                cards.add(cards.Card(suit, type))