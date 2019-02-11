from openpyxl import *
from tkinter import *



wb = load_workbook("Book2.xlsx")
sheet = wb.active

my_list = []

def checkData():
    username = e1.get()
    password = e1.get()

    for x in sheet.iter_rows(min_row=2, min_col=1, max_row=5):
        for i in x:
            print(i.value)

root = Tk()


e1 = Entry(root)
e2 = Entry(root)
e1.pack()
e2.pack()

Button(root, text = "login", command = checkData).pack()

mainloop()