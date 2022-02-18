#The program should do all necessary set-up, create the turtle, set the shape to "turtle", and pick up the pen. Then the turtle should repeat the following ten times: go forward 50 pixels, leave a copy of the turtle at the current position, reverse for 50 pixels, and then turn right 36 degrees. After the loop, set the window to close when the user clicks in it.
import turtle

window = turtle.Screen()
window.bgcolor('black')

alex = turtle.Turtle()
alex.color('white')
alex.shape('turtle')
alex.up()

for _ in range(10):
    alex.forward(50)
    alex.stamp()
    alex.backward(50)
    alex.right(36)
alex.color('blue')
window.exitonclick()
