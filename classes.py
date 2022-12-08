class Person:
    species = "Homosapien"

    def hi(self):
        print(f"{self.name}'s Attributes: {self.species}, {self.age}")

    def __init__(self, name, age):
        self.name = name
        self.age = age


saint = Person("Saint", "17")

saint.hi()

tahmauri = Person("Tahmauri", "17")

tahmauri.hi()

