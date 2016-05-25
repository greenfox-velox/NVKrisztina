from tkinter import *

root = Tk()

canvas = Canvas(root, width = '300', height = '300')
canvas.pack()

def drawRectangle(x, y):
    a = 1
    a = a * 2
    for i in range(1, 70, 10):
        a = i * 2
        rectangle = canvas.create_rectangle(i, i, a, a, fill = "#B145F3")
drawRectangle(1, 1)

root.mainloop()
