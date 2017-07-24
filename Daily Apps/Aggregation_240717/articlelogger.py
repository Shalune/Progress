from tkinter import *
import os
from lxml.html import fromstring
import time
import requests

targetDir = 'C:' + os.path.join(os.environ["HOMEPATH"], 'Desktop\\notebook\\_logged\\')
newsLogFile = '_log news.txt'



def logNews(inputEntry):
    inputString = inputEntry.get()
    if isWebAddress(inputString):
        logNewsFromWeb(inputString)
    else:
        logNewsFromFile(inputString)


def logNewsFromWeb(inputString):
    targetFile = open(targetDir + newsLogFile, "a")
    if isinstance(inputString, type(newsLogFile)):
        checkMultipleAddresses(inputString, targetFile)
    else:
        logNewsManyWebsites(inputString, targetFile)
    targetFile.close()


def checkMultipleAddresses(inputString, targetFile):
    if inputString.count('\n') > 0:
        parsedString = inputString.split('\n')
        logNewsManyWebsites(parsedString, targetFile)
    else:
        logNewsOneWebsite(inputString, targetFile)


def logNewsManyWebsites(inputString, targetFile):
    for line in inputString:
        logNewsOneWebsite(line, targetFile)


def logNewsOneWebsite(line, targetFile):
    line = line.replace(' ', '')
    if isWebAddress(line):
        targetFile.write(getFormatedEntryFromWebsite(line))


def getFormatedEntryFromWebsite(webAddress):
    title = fromstring(requests.get(webAddress).content).findtext('.//title')
    #title = lxml.html.parse(webAddress).find(".//title").text
    date = dateLine(webAddress)
    return title + ' - ' + date + '\n' + webAddress + '\n\n'

def logNewsFromFile(inputString):
    file = open(inputString, "r+")
    logNewsFromWeb(file)
    file.close()
    wipeFile(inputString)


def wipeFile(inputString):
    file = open(inputString, "r+")
    file.truncate()


def isWebAddress(inputString):
    if inputString.find('http') == 0:
        return True
    return False


def dateLine(webAddress):
    return 'date saved: ' + time.strftime("%d/%m/%Y")

window = Tk()
inputEntry = Entry(window)
newsButton = Button(window, text="News")
newsButton['command'] = lambda: logNews(inputEntry)

inputEntry.pack()
newsButton.pack()
window.mainloop()