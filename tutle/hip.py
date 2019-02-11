import turtle
from turtle import Turtle, Screen

t = Turtle()

def up():
    t.setheading(90)
    t.forward(100)

def w():
    t.setheading(90)
    t.forward(100)

def left():
    t.setheading(180)
    t.forward(100)

def a():
    t.setheading(180)
    t.forward(100)

def d():
    t.setheading(0)
    t.forward(100)

def right():
    t.setheading(0)
    t.forward(100)

def s():
    t.setheading(270)
    t.forward(100)

def down():
    t.setheading(270)
    t.forward(100)

screen =Screen()
screen.window_height()
screen.window_width()

screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkeypress(a, "a")
screen.onkeypress(s, "s")
screen.onkeypress(w, "w")
screen.onkeypress(d, "d")

screen.mainloop()