class Student:
    all_students = []
    #define total marks as the class level, set in the constructor but not passed as a param
    total_marks = 1000
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
        self.total_marks = Student.total_marks
        Student.all_students.append(self)


s1 = Student("Sohail", 24, 500)
s2 = Student("Jack", 67, 670)
s3 = Student("John", 33, 300)
s4 = Student("Pete", 22, 200)
s5 = Student("Charles", 18, 100)
s6 = Student("Fred", 27, 50)

print(s6.total_marks)