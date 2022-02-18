#Now we have a working program that draws a random walk of our turtle that has a 90% chance of staying on the screen. We are in a good position, because a large part of our program is working and we can focus on the next bit of work – deciding whether the turtle is inside the screen boundaries or not.
#We can find out the width and the height of the screen using the window_width and window_height methods of the screen object. However, remember that the turtle starts at position 0,0 in the middle of the screen. So we never want the turtle to go farther right than width/2 or farther left than negative width/2. We never want the turtle to go further up than height/2 or further down than negative height/2. Once we know what the boundaries are we can use some conditionals to check the turtle position against the boundaries and return False if the turtle is outside or True if the turtle is inside.
import random
import turtle

def isInScreen(window,turt):
    leftbound = -(window.window_width()/2)
    rightbound = (window.window_width()/2)
    upperbound = (window.window_height()/2)
    lowerbound = -(window.window_height()/2)
    x_coord = turt.xcor()
    y_coord = turt.ycor()
    stillIn = True
    if x_coord > rightbound or x_coord < leftbound:
        stillIn = False
    if y_coord > upperbound or y_coord < lowerbound:
        stillIn = False
    return stillIn

wn = turtle.Screen()
alex = turtle.Turtle()

alex.shape('turtle')
while isInScreen(wn,alex):
    coin = random.randrange(0,2)
    if coin == 0:
        alex.left(90)
    else:
        alex.right(90)
    alex.forward(50)

wn.exitonclick()
#We could have written this program without using a boolean function. You might want to try to rewrite it using a complex condition on the while statement. However, using a boolean function makes the program much more readable and easier to understand. It also gives us another tool to use if this was a larger program and we needed to have a check for whether the turtle was still in the screen in another part of the program. Another advantage is that if you ever need to write a similar program, you can reuse this function with confidence the next time you need it. Breaking up this program into a couple of parts is another example of functional decomposition.
