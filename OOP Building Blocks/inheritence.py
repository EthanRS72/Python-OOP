class Phone:
    phones = []
    def __init__(self, brand, model, price):
        Phone.phones.append(self)
        self.brand = brand
        self.model = model
        self.price = price

    @staticmethod
    def make_call(phone_number):
        print(f"Calling {phone_number}...")

    def full_name(self):
        return f"{self.brand} {self.model}"



#Class Smartphone inherits Phone. Uncommon method of inheritence
#class Smartphone(Phone):
#    smartphones = []
#    def __init__(self, brand, model, price, ram, storage, camera):
#        Phone.__init__(self, brand, model, price)
#        Smartphone.smartphones.append(self)
#        self.ram = ram
#        self.storage = storage
#        self.camera = camera


#Class Smartphone inherits Phone. Common method of inheritence
class Smartphone(Phone):
    smartphones = []
    def __init__(self, brand, model, price, ram, storage, camera):
        super().__init__(brand, model, price)
        Smartphone.smartphones.append(self)
        self.ram = ram
        self.storage = storage
        self.camera = camera

P1 = Phone("Nokia", "1100", 4000)
print(P1.__dict__)

SP1 = Smartphone("Samsung", "A7", 60000, "4GB", "128GB", "16MP")
print(SP1.__dict__)

for phone in Phone.phones:
    print(phone.full_name())