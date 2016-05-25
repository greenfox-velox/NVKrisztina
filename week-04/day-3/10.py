# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# create a loop that draws 20 squares with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width = '300', height = '300')
canvas.pack()
z = 10
def drawRectangle(z):
    for i in range(1, 21):
        z = z + i
        rectangle = canvas.create_rectangle(300/2 - z/2, 300/2 - z/2, 300/2 - z/2 + z, 300/2 - z/2 + z)
        print (rectangle)
drawRectangle(z)

root.mainloop()
