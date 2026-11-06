from Inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped
from File_handler import load_inventory, save_inventory
from order import Order
from supplier import Supplier

FILENAME = "inventory.json"


def show_menu():
    print("\n=== Inventory Management System ===")
    print("1. Display all products")
    print("2. Add a product")
    print("3. Update stock")
    print("4. Search for a product")
    print("5. Create an order")
    print("6. Save inventory")
    print("7. Exit")

def choose_supplier(inventory: Inventory) -> Supplier:
    known = {p.get_supplier().get_supplier_id().lower(): p.get_supplier()
             for p in inventory.get_products()}
    supplier_id = input("Supplier ID: ").strip()
    if supplier_id.lower() in known:
        supplier = known[supplier_id.lower()]
        print("Using existing supplier:")
        supplier.display_information()
        return supplier
    name = input("Supplier name: ").strip()
    email = input("Supplier contact email: ").strip()
    return Supplier(supplier_id, name, email)


def add_product(inventory: Inventory) -> None:
    kind = input("Product type - (P)hysical or (D)igital: ").strip().lower()
    if kind not in ("p", "d"):
        print("Invalid type. Enter P or D.")
        return
    try:
        pid = input("Product ID: ").strip()
        name = input("Name: ").strip()
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        supplier = choose_supplier(inventory)
        if kind == "p":
            weight = float(input("Weight (kg): "))
            product = PhysicalProduct(pid, name, price, stock, weight, supplier)
        else:
            size = float(input("Download size (MB): "))
            product = DigitalProduct(pid, name, price, stock, size, supplier)
        inventory.add_product(product)
        print("Product added.")
    except ValueError as e:
        print(f"Invalid input: {e}")


def update_stock(inventory: Inventory) -> None:
    product = inventory.search_product(input("Product ID: "))
    if product is None:
        print("Product not found.")
        return
    try:
        product.update_stock(int(input("New stock quantity: ")))
        print("Stock updated.")
    except ValueError as e:
        print(f"Invalid input: {e}")


def search_product(inventory: Inventory) -> None:
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

def create_order(inventory: Inventory) -> None:
    order_id = input("Order ID: ").strip()
    if not order_id:
        print("Order ID cannot be empty.")
        return
    order = Order(order_id)
    while True:
        pid = input("Product ID to add (leave blank to finish): ").strip()
        if not pid:
            break
        product = inventory.find_product(pid)
        if product is None:
            print("Product not found.")
            continue
        try:
            quantity = int(input("Quantity: "))
            if quantity > product.get_stock():
                print(f"Only {product.get_stock()} in stock.")
                continue
            order.add_order_line(product, quantity)
        except ValueError as e:
            print(f"Invalid input: {e}")
    if not order.get_order_lines():
        print("Order is empty, nothing created.")
        return
    order.display_order()


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
            create_order(inventory)
        elif choice == "6":
            save_inventory(inventory, FILENAME)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter 1-7.")


if __name__ == "__main__":
    main()