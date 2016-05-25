from tkinter import *

root = Tk()

canvas_size = 400
canvas = Canvas(root, width = canvas_size, height = canvas_size)
canvas.pack()

half = canvas_size // 2

for i in range(0, half + 1, 2):
    canvas.create_line(i, half, half, half-i, fill = "green")
    canvas.create_line(canvas_size-i, half, half, half-i, fill = "green")
    canvas.create_line(i, half, half, half+i, fill = "green")
    canvas.create_line(canvas_size-i, half, half, half+i, fill = "green")

root.mainloop()
