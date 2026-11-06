import json
import os

from Inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier


PRODUCT_TYPES = {
    "physical": PhysicalProduct,
    "digital": DigitalProduct,
}

DEFAULT_SUPPLIER = {
    "supplier_id": "S000",
    "name": "Unknown Supplier",
    "contact_email": "unknown@example.com",
}

def load_inventory(filename: str ="inventory.json") -> Inventory:
    inventory = Inventory()
    if not os.path.exists(filename):
        return inventory
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Warning: {filename} is not valid JSON ({e}).")
        return inventory

    suppliers: dict[str, Supplier] = {}

    for item in data:
        try:
            supplier_data = item.get("supplier", DEFAULT_SUPPLIER)
            supplier_id = supplier_data["supplier_id"]
            if supplier_id not in suppliers:
                suppliers[supplier_id] = Supplier.from_dict(supplier_data)
            product_class = PRODUCT_TYPES[item["type"]]
            inventory.add_product(product_class.from_dict(item, suppliers[supplier_id]))
        except (KeyError, ValueError) as e:
            print(f"Skipped a bad record in {filename}: {e}")
    return inventory

def save_inventory(inventory : Inventory, filename: str ="inventory.json") -> None:
    with open(filename, "w") as f:
        json.dump([p.to_dict() for p in inventory.get_products()], f, indent=4)
    print(f"Inventory saved to {filename}.")