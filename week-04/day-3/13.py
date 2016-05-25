# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

from tkinter import *

root = Tk()

canvas = Canvas(root, width = '300', height = '300')
canvas.pack()

x = 1
y = 1
def lineDraw(x, y):
    for i in range(0, 300, 20):
        canvas.create_line(x, y + i, 150, 150)
        canvas.create_line(x + i, y, 150, 150)
        canvas.create_line(300 * x, y + i, 150, 150)
        canvas.create_line(x + i, 300 * y, 150, 150)
lineDraw(x, y)

root.mainloop()
