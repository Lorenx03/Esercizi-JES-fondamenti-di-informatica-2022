pic1 = makePicture(pickAFile())
pic2 = makePicture(pickAFile())

def getLum(pix):
    return (getRed(pix) + getGreen(pix) + getBlue(pix))

def trovaEquiLum(P1,P2):
    pixs1 = getPixels(P1)
    pixs2 = getPixels(P2)

    for i in range(0, len(pixs1)):
        for j in range(0, len(pixs2)):
            if getLum(pixs1[i]) == getLum(pixs2[j]):
                return "le due immagini hanno almeno un pix equilum"

    return "Nessuna corrispondenza"

print(trovaEquiLum(pic1, pic2))
