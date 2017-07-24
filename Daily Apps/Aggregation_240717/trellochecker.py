from trello import *
import os


baseDir = 'C:'
keyFrom = baseDir +  os.path.join(os.environ["HOMEPATH"], "Desktop\\scripts\\API keys\\trello.txt")
boardFile = "\\boardname.txt"
cardIndex = "name"

def main():
    apiKey = GetTrelloKey()
    trello = TrelloApi(apiKey)
    cards = trello.lists.get_card(DoneID())
    cardNames = CardNames(cards)
    for c in cardNames:
        print(c)


def GetTrelloKey():
    file = open(keyFrom)
    lines = file.readlines()
    return lines[0]


def BoardID():
    localDir = os.path.dirname(os.path.realpath(__file__))
    file = open(localDir + boardFile)
    lines = file.readlines()
    return lines[0]


def DoneID():
    localDir = os.path.dirname(os.path.realpath(__file__))
    file = open(localDir + boardFile)
    lines = file.readlines()
    return lines[1]


def CardNames(rawCards):
    results = []
    for c in rawCards:
        results.append(FindCardName((c)))
    return results


def FindCardName(card):
    return card[cardIndex]


if __name__ == "__main__":
    main()