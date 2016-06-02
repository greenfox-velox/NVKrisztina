from tkinter import *

root = Tk()

canvas = Canvas(root, width = '600', height = '600')
canvas.pack()

def drawRectangle(z, color):
    for i in range(300, 0, -5):
        z = i
        color = color + i
        color2 = '#' + str(color)
        rectangle = canvas.create_rectangle(300/2 - z/2, 300/2 - z/2, 300/2 - z/2 + z, 300/2 - z/2 + z, fill=color2)
drawRectangle(z, color)

root.mainloop()
