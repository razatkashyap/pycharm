from tkinter import *

def kill():
    print("hell")

root = Tk()
Button(root, text = "Button 1", command = kill).grid(row = 2, column = 2)
v = IntVar()
root.mainloop()