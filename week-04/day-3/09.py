# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width = '300', height = '300')
canvas.pack()

def drawRectangle(z):
    rectangle = canvas.create_rectangle(300/2 - z/2, 300/2 - z/2, 300/2 - z/2 + z, 300/2 - z/2 + z)
drawRectangle(10)
drawRectangle(30)
drawRectangle(50)

root.mainloop()
