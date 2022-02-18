import image

p = image.Pixel(45,76,200)
print(p.getRed())
print(p.getGreen())
print(p.getBlue())

#Change the values of RGB and then print them out
p.setRed(100)
p.setGreen(p.setBlue())
p.setBlue(300)

print(p.getRed())
print(p.getGreen())
print(p.getBlue())
