


def inputPlayerHits(playerHand, dealerHand, hitstay, playerTurnPrompt, invalidPlayOptionPrompt):
    while (True):
        selection = str.lower(input(playerTurnPrompt))
        if selection in hitstay:
            return hitstay[selection]
        else:
            print(invalidPlayOptionPrompt)