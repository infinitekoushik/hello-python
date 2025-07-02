# Object-Oriented Programming – Basics

class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def introduce(self):
        print("Hi, I'm", self.name, "from", self.branch)

# Create object
s1 = Student("Chandra Koushik", "Computer Science")
s1.introduce()
