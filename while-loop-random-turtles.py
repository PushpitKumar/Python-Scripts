#Suppose we want to entertain ourselves by watching a turtle wander around randomly inside the screen. When we run the program we want the turtle and program to behave in the following way:
#1. The turtle begins in the center of the screen.
#2. Flip a coin. If it’s heads then turn to the left 90 degrees. If it’s tails then turn to the right 90 degrees.
#3. Take 50 steps forward.
#4. If the turtle has moved outside the screen then stop, otherwise go back to step 2 and repeat.\
#Notice that we cannot predict how many times the turtle will need to flip the coin before it wanders out of the screen, so we can’t use a for loop in this case. In fact, although very unlikely, this program might never end, that is why we call this indefinite iteration.
#Now, probably the only thing that seems a bit confusing to you is the part about whether or not the turtle is still in the screen. But this is the nice thing about programming, we can delay the tough stuff and get something in our program working right away. The way we are going to do this is to delegate the work of deciding whether the turtle is still in the screen or not to a boolean function. Let’s call this boolean function isInScreen We can write a very simple version of this boolean function by having it always return True, or by having it decide randomly, the point is to have it do something simple so that we can focus on the parts we already know how to do well and get them working. Since having it always return True would not be a good idea we will write our version to decide randomly. Let’s say that there is a 90% chance the turtle is still in the window and 10% that the turtle has escaped.
import random
import turtle
def isInScreen(window,turt):
    if random.random() > 0.1:
        return True
    return False

wn = turtle.Screen()
alex = turtle.Turtle()

alex.shape('turtle')
while isInScreen(wn,alex):
    coin = random.randrange(0,2)
    if coin == 0: #heads
        alex.left(90)
    else:
        alex.right(90)
    alex.forward(50)
wn.exitonclick()
