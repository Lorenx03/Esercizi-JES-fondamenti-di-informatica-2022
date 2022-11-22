file = pickAFile()

pic = makePicture(file)

height = getHeight(pic)
width = getWidth(pic)

limit = 200


def swapBlueRed(img, k):
#@param img: oggetto immagine, immagine di input
#param k: int, limite k
    for y in range(0, height):
        for x in range(0, k):
            pix = getPixel(img,x,y)
            
            col1 = getRed(pix)
            col2 = getBlue(pix)

            setRed(pix, col2)
            setBlue(pix, col1)

            repaint(img)


swapBlueRed(pic,limit)


