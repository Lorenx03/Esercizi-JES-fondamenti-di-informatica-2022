from jes4py import *


img = makePicture(pickAFile())


def func(A):
    v = 0
    pixs = getPixels(A)
    for i in range(len(pixs)):
        v = 0
        for j in range(len(pixs)):
            if getRed(pixs[i]) == (getGreen(pixs[j]) + getBlue(pixs[j])):
                v = v + 1

        if v == len(pixs):
            return True

    return False
        
    


    
