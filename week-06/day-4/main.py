from tkinter import *
import random

master = Tk()

canvas = Canvas(master, width = '720', height = '780')
canvas.pack()

photo0 = PhotoImage(file = "floor.png")
photo1 = PhotoImage(file = "wall.png")
photo2 = PhotoImage(file = "hero-down.png")
photo3 = PhotoImage(file = "hero-right.png")
photo4 = PhotoImage(file = "hero-left.png")
photo5 = PhotoImage(file = "hero-up.png")
photo6 = PhotoImage(file = "skeleton.png")
photo7 = PhotoImage(file = "boss.png")

class Tile:

    def __init__(self, x, y, type, image):
            self.x = x
            self.y = y
            self.type = type
            self.image = image

    def draw(self):
        canvas.create_image(self.x * 72, self.y * 72, anchor = NW, image = self.image)

class Floor(Tile):

    def __init__(self, x, y):
        super(Floor, self).__init__(x, y, 'Floor', photo0)

class Wall(Tile):

    def __init__(self, x, y):
        super(Wall, self).__init__(x, y, 'Wall', photo1)

class Map:

    def __init__(self):
        self.map1 = [[0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
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

map = Map()
map.gameScreenDraw()
map.getFloorCoordinates()

placeTaken = []

class Draw():

    def draw(self):
        canvas.create_image(self.playerposition[0], self.playerposition[1], anchor = NW, image = self.image)

class Character():

    def __init__(self, playerposition, image, HP, DP, SP):
        self.playerposition = playerposition
        self.image = image
        self.randomNumberList = []
        self.HP = HP
        self.DP = DP
        self.SP = SP
        self.T = Text(master, height = 2, width = 70)
        self.T.place(x = 5, y = 720)

    def printPoints(self):
        self.T.insert(INSERT, 'HP: ', self.HP)
        self.T.insert(INSERT, self.HP)
        self.T.insert(INSERT, ' | DP: ', self.DP)
        self.T.insert(INSERT, self.DP)
        self.T.insert(INSERT, ' | SP: ', self.SP)
        self.T.insert(INSERT, self.SP)

    def draw(self):
        canvas.create_image(self.playerposition[0], self.playerposition[1], anchor = NW, image = self.image)

class Enemy(Character):

    def __init__(self, playerposition, image, HP, DP, SP):
        super(Enemy, self).__init__(playerposition, image, HP, DP, SP)
        self.randomPositionGenerator()
        self.draw()

    def randomPositionGenerator(self):
        self.randomNumberList = []
        global placeTaken
        x = random.randint(0, 10)
        self.randomNumberList.append(x)
        z = random.randint(0, 10)
        self.randomNumberList.append(z)
        if self.randomNumberList in map.getFloorCoordinates() and self.randomNumberList not in placeTaken and self.randomNumberList != [0, 0]:
            placeTaken = placeTaken + [self.randomNumberList]
            self.playerposition[0] = x * 72
            self.playerposition[1] = z * 72
        else:
            self.randomPositionGenerator()

class Skeleton(Enemy):

    def __init__(self, playerposition):
        super(Skeleton, self).__init__(playerposition, photo6, self.calculate() * 2, self.calculate() / 2, self.calculate())
        self.T.place(x = 10, y = 720)
        self.T.insert(INSERT, 'Skeleton ' )
        self.printPoints()

    def calculate(self):
        return random.randint(1, 6)

class Boss(Enemy):

    def __init__(self, playerposition):
        super(Boss, self).__init__(playerposition, photo7, self.calculate() * 2 + self.calculate(), self.calculate() / 2 + self.calculate() / 2, self.calculate())
        self.T.place(x = 500, y = 720)
        self.T.insert(INSERT, 'Boss ' )
        self.printPoints()

    def calculate(self):
        return random.randint(1, 6)

class Hero(Character):

    def __init__(self, playerposition):
        super(Hero, self).__init__(playerposition, photo2, self.calculate() * 3 + 20, self.calculate() * 2, self.calculate() + 5)
        self.T.place(x = 300, y = 720)
        self.T.insert(INSERT, 'Hero ' )
        self.printPoints()

    def calculate(self):
        return random.randint(1, 6)

    # def battle(self):

    def containAbsoltePlayerpositionParts(self):
        absolutePlayerposition = 0
        absolutePlayerposition = self.playerposition[0] // 72
        return absolutePlayerposition

    # def containAbsoltePlayerpositionParts1(self):
        # output = []
        # absolutePlayerposition = 0
        # absolutePlayerposition = self.playerposition[0] // 72
        # output.append(absolutePlayerposition)
        # return absolutePlayerposition

    def absolutePlayerpositionUp(self):
        output = []
        output.append(self.containAbsoltePlayerpositionParts())
        absolutePlayerposition = self.playerposition[1] // 72
        absolutePlayerposition = absolutePlayerposition + 1
        output.append(absolutePlayerposition)
        return output

    def absolutePlayerpositionDown(self):
        output = []
        output.append(self.containAbsoltePlayerpositionParts())
        absolutePlayerposition = self.playerposition[1] // 72
        absolutePlayerposition = absolutePlayerposition - 1
        output.append(absolutePlayerposition)
        return output

    def absolutePlayerpositionRight(self):
        output = []
        absolutePlayerposition = self.containAbsoltePlayerpositionParts()
        absolutePlayerposition = absolutePlayerposition + 1
        output.append(absolutePlayerposition)
        absolutePlayerposition = self.playerposition[1] // 72
        output.append(absolutePlayerposition)
        return output

    def absolutePlayerpositionLeft(self):
        output = []
        absolutePlayerposition = self.containAbsoltePlayerpositionParts()
        absolutePlayerposition = absolutePlayerposition - 1
        output.append(absolutePlayerposition)
        absolutePlayerposition = self.playerposition[1] // 72
        output.append(absolutePlayerposition)
        return output

    def containMovementParts(self):
        map.gameScreenDraw()
        boss.draw()
        skeleton.draw()
        skeleton1.draw()
        skeleton2.draw()
        hero.draw()

    def move_down(self):
        if self.playerposition[1] != 9 * 72 and self.absolutePlayerpositionUp() in map.getFloorCoordinates():
            self.playerposition[1] = self.playerposition[1] + 72
            self.image = photo2
            self.containMovementParts()
        else:
            self.playerposition[1] = self.playerposition[1]
            self.image = photo2
            self.containMovementParts()

    def move_right(self):
        if self.playerposition[0] != 9 * 72 and self.absolutePlayerpositionRight() in map.getFloorCoordinates():
            self.playerposition[0] = self.playerposition[0] + 72
            self.image = photo3
            self.containMovementParts()
        else:
            self.playerposition[0] = self.playerposition[0]
            self.image = photo3
            self.containMovementParts()

    def move_left(self):
        if self.playerposition[0] != 0 and self.absolutePlayerpositionLeft() in map.getFloorCoordinates():
            self.playerposition[0] = self.playerposition[0] - 72
            self.image = photo4
            self.containMovementParts()
        else:
            self.playerposition[0] = self.playerposition[0]
            self.image = photo4
            self.containMovementParts()

    def move_up(self):
        if self.playerposition[1] != 0 and self.absolutePlayerpositionDown() in map.getFloorCoordinates():
            self.playerposition[1] = self.playerposition[1] - 72
            self.image = photo5
            self.containMovementParts()
        else:
            self.playerposition[1] = self.playerposition[1]
            self.image = photo5
            self.containMovementParts()

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
