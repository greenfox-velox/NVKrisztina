from tkinter import *

root = Tk()

canvas = Canvas(root, width = '600', height = '600')
canvas.pack()

def circle(x, y, s):
    canvas.create_oval(x, y, x + s, y + s, outline='black')

def fractal(x, y, s):
    circle(x, y, s)
    if s > 5:
        fractal(x + x, y + y, s/2)
        # fractal(x + x, y + y, s/2)

fractal(50, 50, 400)
mainloop()
