import turtle

window = turtle.Screen()
window.bgcolor('black')

alex = turtle.Turtle()
alex.color('white')
alex.pensize(3)

distance = 50
for _ in range(32):
    alex.forward(distance)
    alex.right(90)
    distance = distance + 10

window.exitonclick()
