class Phone:
    phones = []
    def __init__(self, brand, model, price):
        Phone.phones.append(self)
        self.brand = brand
        self.model = model
        self.price = price

    #Used for dev
    def __repr__(self):
        return f"{self.brand} {self.model}"
    
    #Used for users
    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}"

    

P1 = Phone('Nokia', '3310', 150)

#Standard print(P1) prints memory address of the instance

#Dunder/Magic methods created with __name__

#Now uses __str__ to print string
print(P1)

#Can call either
print(P1.__str__())
print(P1.__repr__())