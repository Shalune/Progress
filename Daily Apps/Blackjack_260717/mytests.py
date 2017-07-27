from Blackjack_260717 import cards

def main():
    tValidateTypes()


def tValidateTypes():
    baseDescription = "valid card type, checked type: "
    types = {"ace", "jack", "queen", "king"}
    c = cards.Card()

    for i in range(1,15):
        types.add(str(i))

    for tType in types:
        myTest(baseDescription + str(tType), c.validateType(tType))


def myTest(description, conditional):
    print("Test for: " + description + " - result = " + str(conditional))


if __name__ == "__main__":
    main()