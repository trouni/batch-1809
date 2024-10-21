from datetime import date

class Student:
    # class attribute
    school = 'lewagon'

    # initializer of instance attributes
    def __init__(self, name, age): # Note the `self` parameter
        self.name = name.capitalize()
        self.age = age
        print(__file__)

    # instance method
    def says(self, something):
        print(f'{self.name} says {something}')

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = date.today().year - birth_year
        return cls(name, age) # => Student(name, age)
