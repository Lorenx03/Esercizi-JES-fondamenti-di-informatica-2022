from jes4py import *

file = pickAFile()

pic = makePicture(file)

allPixels = getPixels(pic)

# print (allPixels)

for i in range(0, len(allPixels)):
    currentRed = getRed(allPixels[i])
    setRed(allPixels[i], currentRed * 0.5)
    print ("working on pixel n", i)

show(pic)

writePictureTo(pic, "/Users/lorenzo/Downloads/immagineModificata.jpeg")

input()