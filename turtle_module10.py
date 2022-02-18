import turtle

wn = turtle.Screen()
wn.bgcolor('black')

alex = turtle.Turtle()
alex.color('white')
alex.speed(10)

alex.circle(100)
alex.left(90)
alex.forward(100)

for i in range(24):
    alex.right(15)
    alex.forward(100)
    alex.backward(100)
wn.exitonclick()
