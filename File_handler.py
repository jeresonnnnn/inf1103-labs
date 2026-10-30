import json
import os

from Inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

PRODUCT_TYPES = {
    "physical": PhysicalProduct,
    "digital": DigitalProduct,
}

def load_inventory(filename="inventory.json"):
    inventory = Inventory()
    if not os.path.exists(filename):
        return inventory
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Warning: {filename} is not valid JSON ({e}).")
        return inventory
    for item in data:
        try:
            product_class = PRODUCT_TYPES[item["type"]]
            inventory.add_products(product_class.from_dict(item))
        except (KeyError, ValueError) as e:
            print(f"Skipped a bad record in {filename}: {e}")
    return inventory

def save_inventory(inventory, filename="inventory.json"):
    with open(filename, "w") as f:
        json.dump([p.to_dict() for p in inventory.get_products()], f, indent=4)
    print(f"Inventory saved to {filename}.")