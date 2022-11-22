from jes4py import *

H = 500

img = makeEmptyPicture(H,H)

red = makeColor(255,0,0)

x = 0

for y in range(0, H):
    pix = getPixel(img,x,y)
    setColor(pix, red)
    x = x+1

x=H

for y in range(0, H):
    x = x-1
    pix = getPixel(img, x, y)
    setColor(pix, red)

y = H

for x in range(int(H/2), H):
    y -= 1
    pix = getPixel(img, x, y)
    setColor(pix, red)

y = H

for x in range(int(H/2), 0, -1):
    y -= 1
    pix = getPixel(img, x, y)
    setColor(pix, red)


show(img) 

input()