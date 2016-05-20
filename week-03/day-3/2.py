class Car:

    def __init__(self, typo, km):
        self.typo = typo
        self.km = km

    def run(self, number):
        self.number = number * km

my_mazda = Car("mazda", 12000)

print(my_mazda.typo) # "mazda"
print(my_mazda.km) # 12100
