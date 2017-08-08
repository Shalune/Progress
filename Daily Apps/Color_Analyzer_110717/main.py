from Color_Analyzer_110717.lina import *
from Color_Analyzer_110717.palette import *
from tkinter import *
import math
import numpy


hexToDecimal = {'1' : '1', '2' : '2', '3' : '3', '4' : '4',
                '5' : '5', '6' : '6', '7' : '7', '8' : '8',
                '9' : '9', '0' : '0', 'A' : '10', 'B' : '11',
                'C' : '12', 'D' : '13', 'E' : '14', 'F' : '15'}
huePrefix = 'hue = '
lightnessPrefix = 'lightness = '
saturationPrefix = 'saturation = '
palettePrefix = 'generated palette (vector form) = '
colorNameVectorPairs = {'Red' : lambda: redVector(), 'Blue' : lambda: blueVector(), 'Green' : lambda: greenVector(),
                        'Purple' : lambda: purpleVector(), 'Orange' : lambda: orangeVector(), 'Yellow' : lambda: yellowVector()}
RGBscale = 255
colorLoaded = False


def main():
    window = Tk()
    colorEntry = Entry(window)
    submitButton = Button(window, text="Analyze")
    results = Label(window, text='Enter a color')
    submitButton['command'] = lambda: analyze(colorEntry, results)

    colorEntry.pack()
    results.pack()
    submitButton.pack()
    window.mainloop()


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
    for i in range(len(input) // 2):
        result.append((int(input[i*2]) * 16) + int(input[i*2 + 1]))
    return result


def convertHexToDecimal(hex):
    result = []
    for c in hex:
        result.append(hexToDecimal[c])
    return result


def analyzeColor(color, results):
    colorVec = colorToVector(color)
    output = analyzeHue(color, colorVec) + "\n"
    output += analyzeLightness(color) + "\n"
    output += analyzeSaturation(colorVec) + "\n"
    output += generatePalette(colorVec)
    results['text'] = output


def analyzeSaturation(colorVec):
    magnitude = (vectorMagnitude(colorVec) / RGBscale) * 100
    return saturationPrefix + str(math.floor(magnitude)) + '%'


def analyzeLightness(color):
    value = colorLightness(color)
    return lightnessPrefix + str(value * 100) + '%'


def colorLightness(color):
    total = 0
    for c in color:
        total += int(c)
    value = (total / 3) / RGBscale
    return value


def analyzeHue(color, colorVec):
    closestColor = ''
    closestMatch = 0
    for name, vec in colorNameVectorPairs.items():
        #dot = numpy.dot(colorVec, vec())
        dot = dotProduct(colorVec, vec())
        if dot > closestMatch:
            closestMatch = dot
            closestColor = name
    return huePrefix + closestColor


def generatePalette(colorVec):
    #get set of colors from palette
    palette = createPalette(colorVec, PaletteType.ANALAGOUS)
    #print colors with palette prefix
    resultString = palettePrefix + "\n"
    for c in palette:
        resultString += str(c) + "\n"
    return resultString


def colorToVector(color):
    result = [0,0,0]
    result[0] = colorVectorX(color)
    result[1] = colorVectorY(color)
    result[2] = colorVectorZ(color)
    return result


def colorVectorX(color):
    return (redVector()[0] * int(color[0])) + (greenVector()[0] * int(color[1])) + (blueVector()[0] * int(color[2]))


def colorVectorY(color):
    return (redVector()[1] * int(color[0])) + (greenVector()[1] * int(color[1])) + (blueVector()[1] * int(color[2]))


def colorVectorZ(color):
    #find min and return
    return colorLightness(color)


def redVector():
    return [0,1]


def blueVector():
    ratio = math.tan(math.pi / 3)
    o = 1
    a = o * ratio
    unitVector = normalizeVector(a, o)
    unitVector[1] *= -1
    return unitVector


def greenVector():
    ratio = math.tan(math.pi / 3)
    o = 1
    a = o * ratio
    unitVector = normalizeVector(a, o)
    unitVector[0] *= -1
    unitVector[1] *= -1
    return unitVector


def yellowVector():
    ratio = math.tan(math.pi * 4 / 9)
    o = 1
    a = o * ratio
    unitVector = normalizeVector(a, o)
    unitVector[0] *= -1
    return unitVector

def orangeVector():
    ratio = math.tan(math.pi * 2 / 9)
    o = 1
    a = o * ratio
    unitVector = normalizeVector(a, o)
    unitVector[0] *= -1
    return unitVector

def purpleVector():
    ratio = math.tan(math.pi / 3)
    o = 1
    a = o * ratio
    unitVector = normalizeVector(a, o)
    return unitVector





if __name__ == "__main__":
    main()
