# Convenience Store Management System

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} x {self.quantity}"

class ConvenienceStore:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"{product_name} removed from inventory.")
                return
        print(f"{product_name} not found in inventory.")

    def display_inventory(self):
        print(f"Inventory for {self.name}:")
        for product in self.products:
            print(product)

    def calculate_total_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.price * product.quantity
        return total_value

def main():
    store = ConvenienceStore("QuickMart")

    # Add products to inventory
    store.add_product(Product("Coke", 2.50, 10))
    store.add_product(Product("Chips", 1.50, 20))
    store.add_product(Product("Milk", 3.00, 5))

    # Display inventory
    store.display_inventory()

    # Calculate total value of inventory
    total_value = store.calculate_total_value()
    print(f"Total value of inventory: ${total_value:.2f}")

    # Remove a product from inventory
    store.remove_product("Chips")

    # Display updated inventory
    store.display_inventory()

if __name__ == "__main__":
    main()