from Blackjack_260717 import cards
from Blackjack_260717 import deck

yesno = {"y" : True, "n" : False}

def main():
    playDeck = deck.Deck()
    while(True):
        playOneHand(playDeck)
        if not checkPlayAgain():
            return

def checkPlayAgain():
    while(True):
        selection = str.lower(input("Would you like you play another hand? (y/n)\n"))
        if selection in yesno:
            return yesno[selection]
        else:
            print("That's not a valid option, enter y or n \n\n")


def playOneHand(playDeck):
    playerHand = drawNewHand(playDeck)


def drawNewHand(playDeck):
    results = []
    results.append(playDeck.drawCard())
    results.append(playDeck.drawCard())
    return results


if __name__ == "__main__":
    main()