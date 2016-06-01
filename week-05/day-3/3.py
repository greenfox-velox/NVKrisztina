# Write a Person class that has a name and a birth_date property
# It should raise an error if the birthdate is less than 0 or more than 2016
class Person:

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    def personal_data(self):
        if int(self.birth_date) < 0 or int(self.birth_date) > 2016:
            raise ValueError('invalid number')

person1 = Person('Geza', '2014')

person1.personal_data()
