from jes4py import *

file = pickAFile()

img = makePicture(file)

allpix = getPixels(img)

imgw = getWidth(img)
imgh = getHeight(img)

reverse = makeEmptyPicture(imgw,imgh)


reverseAllPix = getPixels(reverse)

for i in range(1, len(allpix)):
    chang = getColor(allpix[len(allpix)-i])
    setColor(reverseAllPix[i], chang)

show(reverse) 

input()
