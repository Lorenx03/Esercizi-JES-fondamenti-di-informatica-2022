from jes4py import *

pic = makePicture(pickAFile())

def getLum(pix):
    return (getRed(pix) + getGreen(pix) + getBlue(pix))


def trovaEquiLum(P, k):
    width = getWidth(pic)
    height = getHeight(pic)

    redRow = 0

    for y in range(0, width):
        redRow = 0
        for x in range(0, height):
            redRow = redRow + getRed(getPixel(P, x, y))
        
    if redRow == k:
        return true
    else:
        return false


    
    


