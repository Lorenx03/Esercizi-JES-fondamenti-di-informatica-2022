file = pickAFile()

def ShowCorners(f):
# @param f: string; percorso file selezionato dall'utente
    pic = makePicture(f)
    allPixels = getPixels(pic)
    print (allPixels[0])
    print (allPixels[len(allPixels)-1])


ShowCorners(file)