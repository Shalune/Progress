from Blackjack_260717 import cards
from Blackjack_260717 import deck

yesno = {"y" : True, "n" : False}
playAgainPrompt = "Would you like you play another hand? (y/n)\n"
invalidYNOptionPrompt = "That's not a valid option, enter y or n \n\n"
statusPlayerHandText = "You are currently holding:\n"
statusDealerShowingText = "The dealer is currently showing\n"
playerTurnPrompt = "Would you like to hit or stay?\nType \"hit\" or \"stay\"\n"
invalidPlayOptionPrompt = "That's not a valid option."
hitstay = {"hit" : True, "stay" : False}

maxHandScore = 21


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
    dealerHand = drawNewHand(playDeck)
    while(True):
        printGameStatus(playerHand, dealerHand)
        print("score1 = " + str(scoreHand(playerHand)))
        print("score2 = " + str(scoreHand(playerHand, True)))
        if not playerHits(playerHand):
            break
        playerHand.append(playDeck.drawCard())
        #inform if loss


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
        print("\n")
    print(statusPlayerHandText)
    for c in playerHand:
        print(c.name())
    print("\n")


def playerHits(playerHand):
    while (True):
        selection = str.lower(input(playerTurnPrompt))
        if selection in hitstay:
            return hitstay[selection]
        else:
            print(invalidPlayOptionPrompt)


def scoreHand(hand, finalScoring = False):
    numAces = 0
    total = 0
    for c in hand:
        if c.type == cards.acename and finalScoring:
            numAces += 1
            total += 1
        else:
            total += c.value()
    if not finalScoring or numAces == 0:
        return total
    else:
        final = total
        for i in range(1,numAces):
            if(final + cards.acebonusvalue <= maxHandScore):
                final += cards.acebonusvalue
            else:
                break
        return final


if __name__ == "__main__":
    main()