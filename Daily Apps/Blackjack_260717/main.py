from Blackjack_260717 import cards
from Blackjack_260717 import deck
from Blackjack_260717 import controlmethods

yesno = {"y" : True, "n" : False}
hitstay = {"hit" : True, "stay" : False}
controlTypes = {"input" : "inputPlayerHits", "house" : "housePlayerHits", "ai" : "aiPlayerHits"}

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

textPackage = {"playAgainPrompt" : playAgainPrompt, "invalidYNOptionPrompt" : invalidYNOptionPrompt, "statusPlayerHandText": statusPlayerHandText,
               "statusDealerShowingText" : statusDealerShowingText, "playerTurnPrompt" : playerTurnPrompt,
               "invalidPlayOptionPrompt" :  invalidPlayOptionPrompt, "playerHandBustText" : playerHandBustText,
               "dealerHitsText" : dealerHitsText, "dealerBustText": dealerBustText}

maxHandScore = 21


def main():
    playDeck = deck.Deck()
    while(True):
        playOneHand(playDeck)
        if not checkPlayAgain():
            return


def thingy():
    print ("we done did it")


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
    continueGame = playTurn(playDeck, playerHand, dealerHand, "input")
    if continueGame:
        dealerTurn(playDeck, playerHand, dealerHand, "house")
    else:
        print(playerHandBustText)


def playTurn(playDeck, hand, otherHand, control):
    while (True):
        printGameStatus(hand, otherHand)
        if not doesHit(hand, otherHand, control):
            return True
        hand.append(playDeck.drawCard())
        if handOverMax(hand):
            return False
    return True


def dealerTurn(playDeck, playerHand, dealerHand):
    dealerLost = not playTurn(playDeck, dealerHand, playerHand)
    printGameStatus(playerHand, dealerHand)
    if dealerLost:
        print(dealerBustText)
    else:
        endHand(playerHand, dealerHand)


def doesHit(hand, otherHand, control):
    #return controlmethods.inputPlayerHits(hand, otherHand, hitstay, playerTurnPrompt, invalidPlayOptionPrompt)
    return getattr(controlmethods, controlTypes[control])(hand, otherHand, hitstay, textPackage)


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