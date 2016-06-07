
from tkinter import *

master = Tk()

canvas = Canvas(master, width = '720', height = '720')
canvas.pack()

photo0 = PhotoImage(file = "floor.png")
photo1 = PhotoImage(file = "wall.png")
photo2 = PhotoImage(file = "hero-down.png")
photo3 = PhotoImage(file = "hero-right.png")
photo4 = PhotoImage(file = "hero-left.png")
photo5 = PhotoImage(file = "hero-up.png")
# label = Label(image=photo)
# label.image = photo
# label.pack()

# canvas.create_image(0, 0, anchor = NW, image=photo0)
# canvas.create_image(0, 0, anchor = NW, image=photo1)

def gameScreen():

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
            if map1[j][i] == 0:
                canvas.create_image(i * 72, j * 72, anchor = NW, image = photo0)
            else:
                canvas.create_image(i * 72, j * 72, anchor = NW, image = photo1)

gameScreen()

playerposition = [0, 0]
canvas.create_image(playerposition[0], playerposition[1], anchor = NW, image = photo2)

def move_down(event):
    if playerposition[1] != 9 * 72:
        gameScreen()
        playerposition[1] = playerposition[1] + 72
        canvas.create_image(playerposition[0], playerposition[1], anchor = NW, image = photo2)
    else:
        gameScreen()
        playerposition[1] = playerposition[1]
        canvas.create_image(playerposition[0], playerposition[1], anchor = NW, image = photo2)

master.bind("<Down>", move_down)

def move_right(event):
    if playerposition[0] != 9 * 72:
        gameScreen()
        playerposition[0] = playerposition[0] + 72
        canvas.create_image(playerposition[0], playerposition[1], anchor = NW, image = photo3)
    else:
        gameScreen()
        playerposition[0] = playerposition[0]
        canvas.create_image(playerposition[0], playerposition[1], anchor = NW, image = photo3)

master.bind("<Right>", move_right)

def move_left(event):
    if playerposition[0] != 0:
        gameScreen()
        playerposition[0] = playerposition[0] - 72
        canvas.create_image(playerposition[0], playerposition[1], anchor = NW, image = photo4)
    else:
        gameScreen()
        playerposition[0] = playerposition[0]
        canvas.create_image(playerposition[0], playerposition[1], anchor = NW, image = photo4)

master.bind("<Left>", move_left)

def move_up(event):
    if playerposition[1] != 0:
        gameScreen()
        playerposition[1] = playerposition[1] - 72
        canvas.create_image(playerposition[0], playerposition[1], anchor = NW, image = photo5)
    else:
        gameScreen()
        playerposition[1] = playerposition[1]
        canvas.create_image(playerposition[0], playerposition[1], anchor = NW, image = photo5)

master.bind("<Up>", move_up)


master.mainloop()
