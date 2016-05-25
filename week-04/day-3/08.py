# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width = '300', height = '300')
canvas.pack()

def drawRectangle(x, y):
    rectangle = canvas.create_rectangle(x, y, x + 50, y + 50)
drawRectangle(10, 20)
drawRectangle(30, 100)
drawRectangle(160, 200)

root.mainloop()
