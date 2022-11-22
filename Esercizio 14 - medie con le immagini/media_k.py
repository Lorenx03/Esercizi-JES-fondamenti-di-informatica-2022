from jes4py import *

file = pickAFile()

pic = makePicture(file)

height = getHeight(pic)
width = getWidth(pic)

limit = 200

def mediaRed(img,k):
    totalRed = 0
    numOfPixels = height*k

    for y in range(0,height):
        for x in range(0,k):
            totalRed += getRed(getPixel(img,x,y))
    
    avgRed = totalRed/numOfPixels
    return avgRed


print ("average red in this picture:", mediaRed(pic,limit))
