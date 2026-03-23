class Phone:
    phones = []
    def __init__(self, brand, model, price):
        Phone.phones.append(self)
        self.brand = brand
        self.model = model
        self.price = price

    #Overloading the add (+) operator
    def __add__(self, other):
        return self.price + other.price
    
    #Overloading the add (-) operator
    def __sub__(self, other):
        return self.price - other.price

    #Overloading the multiplication (*) operator
    def __mul__(self, other):
        return self.price * other.price

P1 = Phone('Nokia', '3310', 150)
P2 = Phone('Nokia', '1600', 100)

print(P1 + P2)
print(P1 - P2)
print(P1 * P2)