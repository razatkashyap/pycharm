from tkinter import *

def file_open():
    print("File is open")

def file_new():
    print("New file created")

def file_save():
    print("File has saved")

def edit_undo():
    print("Undo has done")

def edit_find():
    print("One match found")

def edit_replace():
    print("Replace is done")

def help_about():
    print("Version 1.0")

root = Tk()

menu = Menu(root)
root.config(menu = menu)
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu = fileMenu)
fileMenu.add_command(label="New", command = file_new)
fileMenu.add_command(label = "Open", command = file_open)
fileMenu.add_command(label = "Save", command = file_save)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command = root.quit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu = editMenu)
editMenu.add_command(label="Undo", command = edit_undo)
editMenu.add_command(label = "Find", command = edit_find)
editMenu.add_command(label = "Replace", command = edit_replace)

helpMenu = Menu(menu)
menu.add_cascade(label = "Help", menu = helpMenu)
helpMenu.add_command(label = "About", command = help_about)


e = Button(root, text = "Log in", bg = "red", fg = "black")
e.grid(row = 4, column = 4)
root.mainloop()