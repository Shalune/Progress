import math


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


def rotateVec2D(vec, rotateByDegrees):
    result = [0,0]
    angleInRad = degreesToRad(rotateByDegrees)
    result[0] = (vec[0] * math.cos(angleInRad)) + (vec[1] * math.sin(angleInRad))
    result[1] = (vec[0] * -math.sin(angleInRad)) + (vec[1] * math.cos(angleInRad))
    return result


def degreesToRad(degrees):
    return degrees * (math.pi / 180)