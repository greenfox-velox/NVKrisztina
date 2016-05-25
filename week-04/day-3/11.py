# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *

root = Tk()

canvas = Canvas(root, width = '300', height = '300')
canvas.pack()
z = 100
color = 660200
def drawRectangle(z, color):
    for i in range(300, 0, -5):
        z = i
        color = color + i
        color2 = '#' + str(color)
        rectangle = canvas.create_rectangle(300/2 - z/2, 300/2 - z/2, 300/2 - z/2 + z, 300/2 - z/2 + z, fill=color2)
drawRectangle(z, color)

root.mainloop()
