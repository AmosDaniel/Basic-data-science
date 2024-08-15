'''
Write a Python class Inventory with attributes like id, productName, availableQuantity and price. Add methods like addItem, updateItem, and checkItem_details.

Use a dictionary to store the item details, where the key is the id and the value is a dictionary containing the productName, availableQuantity and price.

Sample Data:

{
  "97410": {
    "name": "Television",
    "availableQuantity": 20,
    "price": 1455.99
  },
  "97411": {
    "name": "Radio",
    "availableQuantity": 32,
    "price": 654.25
  }
}


'''

class Inventory:
    def __init__(self):
        # Initialize with an empty inventory dictionary
        self.stock = {}

    def add_product(self, product_id, product_name, quantity, unit_price):
        # Add a product to the inventory
        if product_id in self.stock:
            return f"Product with id {product_id} already exists."
        self.stock[product_id] = {
            'productName': product_name,
            'quantityAvailable': quantity,
            'unitPrice': unit_price
        }
        return f"Product {product_id} added successfully."

    def modify_product(self, product_id, product_name=None, quantity=None, unit_price=None):
        # Modify details of an existing product
        if product_id not in self.stock:
            return f"Product with id {product_id} does not exist."
        if product_name is not None:
            self.stock[product_id]['productName'] = product_name
        if quantity is not None:
            self.stock[product_id]['quantityAvailable'] = quantity
        if unit_price is not None:
            self.stock[product_id]['unitPrice'] = unit_price
        return f"Product {product_id} updated successfully."

    def get_product_details(self, product_id):
        # Get details of a specific product
        if product_id not in self.stock:
            return f"Product with id {product_id} not found."
        product = self.stock[product_id]
        return (
            f"Product: {product['productName']}\n"
            f"Quantity Available: {product['quantityAvailable']}\n"
            f"Unit Price: ${product['unitPrice']}"
        )

    def __str__(self):
        # String representation of the inventory
        return str(self.stock)


# Example usage
inventory = Inventory()

# Adding products
print(inventory.add_product("P1001", "Tomato Sauce", 200, 2.99))
print(inventory.add_product("P1002", "Chili Sauce", 150, 3.49))
print(inventory.add_product("P1001", "BBQ Sauce", 100, 4.99))  # Should indicate duplicate

print("="*50)

# Getting product details
print(inventory.get_product_details("P1001"))
print(inventory.get_product_details("P1003"))  # Should indicate not found

print("="*50)

# Modifying a product
print(inventory.modify_product("P1001", quantity=180))
print(inventory.modify_product("P1003", product_name="Mustard", quantity=80))  # Should indicate not found

# Getting updated product details
print(inventory.get_product_details("P1001"))

print("="*50)

# Printing the entire inventory
print(inventory)