import turtle
wn = turtle.Screen()
wn.bgcolor('black')
bob=turtle.Turtle()
bob.color('white')
bob.speed(0)
bob.backward(150)
for _ in range(131):
    bob.forward(300)
    bob.right(180-(180/131))
wn.exitonclick()
