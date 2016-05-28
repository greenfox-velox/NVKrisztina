from tkinter import *

root = Tk()

canvas = Canvas(root, width = '600', height = '600')
canvas.pack()

def draw_rectangle(x, y, s):
    canvas.create_rectangle(x, y, x + s, y + s)
draw_rectangle(10, 10, 400)
draw_rectangle(10 + 400/3, 10, 400/3)
draw_rectangle(10 + 400/3, 10 + 2 * (400/3), 400/3)
draw_rectangle(10, 10 + 400/3, 400/3)
draw_rectangle(10 + 2 * (400/3), 10 + 400/3, 400/3)

root.mainloop()
