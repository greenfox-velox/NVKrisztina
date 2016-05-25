from tkinter import *

root = Tk()

canvas = Canvas(root, width = '300', height = '300')
canvas.pack()

def drawRectangle(x, y):
    for i in range(2, 201, 10):
        x = i
        y = i
        rectangle = canvas.create_rectangle(x, y, x + 10, y + 10, fill = "#B145F3")

drawRectangle(20, 20)

root.mainloop()
