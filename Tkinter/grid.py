from tkinter import *


def getAge():
    print(s.get())

v = IntVar
var1 = IntVar
var2 = IntVar

root = Tk()

Label(root, text = "Username").grid(row = 0, column = 0, sticky = E)
Entry(root).grid(row = 0, column = 1)

Label(root, text = "Password").grid(row = 1, column = 0, sticky = E)
Entry(root).grid(row = 1, column = 1)

Radiobutton(root, text = "Male", padx = 10, variable = v, value = 1).grid(row =3, column = 0)
Radiobutton(root, text = "Female", padx = 10, variable = v, value = 2).grid(row =3, column = 1)

Checkbutton(root, text = "Java", variable = var1).grid(row = 4, column = 0)
Checkbutton(root, text = "Python", variable = var2).grid(row = 4, column = 1)

Label(root, text = "Age").grid(row = 5, column = 0, sticky = E)
s = Scale(root, from_= 0, to = 100, orient = HORIZONTAL)
s.grid(row = 5, column = 1)

Button(root, text = "Log In", command = getAge).grid(row = 6, column = 0)
Button(root, text = "Sign Up").grid(row = 6, column = 1)
root.mainloop()