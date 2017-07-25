from Aggregation_240717 import articlelogger
from Aggregation_240717 import coloranalyzer
from Aggregation_240717 import filegatherer
from Aggregation_240717 import imagesorter
from Aggregation_240717 import sheetstodochecker
from Aggregation_240717 import trellochecker

startfunctions = {1 : lambda:articlelogger.main(),
                  2 : lambda:coloranalyzer.main(),
                  3 : lambda:filegatherer.main(),
                  4 : lambda:imagesorter.main(),
                  5 : lambda:sheetstodochecker.main(),
                  6 : lambda:trellochecker.main()}


optiontrings = ["1 = Article Logger",
                "2 = Color Analyzer",
                "3 = File Gatherer",
                "4 = Image Sorter",
                "5 = Google Sheets Todo Checker",
                "6 = Trello Done Checker"]


def main():
    selection = userinput()
    startfunctions[selection]()


def userinput():
    printmenu()
    while(True):
        try:
            selection = int(input("Enter a number selection:\n"))
            if 1 <= selection <= len(startfunctions.keys()):
                break
            else:
                print("That's not one of the options.")
        except ValueError:
            print("Entry must be a number.")
    return selection


def printmenu():
    for line in optiontrings:
        print(line)


if __name__ == "__main__":
    main()