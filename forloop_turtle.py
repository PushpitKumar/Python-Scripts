import turtle

window = turtle.Screen()
alex = turtle.Turtle()

for color in ['yellow','blue','green','red']:
    alex.color(color)
    alex.forward(100)
    alex.left(90)

window.exitonclick()
