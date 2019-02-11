from tkinter import *



root = Tk()

def login():
    print(e1.get())

Label(root, text = "Username").pack(side = LEFT)
e1 = Entry(root).pack(side = RIGHT)

Label(root, text = "Password").pack(side = "left")
e2 = Entry(root).pack(side = RIGHT)

Button(root, text = "Log In", bg = "green", fg = "red", command = login).pack(side=LEFT)

root.mainloop()