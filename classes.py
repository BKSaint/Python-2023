class Person:
    species = "Homosapien"

    def hi(self):
        print(f"{self.name}'s Attributes: {self.species}, {self.age}")

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    role = "Teacher"
    def hi(self):
        print(f"{self.name}'s Attributes: {self.species}, {self.age}, {self.role}")

class Student(Person):
    role = "Student"
    def hi(self):
        print(f"{self.name}'s Attributes: {self.species}, {self.age}, {self.role}")

saint = Student("Saint", 17)
saint.hi()

tahmauri = Student("Tahmauri", 17)
tahmauri.hi()

forlenza = Teacher("Forlenza", 184)
forlenza.hi()

