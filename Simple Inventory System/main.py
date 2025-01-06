class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def display_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")

    def update_quantity(self, amount):
        self.quantity += amount

    def total_value(self):
        return self.price * self.quantity
    
class Inventory:
    def __init__(self):
        self.products = []
    
    def buy_product(self, product_name, quantity):
        for product in self.products:
            if product.name == product_name:
                product.update_quantity(quantity)
                return
        print("Product not found")

    def sell_product(self, product_name, quantity):
        for product in self.products:
            if product.name == product_name:
                product.update_quantity(-quantity)
                return
        print("Product not found")
    
    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        self.products = [product for product in self.products if product.name != product_name]

    def display_inventory(self):
        for product in self.products:
            product.display_info()
            print("-" * 20)

    def total_inventory_value(self):
        return sum(product.total_value() for product in self.products)

# Example usage
if __name__ == "__main__":
    inventory = Inventory()

    product1 = Product("Laptop", 1000, 5)
    product2 = Product("Phone", 500, 10)

    inventory.add_product(product1)
    inventory.add_product(product2)

    inventory.buy_product("Laptop", 5)
    inventory.sell_product("Phone", 2)

    inventory.display_inventory()
    print(f"Total Inventory Value: ${inventory.total_inventory_value()}")