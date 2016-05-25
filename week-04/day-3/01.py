from tkinter import *

root = Tk()

canvas = Canvas(root, width = '300', height = '300')
canvas.pack()

redLine = canvas.create_line(0, 150, 300, 150, fill="red")
greenLine = canvas.create_line(150, 0, 150, 300, fill="green")
root.mainloop()
