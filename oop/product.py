class Product:
    # class attribute
    taxrate = 18

    # constructor
    def __init__(self, name, price, qoh):
        # create object attributes
        self.name = name
        self.price = price
        self.qoh = qoh

    def print_details(self):
        print("Name  : ", self.name)
        print("Price : ", self.price)
        print("Qoh   : ", self.qoh)

    @property
    def sellingprice(self):
        return self.price + (self.price * Product.taxrate / 100)

    def sell(self, qty):
        if self.qoh < qty:
            raise ValueError('Insufficient stock!')
        self.qoh -= qty

    def __eq__(self, other):
        # print('__eq__')
        return self.name == other.name and self.price == other.price

    def __gt__(self, other):
        return self.price > other.price

    def __str__(self):
        return f"{self.name} - {self.price} - {self.qoh}"


# Create an object of Product class
p1 = Product("Product1", 15000, 20)
print(p1.sellingprice)

p2 = Product("Product1", 10000, 20)

print(id(p1), id(p2))
print(p1 > p2)  # p1.__eq__(p2)
print(str(p1))  # p1.__str__()
