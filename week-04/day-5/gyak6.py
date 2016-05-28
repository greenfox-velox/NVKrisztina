from tkinter import *

root = Tk()

canvas = Canvas(root, width = '600', height = '600')
canvas.pack()

def polygon(x, y, s)
    canvas.create_polygon([x, y, x + s, y], fill='white', outline='black')



root.mainloop()
