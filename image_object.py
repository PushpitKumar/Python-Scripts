import image

img = image.Image('ER.jpg')

print(img.getWith())
print(img.getHeight())

p = img.getPixel(30,50) #Get pixel at column 30 and row 50
print(p.getRed(),p.getGreen(),p.getBlue())
