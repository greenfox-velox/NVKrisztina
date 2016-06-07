from tkinter import *

master = Tk()

canvas = Canvas(master, width = '720', height = '720')
canvas.pack()

photo0 = PhotoImage(file = "floor.png")
photo1 = PhotoImage(file = "wall.png")
# label = Label(image=photo)
# label.image = photo
# label.pack()

# canvas.create_image(0, 0, anchor = NW, image=photo0)
# canvas.create_image(0, 0, anchor = NW, image=photo1)

map1 = [[0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
[0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
[0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
[0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
[0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
[1, 1, 1, 0, 0, 1, 0, 0, 0, 1]]

for i in range(10):
    for j in range(10):
        if map1[i][j] == 0:
            canvas.create_image(i * 72, j * 72, anchor = NW, image=photo0)
        else:
            canvas.create_image(i * 72, j * 72, anchor = NW, image=photo1)

master.mainloop()
