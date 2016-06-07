from tkinter import *

master = Tk()

canvas = Canvas(master, width = '720', height = '720')
canvas.pack()

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


def putFloorAndWallCoordinatesInaList():
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
    out = []
    for x in range(10):
        for y in range(10):
            if map1[y][x] == 0:
                floor = Floor(x, y)
                out.append(floor)
            else:
                wall = Wall(x, y)
                out.append(wall)
    return out

a = putFloorAndWallCoordinatesInaList()
