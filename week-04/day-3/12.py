# create a 300x300 canvas.
# fill it with a checkerboard pattern.

from tkinter import *

root = Tk()

canvas = Canvas(root, width = '300', height = '300')
canvas.pack()

a = 37
x = 1
def checkerBoard(x):
    for i in range(1, 301, 37):
        for j in range(2, 9, 2):
            x = i
            a = 37
            rectangle = canvas.create_rectangle(x, x, x + a, x + a, fill = "black")
            rectangle = canvas.create_rectangle(x + a * j, x, x + a * (j + 1), x + a, fill = "black")
            rectangle = canvas.create_rectangle(x, x + a * j, x + a, x + a * (j + 1), fill = "black")
checkerBoard(x)

root.mainloop()

"""
canvas_size = 400
canvas = Canvas(root, width=canvas_size, height=canvas_size)
canvas.pack()

size = canvas_size//8
for i in range(8):
    for j in range(8):
        x = i * size
        y = j * size
        color = 'white'
        if (i+j) % 2 == 0:
            color = 'black'
        canvas.create_rectangle(x, y, x+size, y+size, fill = "black")
root.mainloop()
"""
