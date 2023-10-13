import turtle
import random

s = turtle.getscreen()
t = turtle.Turtle()

t.pen(pensize=3)
t.color("purple")

colors = ["green", "blue", "red", "yellow", "orange"]  # Hier kannst du weitere Farben hinzufügen

for i in range(100, 0, -10):
    t.begin_fill()
    t.color(random.choice(colors))  # Zufällige Farbauswahl aus der Liste "colors"
    
    for _ in range(4):
        t.forward(i)
        t.right(90)
    
    t.end_fill()
    t.penup()
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.pendown()

turtle.done()
