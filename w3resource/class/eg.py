class Person:
    def __init__(self, name, age):
        self.name = name.capitalize()
        self.age = age
        self.author = "calvin mas"

    def __str__(self):
        return f"Hello {self.name}"

class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduationYear = year 

    def welcome(self):
        print(f"welcome to the python class by {self.author}")

s1 = Student("Katlego Tefo", 2023 - 2005, 2024)

s1.welcome()
