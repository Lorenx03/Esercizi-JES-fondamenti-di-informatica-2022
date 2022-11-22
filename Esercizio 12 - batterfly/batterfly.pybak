file = pickAFile()
pict = makePicture(file)

height = getHeight(pict)
width = getWidth(pict)

halfWidth = width/2
halfHeight = height/2

def batterfly(pic):
# @param pic: picture; immagine di input

    for y in range(0, int(halfHeight)):
        for x in range(int(halfWidth), width):
            pixTopLeft = getPixel(pic, x, y)
            pixBottomRight = getPixel(pic, x-halfWidth, y+halfHeight)

            pixBottomRightColor = getColor(pixBottomRight)
            pixTopLeftColor = getColor(pixTopLeft)

            setColor(pixBottomRight, pixTopLeftColor)
            setColor(pixTopLeft, pixBottomRightColor)

            repaint(pic)

            
batterfly(pict)