#Define circle class with two variables, circumfrence = area

class Circle:
    all_circles = []
    #Define Pi at class level, instead of passing to contructor everytime.
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius

    def circle_circumfrence(self):
        return 2 * Circle.pi * self.radius

    def circle_area(self):
        return(Circle.pi *  self.radius ** 2)
    
c1 = Circle(23)
c2 = Circle(13)

print(c1.circle_circumfrence())
print(c2.circle_area())