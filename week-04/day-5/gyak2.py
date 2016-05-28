from tkinter import *

root = Tk()

canvas = Canvas(root, width = '600', height = '600')
canvas.pack()

def draw_triangle(x, y, s):
    canvas.create_polygon([x, y, x + s, y, x + s / 2, y + ((3 ** (1 / 3)) / 2) * s], outline = 'black', fill = 'white')
draw_triangle(0, 0, 500)
draw_triangle(0, 0, 500/2)
draw_triangle(500/2, 0, 500/2)
draw_triangle(500/4, (500/4) * 1.45, 500/2)


mainloop()




# draw_triangle(10 + 500/2, 10 + ((3 ** (1 / 3)) / 2) * 500, 500/2)


"""
def draw_fractal(x, y, size):
    draw_triangle(x, y, size)
    third = size / 3
    half = size / 2
    if size > 5:
        draw_fractal(x, y, half)
        # draw_fractal(x + half, y, half)
        # draw_fractal(x + half, y + half, half)

draw_fractal(10, 10, 500)
"""


"""
def draw_rectangle(x, y, s):
    canvas.create_rectangle(x, y, x + s, y + s, fill='green')

def draw_fractal(x, y, size):
    draw_rectangle(x, y, size)
    third = size / 3
    if size > 5:
        draw_fractal(x + third, y, third)
        draw_fractal(x + third, y + 2 * third, third)
        draw_fractal(x, y + third, third)
        draw_fractal(x + 2 * third, y + third, third)

draw_fractal(10, 10, 500)
"""
