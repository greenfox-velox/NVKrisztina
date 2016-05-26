from tkinter import *

root = Tk()

canvas = Canvas(root, width = '586', height = '586', bg = "yellow")
canvas.pack()


def draw(x, y, z, k):
    canvas.create_line(x - x, y, 3 * x, y)
    canvas.create_line(x - x, 2 * y, 3 * x, 2 * y)
    canvas.create_line(x, y - y, x, 3 * y)
    canvas.create_line(2 * x, y - y, 2 * x, 3 * y)
draw(196, 196, 196, 196)

def draw2(x, y, z, k):
    canvas.create_line(x - x, y, 3 * x, y)
    canvas.create_line(x - x, 2 * y, 3 * x, 2 * y)
    canvas.create_line(x, y - y, x, 3 * y)
    canvas.create_line(2 * x, y - y, 2 * x, 3 * y)
draw(196/3, 196 + 196/3, 196/3, 196 + 196/3)

root.mainloop()
