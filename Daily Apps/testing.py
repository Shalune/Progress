from lxml.html import fromstring
import requests
import math
import numpy

input = '255,255,255'
hexInput = 'FF9100'
hexToDecimal = {'1' : '1', '2' : '2', '3' : '3', '4' : '4',
                '5' : '5', '6' : '6', '7' : '7', '8' : '8',
                '9' : '9', '0' : '0', 'A' : '10', 'B' : '11',
                'C' : '12', 'D' : '13', 'E' : '14', 'F' : '15'}

def getRGBColor(input):
    input.replace(',','')
    return input.split(',')

def getColor(input):
    if input.count(",") > 0:
        print('RGB')
    else:
        print('HEX')

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

def colorToVector(color):
    result = [0,0]
    result[0] = colorVectorX(color)
    result[1] = colorVectorY(color)
    return result

def colorVectorX(color):
    r = redVector()[0] * int(color[0])
    g = greenVector()[0] * int(color[1])
    b = blueVector()[0] * int(color[2])
    print('x = ' + str(r) + '   ' + str(g) + '   ' + str(b))
    return r + g + b

def colorVectorY(color):
    r = redVector()[1] * int(color[0])
    g = greenVector()[1] * int(color[1])
    b = blueVector()[1] * int(color[2])
    print('y = ' + str(r) + '   ' + str(g) + '   ' + str(b))
    return r + g + b


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
    return [-1,0]

def orangeVector():
    ratio = math.tan(math.pi / 3)
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

def dotProduct(vec1, vec2):
    result = sum([vec1[i]*vec2[i] for i in range(len(vec1))])
    return result

#def boxProduct(vec1, vec2, vec3):
#    cross = numpy.cross(vec2,vec3)
#    return dotProduct(vec1, cross)

color = getRGBColor(input)
print(redVector())
print(greenVector())
print(blueVector())
#print(int(color[0]))
#print(int(color[1]))
#print(int(color[2]))
print(colorToVector(input))

print(laGrange(redVector(),blueVector(),greenVector()))
print(getHexColor(hexInput))