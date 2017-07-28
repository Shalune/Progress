from Blackjack_260717 import cards
from Blackjack_260717 import deck
from Blackjack_260717 import controlmethods

yesno = {"y" : True, "n" : False}
hitstay = {"hit" : True, "stay" : False}

dealerHitsOn = 16

playAgainPrompt = "Would you like you play another hand? (y/n)\n"
invalidYNOptionPrompt = "That's not a valid option, enter y or n \n\n"
statusPlayerHandText = "You are currently holding:\n"
statusDealerShowingText = "The dealer is currently showing\n"
playerTurnPrompt = "Would you like to hit or stay?\nType \"hit\" or \"stay\"\n"
invalidPlayOptionPrompt = "That's not a valid option."
playerHandBustText = "Bust!\nYour hand is over 21. Dealer wins.\n"
dealerHitsText = "Dealer hits.\n\n"
dealerBustText = "Dealer went bust. You win!\n\n"

gameEndText1 = "The game is over. Your hand = "
gameEndText2 = "   Dealer's hand = "
gameEndText3 = "\n\n"
playerWinText = "You won!\n\n"
dealerWinText = "Dealer wins.\n\n"

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
    continueGame = playerTurn(playDeck, playerHand, dealerHand)
    if continueGame:
        dealerLost = not dealerTurn(playDeck, playerHand, dealerHand)
        printGameStatus(playerHand, dealerHand)
        if dealerLost:
            print(dealerBustText)
        else:
            endHand(playerHand, dealerHand)
    else:
        print(playerHandBustText)


def playerTurn(playDeck, playerHand, dealerHand):
    while (True):
        printGameStatus(playerHand, dealerHand)
        if not playerHits(playerHand, dealerHand):
            return True
        playerHand.append(playDeck.drawCard())
        print("TEMP - drew card")
        if handOverMax(playerHand):
            return False
    return True


def dealerTurn(playDeck, playerHand, dealerHand):
    while (True):
        if scoreHand(dealerHand, True) <= dealerHitsOn or scoreHand(dealerHand) <= dealerHitsOn:
            dealerHits(playDeck, dealerHand)
            if handOverMax(dealerHand):
                return False
        else:
            return True
    return True


def playerHits(playerHand, dealerHand):
    return controlmethods.inputPlayerHits(playerHand, dealerHand, hitstay, playerTurnPrompt, invalidPlayOptionPrompt)


def dealerHits(playDeck, dealerHand):
    print (dealerHitsText)
    dealerHand.append(playDeck.drawCard())


def endHand(playerHand, dealerHand):
    playerScore = scoreHand(playerHand, True)
    dealerScore = scoreHand(dealerHand, True)
    print(gameEndText1 + str(playerScore) + gameEndText2 + str(dealerScore) + gameEndText3)
    if playerScore > dealerScore:
        print(playerWinText)
    else:
        print(dealerWinText)


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


def handOverMax(hand):
    return scoreHand(hand) > maxHandScore


if __name__ == "__main__":
    main()