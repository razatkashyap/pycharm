import turtle
from turtle import *

# tim = turtle.Turtle()
# tim.color("black")
# tim.shape("turtle")
# tim.pensize(4)
#
# def up():
#     tim.setheading(90)
#     tim.forward(100)
#
# def down():
#     tim.setheading(270)
#     tim.forward(100)
#
# def left():
#     tim.setheading(180)
#     tim.forward(100)
#
# def right():
#     tim.setheading(0)
#     tim.forward(100)
#
# screen = Screen()
#
# screen._listen()
#
# screen.onkey(up, "Up")
# screen.onkey(down, "Down")
# screen.onkey(left, "Left")
# screen.onkey(right, "Right")
#
# screen.mainloop()

tim = turtle.Turtle()
tim.shape("turtle")
tim.color("green")
tim.pensize(4)
tim.speed(5)


tim.begin_fill()
tim.circle(50)
tim.end_fill()