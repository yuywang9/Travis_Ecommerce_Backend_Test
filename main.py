from user import User
from product import Product
from shopping_cart import ShoppingCart

# create users first
user1 = User("john_doe", "password123")
user2 = User("jane_smith", "securepass")

# then login test
print("Login test:")
print(User.login("john_doe", "password123"))  # Output: True
print(User.login("jane_smith", "wrongpass"))  # Output: False

# now we create products
product1 = Product(1, "Laptop", 1200.99)
product2 = Product(2, "Mouse", 25.50)

# create shopping cart of user1
cart = ShoppingCart(user1)
cart.add_product(product1, 1)
cart.add_product(product2, 2)
cart.add_product(product1, 1)  # update quantity for Laptop

# Display cart items
print("Cart items:")
for item in cart.items:
    print(f"Product: {item[0].name}, Quantity: {item[1]}")