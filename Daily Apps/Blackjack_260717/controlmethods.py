


def inputPlayerHits(playerHand, dealerHand, hitstay, textPackage):
    while (True):
        selection = str.lower(input(textPackage["playerTurnPrompt"]))
        if selection in hitstay:
            return hitstay[selection]
        else:
            print(textPackage["invalidPlayOptionPrompt"])

def housePlayerHits(playerHand, dealerHand, hitstay, textPackage):
    while (True):
        if selection in hitstay:
            return hitstay[selection]
        else:
            print(textPackage["invalidPlayOptionPrompt"])

def aiPlayerHits(playerHand, dealerHand, hitstay, textPackage):
    while (True):
        selection = str.lower(input(textPackage["playerTurnPrompt"]))
        if selection in hitstay:
            return hitstay[selection]
        else:
            print(textPackage["invalidPlayOptionPrompt"])