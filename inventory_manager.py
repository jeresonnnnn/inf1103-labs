import json

FILENAME = "inventory.json"

def load_inventory():
    try:
        file = open(FILENAME, "r")
        inventory = json.load(file)
        file.close()
        print("\ninventory.json found.")
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
    print("\nAdd New Product")
    product_id = input("Product ID: ")
    if find_product(inventory, product_id) is not None:
        print("A product with that ID already exists.")
        return

    name = input("Product Name: ")
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("\nInvalid number entered. Product not added.")
        return
    product = {"id": product_id, "name": name, "price": price, "stock": stock}
    inventory.append(product)
    print("\nProduct added successfully")

def display_all(inventory):
    print("\nCurrent Inventory")
    print("-"*50)
    if len(inventory) == 0:
        print("No products.")
    for p in inventory:
        print(f"ID: {p['id']} | Name: {p['name']} | Price: ${p['price']:.2f} | Stock: {p['stock']}")
    print("-"*50)
    
def save_inventory(inventory):
    file = open(FILENAME, "w")
    json.dump(inventory, file, indent=4)
    file.close()
    print("\nInventory saved successfully to inventory.json")

def update_stocks(inventory):
    print("\nUpdate stocks")
    product_id = input("Enter Product ID: ")
    product = find_product(inventory, product_id)

    if product is None:
        print("\nProduct is not found.")
        return

    print("\nProduct is found: ")
    print("Name:", product["name"])
    print("Current stock:", product["stock"])
    try:
        product["stock"] = int(input("\nNew stock quantity: "))
        print("\nStock updated successfully!")
    except ValueError:
        print("\nInvalid number entered. Stock not updated.")

def search_product(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ")
    product = find_product(inventory, product_id)

    if product is None:
        print("\nProduct not found.")
        return

    print("\nProduct found.")
    print("-"*50)
    print("ID:", product["id"])
    print("Name:", product["name"])
    print(f"Price: ${product['price']:.2f}")
    print("Stock: ", product["stock"])
    print("-"*50)

def show_menu():
    print("\n----------MENU----------")
    print("1. Display All Products")
    print("2. Add product")
    print("3. Update Stocks")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("-"*20)

def main():
    print("="*40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("="*40)

    inventory = load_inventory()
    show_menu()

    running = True
    while running:
        choice = input("\nEnter option: ")

        if choice == "1":
            display_all(inventory)
        elif choice == "2":
            add_product(inventory)
        elif choice =="3":
            update_stocks(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            save_inventory(inventory)
        elif choice == "6":
            print("Saving inventory before exiting...")
            save_inventory(inventory)
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            running = False
        else:
            print("Invalid option. Please choose 1-6.")

main()