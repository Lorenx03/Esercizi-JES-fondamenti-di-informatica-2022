from turtle import width
from jes4py import *

file = pickAFile()

img = makePicture(file)

height = getHeight(img)
width = getWidth(img)

numOfPixels = height*width

pixels = getPixels(img)

totalRed = 0

for i in range(0, len(pixels)):
    totalRed += getRed(pixels[i])

avgRed = totalRed/numOfPixels

print ("average red in this picture:" , avgRed)
