
cardsuits = {"c" : "clubs", "d" : "diamonds", "h" : "hearts", "s" : "spades"}
cardvalues = {"ace" : 1, "ace" : 11, "jack" : 10, "queen" : 10, "king" : 10}

class Card:
    suit = None
    type = None


    def __init__(self, suit, type):
        #validate input
        self.suit = suit
        self.type = type


    def validateType(self, type):
        try:
            int(type)
            return True
        except ValueError:
            return self.specialType(type)


    def value(self):
        if self.specialType(self.type):
            return cardvalues[self.type]
        return int(self.type)


    def specialType(self, type):
        if type in cardvalues:
            return True
        return False