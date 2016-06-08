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

class Floor:

    def __init__(self, x, y):
            self.x = x
            self.y = y
            self.type = 'Floor'

    def draw(self):
        canvas.create_image(self.x * 72, self.y * 72, anchor = NW, image = photo0)

class Wall:

    def __init__(self, x, y):
            self.x = x
            self.y = y
            self.type = 'Wall'

    def draw(self):
        canvas.create_image(self.x * 72, self.y * 72, anchor = NW, image = photo1)

class Coordinates:

    def __init__(self):
        self.map1 = [[0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
        [0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
        [1, 1, 1, 0, 0, 1, 0, 0, 0, 1]]

    def putFloorAndWallCoordinatesInaList(self):
        out = []
        for x in range(10):
            for y in range(10):
                if self.map1[y][x] == 0:
                    floor = Floor(x, y)
                    out.append(floor)
                else:
                    wall = Wall(x, y)
                    out.append(wall)
        return out

    def gameScreenDraw(self):
        a = self.putFloorAndWallCoordinatesInaList()
        for i in a:
            i.draw()

coordinates = Coordinates()
coordinates.gameScreenDraw()


master.mainloop()
