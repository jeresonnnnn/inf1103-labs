from Product import Product
from Inventory import Inventory
from File_handler import load_inventory, save_inventory

FILENAME = "inventory.json"

def show_menu():
    print("\n=== Inventory Management System ===")
    print("1. Display all products")
    print("2. Add a product")
    print("3. Update stock")
    print("4. Search for a product")
    print("5. Save inventory")
    print("6. Exit")

def add_product(inventory):
    try:
        pid = input("Product ID: ").strip()
        name = input("Name: ").strip()
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        inventory.add_products(Product(pid, name, price, stock))
        print("Product added.")
    except ValueError as e:
        print(f"Invalid input: {e}")

def update_stock(inventory):
    product = inventory.search_product(input("Product ID: "))
    if product is None:
        print("Product not found.")
        return
    try:
        product.update_stock(int(input("New stock quantity: ")))
        print("Stock updated.")
    except ValueError as e:
        print(f"Invalid input: {e}")

def search_product(inventory):
    keyword = input("Enter product ID or name: ")
    product = inventory.search_product(keyword)
    results = [product] if product else inventory.search_by_name(keyword)
    if not results:
        print("No matching product found.")
    for p in results:
        p.display_information()

def main():
    inventory = load_inventory(FILENAME)
    while True:
        show_menu()
        choice = input("Choose and option (1-6): ").strip()
        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            save_inventory(inventory, FILENAME)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1-6.")

if __name__ == "__main__":
    main()