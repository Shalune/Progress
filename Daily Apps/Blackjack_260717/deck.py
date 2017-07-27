from Blackjack_260717 import cards
import random


class Deck:
    cards = []
    drawnCards = []
    numPacks = 0


    def __init__(self, numPacks = 1):
        self.numPacks = numPacks
        self.createPacks()


    def createPacks(self, numPacks = 0):
        if numPacks == 0:
            numPacks = self.numPacks
        for i in range(1, numPacks):
            self.createOnePack()

    def createOnePack(self):
        for suit in cards.cardsuits:
            for type in cards.cardvalues:
                self.cards.add(cards.Card(suit, type))
            for type in range(2,10):
                self.cards.add(cards.Card(suit, type))


    def drawCard(self):
        drawnCard = random.choice(self.cards)
        self.cards.remove(drawnCard)
        self.drawnCards.add(drawnCard)
        return drawnCard


    def checkReset(self):
        if len(cards) == 0:
            self.cards = self.drawnCards
            self.drawnCards = []
