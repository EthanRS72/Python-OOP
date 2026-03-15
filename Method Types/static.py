class Student:
    students = []
    def __init__(self, name, age):
        Student.students.append(self)
        self.name = name
        self.age = age

    @staticmethod
    def print_statement():
        print("This is a static method")

s1 = Student('Sohail', 24)

s1.print_statement()