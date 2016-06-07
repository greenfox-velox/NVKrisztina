from tkinter import *

master = Tk()

canvas = Canvas(master, width = '720', height = '720')
canvas.pack()

photo = PhotoImage(file = "floor.png")
# label = Label(image=photo)
# label.image = photo
# label.pack()

canvas.create_image(0, 0, anchor = NW, image=photo)

a = 72

map1 = [[[0, 0], [a, 0], [2 * a, 0], [3 * a, 0], [4 * a, 0], [5 * a, 0], [6 * a, 0], [7 * a, 0], [8 * a, 0], [9 * a, 0]],
[[0, a], [a, a], [2 * a, a], [3 * a, a], [4 * a, a], [5 * a, a], [6 * a, a], [7 * a, a], [8 * a, a], [9 * a, a]],
[[0, 2 * a], [a, 2 * a], [2 * a, 2 * a], [3 * a, 2 * a], [4 * a, 2 * a], [5 * a, 2 * a], [6 * a, 2 * a], [7 * a, 2 * a], [8 * a, 2 * a], [9 * a, 2 * a]],
[[0, 3 * a], [a, 3 * a], [2 * a, 3 * a], [3 * a, 3 * a], [4 * a, 3 * a], [5 * a, 3 * a], [6 * a, 3 * a], [7 * a, 3 * a], [8 * a, 3 * a], [9 * a, 3 * a]],
[[0, 4 * a], [a, 4 * a], [2 * a, 4 * a], [3 * a, 4 * a], [4 * a, 4 * a], [5 * a, 4 * a], [6 * a, 4 * a], [7 * a, 4 * a], [8 * a, 4 * a], [9 * a, 4 * a]],
[[0, 5 * a], [a, 5 * a], [2 * a, 5 * a], [3 * a, 5 * a], [4 * a, 5 * a], [5 * a, 5 * a], [6 * a, 5 * a], [7 * a, 5 * a], [8 * a, 5 * a], [9 * a, 5 * a]],
[[0, 6 * a], [a, 6 * a], [2 * a, 6 * a], [3 * a, 6 * a], [4 * a, 6 * a], [5 * a, 6 * a], [6 * a, 6 * a], [7 * a, 6 * a], [8 * a, 6 * a], [9 * a, 6 * a]],
[[0, 7 * a], [a, 7 * a], [2 * a, 7 * a], [3 * a, 7 * a], [4 * a, 7 * a], [5 * a, 7 * a], [6 * a, 7 * a], [7 * a, 7 * a], [8 * a, 7 * a], [9 * a, 7 * a]],
[[0, 8 * a], [a, 8 * a], [2 * a, 8 * a], [3 * a, 8 * a], [4 * a, 8 * a], [5 * a, 8 * a], [6 * a, 8 * a], [7 * a, 8 * a], [8 * a, 8 * a], [9 * a, 8 * a]],
[[0, 9 * a], [a, 9 * a], [2 * a, 9 * a], [3 * a, 9 * a], [4 * a, 9 * a], [5 * a, 9 * a], [6 * a, 9 * a], [7 * a, 9 * a], [8 * a, 9 * a], [9 * a, 9 * a]]]


for i in map1:
    for j in i:
        canvas.create_image(j, anchor = NW, image=photo)


master.mainloop()
