#Draw a star using python's turtle module
import turtle

window = turtle.Screen()
window.bgcolor('black')
tess = turtle.Turtle()
tess.color('white')

for _ in range(5):
    tess.forward(200)
    tess.right(144)
window.exitonclick()
