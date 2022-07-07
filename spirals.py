"""
A file containing Turtle library to create unique designs

"""

import turtle
import random

''' 
turtle.Screen() returns the list of turtles on the screen
screen.bgcolor() return the background color of the screen
turtle.Turtle() :  the constructor method of class Turtle. it returns an 
instance of the class
.speed() : change the speed of the turtle
'''
screen = turtle.Screen()
screen.bgcolor("black")
a = turtle.Turtle()
a.speed(100)

for i in range(350):
    '''
    (r, b, g) : value of color triples that range from 0 to 255)
    '''
    r = 255
    g = 200
    b = random.randint(200, 255)
    '''
     turtle.colormode is used to return the color mode. In this case, the mode
     255 is chosen
     '''
    turtle.colormode(255)

    if i <= 255:
        a.pencolor(r, g, i)
    a.forward(250)
    a.left(90 + i)
    a.forward(50)
    a.left(-240 - i)

a.penup()
a.goto(-200, -200)
a.pendown()

x = 1
i = 0
while x < 256:
    r = random.randint(0, 255)
    g = 100
    b = 150
    turtle.colormode(255)
    a.pencolor(i, g, b)
    a.pensize(1)
    a.forward(50 + x)
    a.right(91.5)

    x = x + 1
    i = (i + 1) % 255


a.penup()
a.goto(-200, 300)
a.pendown()

for i in range(200):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle.colormode(255)
    a.pencolor(i, i, i)
    a.forward(2 + i / 4)
    a.left(30 - i / 12)

a.penup()
a.goto(350, 350)
a.pendown()

for i in range(350):
    r = random.randint(0, 255)
    g = 238
    b = random.randint(120, 155)
    turtle.colormode(255)
    if i <= 255:
        a.pencolor(i, g, i)
    a.forward(200)
    a.left(45 + i)
    a.backward(75)
    a.left(45 - i)

turtle.done()
