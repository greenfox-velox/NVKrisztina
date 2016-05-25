# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.

from tkinter import *

root = Tk()

canvas = Canvas(root, width = '300', height = '300')
canvas.pack()

redLine = canvas.create_line(100, 100, 200, 100, fill="red")
greenLine = canvas.create_line(100, 100, 100, 200, fill="green")
blackLine = canvas.create_line(100, 200, 200, 200)
yellowLine = canvas.create_line(200, 100, 200, 200, fill="yellow")
root.mainloop()
