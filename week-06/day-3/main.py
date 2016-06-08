from tkinter import *
import random

master = Tk()

canvas = Canvas(master, width = '720', height = '720')
canvas.pack()

photo0 = PhotoImage(file = "floor.png")
photo1 = PhotoImage(file = "wall.png")
photo2 = PhotoImage(file = "hero-down.png")
photo3 = PhotoImage(file = "hero-right.png")
photo4 = PhotoImage(file = "hero-left.png")
photo5 = PhotoImage(file = "hero-up.png")
photo6 = PhotoImage(file = "skeleton.png")
photo7 = PhotoImage(file = "boss.png")

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

    def getFloorCoordinates(self):
        coordinatesList = []
        for x in range(10):
            for y in range(10):
                if self.map1[y][x] == 0:
                    coordinatesList.append([x, y])
        return coordinatesList

    def gameScreenDraw(self):
        a = self.putFloorAndWallCoordinatesInaList()
        for i in a:
            i.draw()

coordinates = Coordinates()
coordinates.gameScreenDraw()
coordinates.getFloorCoordinates()

placeTaken = []

class Skeleton:

    def __init__(self, playerposition):
        self.playerposition = playerposition
        self.image = photo6
        self.randomNumberList = []

    def draw(self):
        self.randomNumberList = []
        global placeTaken
        x = random.randint(0, 10)
        self.randomNumberList.append(x)
        z = random.randint(0, 10)
        self.randomNumberList.append(z)
        if self.randomNumberList in coordinates.getFloorCoordinates() and self.randomNumberList not in placeTaken and self.randomNumberList != [0, 0]:
            canvas.create_image(self.randomNumberList[0] * 72, self.randomNumberList[1] * 72, anchor = NW, image = self.image)
            placeTaken = placeTaken + [self.randomNumberList]
        else:
            self.draw()

    def drawAnyway(self):
        canvas.create_image(self.randomNumberList[0] * 72, self.randomNumberList[1] * 72, anchor = NW, image = self.image)


class Boss:

    def __init__(self, playerposition):
        self.playerposition = playerposition
        self.image = photo7
        self.randomNumberList = []

    def draw(self):
        self.randomNumberList = []
        global placeTaken
        x = random.randint(0, 10)
        self.randomNumberList.append(x)
        z = random.randint(0, 10)
        self.randomNumberList.append(z)
        if self.randomNumberList in coordinates.getFloorCoordinates() and self.randomNumberList not in placeTaken and self.randomNumberList != [0, 0]:
            canvas.create_image(self.randomNumberList[0] * 72, self.randomNumberList[1] * 72, anchor = NW, image = self.image)
            placeTakenbyBoss = [self.randomNumberList]
        else:
            self.draw()

    def drawAnyway(self):
        canvas.create_image(self.randomNumberList[0] * 72, self.randomNumberList[1] * 72, anchor = NW, image = self.image)

class Hero:

    def __init__(self, playerposition):
        self.playerposition = playerposition
        self.image = photo2

    def draw(self):
        canvas.create_image(self.playerposition[0], self.playerposition[1], anchor = NW, image = self.image)

    def absolutePlayerpositionUp(self):
        absolutePlayerposition = 0
        output = []
        absolutePlayerposition = self.playerposition[0] // 72
        output.append(absolutePlayerposition)
        absolutePlayerposition = self.playerposition[1] // 72
        if absolutePlayerposition != 0:
            absolutePlayerposition = absolutePlayerposition + 1
        output.append(absolutePlayerposition)
        return output

    def absolutePlayerpositionDown(self):
        absolutePlayerposition = 0
        output = []
        absolutePlayerposition = self.playerposition[0] // 72
        output.append(absolutePlayerposition)
        absolutePlayerposition = self.playerposition[1] // 72
        if absolutePlayerposition != 0:
            absolutePlayerposition = absolutePlayerposition - 1
        output.append(absolutePlayerposition)
        return output

    def absolutePlayerpositionRight(self):
        absolutePlayerposition = 0
        output = []
        absolutePlayerposition = self.playerposition[0] // 72
        if absolutePlayerposition != 0:
            absolutePlayerposition = absolutePlayerposition + 1
        output.append(absolutePlayerposition)
        absolutePlayerposition = self.playerposition[1] // 72
        output.append(absolutePlayerposition)
        return output

    def absolutePlayerpositionLeft(self):
        absolutePlayerposition = 0
        output = []
        absolutePlayerposition = self.playerposition[0] // 72
        if absolutePlayerposition != 0:
            absolutePlayerposition = absolutePlayerposition - 1
        output.append(absolutePlayerposition)
        absolutePlayerposition = self.playerposition[1] // 72
        output.append(absolutePlayerposition)
        return output

    def move_down(self):
        if self.playerposition[1] != 9 * 72 and self.absolutePlayerpositionUp() in coordinates.getFloorCoordinates():
            coordinates.gameScreenDraw()
            boss.drawAnyway()
            skeleton.drawAnyway()
            skeleton1.drawAnyway()
            skeleton2.drawAnyway()
            self.playerposition[1] = self.playerposition[1] + 72
            self.image = photo2
            self.draw()
        else:
            coordinates.gameScreenDraw()
            boss.drawAnyway()
            skeleton.drawAnyway()
            skeleton1.drawAnyway()
            skeleton2.drawAnyway()
            self.playerposition[1] = self.playerposition[1]
            self.image = photo2
            self.draw()

    def move_right(self):
        if self.playerposition[0] != 9 * 72 and self.absolutePlayerpositionRight() in coordinates.getFloorCoordinates():
            coordinates.gameScreenDraw()
            boss.drawAnyway()
            skeleton.drawAnyway()
            skeleton1.drawAnyway()
            skeleton2.drawAnyway()
            self.playerposition[0] = self.playerposition[0] + 72
            self.image = photo3
            self.draw()
        else:
            coordinates.gameScreenDraw()
            boss.drawAnyway()
            skeleton.drawAnyway()
            skeleton1.drawAnyway()
            skeleton2.drawAnyway()
            self.playerposition[0] = self.playerposition[0]
            self.image = photo3
            self.draw()

    def move_left(self):
        if self.playerposition[0] != 0 and self.absolutePlayerpositionLeft() in coordinates.getFloorCoordinates():
            coordinates.gameScreenDraw()
            boss.drawAnyway()
            skeleton.drawAnyway()
            skeleton1.drawAnyway()
            skeleton2.drawAnyway()
            self.playerposition[0] = self.playerposition[0] - 72
            self.image = photo4
            self.draw()
        else:
            coordinates.gameScreenDraw()
            boss.drawAnyway()
            skeleton.drawAnyway()
            skeleton1.drawAnyway()
            skeleton2.drawAnyway()
            self.playerposition[0] = self.playerposition[0]
            self.image = photo4
            self.draw()

    def move_up(self):
        if self.playerposition[1] != 0 and self.absolutePlayerpositionDown() in coordinates.getFloorCoordinates():
            coordinates.gameScreenDraw()
            boss.drawAnyway()
            skeleton.drawAnyway()
            skeleton1.drawAnyway()
            skeleton2.drawAnyway()
            self.playerposition[1] = self.playerposition[1] - 72
            self.image = photo5
            self.draw()
        else:
            coordinates.gameScreenDraw()
            boss.drawAnyway()
            skeleton.drawAnyway()
            skeleton1.drawAnyway()
            skeleton2.drawAnyway()
            self.playerposition[1] = self.playerposition[1]
            self.image = photo5
            self.draw()

def move_up_press_key(event):
    hero.move_up()

master.bind("<Up>", move_up_press_key)

def move_left_press_key(event):
    hero.move_left()

master.bind("<Left>", move_left_press_key)

def move_right_press_key(event):
    hero.move_right()

master.bind("<Right>", move_right_press_key)

def move_down_press_key(event):
    hero.move_down()

master.bind("<Down>", move_down_press_key)



hero = Hero([0, 0])
hero.draw()

skeleton = Skeleton([0, 0])
skeleton.draw()

skeleton1 = Skeleton([0, 0])
skeleton1.draw()

skeleton2 = Skeleton([0, 0])
skeleton2.draw()

boss = Boss([0, 0])
boss.draw()

master.mainloop()
