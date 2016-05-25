# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width = '300', height = '300')
canvas.pack()

def lineDraw(x, y):
    id = canvas.create_line(x, y, 150, 150)
    return id
lineDraw(2, 3)
lineDraw(100, 50)
lineDraw(260, 100)

root.mainloop()
