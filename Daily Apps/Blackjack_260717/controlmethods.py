from Blackjack_260717.main import scoreHand
from Blackjack_260717.main import maxHandScore
from Blackjack_260717 import deck
from Blackjack_260717 import cards
import copy

dealerHitsOn = 16
assumeStayMinimum = 17
assumeAceHighMax = 5


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
    avgLow = averageOnHit(unseen, False)
    avgHigh = averageOnHit(unseen, True)
    estOtherScore = estimateOpponentsHand(unseen, otherHand)
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


def estimateOpponentsHand(unseen, otherHand):
    showingValue = 0
    numAces = 0
    for c in otherHand:
        if not c == otherHand[0]:
            showingValue += c.value()
            if(c.type == cards.acename):
                numAces += 1

    estimateHidden = 0
    num = 0
    for c in unseen:
        if includeInEstimation(c, showingValue, numAces):
            estimateHidden += c.value
            num += 1
        elif includeAceBonusInEstimation(c, showingValue, numAces):
            estimateHidden += c.value + cards.acebonusvalue
            num += 1
    estimateHidden /= num
    return estimateHidden + showingValue


def includeInEstimation(c, showingValue, numAces):
    if maxHandScore > c.value + showingValue > assumeStayMinimum:
        return True
    if maxHandScore > c.value + showingValue + (cards.acebonusvalue * numAces) > assumeStayMinimum:
        return True
    return False

def includeAceBonusInEstimation(c, showingValue, numAces):
    if c.type == cards.acename:
        if maxHandScore > c.value + cards.acebonusvalue + showingValue > assumeStayMinimum:
            return True
        if maxHandScore > c.value + cards.acebonusvalue + showingValue + (cards.acebonusvalue * numAces) > assumeStayMinimum:
            return True
    return False