import gspread
from oauth2client.service_account import ServiceAccountCredentials
from tkinter import *
import time
import os

gatherOptions = ["Day", "Week"]
getFromSectionsDaily = ["Tonwrite", "unplanned"]
getFromSectionsWeekly = ["Week"]
todoSheet = None

def main():
    global todoSheet
    todoSheet = loadTodoSheet()
    createUI(todoSheet)


def createUI(todoSheet):
    window = Tk()
    option = StringVar(window)
    option.set(gatherOptions[0])
    dropOptions = OptionMenu(window, option, *gatherOptions)
    button = Button(window, text="gather done stuffs")
    button['command'] = lambda: buttonPress(option, todoSheet)
    dropOptions.pack()
    button.pack()
    window.mainloop()


def loadTodoSheet():
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('sheetscred.json', scope)
    client = gspread.authorize(credentials)
    return client.open('_odot prototype').sheet1


def buttonPress(option, todoSheet):
    printDoneTasks(option.get(), todoSheet)


def printDoneTasks(option, todoSheet):
    printSection = False
    for i in range(1,todoSheet.row_count):
        if isEmptyRow(todoSheet, i):
            break
        if isNewSection(todoSheet, i):
            printSection = shouldPrintSection(todoSheet, i, option)
        if todoSheet.row_values(i)[1] == 'Done' and printSection:
            print(todoSheet.row_values(i)[0])


def shouldPrintSection(todoSheet, i, option):
    if option == "Day":
        for findVal in getFromSectionsDaily:
            if todoSheet.cell(i+1,1).value.find(findVal) > -1:
                return True
    elif option == "Week":
        for findVal in getFromSectionsWeekly:
            if todoSheet.cell(i+1,1).value.find(findVal) > -1:
                return True
    return False


def isNewSection(todoSheet, i):
    if todoSheet.cell(i,1).value == " ":
        if todoSheet.cell(i+1,1).value.find("--") > -1:
            return True
    return False


def isEmptyRow(todoSheet, i):
    for j in range(1,10):
        if todoSheet.cell(i,j).value != '':
            return False
    return True


if __name__ == "__main__":
    main()