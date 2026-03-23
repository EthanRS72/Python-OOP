class Phone:
    phones = []
    def __init__(self, brand, model, price):
        Phone.phones.append(self)
        self.brand = brand
        self.model = model
        self.__price = price
        #Private var discount
        self._discount = 10

    def apply_discount(self):
        return (self.__price/100) * (100-self._discount)
    
    def __full_name(self):
        return f"{self.brand} {self.model}"
    
    #Encapsulation - provides get method for price that works with name mangling
    @property
    def price(self):
        return self.__price

#Class Smartphone inherits Phone. Common method of inheritence
class Smartphone(Phone):
    smartphones = []
    def __init__(self, brand, model, price, ram, storage, camera):
        super().__init__(brand, model, price)
        Smartphone.smartphones.append(self)
        self.ram = ram
        self.storage = storage
        self.camera = camera

    def __full_name(self):
        return f"{self.brand} {self.model}, price is: {self.price}"

#Multiple inheritance. Phone (Brand, Model, Price) -> Smartphone (RAM, Storage, Camera) -> Flagship (Front Camera)
class Flagship(Smartphone):
    flagships = []
    def __init__(self, brand, model, price, ram, storage, camera, front_camera):
        super().__init__(brand, model, price, ram, storage, camera)
        Flagship.flagships.append(self)
        self.front_camera = front_camera

    def full_name(self):
        return f"{self.brand} {self.model}, price is: {self.price}. Back camera is {self.camera}, front camera is {self.front_camera}"


P1 = Phone("Brick", "Big Brick", 10)
SP1 = Smartphone("Blackberry", "XYT", 1000, "10GB", "28GB", "8MP")
FS1 = Flagship("Samsung", "A7", 60000, "4GB", "128GB", "16MP", "4MP")
#Python converts __price to _Phone__price as __ used in naming convention
print(P1.__dict__)

#Returns error if setter not used
print(P1.price)
#Must use otherwise
print(P1._Phone__price)

#Also inherited in subclasses
print(FS1.price)
print(FS1._Phone__price)

#Will throw error if getter property is not defined
#If using -- in method name as Phone + Smartphone call as below
print(SP1._Smartphone__full_name())
print(FS1.full_name())


print(FS1._Smartphone__full_name())

