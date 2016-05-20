class Pirate:

    def __init__(self, rum):
        self.rum = rum

    def drink_rum(self):
        self.rum = self.rum + 1

    def hows_goin_mate(self):
        if self.rum >= 5:
            print("Arrr!")

pirate1 = Pirate(6)

pirate1.drink_rum()
pirate1.hows_goin_mate()
