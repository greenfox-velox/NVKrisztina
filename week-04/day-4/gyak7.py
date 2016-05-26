from tkinter import *

root = Tk()

canvas = Canvas(root, width = '586', height = '586', bg = "yellow")
canvas.pack()

def drawLines(x):
    if x <= 100:
        return 0
    else:
        return canvas.create_line(x - x, x, 3 * x, x)
        return canvas.create_line(x - x, 2 * x, 3 * x, 2 * x)
        return canvas.create_line(x, x - x, x, 3 * x)
        return canvas.create_line(2 * x, x - x, 2 * x, 3 * x)
        return drawLines(x + 10)
drawLines(196)
# return drawLines(x - 1)

root.mainloop()
