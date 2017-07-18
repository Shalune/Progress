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
    output += analyzeSaturation(colorVec)
    results['text'] = output


def analyzeSaturation(colorVec):
    magnitude = (vectorMagnitude(colorVec) / RGBscale) * 100
    return saturationPrefix + str(math.floor(magnitude)) + '%'

def analyzeLightness(color):
    total = 0
    for c in color:
        total += int(c)
    value = (total/3)/RGBscale*100
    return lightnessPrefix + str(value) + '%'


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

def colorToVector(color):
    result = [0,0]
    result[0] = colorVectorX(color)
    result[1] = colorVectorY(color)
    return result


def colorVectorX(color):
    return (redVector()[0] * int(color[0])) + (greenVector()[0] * int(color[1])) + (blueVector()[0] * int(color[2]))


def colorVectorY(color):
    return (redVector()[1] * int(color[0])) + (greenVector()[1] * int(color[1])) + (blueVector()[1] * int(color[2]))


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


def normalizeVector(x, y):
    magnitude = math.sqrt(math.pow(x,2) + math.pow(y,2))
    return [x/magnitude, y/magnitude]


def dotProduct(vec1, vec2):
    result = sum([vec1[i]*vec2[i] for i in range(len(vec1))])
    return result


def vectorMagnitude(vec):
    result = 0
    for val in vec:
        result += math.pow(val,2)
    return math.sqrt(result)


def subtractVector(vec1,vec2):
    result = []
    for i in range(len(vec1)):
        result.append(vec1[i] - vec2[i])
    return result


def vecXConstant(vec,c):
    result = []
    for i in range(len(vec)):
        result.append(vec[i] * c)
    return result


def laGrange(cVec1, cVec2, cVec3):
    dot1 = dotProduct(cVec3, cVec2)
    dot2 = dotProduct(cVec3, cVec1)
    set1 = vecXConstant(cVec1,dot1)
    set2 = vecXConstant(cVec2,dot2)
    return subtractVector(set1, set2)


if __name__ == "__main__":
    main()
