#Everything is public

#Use _Name to denote privately treated variables

class Phone:
    phones = []
    def __init__(self, brand, model, price):
        Phone.phones.append(self)
        self.brand = brand
        self.model = model
        self.price = price
        #Private var discount
        self._discount = 10

    def apply_discount(self):
        return (self.price/100) * (100-self._discount)



P1 = Phone("Brick", "Big Brick", 10)
print(P1.apply_discount())

print(P1.__dict__) #Dunder/Magic method as denoted by __Name__
