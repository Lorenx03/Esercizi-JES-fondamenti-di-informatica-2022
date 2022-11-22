from jes4py import *

file = pickAFile()

A = makePicture(file)

C = makeColor(254,0,0)

S = 45

def diagonaleContene(A,C,S):
    i = 0

    for x in range(getWidth(A)):
        pix = getPixel(A, x, x)
        print(pix)
        if getColor(pix) == C:
            i += 1

    if i > S:
        return true
    else:
        return false


print(diagonaleContene(A, C, S))

input()