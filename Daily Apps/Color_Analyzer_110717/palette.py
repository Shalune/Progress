from Color_Analyzer_110717.lina import *
from enum import Enum

class PaletteType(Enum):
    ANALAGOUS = 1
    TRIAD = 2
    COMPLIMENTARY = 3

hueShiftCodes = {PaletteType.ANALAGOUS : [-12, -6, 6, 12],
                 PaletteType.TRIAD : [0, 120,240],
                 PaletteType.COMPLIMENTARY : [180]}


def createPalette(baseColor, paletteType):
    result = [baseColor]
    for shiftBy in hueShiftCodes[paletteType]:
        result.append(hueShift(baseColor, shiftBy))
    return result


def hueShift(color, shiftDegrees):
    result = rotateVec2D([color[0], color[1]], shiftDegrees)
    result.append(color[2])
    return result

