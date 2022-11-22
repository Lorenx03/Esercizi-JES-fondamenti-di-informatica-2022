file = pickAFile()
img = makePicture(file)

imgW = getWidth(img)
imgH = getHeight(img)

red = makeColor(255,0,0)

def Rect(pic, startX, startY, width, height):
    for i in range(startX, height+startY, 1):
        print i
        for j in range(startY, width+startX, 1):
            pix = getPixel(pic, i , j)
            setColor(pix,red)

            repaint(pic)


Rect(img,100,100,50,100)

