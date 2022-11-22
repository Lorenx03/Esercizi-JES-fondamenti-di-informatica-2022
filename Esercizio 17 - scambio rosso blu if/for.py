file = pickAFile()

pic = makePicture(file)

height = getHeight(pic)
width = getWidth(pic)


def swapBlueRed(img, H, W):
#@param img: oggetto immagine, immagine di input
#@param H: int, altezza immagine
#@param W: int, larghezza immagine

    for y in range(H):
        for x in range(W):
            pix = getPixel(img,x,y)
            
            col1 = getRed(pix)
            col2 = getBlue(pix)

            if col1 < col2:
                setRed(pix, col2)
                setBlue(pix, col1)



swapBlueRed(pic, height, width)
show(pic)

