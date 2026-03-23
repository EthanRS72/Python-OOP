class Phone:
    phones = []
    def __init__(self, brand, model, price):
        Phone.phones.append(self)
        self.brand = brand
        self.model = model
        self.price = price

    #Overloading
    def __add__(self, other):
        return f"{self.brand} {self.model}, " + f"{other.brand} {other.model}"

#Class Smartphone inherits Phone. Common method of inheritence
class Smartphone(Phone):
    smartphones = []
    def __init__(self, brand, model, price, ram, storage, camera):
        super().__init__(brand, model, price)
        Smartphone.smartphones.append(self)
        self.ram = ram
        self.storage = storage
        self.camera = camera

    #Overloading
    def __add__(self, other):
        return f"{self.price}, " + f"{other.price}"

#Multiple inheritance. Phone (Brand, Model, Price) -> Smartphone (RAM, Storage, Camera) -> Flagship (Front Camera)
class Flagship(Smartphone):
    flagships = []
    def __init__(self, brand, model, price, ram, storage, camera, front_camera):
        super().__init__(brand, model, price, ram, storage, camera)
        Flagship.flagships.append(self)
        self.front_camera = front_camera

    #Overloading
    def __add__(self, other):
        return f"{self.camera}, " + f"{other.camera}"

P1 = Phone("Brick", "Big Brick", 10)
P2= Phone("Bloc", "BlocPhone", 30)
SP1 = Smartphone("Blackberry", "XYT", 1000, "10GB", "28GB", "8MP")
SP2 = Smartphone("Oppo", "ABC", 500, "5GB", "22GB", "4MP")
FS1 = Flagship("Samsung", "A7", 60000, "4GB", "128GB", "16MP", "4MP")
FS2 = Flagship("Apple", "iPhone 16 Pro", 2000, "8GB", "257GB", "32MP", "8MP")

#Phone method - models
print(P1 + P2)
#Smartphone method - price
print(SP1 + SP2)
#Flagship method - cameras
print(FS1 + FS2)