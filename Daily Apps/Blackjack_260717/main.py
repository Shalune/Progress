from Blackjack_260717 import cards

yesno = {"y" : True, "n" : False}

def main():
    while(True):
        playOneHand()
        if not checkPlayAgain():
            return

def checkPlayAgain():
    while(True):
        selection = str.lower(input("Would you like you play another hand? (y/n)\n"))
        if selection in yesno:
            return yesno[selection]
        else:
            print("That's not a valid option, enter y or n \n\n")


def playOneHand():
    return


if __name__ == "__main__":
    main()