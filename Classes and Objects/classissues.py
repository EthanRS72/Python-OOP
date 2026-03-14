class Phone:
    phones = []
    def __init__(self, brand, model, price):
        Phone.phones.append(self)
        self.brand = brand
        self.model = model
        self.price = max(price, 0)

    @property
    def complete_specification(self):
        return f"{self.brand} {self.model} and price is {self.price}"
    
    @staticmethod
    def make_a_call(phone_number):
        print(f"Calling {phone_number}...")

    def full_name(self):
        return f"{self.brand} {self.model}"
    

p1 = Phone("Nokia", "1100", -5000)
print(p1.complete_specification)
