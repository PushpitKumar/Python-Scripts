import turtle

def drawsquare(t,s):
    """Make turtle t draw a square of with side s."""
    for i in range(4):
        t.forward(s)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor('white')

alex = turtle.Turtle()
drawsquare(alex,100)

wn.exitonclick()
help(drawsquare) #will display the docstring
