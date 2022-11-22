from jes4py import *


img = makePicture(pickAFile())

def func(A):
    pixs = getPixels(A)
    for i in range(len(pixs)):
        for j in range(len(pixs)):
            if getRed(pixs[i]) == (getGreen(pixs[j]) + getBlue(pixs[j])):
                return True
    
    return False

