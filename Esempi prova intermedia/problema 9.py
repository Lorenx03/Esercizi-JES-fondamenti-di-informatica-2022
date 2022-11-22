from jes4py import *

pic = makePicture(pickAFile())

def func(img, c):
    totalGreen = 0
    
    if c > getWidth(img) or c < 0:
        return -1
    else:
        for y in range(getHeight(img)):
            pix = getPixel(img, c, y)
            totalGreen = totalGreen + getGreen(pix)
    
        return totalGreen


print(func(pic, 50))