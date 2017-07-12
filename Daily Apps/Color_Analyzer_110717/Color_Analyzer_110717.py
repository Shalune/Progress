from tkinter import *
import math


hexToDecimal = {'1' : '1', '2' : '2', '3' : '3', '4' : '4',
                '5' : '5', '6' : '6', '7' : '7', '8' : '8',
                '9' : '9', '0' : '0', 'A' : '11', 'B' : '12',
                'C' : '13', 'D' : '14', 'E' : '15', 'F' : '16'}
huePrefix = 'hue = '
lightnessPrefix = 'lightness = '
saturationPrefix = 'saturation = '

def analyze(colorEntry, results):
   input = colorEntry.get()
   color = getColor(input)
   analyzeColor(color, results)

def getColor(input):
    if input.count(",") > 0:
        return getRGBColor(input)
    else:
        return getHexColor(input)

def getRGBColor(input):
    input.replace(',','')
    return input.split(',')


def getHexColor(input):
    input.upper()
    input = convertHexToDecimal(input)
    result = []
    for i in range(len(input) / 2):
        result.append((int(input[i]) * 16) + int(input[i + 1]))
    return result


def convertHexToDecimal(hex):
    result = []
    for c in hex:
        result.append(hexToDecimal[c])
    return result


def analyzeColor(color, results):
    output = analyzeHue(color) + "\n"
    output += analyzeLightness(color) + "\n"
    output += analyzeSaturation(color)
    results['text'] = output


def analyzeSaturation(color):

    return

def analyzeLightness(color):
    total = 0
    for c in color:
        total += int(color[c])
    return lightnessPrefix + (total/3)


def analyzeHue(color):
    return

def boxProduct(cVec1, cVec2, cVec3):
    return


def redVector():
    return [0,1]


def blueVector():
    ratio = math.tan(math.pi / 6)
    o = 1
    a = o * ratio
    unitVector = normalizeVector(a, o)
    unitVector[1] *= -1
    return unitVector


def greenVector():
    ratio = math.tan(math.pi / 6)
    o = 1
    a = o * ratio
    unitVector = normalizeVector(a, o)
    unitVector[0] *= -1
    return unitVector


def yellowVector():
    return

def orangeVector():
    return

def purpleVector():
    return


def normalizeVector(x, y):
    magnitude = math.sqrt(math.pow(x,2) + math.pow(y,2))
    return [x/magnitude, y/magnitude]


window = Tk()
colorEntry = Entry(window)
submitButton = Button(window, text="Analyze")
results = Label(window, text='Enter a color')
submitButton['command'] = analyze(colorEntry, results)


colorEntry.pack()
results.pack()
submitButton.pack()
window.mainloop()
