from tkinter import *

root = Tk()

canvas = Canvas(root, width = '600', height = '600')
canvas.pack()

def draw_triangle(x, y, s):
    canvas.create_polygon([x, y, x + s, y, x + s / 2, y + ((3 ** (1 / 3)) / 2) * s], outline = 'black', fill = 'white')

def draw_fractal(x, y, size):
    draw_triangle(x, y, size)
    if size > 5:
        draw_fractal(x, y, size/2)
        draw_fractal(x + size/2, y, size/2)
        draw_fractal(x + size/4, y + ((size/4) * 1.45), size/2)
draw_fractal(0, 0, 500)
root.mainloop()
