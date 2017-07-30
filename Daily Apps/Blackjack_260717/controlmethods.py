from Blackjack_260717.main import scoreHand
from Blackjack_260717 import deck
from Blackjack_260717 import cards
import copy

dealerHitsOn = 16


def inputPlayerHits(playDeck, hand, otherHand, hitstay, textPackage):
    while (True):
        selection = str.lower(input(textPackage["playerTurnPrompt"]))
        if selection in hitstay:
            return hitstay[selection]
        else:
            print(textPackage["invalidPlayOptionPrompt"])


def housePlayerHits(playDeck, hand, otherHand, hitstay, textPackage):
    return scoreHand(hand) <= dealerHitsOn


def aiPlayerHits(playDeck,hand, otherHand, hitstay, textPackage):
    unseen = unseenCards(playDeck, otherHand)
    #estimate average value on hit
    #estimate opponent's score
    #hit if average hit + hand value > other hand and less than equal 21



def unseenCards(playDeck, otherHand):
    results = copy(playDeck)
    results.append(otherHand[0])
    return results


def averageOnHit(testCards, acesHigh):
    result = 0
    num = 0
    for c in testCards:
        if acesHigh and c.type == cards.acename:
            result += c.value() + cards.acebonusvalue
        else:
            result += c.value()
        num += 1
    result /= num
    return result