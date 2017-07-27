
cardsuits = {"c" : "clubs", "d" : "diamonds", "h" : "hearts", "s" : "spades"}
cardvalues = {"ace" : 1, "ace" : 11, "jack" : 10, "queen" : 10, "king" : 10}

class Card:
    suit = None
    type = None


    def __init__(self, suit, type):
        #validate input
        self.suit = suit
        self.type = type





    def value(self):
        if type in cardvalues:
            return cardvalues[type]
        return int(type)