from Inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped
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
    kind = input("Product type - (P)hysical or (D)igital: ").strip().lower()
    if kind not in ("p", "d"):
        print("Invalid type. Enter P or D.")
        return
    try:
        pid = input("Product ID: ").strip()
        name = input("Name: ").strip()
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        if kind == "p":
            weight = float(input("Weight (kg): "))
            product = PhysicalProduct(pid, name, price, stock, weight)
        else:
            size = float(input("Download size (MB): "))
            product = DigitalProduct(pid, name, price, stock, size)
        inventory.add_product(product)
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
        print(f"        {p.get_fulfilment_info()}")
        if isinstance(p, CanBeShipped):
            print(f"        Shipping cost: ${p.calculate_shipping_cost():.2f}")


def main():
    inventory = load_inventory(FILENAME)
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()
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