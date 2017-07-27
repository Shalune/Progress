from Blackjack_260717 import cards

def main():
    tValidateTypes()
    print("\n")
    tValidateSuits()


def tValidateTypes():
    baseDescription = "valid card type, checked type: "
    types = {"ace", "jack", "queen", "king"}
    c = cards.Card()

    for i in range(-1,15):
        types.add(str(i))
        #types.add(i)

    for tType in types:
        myTest(baseDescription + str(tType), c.validateType(tType))


def tValidateSuits():
    baseDescription = "valid card suit, checked suit: "
    suits = {"c", "d", "h", "s", "q", "clown car"}
    c = cards.Card()

    for i in range(-2,2):
        suits.add(str(i))

    for tSuit in suits:
        myTest(baseDescription + str(tSuit), c.validateSuit(tSuit))


def myTest(description, conditional):
    print("Test for: " + description + " - result = " + str(conditional))


if __name__ == "__main__":
    main()