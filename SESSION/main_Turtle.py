# loading module turtle
import turtle
from turtle import *
"""
    Turtle can be moved in four directions.
    
    Method	Parameter	Description
    Turtle()	None	Creates and returns a new turtle object
    forward()	amount	Moves the turtle forward by the specified amount
    backward()	amount	Moves the turtle backward by the specified amount
    right()	angle	Turns the turtle clockwise
    left()	angle	Turns the turtle counterclockwise
    penup()	None	Picks up the turtle’s Pen
    pendown()	None	Puts down the turtle’s Pen
    up()	None	Picks up the turtle’s Pen
    down()	None	Puts down the turtle’s Pen
    color()	Color name	Changes the color of the turtle’s pen
    fillcolor()	Color name	Changes the color of the turtle will use to fill a polygon
    heading()	None	Returns the current heading
    position()	None	Returns the current position
    goto()	x, y	Move the turtle to position x,y
    begin_fill()	None	Remember the starting point for a filled polygon
    end_fill()	None	Close the polygon and fill with the current fill color
    dot()	None	Leave the dot at the current position
    stamp()	None	Leaves an impression of a turtle shape at the current location
    shape()	shapename	Should be ‘arrow’, ‘classic’, ‘turtle’ or ‘circle’
        
    The roadmap for executing a turtle program follows 4 steps:  

    Import the turtle module
    Create a turtle to control.
    Draw around using the turtle methods.
    Run turtle.done().
    
"""

# up()
# goto(-100,100)
# down()

# turtle.Screen()
# TH = turtle.Turtle()
# i = 0
#TH.shape("turtle")


#print(TH.pos())

## create turtle with background color light green
bg = turtle.Screen()
bg.bgcolor("light green")
bg.title("Turtle")
#TH = turtle.Turtle()

# Shape 1: Square
up()
goto(-400, 0)
down()

for i in range(4):
    forward(50)
    right(90)
    
# Shape 2: Hexagone

up()
goto(-300, 0)
down()

i = 0
while (i<6):
    i+=1
    forward(110)
    left(60)
    
# Shape 2.1: Hexagon (update)
up()
goto(0, 0)
down()
num_sides = 8 # numnber of slide
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
    forward(side_length)
    right(angle)


# Shape 3: Star

up()
goto(-100, 0)
down()

right(75)
forward(100)

i=0
for i in range(4):
    right(144)
    forward(100)

# Some amazing Turtle Programs

# 1. Spiral Square Outside In and Inside Out 

up()
goto(100, 0)
down()

def sqrfunc(size):
    for i in range(4):
        forward(size)
        left(90)
        size = size - 5
        

sqrfunc(146)
sqrfunc(126)
sqrfunc(106)
sqrfunc(86)
sqrfunc(66)
sqrfunc(46)
sqrfunc(26)

up()
goto(250, 0)
down()

def sqrfunc(size):
    for i in range(4):
        forward(size)
        left(90)
        size = size + 5
        

sqrfunc(6)
sqrfunc(26)
sqrfunc(46)
sqrfunc(66)
sqrfunc(86)
sqrfunc(106)
sqrfunc(146)

# 2. User Input Pattern 
# Python program to user input pattern
# up()
# goto(350, 0)
# down()

# import time, random
# print ("This program draws shapes based on the number you enter in a uniform pattern.")
# num_str = input("Enter the side number of the shape you want to draw: ")
# if num_str.isdigit():
#     squares = int(num_str)

# angle = 180 - 180*(squares-2)/squares

# up()

# x = 450
# y = 0
# setpos(x, y)

# numshapes = 8
# for x in range(numshapes):
#     turtle.color(random.random(), random.random(), random.random())
#     x += 5
#     y += 5
#     turtle.forward(x)
#     turtle.left(y)
#     for i in range(squares):
#         turtle.begin_fill()
#         turtle.down()
#         turtle.forward(40)
#         turtle.left(angle)
#         turtle.forward(40)
#         print (turtle.pos())
#         turtle.up()
#         turtle.end_fill()

# time.sleep(5)
# #turtle.bye()

# 3. Spiral Helix Pattern

up()
goto(-400, -200)
down()

speed(1)

for i in range(10): #100
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)

# 4. Rainbow Benzene 

# up()
# goto(400, -200)
# down()

# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
# t = turtle.Pen()
# #turtle.bgcolor('black')
# for x in range(360):
#     t.pencolor(colors[x%6])
#     t.width(x//100 + 1)
#     t.forward(x)
#     t.left(59)

turtle.mainloop() # To stop the screen to display  
#done()
exitonclick()