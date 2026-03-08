#Problem: Create a 'Product' class wtih attributes including product name, brand name, model name and price

class Product:
    def __init__(self, product_name, brand_name, model_name, price):
        self.product_name = product_name
        self.brand_name = brand_name
        self.model_name =model_name
        self.price = price
        #Attribute created from other attributes, created through constructor
        self.product_and_model  = product_name + " " + model_name

Laptop = Product("Laptop", "Dell", "XPS13", 2499)
print(Laptop.product_name)
print(Laptop.brand_name)
print(Laptop.model_name)
print(Laptop.price)
print(Laptop.product_and_model)

print("\n")

Mobile = Product("iPhone", "Apple", "17", 1699)
print(Mobile.product_name)
print(Mobile.brand_name)
print(Mobile.model_name)
print(Mobile.price)
print(Mobile.product_and_model)