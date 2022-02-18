#Write a program to draw a face of a clock
import turtle

window = turtle.Screen()
window.bgcolor('lightgreen')
alex = turtle.Turtle()
alex.shape('turtle')
alex.color('blue')
alex.up()

for _ in range(12):
    alex.forward(200)
    alex.stamp()
    alex.down()
    alex.backward(30)
    alex.up()
    alex.backward(170)
    alex.right(30)
window.exitonclick()
