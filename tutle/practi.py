import turtle
from turtle import *

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.pensize(5)

def up():
    tim.setheading(90)
    tim.forward(100)

def down():
    tim.setheading(270)
    tim.forward(100)

def right():
    tim.setheading(0)
    tim.forward(100)

def left():
    tim.setheading(180)
    tim.forward(100)

screen = Screen()


screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()
screen.bgcolor("green")
screen.mainloop()
