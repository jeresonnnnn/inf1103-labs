import json

FILENAME = "inventory.json"

def load_inventory():
    try:
        file = open(FILENAME, "r")
        inventory = json.load(file)
        file.close()
        print("inventory.json found.")
        print("Inventory loaded succcessfully.")
        return inventory
    except FileNotFoundError:
        print("inventory.json not found.")
        return []
    except json.JSONDecodeError:
        print("file is empty.")
        return []

def find_product(inventory, product_id):
    for product in inventory:
        if product["id"] == product_id:
            return product
    return None

def add_product(inventory):
    print("Add New Product")
    product_id = input("Product ID: ")
    if find_product(inventory, product_id) is not None:
        print("A product with that ID already exists.")
        return

    name = input("Product Name: ")
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Invalid number entered. Product not added.")
        return
    product = {"id": product_id, "name": name, "price": price, "stock": stock}
    inventory.append(product)
    print("Product added successfully")

def display_all(inventory):
    print("Current Inventory")
    if len(inventory) == 0:
        print("No products.")
    for p in inventory:
        print(f"ID: {p['id']} | Name: {p['name']} | Price: ${p['price']:.2f} | Stock: {p['stock']}")

inventory = load_inventory()
display_all(inventory)
    