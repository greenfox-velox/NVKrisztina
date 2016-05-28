from tkinter import *

root = Tk()

canvas = Canvas(root, width = '600', height = '600')
canvas.pack()

def triangle(x, y, s):
    canvas.create_polygon([x, y, x + s, y, x + s/2, y + ((3 ** (1/3)) / 2) * s], outline='black', fill='white')

def fractals(x, y, s):
    triangle(x, y, s)
    if s > 5:
        fractals(x, y, s/2)
        fractals(x + s/2, y, s/2)
        fractals(x + s/4, y + ((3 ** (1/3))/4) * s, s/2)
        # fractals(x + s/4, y + s/2, s/2)

fractals(10, 10, 400)

root.mainloop()
