from jes4py import *

file = pickAFile()

pic = makePicture(file)

height = getHeight(pic)
width = getWidth(pic)


def getMinLum(img):
    #@param img: oggetto immagine, immagine di input
    #@return minLum: int, luminosità minima
    pixs = getPixels(img);
    minLum = 255

    for i in range(0, len(pixs)):
        if minLum > round(((getRed(pixs[i]) + getGreen(pixs[i]) + getBlue(pixs[i]))/3)):
            minLum = round((((getRed(pixs[i]) + getGreen(pixs[i]) + getBlue(pixs[i]))/3)))
    
    return minLum


print ("Luminosità media minore:", getMinLum(pic))
