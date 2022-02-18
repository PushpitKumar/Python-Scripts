import turtle

window = turtle.Screen()
window.bgcolor('black')

tess = turtle.Turtle()
tess.shape('turtle')
tess.color('white')
tess.pensize(3)
tess.up() #can also write tess.penup() i.e turtle will no longer draw lines on the canvas but can leave stamps
distance = 5
for _ in range(30):
    tess.stamp() #leaves an impression on the canvas
    tess.forward(distance)
    tess.right(24)
    distance = distance + 2
tess.color('blue') #The final position is the real turtle i.e the rest are just stamps
window.exitonclick()
