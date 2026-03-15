import re

#Class
class Laptop:
    #Class variables
    laptops = []
    discount = 10
    def __init__(self, name, price):
        #Class attributes
        self.name = name
        self.price = float(price)

    @classmethod #Class method
    def from_string(cls, string):
        item = re.findall('is \w*', string)
        name = item[0][3:]
        price = item[1][3:]
        return cls(name, price)
    
    #Instance method
    def apply_discount(self):
        return float(self.price - ((self.price / 100) * self.discount))

m6600 = Laptop('m6600', 50000)
m6600.discounted_price = m6600.apply_discount()

m4600 = Laptop.from_string("my laptop name is m4800 and the price is 60000")
m4600.discounted_price = m4600.apply_discount() 
print(m4600.__dict__)
