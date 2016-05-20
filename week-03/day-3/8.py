class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet():
        print(self.first_name + self.last_name)

class Student(Person):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.grades = []

    def add_grades(self, grades):
        self.grades.append(grades)

    def salute(self):
        summa = 0
        for n in self.grades:
            summa = n + summa
        aver = summa / len(self.grades)
        print(self.first_name + self.last_name + str(aver))

s1 = Student('Eva', 'Stone')

s1.add_grades(5)
s1.salute()
