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


#Class Smartphone inherits Phone. Common method of inheritence
class Smartphone(Phone):
    smartphones = []
    def __init__(self, brand, model, price, ram, storage, camera):
        super().__init__(brand, model, price)
        Smartphone.smartphones.append(self)
        self.ram = ram
        self.storage = storage
        self.camera = camera

#Multiple inheritance. Phone (Brand, Model, Price) -> Smartphone (RAM, Storage, Camera) -> Flagship (Front Camera)
class Flagship(Smartphone):
    flagships = []
    def __init__(self, brand, model, price, ram, storage, camera, front_camera):
        super().__init__(brand, model, price, ram, storage, camera)
        Flagship.flagships.append(self)
        self.front_camera = front_camera

P1 = Phone("Brick", "Big Brick", 10)
SP1 = Smartphone("Blackberry", "XYT", 1000, "10GB", "28GB", "8MP")
FS1 = Flagship("Samsung", "A7", 60000, "4GB", "128GB", "16MP", "4MP")

print("Phone class")
print(*(vars(p) for p in Phone.phones), sep="\n", end="\n\n")

print("Smartphone class")
print(*(vars(s) for s in Smartphone.smartphones), sep="\n", end="\n\n")

print("Flagship class")
print(*(vars(f) for f in Flagship.flagships), sep="\n", end="\n\n")

print(type(Phone.phones[0]))

#Method resolution order aka class trace
print(Flagship.mro())

print(FS1.full_name())