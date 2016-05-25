# create a 300x300 canvas.
# fill it with four different size and color rectangles.

from tkinter import *

root = Tk()

canvas = Canvas(root, width = '300', height = '300')
canvas.pack()

def drawRectangle(x, y, color):
    rectangle = canvas.create_rectangle(x, y, x + 10, y + 10, fill = color)
drawRectangle(10, 20, "green")
drawRectangle(30, 100, "yellow")
drawRectangle(160, 200, "red")
drawRectangle(210, 250, "black")


root.mainloop()
