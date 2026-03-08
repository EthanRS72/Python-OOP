#Methods examples

l1 = [1,2,3,4,5]
#Pop "pops" out the last element of the list, List is a pre-defined class
list.pop(l1)
print(l1)


class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    #Example of method defined within a class
    def result(self):
        if self.marks > 500:
            return "Pass"
        return "Fail"


#Here 'self' is s1
s1 = Student("Sohail", 24, 501)

#Using result method defined within the student class.
print(s1.result())













#Example for tracking objects
class MyClass:
    instances = []

    def __init__(self):
        MyClass.instances.append(self)

x = MyClass()
y = MyClass()

print(MyClass.instances)