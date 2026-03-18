#All attributes and functions for the phone Class are encapsulated within the class.
#Getters and setter used to retrieve and modify attributes.
#Abstraction is used to hide functionality, details are not required. Hides complexity. 

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

p1 = Phone("Nokia", 1100, 4000)
print(p1.__dict__)

p1.make_call('0213832937')
print(p1.full_name())