from tkinter import *

root = Tk()

canvas = Canvas(root, width = '300', height = '300')
canvas.pack()

def drawRectangle(x, y):
    summa = 0
    for i in range(1, 7, 1):
        a = i * 10
        rectangle = canvas.create_rectangle(summa, summa, summa + a, summa + a, fill = "#B145F3")
        summa += a
drawRectangle(1, 1)

root.mainloop()
