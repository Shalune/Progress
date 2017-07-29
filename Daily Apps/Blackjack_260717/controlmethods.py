from Blackjack_260717.main import scoreHand

dealerHitsOn = 16


def inputPlayerHits(hand, otherHand, hitstay, textPackage):
    while (True):
        selection = str.lower(input(textPackage["playerTurnPrompt"]))
        if selection in hitstay:
            return hitstay[selection]
        else:
            print(textPackage["invalidPlayOptionPrompt"])

def housePlayerHits(hand, otherHand, hitstay, textPackage):
    return scoreHand(hand) <= dealerHitsOn

def aiPlayerHits(hand, otherHand, hitstay, textPackage):
    return False