from jes4py import *

width = 500
height = 500
pic = makeEmptyPicture(width, height)


def disegnaRombo(picture, H, W, color):
#@param picture: picture, input image
#@param H: int, height of the canvas
#@param W: int, width of the canvas
    for x in range(0, int(width/2)):
        y = int(height/2) - x
        pix = getPixel(picture, x, y)
        setColor(pix, color)

    for x in range(int(width/2), width):
        y = x - int(height/2)
        pix = getPixel(picture, x, y)
        setColor(pix, color)

    for x in range(0, int(width/2)):
        y = int(height/2) + x
        pix = getPixel(picture, x, y)
        setColor(pix, color)

    for x in range(int(width/2), width):
        y = (height-1) - (x-int(height/2))
        pix = getPixel(picture, x, y)
        setColor(pix, color)


def disegnaQuadrato(picture, H, W, color):
    #@param picture: picture, input image
    #@param H: int, height of the canvas
    #@param W: int, width of the canvas
    for x in range(int(width/4), int((width/2)+(width/4))):
        pix = getPixel(picture, x, int(height/4))
        setColor(pix, color)

    for y in range(int(height/4), int((height/2)+(height/4))):
        pix = getPixel(picture, int(width/4), y)
        setColor(pix, color)

    for x in range(int(width/4), int((width/2)+(width/4))):
        pix = getPixel(picture, x, int((height/2)+(height/4)))
        setColor(pix, color)

    for y in range(int(height/4), int((height/2)+(height/4))):
        pix = getPixel(picture, int((width/2)+(width/4)), y)
        setColor(pix, color)


disegnaRombo(pic, height, width, green)
disegnaQuadrato(pic, height, width, red)
addOval(pic, int(height/4), int(width/4), int(width/2), int(height/2), blue)

show(pic)
input()