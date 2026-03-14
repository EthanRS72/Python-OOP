#Methods exercise 1

class Student:
    #List to store all students on creation
    all_students = []
    def __init__(self, name, marks):
        self.name = name
        self.marks =marks
        #Add students into tracking list
        Student.all_students.append(self)

    #Method to check pass criteria
    def result(self):
        if self.marks >= 500:
            return "Pass"
        return "Fail"

#init Student objects
s1 = Student("Sohail", 400)
s2 = Student("John", 500)
s3 = Student("Jack", 600)
s4 = Student("Pete", 200)
s5 = Student("Steve", 900)

#init lists and dict for student results
students_passed = []
students_failed = []
students_results = {}

#Process Student results
for student in Student.all_students:
    if student.result() == "Pass":
        students_passed.append(student.name)
        students_results['Passed Students'] = students_passed
    else:
        students_failed.append(student.name)
        students_results['Failed Students'] = students_failed


print(students_results)