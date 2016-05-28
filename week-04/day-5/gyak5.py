from tkinter import *

root = Tk()

canvas = Canvas(root, width = '600', height = '600')
canvas.pack()

def draw_rectangle(x, y, s):
    canvas.create_rectangle(x, y, x + s, y + s)

def draw_fractals(x, y, s):
    draw_rectangle(x, y, s)
    if s > 5:
        draw_fractals(x + s/3, y, s/3)
        draw_fractals(x + s/3, y + 2 * (s/3), s/3)
        draw_fractals(x, y + s/3, s/3)
        draw_fractals(x + 2 * (s/3), y + s/3, s/3)

draw_fractals(10, 10, 400)

root.mainloop()
