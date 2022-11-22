height = 200
width = 200

img = makeEmptyPicture(height, width)

black = makeColor(0,0,0)

startDrawX = 0
startDrawY = 0


def disegnaScalini(startX,startY,dim,col):
    numScalini = int((width-startX)/dim)
    ultimoScalinoDim = (width-startX)%dim

    for i in range(0, numScalini):
        for x in range(0,dim):
            pix = getPixel(img, startX+x, startY)
            setColor(pix, col)

        startX = startX + dim

        for y in range(0,dim):
            pix = getPixel(img, startX, startY+y)
            setColor(pix, col)
            
        startY = startY + dim
        
        
        
    for x in range(0,ultimoScalinoDim):
        pix = getPixel(img, startX+x, startY)
        setColor(pix, col)
        
    repaint(img)
    

disegnaScalini(int(startDrawX),int(startDrawY),30,black)