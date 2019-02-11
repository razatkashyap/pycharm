import turtle
from turtle import Turtle, Screen

screen = Screen()
t = Turtle("turtle")
t.speed(0)


def dragg(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x,y))
    t.goto(x,y)
    t.ondrag(dragg)

def clickright(x, y):
    global  a
    a
    t.clear()

def leftcl(x, y):
    t.color("red")
    t.pensize(a)

def main():
    turtle.listen()
    t.ondrag(dragg)
    turtle.onscreenclick(clickright, 3)
    turtle.onscreenclick(leftcl, 2)
    screen.mainloop()

main()