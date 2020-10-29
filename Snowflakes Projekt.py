#!/bin/python3

import turtle
import random
kevin = turtle.Turtle()
turtle.Screen().bgcolor("white")
colours = ["cyan", "purple", "white", "blue"]
kevin.color("cyan")

kevin.penup()
kevin.forward(90)
kevin.left(45)
kevin.pendown()

def branch():
    for i in range(3):
        for i in range(3):
            kevin.forward(30)
            kevin.backward(30)
            kevin.right(45)
        kevin.left(90)
        kevin.backward(30)
        kevin.left(45)
    kevin.right(90)
    kevin.forward(90)
    
for i in range(8):
    branch()
    kevin.left(45)


# kevin.color(random.choice(colours))



