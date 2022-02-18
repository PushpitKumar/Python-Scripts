import turtle

sides = int(input('Enter number of sides of polygon:'))
length = input('Enter length of a side of polygon:')
color = input('Enter color of your turtle:')
fill_color = input('Enter fill color of your turtle:')

window = turtle.Screen()
window.bgcolor('black')
tess = turtle.Turtle()

tess.color(color)
tess.fillcolor(fill_color)

tess.begin_fill()

for i in range(sides):
    tess.forward(length)
    tess.left(360/sides)

tess.end_fill()
window.exitonclick()
