#A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, takes another 100 steps, turns another random amount, etc. A social science student records the angle of each turn before the next 100 steps are taken. Her experimental data is 160, -43, 270, -97, -43, 200, -940, 17, -86. (Positive angles are counter-clockwise.) Use a turtle to draw the path taken by our drunk friend. After the pirate is done walking, print the current heading. Assume that the turtle originally has a heading of 0 and accumulate the changes in heading to print out the final.
import turtle

window = turtle.Screen()
window.bgcolor('black')
pirate = turtle.Turtle()
pirate.color('white')

# move the turtle forward a little so that the whole path fits on the screen
pirate.penup()
pirate.forward(60)
pirate.pendown()

steps = 100
current_heading = 0
turns = [160,-43,270,-97,-43,200,-940,17,-86]

for turn in turns:
    pirate.left(turn)
    pirate.forward(steps)
    current_heading = (current_heading + turn) % 360

print("Pirate's final heading:",current_heading)
window.exitonclick()
   
