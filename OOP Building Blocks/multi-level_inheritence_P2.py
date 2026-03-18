class A:
    def class_a_method(self):
        return "Class A method"
    
    def hello(self):
        return "Hello from class A"
    

class B:
    def class_b_method(self):
        return "Class B method"
    
    def hello(self):
        return "Hello from class B"
    

class C(A, B):
    pass

instanceA = A()
instanceB = B()
instanceC = C()

print(instanceA.class_a_method())
print(instanceB.class_b_method())
print(instanceC.class_a_method())
print(instanceC.class_b_method())
print("\n")
print(instanceA.hello())
print(instanceB.hello())
print(instanceC.hello())

#Shows Trace as: C -> A -> B, as a result instanceC.hello returns "Hello from class A". Because order specified in class definition as C(A, B)
print(C.mro())
#Shows all inheritance
print(help(instanceC))