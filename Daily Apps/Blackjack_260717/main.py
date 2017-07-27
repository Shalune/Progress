from Blackjack_260717 import cards
from Blackjack_260717 import deck

yesno = {"y" : True, "n" : False}
playAgainPrompt = "Would you like you play another hand? (y/n)\n"
invalidYNOptionPrompt = "That's not a valid option, enter y or n \n\n"
statusPlayerHandText = "You are currently holding:\n"
statusDealerShowingText = "The dealer is currently showing\n"

def main():
    playDeck = deck.Deck()
    while(True):
        playOneHand(playDeck)
        if not checkPlayAgain():
            return

def checkPlayAgain():
    while(True):
        selection = str.lower(input(playAgainPrompt))
        if selection in yesno:
            return yesno[selection]
        else:
            print(invalidYNOptionPrompt)


def playOneHand(playDeck):
    playerHand = drawNewHand(playDeck)
    printGameStatus(playerHand)


def drawNewHand(playDeck):
    print("playdeck has num cards: " + str(len(playDeck.cards)))
    results = []
    results.append(playDeck.drawCard())
    results.append(playDeck.drawCard())
    return results


def printGameStatus(playerHand, dealerHand = None):
    if not dealerHand == None:
        print(statusDealerShowingText)
        for i in range(1,len(dealerHand)):
            print(dealerHand[i].name())
    print(statusPlayerHandText)
    for c in playerHand:
        print(c.name())


if __name__ == "__main__":
    main()