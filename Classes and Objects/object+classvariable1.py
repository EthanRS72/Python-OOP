class Laptop:
    laptops = []
    discount = 10
    serial_number = 0
    def __init__(self, name, price):
        Laptop.laptops.append(self)
        Laptop.serial_number += 1
        self.serial_number = Laptop.serial_number
        self.name = name
        self.price = price

    def apply_discount(self):
        return self.price - ((self.price / 100) * self.discount)

m6600 = Laptop('m6600', 55000)
m4800 = Laptop('m4800', 55000)

#Adds/modify object attributes
m4800.bluetooth = True
m4800.discount = 5

print(m4800.apply_discount())
print(m6600.apply_discount())

#Use dict to view all object attributes
print(m4800.__dict__)
print(m6600.__dict__)