from product import Product
from user import User
class ShoppingCart:
    def __init__(self, owner: User):
        self.owner = owner
        self.items = []  # list of tuples: (Product, quantity)

    def add_product(self, product, quantity):
        for i, item in enumerate(self.items):
            if item[0].product_id == product.product_id:
                self.items[i] = (item[0], item[1] + quantity) # tuple immutable, so we need to create a new tuple
                return
        self.items.append((product, quantity))