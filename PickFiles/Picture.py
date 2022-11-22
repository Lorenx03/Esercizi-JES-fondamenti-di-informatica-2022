def pickAndShow():
  myFile = pickAFile()
  myPict = makePicture(myFile)
  show(myPict)
  
def showNamed(f):
  myPict = makePicture(f)
  show(myPict)