#Use for loops to make a turtle draw 1. an equilateral triangle, 2. square, 3. hexagon and 4. octagon.
import turtle

wn = turtle.Screen()
wn.bgcolor('black')

alex = turtle.Turtle()
alex.color('white')

def triangle():
    for i in range(3):
        alex.forward(100)
        alex.left(120)
def square():
    for i in range(4):
        alex.forward(100)
        alex.left(90)
def hexagon():
    for i in range(6):
        alex.forward(100)
        alex.left(60)

def octagon():
    for i in  range(8):
        alex.forward(100)
        alex.left(45)

ask = int(input('Enter 1 for Triangle\n2 for Square\n3 for Hexagon\n4 for Octagon\n'))
if ask == 1:
    triangle()
elif ask == 2:
    square()
elif ask == 3:
    hexagon()
elif ask == 4:
    octagon()
else:
    print('Please Enter a Valid Number!!!')
    exit()
wn.exitonclick()
