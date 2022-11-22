myPict = makePicture(pickAFile())

def schiarisciDueVolte(pict): 
# @param pict: Picture
  
  allPix = getPixels(pict)
  
  for i in range(0, len(allPix)):
    col = getColor(allPix[i])
    lightCol = makeLighter(col)  
    lighterCol = makeLighter(lightCol)  
    setColor(allPix[i], lighterCol)
  
  show(pict) # Aggiunto per verificare risultato finale
  

schiarisciDueVolte(myPict)
