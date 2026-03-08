#OOP methods exercise 2

class Product:
    all_products = []

    def __init__(self, product_name, price):
        Product.all_products.append(self)
        self.product_name = product_name
        self.price = price

    def discount(self, discount_percentage):
        return int((self.price / 100) * (100-discount_percentage))


p1 = Product("laptop", 1000)
print(p1.discount(25))