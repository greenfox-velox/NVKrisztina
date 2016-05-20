class Student:

    def __init__(self):
        self.grade = []

    def add_grade(self, grade):
        if grade <= 5 and grade > 0:
            self.grade.append(grade)

    def get_average(self):
        summa = 0
        for n in self.grade:
            summa = n + summa
        aver = summa / len(self.grade)
        print (aver)

student1 = Student()

student1.add_grade(5)
student1.get_average()
