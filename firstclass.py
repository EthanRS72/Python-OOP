#Creating first class

#Student class definition
class Student:
    #User defined default constructor
    #Self can be defined with any term as the first parameter
    def __init__(self, name, roll_number, marks):
        #self.name reference to attribute of Student object, marks is passed as an argument to the constructor
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

#Create Student objects
student1 = Student('Sohail', 12345, 500)
print(student1)

student2 = Student("Usuma", 12345, 700)
print(student2)

#Access the name attribute of both students.
print(student1.name)
print(student2.name)
