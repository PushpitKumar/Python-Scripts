import image

img = image.Image('ER.jpg')
win = image.ImageWin(img.getWidth(),img.getHeight())
img.draw(win)
img.setDelay(1,15) #setDelay(0) turns off animation

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col,row)
        new_red = 255 - p.getRed() #negative of red
        new_green = 255 - p.getGreen() #negative of green
        new_blue = 255 - p.getBlue() #negative of blue
        new_pixel = image.Pixel(new_red,new_green,new_blue)
        img.setPixel(col,row,new_pixel)

img.draw(win)
win.exitonclick()
