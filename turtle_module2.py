#Draw an equilateral triangle using python's turtle module. Set the name of turtle as tess, prompt the user to enter desired background color, pencolor and pensize.
import turtle

background_color = input('Enter Background Color:')
pencolor = input('Enter Color of Your Turtle:')
pen_size = int(input('Enter pen-size of Your Turtle:'))

window = turtle.Screen()
window.bgcolor(background_color)

tess = turtle.Turtle()
tess.color(pencolor)
tess.pensize(pen_size)

tess.forward(200)
tess.left(120)
tess.forward(200)
tess.left(120)
tess.forward(200)

window.exitonclick()
