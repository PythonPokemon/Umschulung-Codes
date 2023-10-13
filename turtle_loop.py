import turtle
import random

s = turtle.getscreen()
t = turtle.Turtle()

t.pen(pensize=3)

t.color("purple")

colors = ["green", ]

for i in range(100, 0, -10):
    t.begin_fill()
    t.color