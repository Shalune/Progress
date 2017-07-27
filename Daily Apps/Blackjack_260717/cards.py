
cardsuits = {"c" : "clubs", "d" : "diamonds", "h" : "hearts", "s" : "spades"}
cardvalues = {"ace" : 1, "ace" : 11, "jack" : 10, "queen" : 10, "king" : 10}

class Card:
    suit = None
    type = None


    def __init__(self, suit, type):
        if self.validateType(type) and self.validateSuit(suit):
            self.suit = cardsuits[suit]
            self.type = type
        else:
            print("Attempted to create card with invalid parameters. Type input: "
                  + str(type) + "  Suit input: " + str(suit))


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
        return type in cardvalues


    def validateSuit(self, suit):
        return suit in cardsuits