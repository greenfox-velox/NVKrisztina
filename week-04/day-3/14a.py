# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r1.png]
# divide the canvas into 4 parts and repeat the pattern.
# reproduce this: [https://github.com/greenfox-velox/velox-syllabus/blob/master/week-04/3-graphics/workshop/r2.png]
# can you make the colors change? make every line a different color.

from tkinter import *

root = Tk()

canvas = Canvas(root, width = '300', height = '300')
canvas.pack()

x = 1
def lineDraw(x):
    for i in range(0, 300, 20):
        canvas.create_line(x + i, x, 300 * x, i, fill = "#B145F3")
        canvas.create_line(x, x + i, x + i, 300 * x, fill = "green")
lineDraw(x)
root.mainloop()
